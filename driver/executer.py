from multiprocessing import Queue, Value
import pickle
import time

from events import *
from agents import *
from conditions import *

from arduinopwmmanager import ArduinoPwmManager
from encoderreader import EncoderReader
from settings import ARDUINO_UNO_CONN, ARDUINO_MEGA_CONN, ARDUINO_UNO_TRIGGER_ENCODER_CONN


# with open('filename.pickle', 'rb') as handle:
#     eventDict = pickle.load(handle)

# eventDict = topBottomLightTest(30, 50, [[Top1, Bottom1, Top2, Bottom2, Top3, Bottom1, Top4, Bottom2,]])

# eventDict = leftCenterRight(25, (BottomAll, 90, 200), (TopAll, 90, 80), (BottomAll, 90, 200), 2)

# eventDict = flower(100, 3, 6, [(TopAll, 90), (BottomAll, 90)], 4, 0.5)


timeEvents = eventDict.get('time', [])
positionEvents = eventDict.get('position', [])


discharging = open('/sys/class/power_supply/BAT0/status','r').readline().strip().lower()
if discharging != 'discharging':
    inp = input('Laptop is charging...\nTo continue confirm with "go":')
    if inp.lower() != "go":
        exit()


if __name__ == '__main__':

    topQueue = Queue()
    top = ArduinoPwmManager(ARDUINO_MEGA_CONN, topQueue)
    top.start()

    bottomQueue = Queue()
    bottom = ArduinoPwmManager(ARDUINO_UNO_CONN, bottomQueue)
    bottom.start()

    triggerQueue = Queue()
    trigger = ArduinoPwmManager(ARDUINO_UNO_TRIGGER_ENCODER_CONN, triggerQueue)
    trigger.start()

    position = Value('d', 0.0)
    distance = Value('d', 0.0)
    er = EncoderReader(position, distance)
    er.start()

    print('Setting Up...')
    time.sleep(3)
    bottomQueue.put((220,0,50))
    topQueue.put((200,0))
    bottomQueue.put((200,0))
    time.sleep(4)
    print('Setup Complete!')

    timeEventsIndex = 0
    timeEventsBlocked = False
    positionEventsIndex = 0
    positionEventsBlocked = False

    try:
        last = time.time()

        while True:

            events = []
            now = time.time() - last
            positionNow = position.value

            if not timeEventsBlocked and timeEventsIndex < len(timeEvents):
                nextTimeEvent = timeEvents[timeEventsIndex]
                if nextTimeEvent.condition.met(now):
                    events.append(nextTimeEvent)
                    timeEventsIndex += 1
            
            if not positionEventsBlocked and positionEventsIndex < len(positionEvents):
                nextPositionEvent = positionEvents[positionEventsIndex]
                if nextPositionEvent.condition.met(positionNow):
                    events.append(nextPositionEvent)
                    positionEventsIndex += 1

            for event in events:
                if event.agent.controller != MAIN_CONTROLLER:
                    if event.hasVariable:
                        for i, com in enumerate(event.command):
                            if isinstance(com, Variable):
                                event.command[i] = com.get(now=now, position=positionNow)
                        event.command = event.clean_bytes(event.command)
                        # print(now, positionNow, event.command)
                    if event.agent.controller == TOP_CONTROLLER:
                        topQueue.put(event.command)
                    elif event.agent.controller == BOTTOM_CONTROLLER:
                        bottomQueue.put(event.command)
                else:
                    if event.type == TIME_RESET_TYPE:
                        # print(now, positionNow, 'TIME_RESET_TYPE')
                        last = time.time()
                    elif event.type == ADD_EVENTS_TYPE:
                        timeEvents += event.events.get('time', [])
                        positionEvents += event.events.get('position', [])
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
                        timeEvents = []
                        timeEventsIndex = 0
                    elif event.type == TIME_EVENTS_CLEAR_TO_MARKER_TYPE:
                        timeEvents = timeEvents[timeEvents.index(event.marker)+1:]
                        timeEventsIndex = 0
                    elif event.type == TRIGGER_SET_ANGLE_TYPE:
                        triggerQueue.put([1, event.angle])
                    elif event.type == TRIGGER_DETACH_TYPE:
                        triggerQueue.put([0,])
                
            if timeEventsIndex >= len(timeEvents) and positionEventsIndex >= len(positionEvents):
                time.sleep(2)
                break

    except Exception as e:
        bottomQueue.put((220,0,50))
        topQueue.put((200,50))
        bottomQueue.put((200,0))
        print('Error:', e)
        time.sleep(2)
        exit(-1)

print('Finishing')
time.sleep(1)
bottomQueue.put((220,0,50))
topQueue.put((200,50))
bottomQueue.put((200,0))
time.sleep(1)