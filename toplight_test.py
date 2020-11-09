from arduinopwmmanager import ArduinoPwmManager
from settings import ARDUINO_MEGA_CONN
from multiprocessing import Queue
import time

pwmComm = Queue()
pwm = ArduinoPwmManager(ARDUINO_MEGA_CONN, pwmComm)
pwm.start()

brightness = 0
up = True

lights = ['1','2']

start = time.time()

while True:
    strbrightness = str(brightness)
    if len(strbrightness) == 2:
        strbrightness = '0' + strbrightness
    elif len(strbrightness) == 1:
        strbrightness = '00' + strbrightness
    for l in lights:
        pwmComm.put(int(l+strbrightness))
    
    if up:
        if brightness < 255:
            brightness += 10
        else:
            brightness -= 10
            up = False
    else:
        if brightness > 1:
            brightness -= 10
        else:
            brightness += 10
            up = True
    
    if time.time() - start > 10:
        pwmComm.put(1001)
        break