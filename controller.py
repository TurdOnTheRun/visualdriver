from settings import MOTOR_EN_PIN_L, MOTOR_EN_PIN_R, MOTOR_PWM_PIN_L, MOTOR_PWM_PIN_R, MOTOR_PWM_FREQUENCY, MOTOR_START_FORWARD, MOTOR_BREAK_TIME


class MotorController:

    def __init__(self, apm):
        self.apm = apm
        self aid = MOTOR_ARDUINO_ID
        self.speed = 0
        self.forward = MOTOR_START_FORWARD

    def set_speed(self, speed):
        if type(speed) is int and speed > -1 and speed < 256:
            self.apm.put(self.aid + speed)
            self.speed = speed
        else:
            print('MotorController received invalid speed:', speed)
    
    def change_direction(self, forward=None, breaktime=MOTOR_BREAK_TIME):
        pass



    #SHOULDnT the be controlled from outside? 
    def change_direction(self, forward=None, breaktime=MOTOR_BREAK_TIME):
        pass


    def stop(self, breaktime=MOTOR_BREAK_TIME):
        pass
