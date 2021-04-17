import serial
import time

time_now = lambda: int(round(time.time() * 1000))

BAUDRATE = 115200
startByte = bytes([251])
endByte = bytes([252])

ser = serial.Serial( "/dev/cu.HC-06-SPPDev", baudrate=BAUDRATE )
# ser = serial.Serial( "/dev/cu.usbmodem1431", baudrate=115200 , timeout=1)

def send_it(id, state, steptime):
	print(id, state, steptime)
	if steptime:
		command = startByte + bytes([id]) + bytes([state]) + bytes([steptime]) + endByte
	else:
		command = startByte + bytes([id]) + bytes([state]) + endByte
	ser.write(command)

while True:
    value = input("Please enter a command:\n")
    try:
        commands = value.split(',')
        id = int(commands[0])
        if len(commands) > 1:
        	state = int(commands[1])
        if len(commands) > 2:
        	steptime = int(commands[2])
        else:
        	steptime = None
        send_it(id, state, steptime)
    except Exception as e:
        print('Invalid Command')
        raise e