from arduinopwmmanager import ArduinoPwmManager
from encoderreader import EncoderReader
from trigger import Trigger
from multiprocessing import Value, Queue
from settings import ARDUINO_UNO_CONN, ARDUINO_MEGA_CONN, SONY_TRIGGER
import time
import atexit
import json

INPUT = './scripts/generators/randomlyspacedquickstrobe_TEST2.json'
f = open(INPUT,) 
SCRIPT = json.load(f)
f.close()

topComm = Queue()
bottomComm = Queue()
triggerComm = Queue()
position = Value('d', 0.0)
distance = Value('d', 0.0)
er = EncoderReader(position, distance)

top = ArduinoPwmManager(ARDUINO_MEGA_CONN, topComm)
top.start()
bottom = ArduinoPwmManager(ARDUINO_UNO_CONN, bottomComm)
bottom.start()
trigger = Trigger(SONY_TRIGGER[0], SONY_TRIGGER[1], triggerComm)
trigger.start()


def execute_step(executer,step):

    timereset = None

    if executer == 'bottom':
        bottomComm.put(step)
    elif executer == 'top':
        topComm.put(step)
    elif executer == 'raspy':
        if step[0] == 1:
            triggerComm.put(step[1]/10)
        elif step[0] == 2:
            timereset = True
        elif step[0] == 3:
            triggerComm.put('DOWN')
        elif step[0] == 4:
            triggerComm.put('UP')
    else:
        print('Executer ' + executer + ' not implemented!')
    
    return timereset


def setup():
    bottomComm.put((220,0))
    topComm.put((200,0))
    bottomComm.put((200,0))
    print('Setup Complete!')


def shutdown():
    bottomComm.put((220,0))
    topComm.put((200,50))
    bottomComm.put((200,0))


atexit.register(shutdown)

setup()
time.sleep(5)

try:
    last = time.time()
    i = 0
    while i < len(SCRIPT):
        step = SCRIPT[i]
        # print(step[0:2])
        if step[0] == 'time':
            if time.time() - last > step[1]:
                for x in step[2:]:
                    timereset = execute_step(x[0],x[1])
                    if timereset:
                        last = time.time()
                i+=1
        elif step[0] == 'pos':
            #print(position.value)
            if position.value > step[1]:
                for x in step[2:]:
                    timereset = execute_step(x[0],x[1])
                    if timereset:
                        last = time.time()
                i+=1
except Exception as e:
    print('Error:', e)
    shutdown()
    raise e

print('Finishing')
time.sleep(3)
shutdown()

        

