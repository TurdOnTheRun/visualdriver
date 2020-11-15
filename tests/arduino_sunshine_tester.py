import serial
import time

time_now = lambda: int(round(time.time() * 1000))

BAUDRATE = 115200

# ser = serial.Serial( "/dev/cu.HC-06-SPPDev", baudrate=BAUDRATE )
ser = serial.Serial( "/dev/cu.usbmodem1431", baudrate=115200 , timeout=1)

def send_it(id, state, tostate, steptime):
	print(id, state, tostate, steptime)
	command = b'<' + bytes([id]) + bytes([state]) + bytes([tostate]) + bytes([steptime]) + b'>'
	ser.write(command)

while True:
    value = input("Please enter a command:\n")
    try:
        commands = value.split(',')
        send_it(int(commands[0]), int(commands[1]), int(commands[2]), int(commands[3]))
    except Exception:
        print('Invalid Command')