from arduinopwmmanager import ArduinoPwmManager
from multiprocessing import Queue


if __name__ == '__main__':

    pwmComm = Queue()
    pwm = ArduinoPwmManager('/dev/tty.usbmodem14141', pwmComm)
    pwm.start()


    while True:
        value = input("Please enter a command:\n")
        
        try:
            commands = value.split(',')
            command = []
            for c in commands:
                command.append(int(c))
            
        except ValueError:
            print('Invalid Command')
        if command:
            pwmComm.put(command)
    