from multiprocessing import Process
import serial
import time

startByte = bytes([251])
endByte = bytes([252])

class ArduinoPwmManager(Process):

    def __init__(self, conn, commands, shutdownQueue):
        super().__init__()
        self.daemon = True
        self.conn = conn
        self.serial = self.connect()
        self.commands = commands
        self.shutdownQueue = shutdownQueue
    

    def connect(self):
        print('Connecting to Arduino...')
        try:
            ser = serial.Serial( self.conn, baudrate=115200 )
        except serial.SerialException as e:
            print('Failed to connect to arduino:', self.conn)
            raise e
        else:
            print('Connected to Arduino!')
        return ser
    

    def run(self):
        while True:
            command = self.commands.get()
            commandstring = startByte
            for comm in command:
                commandstring += bytes([comm])
            commandstring += endByte
            self.serial.write(commandstring)
            time.sleep(0.004)
#            else:
#                print('ArduinoPwmManager received invalid command:', command)
