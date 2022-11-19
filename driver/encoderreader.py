import serial
import time
from multiprocessing import Process, Value
from settings import ARDUINO_UNO_TRIGGER_ENCODER_CONN, ENCODER_REV_PULSE, WHEEL_SIZE, RAIL_LENGTH


class EncoderReader(Process):

    def __init__(self, lock, position, distance):
        super().__init__()
        self.daemon = True
        self.serial = self.connect()
        self.positionBuffer = 0
        self.distanceBuffer = 0
        self.lock = lock
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
                self.positionBuffer += self.positionPerPulse
                self.distanceBuffer += self.distancePerPulse
            else:
                self.positionBuffer -= self.positionPerPulse
                self.distanceBuffer -= self.distancePerPulse
            if self.lock.acquire(False):
                self.position.value += self.positionBuffer
                self.distance.value += self.distanceBuffer
                self.lock.release()
                self.positionBuffer = 0
                self.distanceBuffer = 0
