from multiprocessing import Process
import serial


class ArduinoLightManager(Process):

    def __init__(self, bluetooth, commands):
        super().__init__()
        self.daemon = True
        self.bluetooth = bluetooth
        self.ser = self.connect()
        self.commands = commands
    

    def connect(self):
        print('Connecting to Arduino...')
        try:
            ser = serial.Serial( self.bluetooth, baudrate=9600 )
        except serial.SerialException as e:
            print('Failed to connect to bluetooth:', self.bluetooth)
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
                print('ArduinoLightManager received invalid command:', com)
