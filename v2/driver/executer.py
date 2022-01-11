from multiprocessing import Queue, Value
import pickle
import time

from events import *
from agents import *
from conditions import *

from arduinopwmmanager import ArduinoPwmManager
from encoderreader import EncoderReader
from trigger import Trigger
from settings import ARDUINO_UNO_CONN, ARDUINO_MEGA_CONN, SONY_TRIGGER


# with open('filename.pickle', 'rb') as handle:
#     eventDict = pickle.load(handle)

# eventDict = {
#     'position': [
#         # TimeEventsBlock(At(0)),
#         # MotorSpeed(At(0), 60, 30),
#         # MotorSpeed(At(0.5), 0, 30),
#         # TimeReset(At(0.5)),
#         # TimeEventsUnblock(At(0.5)),
#         # MotorSpeed(At(1), 0, 30)
#     ],
#     'time': [
#         FlashBezier(At(2), TopAll, 100, 0, 2, 72, 33, 32, 72, 100),
#         # MotorSpeed(At(2), 60, 30)
#     ]
# }

#eventDict = thatFuzz(10, (41, 50), (20,30), [(Top1,100), (Top2,100), (Top3,100), (Top4,100)], (BottomAll, 70))

# eventDict = thatFuzz(10, (41, 50), (20,25), [(Top1, 100), (Top2, 100), (Top3, 100), (Top4, 100)], flipAgentAndState=(BottomAll, 70))

# eventDict = thatSpatialEvolvingFuzz([(0.1,0.05), (0.1,0.05), (0.1,0.1), (0.4, 0.2)], 5, (75, 90), (20,25), [(Top1, 100), (Top2, 100), (Top3, 100), (Top4, 100)], flipAgentAndState=(BottomAll, 70))

# buildUp = thatSpatialEvolvingFuzz([(0.1,0.025), (0.1,0.025), (0.1,0.05)], 5, (75, 90), (20,25), [(Top1, 100), (Top2, 100), (Top3, 100), (Top4, 100)])
buildUp = thatSpatialEvolvingFuzz([(0.1,0.025), (0.1,0.025), (0.1,0.05)], 5, (40, 50), (10,20), [(Top1, 100), (Top2, 100), (Top3, 100), (Top4, 100)])

bigBumps = thatSpatialEvolvingFuzz([(0.4, 0.05), (0.4, 0)], 8, (75, 90), (20,30), [(Top1, 100), (Top2, 100), (Top3, 100), (Top4, 100)], flipAgentAndState=(BottomAll, 70))

eventDict = buildUp
eventDict['position'] += bigBumps['position']
eventDict['time'] += bigBumps['time']

eventDict['position'] = [MotorSpeed(At(0), 70, 30), TimeEventsUnblock(At(0.5))] + eventDict['position']
eventDict['time'] = [TimeEventsBlock(At(0)),] + eventDict['time']


timeEvents = eventDict.get('time', [])
positionEvents = eventDict.get('position', [])

if __name__ == '__main__':

    topQueue = Queue()
    top = ArduinoPwmManager(ARDUINO_MEGA_CONN, topQueue)
    top.start()

    bottomQueue = Queue()
    bottom = ArduinoPwmManager(ARDUINO_UNO_CONN, bottomQueue)
    bottom.start()

    triggerQueue = Queue()
    trigger = Trigger(SONY_TRIGGER[0], SONY_TRIGGER[1], triggerQueue)
    trigger.start()

    position = Value('d', 0.0)
    distance = Value('d', 0.0)
    er = EncoderReader(position, distance)

    print('Setting Up...')
    time.sleep(3)
    bottomQueue.put((220,0))
    topQueue.put((200,0))
    bottomQueue.put((200,0))
    time.sleep(2)
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
                
            if timeEventsIndex >= len(timeEvents) and positionEventsIndex >= len(positionEvents):
                time.sleep(2)
                break

    except Exception as e:
        bottomQueue.put((220,0))
        topQueue.put((200,50))
        bottomQueue.put((200,0))
        print('Error:', e)
        time.sleep(2)
        exit(-1)

print('Finishing')
time.sleep(1)
bottomQueue.put((220,0))
topQueue.put((200,50))
bottomQueue.put((200,0))