from arduinopwmmanager import ArduinoPwmManager
from encoderreader import EncoderReader
from multiprocessing import Value, Queue
from settings import ARDUINO_UNO_CONN, ARDUINO_MEGA_CONN
from humanposerecognition import COMMANDS
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


def execute_command(element,value):
    if element == 'motor':
        bottomComm.put(int('5'+value))
        # print('bottom', '5'+value)
    else:
        lightid = element.split('-')[1]
        if element.startswith('top'):
            topComm.put(int(lightid + value))
            # print('top', lightid + value)
        else:
            bottomComm.put(int(lightid + value))
            # print('bottom', lightid + value)


def setup():
    bottomComm.put(5000)
    topComm.put(1001)
    topComm.put(2001)
    topComm.put(5001)
    topComm.put(6001)
    bottomComm.put(1000)
    bottomComm.put(2000)


def shutdown():
    bottomComm.put(5000)
    topComm.put(1200)
    topComm.put(2200)
    topComm.put(5200)
    topComm.put(6200)
    bottomComm.put(1200)
    bottomComm.put(2200)


atexit.register(shutdown)


#setup()
time.sleep(15)


try:
    last = time.time()
    i = 0
    while i < len(COMMANDS):
        command = COMMANDS[i]
        if command[0] == 'time':
            if time.time() - last > command[1]:
                for x in command[2:]:
                    execute_command(x[0],x[1])
                i+=1
        elif command[0] == 'pos':
            if position.value > command[1]:
                for x in command[2:]:
                    execute_command(x[0],x[1])
                i+=1
        elif command[0] == 'resettimer':
            last = time.time()
            i+=1
except Exception:
    shutdown()

shutdown()

        

