

class Light:

    def __init__(self, id, intensity=0):
        self.id = id
        self.intensity = intensity
        self.name = 'Light'

    def __repr__(self):
        return self.name


class ArduinoLight(Light):

    def __init__(self, id, apm, intensity=0):
        #apm: Queue shared with the ArduinoPwmManager

        if type(id) is not int:
            raise ArduinoLightError(message='Id has to be integer not ' + type(id))
        if id < 1 or id > 9:
            raise ArduinoLightError(message='Id is out of range: ' + str(id))
        if 'HC-06' not in apm.conn:
            if id > 3:
                raise ArduinoLightError(message='Id is out of range: ' + str(id))
        super().__init__(id, intensity)
        self.name = 'ArduinoLight-' + str(id)
        self.apm = apm
        self.aid = id * 1000
    

    def set_intensity(self, intensity):
        self.apm.put(self.aid + intensity)
        self.intensity = intensity


class ArduinoLightError(Exception):
    """Exception raised for errors in ArduinoLight setup.

    Attributes:
        message -- explanation of the error
    """

    def __init__(self, message="There is an error with an ArduinoLight"):
        self.message = message
        super().__init__(self.message)


# Does not work
class RaspberryLight(Light):

    def __init__(self, id, pin, intensity=0):
        super().__init__(id, intensity)
        self.name = 'CameraLight-' + str(id)
        self.pin = pin
    

    def set_intensity(self, intensity):
        self.pin.ChangeDutyCycle(intensity)
        self.intensity = intensity
