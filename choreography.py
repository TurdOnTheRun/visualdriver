from multiprocessing import Value, Queue
from ctypes import c_char_p
from arduinolightmanager import ArduinoLightManager
import time


class Choreography():

    def __init__(self):
        self.position = Value('i', 0)
        self.direction = Value(c_char_p, 'fwd')
        # build time manager Timer maybe already exists
        # self.time = Value()

alcom = Queue()
al = ArduinoLightManager('test', alcom)
al.start()

for i in range(20):
    alcom.put(1234 + i)
    time.sleep(2)