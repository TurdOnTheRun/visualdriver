import RPi.GPIO as GPIO
from settings import MOTOR_EN_PIN_L, MOTOR_EN_PIN_R, MOTOR_PWM_PIN_L, MOTOR_PWM_PIN_R, MOTOR_PWM_FREQUENCY, MOTOR_START_FORWARD, MOTOR_BREAK_TIME


class MotorController:

    def __init__(self):
        self.speed = 0
        self.forward = MOTOR_START_FORWARD
        self.forwardPWM, self.backwardPWM = self.giop_setup()
        if self.forward:
            self.currentPWM = self.forwardPWM
        else:
            self.currentPWM = self.backwardPWM
    

    def giop_setup(self):
        if self.forward:
            GPIO.setup(MOTOR_EN_PIN_R, GPIO.OUT, initial=GPIO.HIGH)
            GPIO.setup(MOTOR_EN_PIN_L, GPIO.OUT, initial=GPIO.LOW)
        else:
            GPIO.setup(MOTOR_EN_PIN_R, GPIO.OUT, initial=GPIO.LOW)
            GPIO.setup(MOTOR_EN_PIN_L, GPIO.OUT, initial=GPIO.HIGH)
        GPIO.setup(MOTOR_PWM_PIN_R, GPIO.OUT, initial=GPIO.LOW)
        GPIO.setup(MOTOR_PWM_PIN_L, GPIO.OUT, initial=GPIO.LOW)
        forwardPWM = GPIO.PWM(MOTOR_PWM_PIN_R, MOTOR_PWM_FREQUENCY)
        backwardPWM = GPIO.PWM(MOTOR_PWM_PIN_L, MOTOR_PWM_FREQUENCY)
        return (forwardPWM, backwardPWM)
    

    def set_speed(self, speed):
        if type(speed) is int and speed > -1 and speed < 256:
            self.currentPWM.ChangeDutyCycle(speed)
            self.speed = speed
        else:
            print('MotorController received invalid speed:', speed)
    



    #SHOULDnT the be controlled from outside? 
    def change_direction(self, forward=None, breaktime=MOTOR_BREAK_TIME):
        pass


    def stop(self, breaktime=MOTOR_BREAK_TIME):
        pass


