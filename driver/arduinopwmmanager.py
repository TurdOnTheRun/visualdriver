from multiprocessing import Process
import serial
import socket
import time

startByte = bytes([251])
endByte = bytes([252])

class ArduinoPwmManager(Process):

    def __init__(self, conn, commands, shutdownQueue):
        super().__init__()
        self.daemon = True
        self.conn = conn
        self.commands = commands
        self.shutdownQueue = shutdownQueue
    

    def connect(self):
        print('Connecting to Arduino...')
        try:
            self.connection = serial.Serial( self.conn, baudrate=115200 )
        except serial.SerialException as e:
            print('Failed to connect to arduino:', self.conn)
            raise e
        else:
            print('Connected to Arduino!')
    

    def send_commandstring(self, commandstring):
        self.connection.write(commandstring)


    def shutdown(self):
        self.connection.close()


    def run(self):
        while True:
            command = self.commands.get()
            commandstring = startByte
            try:
                for comm in command:
                    commandstring += bytes([comm])
            except ValueError as e:
                print(e)
                continue
            commandstring += endByte
            self.send_commandstring(commandstring)
            time.sleep(0.004)
#            else:
#                print('ArduinoPwmManager received invalid command:', command)


class ArduinoEspManager(ArduinoPwmManager):


    def connect(self):
        print('Connecting to Esp...')
        try:
            self.connection = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            self.connection.connect((self.conn, 2323))
        except Exception as e:
            print('Failed to connect to Esp.')
            raise e
        else:
            print('Connected to Esp!')


    def send_commandstring(self, commandstring):
        self.connection.send(commandstring)
