from multiprocessing import Process
import serial


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
            if type(command) is int and command > 999 and command < 9256:
                command = str(command)
                self.serial.write(bytes('<' + command + ',' + command + '>\n','utf-8'))
            else:
                print('ArduinoPwmManager received invalid command:', command)
