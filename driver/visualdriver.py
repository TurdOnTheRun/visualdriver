from multiprocessing import Queue, Value, Lock
from pygame import mixer
import queue
import time

from events import *
from agents import *
from conditions import *

from arduinopwmmanager import ArduinoPwmManager
from encoderreader import EncoderReader
from kinectreader import KinectReader
from settings import ARDUINO_UNO_CONN, ARDUINO_MEGA_CONN, ARDUINO_UNO_TRIGGER_ENCODER_CONN


class VisualDriver:

    def __init__(self, eventDict, usesKinect=False, usesTrigger=False, music=None):
        self.timeEvents = eventDict.get('time', [])
        self.positionEvents = eventDict.get('position', [])
        self.usesKinect = usesKinect
        self.usesTrigger = usesTrigger
        self.music = music

        discharging = open('/sys/class/power_supply/BAT0/status','r').readline().strip().lower()
        if discharging != 'discharging':
            inp = input('Laptop is charging...\nTo continue confirm with "go":')
            if inp.lower() != "go":
                exit()

        if self.music:
            mixer.init()
            mixer.music.load(self.music)
            mixer.music.set_volume(1)
        
        self.shutdownQueue = Queue()

        self.topQueue = Queue()
        self.top = ArduinoPwmManager(ARDUINO_MEGA_CONN, self.topQueue, self.shutdownQueue)

        self.bottomQueue = Queue()
        self.bottom = ArduinoPwmManager(ARDUINO_UNO_CONN, self.bottomQueue, self.shutdownQueue)
        
        self.encoderLock = Lock()
        self.position = Value('d', 0.0, lock=False)
        self.distance = Value('d', 0.0, lock=False)
        self.er = EncoderReader(self.encoderLock, self.position, self.distance, self.shutdownQueue)

        if self.usesTrigger:
            self.triggerQueue = Queue()
            self.trigger = ArduinoPwmManager(ARDUINO_UNO_TRIGGER_ENCODER_CONN, self.triggerQueue, self.shutdownQueue)

        if self.usesKinect:
            self.kinectLock = Lock()
            self.kinectQueue = Queue()
            self.kr = KinectReader(self.kinectLock, self.kinectQueue, self.shutdownQueue)
    
    def shutdown(self):
        self.bottomQueue.put((220,0,50))
        self.topQueue.put((200,50))
        self.bottomQueue.put((200,0))
        time.sleep(1)
        self.shutdownQueue.put('STOP')
        time.sleep(3)
    
    def start(self):

        self.top.start()
        self.bottom.start()
        self.er.start()
        if self.usesTrigger:
            self.trigger.start()

        print('Setting Up...')
        time.sleep(3)
        self.bottomQueue.put((220,0,50))
        self.topQueue.put((200,0))
        self.bottomQueue.put((200,0))
        time.sleep(4)
        print('Setup Complete!')

        if self.usesKinect:
            self.kr.start()
            print('Getting first pose...')
            poseNow = self.kinectQueue.get()
            print('Pose received!')

        timeEventsIndex = 0
        timeEventsBlocked = False
        positionEventsIndex = 0
        positionEventsBlocked = False
        last = time.time()
        if self.music:
            mixer.music.play()

        try:

            while True:

                events = []
                now = time.time() - last
                with self.encoderLock:
                    positionNow = self.position.value
                    distanceNow = self.distance.value
                if self.usesKinect:
                    with self.kinectLock:
                        try:
                            poseNow = self.kinectQueue.get(False)
                        except queue.Empty:
                            pass

                if not timeEventsBlocked and timeEventsIndex < len(self.timeEvents):
                    while timeEventsIndex < len(self.timeEvents) and self.timeEvents[timeEventsIndex].condition.met(now):
                        events.append(self.timeEvents[timeEventsIndex])
                        timeEventsIndex += 1
                
                if not positionEventsBlocked and positionEventsIndex < len(self.positionEvents):
                    while positionEventsIndex < len(self.positionEvents) and self.positionEvents[positionEventsIndex].condition.met(positionNow):
                        events.append(self.positionEvents[positionEventsIndex])
                        positionEventsIndex += 1

                for event in events:
                    if event.agent.controller != MAIN_CONTROLLER:
                        if event.hasVariable:
                            for i, com in enumerate(event.command):
                                if isinstance(com, Variable):
                                    event.command[i] = com.get(now=now, position=positionNow, pose=poseNow)
                            event.command = event.clean_bytes(event.command)
                            # print(now, positionNow, event.command)
                        if event.agent.controller == TOP_CONTROLLER:
                            self.topQueue.put(event.command)
                        elif event.agent.controller == BOTTOM_CONTROLLER:
                            self.bottomQueue.put(event.command)
                    else:
                        if event.type == TIME_RESET_TYPE:
                            # print(now, positionNow, 'TIME_RESET_TYPE')
                            last = time.time()
                        elif event.type == ADD_EVENTS_TYPE:
                            self.timeEvents += event.events.get('time', [])
                            self.positionEvents += event.events.get('position', [])
                        elif event.type == POSITION_RESET_TYPE:
                            # print(now, positionNow, 'POSITION_RESET_TYPE')
                            position.value = 0
                        elif event.type == TIME_EVENTS_BLOCK_TYPE:
                            # print(now, positionNow, 'TIME_EVENTS_BLOCK_TYPE')
                            timeEventsBlocked = True
                        elif event.type == TIME_EVENTS_UNBLOCK_TYPE:
                            # print(now, positionNow, 'TIME_EVENTS_UNBLOCK_TYPE')
                            timeEventsBlocked = False
                        elif event.type == TIME_EVENTS_CLEAR_TYPE:
                            # print(now, positionNow, 'TIME_EVENTS_CLEAR_TYPE')
                            self.timeEvents = []
                            timeEventsIndex = 0
                        elif event.type == TIME_EVENTS_CLEAR_TO_MARKER_TYPE:
                            self.timeEvents = timeEvents[timeEvents.index(event.marker)+1:]
                            timeEventsIndex = 0
                        elif event.type == TRIGGER_SET_ANGLE_TYPE:
                            self.triggerQueue.put([1, event.angle])
                        elif event.type == TRIGGER_DETACH_TYPE:
                            self.triggerQueue.put([0,])
                    
                if timeEventsIndex >= len(self.timeEvents) and positionEventsIndex >= len(self.positionEvents):
                    self.shutdown()
                    break

        except Exception as e:
            self.shutdown()
            print('Error:', e)
            exit(-1)