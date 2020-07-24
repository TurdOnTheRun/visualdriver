import time
import RPi.GPIO as GPIO
from multiprocessing import Process
from settings import ENCODER_PIN, ENCODER_REV_PULSE, ENCODER_READ_INTERVAL, WHEEL_SIZE, RAIL_LENGTH


class EncoderReader(Process):

    def __init__(self, position, distance, forward, lock):
        super().__init__()
        self.daemon = True
        self.position = position
        self.distance = distance
        self.forward = forward
        self.lock = lock
        self.pulses = 0
        self.giop_setup()


    def giop_setup(self):
        print('Setting up encoder...')
        try:
            GPIO.setup(ENCODER_PIN, GPIO.IN, pull_up_down=GPIO.PUD_UP)
            GPIO.add_event_detect(ENCODER_PIN, GPIO.RISING, callback=self.pulse_counter)
        except Exception as e:
            print('Failed to set up encoder:')
            raise e
        else:
            print('Encoder set up!')
    

    def pulse_counter(self):
	    self.pulses += 1
    

    def run(self):

        currentSecs = 0
        previousSecs = 0

        while True:
            currentSecs = time.time()
            if (currentSecs - previousSecs) > ENCODER_READ_INTERVAL:
                previousSecs = currentSecs
                pulsesSince = self.pulses
                self.pulses = 0
                distanceSince = (pulsesSince / ENCODER_REV_PULSE) * WHEEL_SIZE
                positionSince = distanceSince / RAIL_LENGTH
                with self.lock:
                    self.distance.value += distanceSince
                    self.position.value += positionSince
    

    def terminate(self):
        GPIO.cleanup()
        super().terminate()
