from multiprocessing import Process
import serial
import time


class ArduinoPwmManager(Process):

    def __init__(self, conn, commands):
        super().__init__()
        self.daemon = True
        self.conn = conn
        self.serial = self.connect()
        self.commands = commands
    

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
            id = command[0]
            state = command[1]
            tostate = command[2]
            steptime = command[3]
            if type(id) is int and type(state) is int and type(tostate) is int and type(steptime) is int:
                command = b'<' + bytes([id]) + bytes([state]) + bytes([tostate]) + bytes([steptime]) + b'>\n'
                self.serial.write(command)
                time.sleep(0.004)
            else:
                print('ArduinoPwmManager received invalid command:', command)
