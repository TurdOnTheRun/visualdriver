from arduinopwmmanager import ArduinoPwmManager
from speedcontroller import SpeedController
from encoderreader import EncoderReader
from multiprocessing import Value, Queue, Lock
from settings import ARDUINO_MEGA_CONN, ARDUINO_UNO_CONN

discharging = open('/sys/class/power_supply/BAT0/status','r').readline().strip().lower()
if discharging != 'discharging':
    inp = input('Laptop is charging...\nTo continue confirm with "go":')
    if inp.lower() != "go":
        exit()

shutdown = Queue()
pwmComm = Queue()

encoderLock = Lock()
position = Value('d', 0.0)
distance = Value('d', 0.0)
er = EncoderReader(encoderLock, position, distance, shutdown)
er.start()

speed = Value('d', 0.0)
targetSpeed = Value('i', 0)
sc = SpeedController(speed, targetSpeed, encoderLock, distance, pwmComm, shutdown)
sc.start()

pwm = ArduinoPwmManager(ARDUINO_UNO_CONN, pwmComm, shutdown)
pwm.start()

while True:
    # with encoderLock:
    #     print(position.value, distance.value)
    value = input("Please enter a command:\n")
    command = None
    
    try:
        commands = value.split(',')
        if len(commands) == 1:
            if commands[0] == 's':
                shutdown.put(1234)
            else:
                targetSpeed.value = int(commands[0])
            continue
        else:
            command = []
            for c in commands:
                command.append(int(c))
    except Exception as e:
        print('Invalid Command')
        print(e)
        pwmComm.put([220,0,50])
        continue
    if command:
        pwmComm.put(command)
