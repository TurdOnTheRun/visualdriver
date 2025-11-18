from multiprocessing import Queue, Value, Lock
from pygame import mixer
import queue
import time
import subprocess

from events import *
from controllers import *
from conditions import *

from arduinopwmmanager import ArduinoPwmManager, ArduinoEspManager
from encoderreader import EncoderReader
from speedcontroller import SpeedController
from kinectreader import KinectReader
from settings import ARDUINO_UNO_CONN, ARDUINO_MEGA_CONN, ARDUINO_UNO_TRIGGER_ENCODER_CONN, WIFI_SSID, WIFI_PWD, ESP_SSID, ESP_PWD


class VisualDriver:

    def __init__(self, eventDict, usesMotor=False, usesKinect=False, usesTrigger=False, music=None, isTake=True, startTime=0):
        self.timeEvents = eventDict.get('time', [])
        self.positionEvents = eventDict.get('position', [])
        self.usesMotor = usesMotor
        self.usesKinect = usesKinect
        self.usesTrigger = usesTrigger
        self.music = music
        self.isTake = isTake
        self.startTime = startTime

        discharging = open('/sys/class/power_supply/BAT0/status','r').readline().strip().lower()
        if discharging != 'discharging':
            inp = input('Laptop is charging...\nTo continue confirm with "go":')
            if inp.lower() != "go":
                exit()

        if self.music:
            mixer.pre_init(frequency=48000)
            mixer.init()
            mixer.music.load(self.music)
            mixer.music.set_volume(1)
        
        self.shutdownQueue = Queue()

        self.topQueue = Queue()
        self.top = ArduinoEspManager(ARDUINO_MEGA_CONN, self.topQueue, self.shutdownQueue)

        self.bottomQueue = Queue()
        self.bottom = ArduinoPwmManager(ARDUINO_UNO_CONN, self.bottomQueue, self.shutdownQueue)

        self.encoderLock = Lock()
        self.position = Value('d', 0.0, lock=False)
        self.distance = Value('d', 0.0, lock=False)

        if self.usesMotor:

            self.er = EncoderReader(self.encoderLock, self.position, self.distance, self.shutdownQueue)

            self.speed = Value('d', 0.0)
            self.targetSpeed = Value('i', 0)
            self.targetDirection = Value('i', MOTOR_CLOCKWISE)
            self.sc = SpeedController(self.speed, self.targetSpeed, self.targetDirection, self.encoderLock, self.distance, self.bottomQueue, self.shutdownQueue)

        if self.usesTrigger:
            self.triggerQueue = Queue()
            self.trigger = ArduinoPwmManager(ARDUINO_UNO_TRIGGER_ENCODER_CONN, self.triggerQueue, self.shutdownQueue)

        if self.usesKinect:
            self.kinectLock = Lock()
            self.kinectQueue = Queue()
            self.kr = KinectReader(self.kinectLock, self.kinectQueue, self.shutdownQueue)

        if self.isTake:
            inp = input('Focus Check:')
            if inp.lower() != "focus":
                exit()

            inp = input('Plugs Check:')
            if inp.lower() != "plugs":
                exit()

            inp = input('Encoder Check:')
            if inp.lower() != "encoder":
                exit()

            inp = input('Sync Check:')
            if inp.lower() != "sync":
                exit()
            
            inp = input('Go:')
    
    def shutdown(self):
        self.bottomQueue.put((220,0,50)) #stop motor
        self.topQueue.put((180,)) #reset settings
        self.topQueue.put((181,)) #reset effects
        self.topQueue.put((182,)) #reset channels
        self.topQueue.put((150,255,3)) #set all lights to 30
        self.bottomQueue.put((180,)) #reset settings
        self.bottomQueue.put((181,)) #reset effects
        self.bottomQueue.put((182,)) #reset channels
        self.bottomQueue.put((150,255,0)) #set all lights to 0
        time.sleep(1)
        self.shutdownQueue.put('STOP')
        time.sleep(1)
        # process = subprocess.Popen(['nmcli', 'device', 'wifi', 'connect', WIFI_SSID, 'password', WIFI_PWD], stdout=subprocess.PIPE, stderr=subprocess.PIPE)
        # stdout, stderr = process.communicate()
        # # Check if there was an error
        # if process.returncode != 0:
        #     print("Error:", stderr.decode("utf-8"))
        # else:
        #     print("Successfully reconnected to _____________")

    
    def start(self):
        # process = subprocess.Popen(['nmcli', 'device', 'wifi', 'connect', ESP_SSID, 'password', ESP_PWD], stdout=subprocess.PIPE, stderr=subprocess.PIPE)
        # stdout, stderr = process.communicate()
        # # Check if there was an error
        # if process.returncode != 0:
        #     print("Error:", stderr.decode("utf-8"))
        #     exit(0)
        # else:
        #     print("Successfully connected to Old Weller")

        self.top.connect()
        self.top.start()
        self.bottom.connect()
        self.bottom.start()

        if self.usesTrigger:
            self.trigger.start()

        print('Setting Up...')
        time.sleep(4)
        self.bottomQueue.put((220,0,50))
        self.topQueue.put((150,255,0))
        self.bottomQueue.put((150,255,0))
        self.topQueue.put((180,)) #reset settings
        self.topQueue.put((181,)) #reset effects
        self.topQueue.put((182,)) #reset channels
        self.bottomQueue.put((180,)) #reset settings
        self.bottomQueue.put((181,)) #reset effects
        self.bottomQueue.put((182,)) #reset channels
        if(self.isTake):
            time.sleep(4)
        else:
            time.sleep(0.5)
        print('Setup Complete!')

        if self.usesKinect:
            self.kr.start()
            print('Getting first pose...')
            poseNow = self.kinectQueue.get()
            print('Pose received!')

        if self.usesMotor:
            self.er.start()
            self.sc.start()

        skippedToStartTime = False

        timeEventsIndex = 0
        timeEventsBlocked = False
        positionEventsIndex = 0
        positionEventsBlocked = False
        last = time.time() - self.startTime
        
        try:

            while True:

                if self.startTime != 0 and not skippedToStartTime:
                    time.sleep(1)
                    last += 1
                    mixer.music.play(start=self.startTime)
                    skippedToStartTime = True

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

                while not timeEventsBlocked and timeEventsIndex < len(self.timeEvents) and self.timeEvents[timeEventsIndex].condition.met(now):
                    if self.timeEvents[timeEventsIndex].type == TIME_EVENTS_BLOCK_TYPE:
                        timeEventsBlocked = True
                    else:
                        events.append(self.timeEvents[timeEventsIndex])
                    timeEventsIndex += 1
                
                while not positionEventsBlocked and positionEventsIndex < len(self.positionEvents) and self.positionEvents[positionEventsIndex].condition.met(positionNow):
                    if self.positionEvents[positionEventsIndex].type == POSITION_EVENTS_BLOCK_TYPE:
                        positionEventsBlocked = True
                    else:
                        events.append(self.positionEvents[positionEventsIndex])
                    positionEventsIndex += 1

                for event in events:
                    if event.controller.type != MAIN_CONTROLLER:
                        if event.hasVariable:
                            for i, com in enumerate(event.command):
                                if isinstance(com, Variable):
                                    event.command[i] = com.get(now=now, position=positionNow, pose=poseNow)
                            event.command = event.clean_bytes(event.command)
                            # print(now, positionNow, event.command)
                        if event.controller.type == TOP_CONTROLLER:
                            self.topQueue.put(event.command)
                        elif event.controller.type == BOTTOM_CONTROLLER:
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
                            self.position.value = 0
                        elif event.type == POSITION_EVENTS_UNBLOCK_TYPE:
                            # print(now, positionNow, 'TIME_EVENTS_UNBLOCK_TYPE')
                            positionEventsBlocked = False
                        elif event.type == TIME_EVENTS_UNBLOCK_TYPE:
                            # print(now, positionNow, 'TIME_EVENTS_UNBLOCK_TYPE')
                            timeEventsBlocked = False
                        elif event.type == TIME_EVENTS_CLEAR_TYPE:
                            # print(now, positionNow, 'TIME_EVENTS_CLEAR_TYPE')
                            self.timeEvents = []
                            timeEventsIndex = 0
                        elif event.type == TIME_EVENTS_CLEAR_TO_MARKER_TYPE:
                            self.timeEvents = self.timeEvents[self.timeEvents.index(event.marker)+1:]
                            timeEventsIndex = 0
                        elif event.type == TRIGGER_SET_ANGLE_TYPE and self.usesTrigger:
                            self.triggerQueue.put([1, event.angle])
                        elif event.type == TRIGGER_DETACH_TYPE and self.usesTrigger:
                            self.triggerQueue.put([0,])
                        elif event.type == MOTOR_SPEED_TYPE and self.usesMotor:
                            # print(now, positionNow, 'MOTOR_SPEED_TYPE')
                            with self.targetSpeed.get_lock():
                                self.targetSpeed.value = event.speed
                        elif event.type == MOTOR_DIRECTION_TYPE and self.usesMotor:
                            with self.targetDirection.get_lock():
                                self.targetDirection.value = event.direction
                        elif event.type == MUSIC_START_TYPE and self.music:
                            if self.startTime:
                                st = self.startTime - event.condition.value + event.startTime
                            else:
                                st = event.startTime
                            mixer.music.play(start=st)
                    
                if timeEventsIndex >= len(self.timeEvents) and positionEventsIndex >= len(self.positionEvents):
                    self.shutdown()
                    break

        except Exception as e:
            self.shutdown()
            print('Error:', e)
            exit(-1)