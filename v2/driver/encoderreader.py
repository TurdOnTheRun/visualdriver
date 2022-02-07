import serial
import time
from multiprocessing import Process, Value
from settings import ARDUINO_UNO_TRIGGER_ENCODER_CONN, ENCODER_REV_PULSE, ENCODER_READ_INTERVAL, WHEEL_SIZE, RAIL_LENGTH


class EncoderReader(Process):

    def __init__(self, position, distance):
        super().__init__()
        self.daemon = True
        self.serial = self.connect()
        self.position = position
        self.distance = distance
        self.distancePerPulse = (1 / ENCODER_REV_PULSE) * WHEEL_SIZE
        self.positionPerPulse = self.distancePerPulse / RAIL_LENGTH


    def connect(self):
        print('Connecting to Encoder...')
        try:
            ser = serial.Serial( ARDUINO_UNO_TRIGGER_ENCODER_CONN, baudrate=115200 )
        except serial.SerialException as e:
            print('Failed to connect to Encoder:', ARDUINO_UNO_TRIGGER_ENCODER_CONN)
            raise e
        else:
            print('Connected to Encoder!')
        return ser


    def run(self):
        self.serial.flushInput()
        while True:
            b = self.serial.read()
            i = int.from_bytes(b, byteorder='little', signed=True)
            if i > 0:
                with self.position.get_lock():
                    self.position.value += self.positionPerPulse
                with self.distance.get_lock():
                    self.distance.value += self.distancePerPulse
            else:
                with self.position.get_lock():
                    self.position.value -= self.positionPerPulse
                with self.distance.get_lock():
                    self.distance.value -= self.distancePerPulse


# position = Value('d', 0.0)
# distance = Value('d', 0.0)
# er = EncoderReader(position, distance)
# er.start()

# from arduinopwmmanager import ArduinoPwmManager
# from multiprocessing import Queue
# q = Queue()
# trigger = ArduinoPwmManager(ARDUINO_UNO_TRIGGER_ENCODER_CONN, q)
# trigger.start()
# while True:
#     q.put((1, 90))
#     time.sleep(2)
#     q.put((1,120))
#     time.sleep(2)
#     print(position.value)
#     print(distance.value)
# time.sleep(100)