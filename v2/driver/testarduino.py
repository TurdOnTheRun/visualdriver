from multiprocessing import Process
import time

startByte = bytes([251])
endByte = bytes([252])

class ArduinoPwmManager(Process):

    def __init__(self, commands):
        super().__init__()
        self.daemon = True
        self.commands = commands
    

    def run(self):
        while True:
            command = self.commands.get()
            commandstring = startByte
            for comm in command:
                commandstring += bytes([comm])
            commandstring += endByte
            print(command, commandstring)
            time.sleep(0.004)