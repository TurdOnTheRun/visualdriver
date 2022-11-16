from arduinopwmmanager import ArduinoPwmManager
from multiprocessing import Queue
from settings import ARDUINO_UNO_TRIGGER_ENCODER_CONN

pwmComm = Queue()

pwm = ArduinoPwmManager(ARDUINO_UNO_TRIGGER_ENCODER_CONN, pwmComm)
pwm.start()

while True:
    value = input("Please enter a command:\n")
    
    try:
        commands = value.split(',')
        command = []
        for c in commands:
            command.append(int(c))
        
    except ValueError:
        print('Invalid Command')
    if command:
        pwmComm.put(command)
    