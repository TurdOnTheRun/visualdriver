from arduinopwmmanager import ArduinoPwmManager
from encoderreader import EncoderReader
from multiprocessing import Value, Queue
from settings import ARDUINO_UNO_CONN, ARDUINO_MEGA_CONN
from uma import SCRIPT
import time
import atexit

topComm = Queue()
bottomComm = Queue()
position = Value('d', 0.0)
distance = Value('d', 0.0)
er = EncoderReader(position, distance)

top = ArduinoPwmManager(ARDUINO_MEGA_CONN, topComm)
top.start()
bottom = ArduinoPwmManager(ARDUINO_UNO_CONN, bottomComm)
bottom.start()


def execute_step(arduino,step):
    if arduino == 'bottom':
        bottomComm.put(step)
    else:
        topComm.put(step)


def setup():
    bottomComm.put((200,0))
    topComm.put((100,0))
    bottomComm.put((100,20))
    print('Setup Complete!')


def shutdown():
    bottomComm.put((200,0))
    topComm.put((100,50))
    bottomComm.put((100,0))


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
                    execute_step(x[0],x[1])
                i+=1
        elif step[0] == 'pos':
            print(position.value)
            if position.value > step[1]:
                for x in step[2:]:
                    execute_step(x[0],x[1])
                i+=1
        elif step[0] == 'resettimer':
            last = time.time()
            i+=1
except Exception as e:
    print('Error:', e)
    shutdown()
    raise e

print('Finishing')
shutdown()

        

