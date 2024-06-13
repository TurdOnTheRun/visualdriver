from multiprocessing import Process
import queue
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
        self.commandstring = b''
    

    def connect(self):
        print('Connecting to Arduino...')
        try:
            self.connection = serial.Serial( self.conn, baudrate=115200 )
        except serial.SerialException as e:
            print('Failed to connect to arduino:', self.conn)
            raise e
        else:
            print('Connected to Arduino!')
    

    def send_commandstring(self):
        self.connection.write(self.commandstring)
        self.commandstring = b''
        time.sleep(0.005)


    def shutdown(self):
        self.connection.close()


    def run(self):

        while True:
            try:
                command = self.commands.get_nowait()
            except queue.Empty:
                if self.commandstring:
                    self.send_commandstring()
                command = self.commands.get()
                
            if len(self.commandstring) + len(command) + 2 > 64: #buffer size of Serial is 64
                self.send_commandstring()
                
            try:
                self.commandstring += startByte
                for comm in command:
                    self.commandstring += bytes([comm])
                self.commandstring += endByte
            except ValueError as e:
                print(e)
                self.commandstring = b''


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


    def send_commandstring(self):
        self.connection.send(self.commandstring)
        self.commandstring = b''
        time.sleep(0.005)
