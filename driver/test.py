from arduinopwmmanager import ArduinoPwmManager
from encoderreader import EncoderReader
from multiprocessing import Value, Queue
from settings import ARDUINO_MEGA_CONN, ARDUINO_UNO_CONN

pwmComm = Queue()
position = Value('d', 0.0)
distance = Value('d', 0.0)
er = EncoderReader(position, distance)
er.start()

pwm = ArduinoPwmManager(ARDUINO_UNO_CONN, pwmComm)
pwm.start()

while True:
    print(position.value, distance.value)
    value = input("Please enter a command:\n")
    
    try:
        commands = value.split(',')
        command = []
        for c in commands:
            command.append(int(c))
        
    except ValueError:
        print('Invalid Command')
        pwmComm.put([220,0,50])
    if command:
        pwmComm.put(command)
    