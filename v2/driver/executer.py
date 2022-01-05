from multiprocessing import Queue
import time

from effects import *
from agents import *
from conditions import *
from testarduino import ArduinoPwmManager

TIMEEVENTS = [
    Instant(Time(2), TopAll, 100),
    Instant(Time(4), TopAll, 0),
    Instant(Time(8), TopAll, 50)
]
TIMEEVENTSINDEX = 0

if __name__ == '__main__':

    topQueue = Queue()
    top = ArduinoPwmManager(topQueue)
    top.start()

    try:
        last = time.time()

        while True:

            nextTimeEvent = TIMEEVENTS[TIMEEVENTSINDEX]
            if nextTimeEvent.condition.met(time.time() - last):
                if nextTimeEvent.agent.controller == TOP_CONTROLLER:
                    topQueue.put(nextTimeEvent.command)
                # elif nextTimeEvent.agent.controller == BOTTOM_CONTROLLER:
                TIMEEVENTSINDEX += 1
                
            if TIMEEVENTSINDEX == len(TIMEEVENTS):
                time.sleep(2)
                break

    except Exception as e:
        print('Error:', e)
        raise e