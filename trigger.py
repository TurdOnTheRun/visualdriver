from multiprocessing import Process
import pigpio
from time import sleep
from settings import TRIGGER_PIN, MG995_PULSEWIDTHS


class Trigger(Process):
    
    def __init__(self, triggerPW, standbyPW, commands):
        super().__init__()
        self.daemon = True
        self.triggerPW = self.trimPulseWidth(triggerPW)
        self.standbyPW = self.trimPulseWidth(standbyPW)
        self.commands = commands
        self.pi = pigpio.pi()
        if not self.pi.connected:
            print('Failed to set up Pig Trigger')
            exit()
        self.setPulseWidth(standbyPW)

    def run(self):
        while True:
            command = self.commands.get()
            if type(command) == int or type(command) == float:
                self.trigger(command)
    
    def trigger(self, triggertime=1):
        self.pi.set_servo_pulsewidth(TRIGGER_PIN, self.triggerPW)
        sleep(triggertime)
        self.pi.set_servo_pulsewidth(TRIGGER_PIN, self.standbyPW)
        sleep(0.6)
    
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
    
    def shutdown(self):
        self.pi.set_servo_pulsewidth(TRIGGER_PIN, 0)
        self.pi.stop()

        
