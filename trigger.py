import pigpio
from time import sleep
from settings import TRIGGER_PIN, MG995_PULSEWIDTHS


class Trigger:
    
    def __init__(self, triggerPW, standbyPW):
        self.triggerPW = self.trimPulseWidth(triggerPW)
        self.standbyPW = self.trimPulseWidth(standbyPW)
        self.pi = pigpio.pi()
        if not self.pi.connected:
            print('Failed to set up Pig Trigger')
            exit()
        self.setPulseWidth(standbyPW)
    
    def trigger(self, triggertime=1):
        self.pi.set_servo_pulsewidth(TRIGGER_PIN, self.triggerPW)
        sleep(triggertime)
        self.pi.set_servo_pulsewidth(TRIGGER_PIN, self.standbyPW)
        sleep(1)
    
    def setPulseWidth(self, pw, triggertime=1):
        pw = self.trimPulseWidth(pw)
        self.pi.set_servo_pulsewidth(TRIGGER_PIN, pw)
        sleep(triggertime)
    
    def trimPulseWidth(self, pw):
        if pw < MG995_PULSEWIDTHS[0]:
            pw = MG995_PULSEWIDTHS[0]
        elif pw > MG995_PULSEWIDTHS[1]:
            pw = MG995_PULSEWIDTHS[1]
        return pw
    
    def shutdown():
        pi.set_servo_pulsewidth(TRIGGER_PIN, 0)
        pi.stop()

        
