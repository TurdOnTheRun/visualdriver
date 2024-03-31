from multiprocessing import Process
import serial
import telnetlib
import time

startByte = bytes([251])
endByte = bytes([252])

class ArduinoPwmManager(Process):

    def __init__(self, conn, commands, shutdownQueue):
        super().__init__()
        self.daemon = True
        self.conn = conn
        self.connection = self.connect()
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
            self.connection.write(commandstring)
            time.sleep(0.004)
#            else:
#                print('ArduinoPwmManager received invalid command:', command)


class ArduinoEspManager(ArduinoPwmManager):


    def connect(self):
        print('Connecting to Arduino...')
        try:
            tn = telnetlib.Telnet(self.conn, 2323)
        except Exception as e:
            print('Failed to connect to esp.')
            raise e
        else:
            print('Connected to Esp!')
        return tn
