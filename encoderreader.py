import time
import RPi.GPIO as GPIO
from multiprocessing import Value
from settings import ENCODER_PIN_A, ENCODER_PIN_B, ENCODER_REV_PULSE, ENCODER_READ_INTERVAL, WHEEL_SIZE, RAIL_LENGTH


class EncoderReader():

    def __init__(self, position, distance):
        self.position = position
        self.distance = distance
        self.distancePerPulse = (1 / ENCODER_REV_PULSE) * WHEEL_SIZE
        self.positionPerPulse = self.distancePerPulse / RAIL_LENGTH
        self.giop_setup()

    def giop_setup(self):
        print('Setting up encoder...')
        try:
            GPIO.setmode(GPIO.BCM)
            GPIO.setup(ENCODER_PIN_A, GPIO.IN, pull_up_down=GPIO.PUD_UP)
            GPIO.add_event_detect(ENCODER_PIN_A, GPIO.RISING, callback=self.pulse_interpreter)
            GPIO.setup(ENCODER_PIN_B, GPIO.IN, pull_up_down=GPIO.PUD_UP)
            GPIO.add_event_detect(ENCODER_PIN_B, GPIO.RISING, callback=self.pulse_interpreter)
        except Exception as e:
            print('Failed to set up encoder:')
            raise e
        else:
            print('Encoder set up!')
    
    def pulse_interpreter(self, _):
        with self.position.get_lock():
            self.position.value += self.positionPerPulse
        with self.distance.get_lock():
            self.distance.value += self.distancePerPulse
