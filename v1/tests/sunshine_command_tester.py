import serial
import time
import atexit

from humanposerecognition import COMMANDS

time_now = lambda: int(round(time.time() * 1000))

BAUDRATE = 115200

ser = serial.Serial( "/dev/cu.HC-06-SPPDev", baudrate=BAUDRATE )
# ser = serial.Serial( "/dev/cu.usbmodem1431", baudrate=115200 , timeout=1)

def send_it(command):
    id = command[0]
    state = command[1]
    tostate = command[2]
    steptime = command[3]
    if type(id) is int and type(state) is int and type(tostate) is int and type(steptime) is int:
        command = b'<' + bytes([id]) + bytes([state]) + bytes([tostate]) + bytes([steptime]) + b'>\n'
        ser.write(command)
        time.sleep(0.004)
    else:
        print('ArduinoPwmManager received invalid command:', command)

def setup():
    send_it((255,0,0,0))


def shutdown():
    send_it((255,150,150,0))


atexit.register(shutdown)

setup()
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
                    if x[0] == 'top':
                        send_it(x[1])
                i+=1
except Exception as e:
    print('Error:', e)
    shutdown()
    raise e

print('Finishing')
shutdown()