import RPi.GPIO as GPIO
from time import sleep
from settings import TRIGGER_PIN


class Trigger:
    
    def __init__(self, triggerAngle, standbyAngle):
        self.triggerDuty = triggerAngle / 18 + 2
        self.standbyDuty = standbyAngle / 18 + 2
        GPIO.setmode(GPIO.BCM)
        GPIO.setup(TRIGGER_PIN, GPIO.OUT)
        self.servo=GPIO.PWM(TRIGGER_PIN, 50)
        self.servo.start(0)
        self.setAngle(standbyAngle)
    
    def trigger(self, triggertime=1):
        GPIO.output(TRIGGER_PIN, True)
        self.servo.ChangeDutyCycle(self.triggerDuty)
        sleep(triggertime)
        self.servo.ChangeDutyCycle(self.standbyDuty)
        sleep(1)
#         GPIO.output(TRIGGER_PIN, False)
#         self.servo.ChangeDutyCycle(0)
    
    def setAngle(self, angle, triggertime=1):
        duty = angle / 18 + 2
        GPIO.output(TRIGGER_PIN, True)
        self.servo.ChangeDutyCycle(duty)
        sleep(triggertime)
#         GPIO.output(TRIGGER_PIN, False)
#         self.servo.ChangeDutyCycle(0)
        