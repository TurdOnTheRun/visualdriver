from time import sleep
from arduinopwmmanager import ArduinoPwmManager
from multiprocessing import Queue
from settings import ARDUINO_MEGA_CONN, ARDUINO_UNO_CONN


topPwmComm = Queue()
bottomPwmComm = Queue()
shutdown = Queue()

top = ArduinoPwmManager(ARDUINO_MEGA_CONN, topPwmComm, shutdown)
top.start()

bottom = ArduinoPwmManager(ARDUINO_UNO_CONN, bottomPwmComm, shutdown)
bottom.start()

sleep(1)
topPwmComm.put([192,])
sleep(1)
bottomPwmComm.put([192,])

while True:
    inp = input('Enter "e" when synced:')
    if inp.lower() == "e":
        bottomPwmComm.put([193,])
        sleep(1)
        topPwmComm.put([193,])
        sleep(3)
        exit()
    