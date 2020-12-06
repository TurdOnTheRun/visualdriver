from encoderreader import EncoderReader
from multiprocessing import Value,Lock
import time

position = Value('d', 0.0)
distance = Value('d', 0.0)
er = EncoderReader(position, distance)

while True:
    print(position.value, distance.value)
    time.sleep(0.1)