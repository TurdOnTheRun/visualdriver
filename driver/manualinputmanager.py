from multiprocessing import Process
import time

startByte = bytes([251])
endByte = bytes([252])

class ManualInputManager(Process):

    def __init__(self, commands):
        super().__init__()
        self.daemon = True
        self.commands = commands

    def run(self):
        while True:
            command = input("Enter command:")
            if command:
                self.commands.put(command)
