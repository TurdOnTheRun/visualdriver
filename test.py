from arduinopwmmanager import ArduinoPwmManager
# from trigger import Trigger
# from encoderreader import EncoderReader
from multiprocessing import Value, Queue
from settings import ARDUINO_MEGA_CONN, ARDUINO_UNO_CONN, SONY_TRIGGER

pwmComm = Queue()
# triggerComm = Queue()
# position = Value('d', 0.0)
# distance = Value('d', 0.0)
# er = EncoderReader(position, distance)

pwm = ArduinoPwmManager(ARDUINO_UNO_CONN, pwmComm)
pwm.start()

# trigger = Trigger(SONY_TRIGGER[0],SONY_TRIGGER[1],triggerComm)
# trigger.start()

while True:
    # print(position.value, distance.value)
    value = input("Please enter a command:\n")
    
    # if value == "trigger":
    #     triggerComm.put(1)
    #     continue
    # if value == "down":
    #     triggerComm.put('DOWN')
    #     continue
    # if value == "up":
    #     triggerComm.put('UP')
    #     continue
    
    try:
        commands = value.split(',')
        command = []
        for c in commands:
            command.append(int(c))
        
    except ValueError:
        print('Invalid Command')
    if command:
        pwmComm.put(command)
    