from arduinopwmmanager import ArduinoPwmManager
from encoderreader import EncoderReader
from kinectreader import KinectReader
from multiprocessing import Value, Queue, Lock
import queue
import time
from settings import ARDUINO_MEGA_CONN, ARDUINO_UNO_CONN

kinectLock = Lock()
kinectQueue = Queue()
kr = KinectReader(kinectLock, kinectQueue)
kr.start()


while True:

    with kinectLock:
        try:
            poseNow = kinectQueue.get(False)
            print(poseNow)
        except queue.Empty:
            print('Nothing to show here')
    
    time.sleep(2)