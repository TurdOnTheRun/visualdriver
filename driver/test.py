from arduinopwmmanager import ArduinoPwmManager
from encoderreader import EncoderReader
from multiprocessing import Value, Queue, Lock
from settings import ARDUINO_MEGA_CONN, ARDUINO_UNO_CONN

discharging = open('/sys/class/power_supply/BAT0/status','r').readline().strip().lower()
if discharging != 'discharging':
    inp = input('Laptop is charging...\nTo continue confirm with "go":')
    if inp.lower() != "go":
        exit()

pwmComm = Queue()
shutdown = Queue()
encoderLock = Lock()
position = Value('d', 0.0)
distance = Value('d', 0.0)
er = EncoderReader(encoderLock, position, distance, shutdown)
er.start()

pwm = ArduinoPwmManager(ARDUINO_UNO_CONN, pwmComm, shutdown)
pwm.start()

while True:
    with encoderLock:
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
    