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


def execute_command(arduino,command):
    if arduino == 'bottom':
        bottomComm.put(command)
    else:
        topComm.put(command)


def setup():
    bottomComm.put((200,0,0,0))
    topComm.put((255,0,0,0))
    bottomComm.put((255,0,0,0))
    print('Setup Complete!')


def shutdown():
    bottomComm.put((200,0,0,0))
    topComm.put((255,150,150,0))
    bottomComm.put((255,0,0,0))


atexit.register(shutdown)


#setup()
time.sleep(15)


try:
    last = time.time()
    i = 0
    while i < len(COMMANDS):
        command = COMMANDS[i]
        # print(command[0:2])
        if command[0] == 'time':
            if time.time() - last > command[1]:
                for x in command[2:]:
                    execute_command(x[0],x[1])
                i+=1
        elif command[0] == 'pos':
            print(position.value)
            if position.value > command[1]:
                for x in command[2:]:
                    execute_command(x[0],x[1])
                i+=1
        elif command[0] == 'resettimer':
            last = time.time()
            i+=1
except Exception as e:
    print('Error:', e)
    shutdown()
    raise e

print('Finishing')
shutdown()

        

