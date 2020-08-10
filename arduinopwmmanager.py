from multiprocessing import Process
import serial


class ArduinoPwmManager(Process):

    def __init__(self, conn, commands):
        super().__init__()
        self.daemon = True
        self.conn = conn
        self.ser = self.connect()
        self.commands = commands
    

    def connect(self):
        print('Connecting to Arduino...')
        try:
            ser = serial.Serial( self.conn, baudrate=9600 )
        except serial.SerialException as e:
            print('Failed to connect to arduino:', self.conn)
            raise e
        else:
            print('Connected to Arduino!')
        return ser
    

    def run(self):
        while True:
            com = self.commands.get()
            if type(com) is int and com > 999 and com < 9256:
                self.ser.write(bytes(str(com) + '\n','utf-8'))
            else:
                print('ArduinoPwmManager received invalid command:', com)
