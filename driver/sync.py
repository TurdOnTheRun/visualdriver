from time import sleep
from arduinopwmmanager import ArduinoPwmManager, ArduinoEspManager
from multiprocessing import Queue
from settings import ARDUINO_MEGA_CONN, ARDUINO_UNO_CONN


topPwmComm = Queue()
bottomPwmComm = Queue()
shutdown = Queue()

top = ArduinoEspManager(ARDUINO_MEGA_CONN, topPwmComm, shutdown)
top.start()

bottom = ArduinoPwmManager(ARDUINO_UNO_CONN, bottomPwmComm, shutdown)
bottom.start()

sleep(1)
topPwmComm.put([192,])
bottomPwmComm.put([192,])

sleep(3.4)
bottomPwmComm.put([193,])
sleep(0.4)
topPwmComm.put([193,])
sleep(3)
    