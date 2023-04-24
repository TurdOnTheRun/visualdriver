from controllers import MainController
from conditions import At
import random
from kinectreader import LEFT_WRIST, RIGHT_WRIST
from settings import MOTOR_MAXIMUM_SPEED, MOTOR_CLOCKWISE, MOTOR_COUNTERCLOCKWISE


ARDUINO_COMMUNICATION_START_BYTE = 251
ARDUINO_COMMUNICATION_STOP_BYTE = 252

TIME_RESET_TYPE = 0
ADD_EVENTS_TYPE = 1
POSITION_RESET_TYPE = 2
TIME_EVENTS_BLOCK_TYPE = 3
TIME_EVENTS_UNBLOCK_TYPE = 4
TIME_EVENTS_CLEAR_TYPE = 5
TIME_EVENTS_CLEAR_TO_MARKER_TYPE = 6
MARKER_TYPE = 7
TRIGGER_SET_ANGLE_TYPE = 8
TRIGGER_DETACH_TYPE = 9
MOTOR_SPEED_TYPE = 10
MOTOR_DIRECTION_TYPE = 11


class Event:

    def __init__(self, condition, controller=None, hasVariable=False):
        self.condition = condition
        self.controller = controller
        self.hasVariable = hasVariable
    

    def abort(self, message, error=None):
        print(message)
        if error:
            raise error
        else:
            raise Exception

    def __str__(self):
        return 'Event({}, {}, {})'.format(self.condition, self.controller, self.hasVariable)


class Variable:

    def get(self, **kwargs):
        pass


class ArduinoEvent(Event):

    def __init__(self, condition, controller=None, hasVariable=False):
        super().__init__(condition, controller, hasVariable)


    def __str__(self):
        return 'ArduinoEvent({}, {}, {})'.format(self.condition, self.controller, self.hasVariable)
    

    def check_state(self, state):
        if state < 0 or state > 100:
            self.abort('State not in range 0-100')

    def make_lightsbyte(self, lightAgents):
        return sum([la.bitvalue for la in lightAgents])
    
    # Checks if the agent is a light
    def check_is_light_controller(self, controller):
        if not controller or not controller.light:
            self.abort('Controller is not a light controller')
    
    # Checks that all Arduino inputs are in the range of 0 to 255 
    # Replaces the "Start" & "Stop" bytes used for Arduino communication (251 & 252)
    def clean_bytes(self, command):
        cleanedcommand = []
        errorMessage = 'Invalid Command: '

        for byte in command:
            if type(byte) == int and byte >= 0 and byte <= 255:
                if byte == ARDUINO_COMMUNICATION_START_BYTE:
                    byte = 250
                if byte == ARDUINO_COMMUNICATION_STOP_BYTE:
                    byte = 253
                cleanedcommand.append(byte)
            else:
                self.abort(errorMessage + str(byte))

        return cleanedcommand


class StaticLight(ArduinoEvent):

    def __init__(self, condition, controller, lightAgents, state, hasVariable=False):
        super().__init__(condition, controller, hasVariable)
        self.lightsByte = self.make_lightsbyte(lightAgents)
        self.state = state
        if not hasVariable:
            self.check_init()
        self.command = self.make_command()

    def __str__(self):
        return 'StaticLight({}, {}, {}, {}, {})'.format(self.condition, self.controller, self.lightsByte, self.state, self.hasVariable)
    
    def check_init(self):
        self.check_state(self.state)
        self.check_is_light_controller(self.controller)
    
    def make_command(self):
        command = [1, self.lightsByte, self.state]
        if not self.hasVariable:
            return self.clean_bytes(command)
        else:
            return command


class StaticFlash(ArduinoEvent):

    def __init__(self, condition, controller, lightAgents, fromState, toState, onTime, hasVariable=False):
        super().__init__(condition, controller, hasVariable)
        self.lightsByte = self.make_lightsbyte(lightAgents)
        self.fromState = fromState
        self.toState = toState
        self.onTime = onTime
        if not hasVariable:
            self.check_init()
        self.command = self.make_command()

    def __str__(self):
        return 'StaticFlash({}, {}, {}, {}, {}, {}, {})'.format(self.condition, self.controller, self.lightsByte, self.fromState, self.toState, self.onTime, self.hasVariable)
    
    def check_init(self):
        self.check_state(self.fromState)
        self.check_state(self.toState)
        self.check_is_light_controller(self.controller)
    
    def make_command(self):
        command = [2, self.lightsByte, self.fromState, self.toState, self.onTime]
        if not self.hasVariable:
            return self.clean_bytes(command)
        else:
            return command


class StaticMachine(ArduinoEvent):

    def __init__(self, condition, controller, lightAgents, onState, offState, onTime, offTime, repetitions, hasVariable=False):
        self.lightsByte = self.make_lightsbyte(lightAgents)
        self.onState = onState
        self.offState = offState
        self.onTime = onTime
        self.offTime = offTime
        self.repetitions = repetitions
        super().__init__(condition, controller, hasVariable)
        if not hasVariable:
            self.check_init()
        self.command = self.make_command()

    def __str__(self):
        return 'StaticMachine({}, {}, {}, {}, {}, {}, {}, {}, {})'.format(self.condition, self.controller, self.lightsByte, self.onState, self.offState, self.onTime, self.offTime, self.repetitions, self.hasVariable)
    
    def check_init(self):
        self.check_state(self.onState)
        self.check_state(self.offState)
        self.check_is_light_controller(self.controller)
    
    def make_command(self):
        command = [3, self.lightsByte, self.onState, self.offState, self.onTime, self.offTime, self.repetitions]
        if not self.hasVariable:
            return self.clean_bytes(command)
        else:
            return command


class LinearDimm(ArduinoEvent):

    def __init__(self, condition, controller, lightAgents, fromState, toState, steptime, hasVariable=False):
        self.lightsByte = self.make_lightsbyte(lightAgents)
        self.fromState = fromState
        self.toState = toState
        self.steptime = steptime
        super().__init__(condition, controller, hasVariable)
        if not hasVariable:
            self.check_init()
        self.command = self.make_command()

    def __str__(self):
        return 'LinearDimm({}, {}, {}, {}, {}, {}, {})'.format(self.condition, self.controller, self.lightsByte, self.fromState, self.toState, self.steptime, self.hasVariable)
    
    def check_init(self):
        self.check_state(self.fromState)
        self.check_state(self.toState)
        self.check_is_light_controller(self.controller)
    
    def make_command(self):
        command = [10, self.lightsByte, self.fromState, self.toState, self.steptime]
        if not self.hasVariable:
            return self.clean_bytes(command)
        else:
            return command


class BezierDimm(ArduinoEvent):

    def __init__(self, condition, controller, lightAgents, fromState, toState, steptime, decisteps, y1, y2, hasVariable=False):
        self.lightsByte = self.make_lightsbyte(lightAgents)
        self.fromState = fromState
        self.toState = toState
        self.steptime = steptime
        self.decisteps = decisteps
        self.y1 = y1
        self.y2 = y2
        super().__init__(condition, controller, hasVariable)
        if not hasVariable:
            self.check_init()
        self.command = self.make_command()

    def __str__(self):
        return 'BezierDimm({}, {}, {}, {}, {}, {}, {}, {}, {}, {})'.format(self.condition, self.controller, self.lightsByte, self.fromState, self.toState, self.steptime, self.decisteps, self.y1, self.y2, self.hasVariable)
    
    def check_init(self):
        self.check_state(self.fromState)
        self.check_state(self.toState)
        self.check_state(self.y1)
        self.check_state(self.y2)
        self.check_is_light_controller(self.controller)
    
    def make_command(self):
        command = [20, self.lightsByte, self.fromState, self.toState, self.steptime, self.decisteps, self.y1, self.y2]
        if not self.hasVariable:
            return self.clean_bytes(command)
        else:
            return command


# EFFECTS

class UpVibrato(ArduinoEvent):

    def __init__(self, condition, controller, lightAgents, amplitude, steptime, hasVariable=False):
        super().__init__(condition, controller, hasVariable)
        self.lightsByte = self.make_lightsbyte(lightAgents)
        self.amplitude = amplitude
        self.steptime = steptime
        if not hasVariable:
            self.check_init()
        self.command = self.make_command()

    def __str__(self):
        return 'UpVibrato({}, {}, {}, {}, {}, {})'.format(self.condition, self.controller, self.lightsByte, self.amplitude, self.steptime, self.hasVariable)
    
    def check_init(self):
        self.check_state(self.amplitude)
        self.check_is_light_controller(self.controller)
    
    def make_command(self):
        command = [100, self.lightsByte, self.amplitude, self.steptime]
        if not self.hasVariable:
            return self.clean_bytes(command)
        else:
            return command


class DownVibrato(ArduinoEvent):

    def __init__(self, condition, controller, lightAgents, amplitude, steptime, hasVariable=False):
        super().__init__(condition, controller, hasVariable)
        self.lightsByte = self.make_lightsbyte(lightAgents)
        self.amplitude = amplitude
        self.steptime = steptime
        if not hasVariable:
            self.check_init()
        self.command = self.make_command()

    def __str__(self):
        return 'DownVibrato({}, {}, {}, {}, {}, {})'.format(self.condition, self.controller, self.lightsByte, self.amplitude, self.steptime, self.hasVariable)
    
    def check_init(self):
        self.check_state(self.amplitude)
        self.check_is_light_controller(self.controller)
    
    def make_command(self):
        command = [101, self.lightsByte, self.amplitude, self.steptime]
        if not self.hasVariable:
            return self.clean_bytes(command)
        else:
            return command


class UpDownVibrato(ArduinoEvent):

    def __init__(self, condition, controller, lightAgents, amplitude, steptime, hasVariable=False):
        super().__init__(condition, controller, hasVariable)
        self.lightsByte = self.make_lightsbyte(lightAgents)
        self.amplitude = amplitude
        self.steptime = steptime
        if not hasVariable:
            self.check_init()
        self.command = self.make_command()

    def __str__(self):
        return 'UpDownVibrato({}, {}, {}, {}, {}, {})'.format(self.condition, self.controller, self.lightsByte, self.amplitude, self.steptime, self.hasVariable)
    
    def check_init(self):
        self.check_state(self.amplitude)
        self.check_is_light_controller(self.controller)
    
    def make_command(self):
        command = [102, self.lightsByte, self.amplitude, self.steptime]
        if not self.hasVariable:
            return self.clean_bytes(command)
        else:
            return command


class Strobe(ArduinoEvent):

    def __init__(self, condition, controller, lightAgents, amplitude, steptime, steptimeFactor, mutliSettingAgents=[], hasVariable=False):
        super().__init__(condition, controller, hasVariable)
        self.lightsByte = self.make_lightsbyte(lightAgents)
        self.amplitude = amplitude
        self.steptime = steptime
        self.steptimeFactor = steptimeFactor
        self.multiSettingByte = self.make_lightsbyte(mutliSettingAgents)
        if not hasVariable:
            self.check_init()
        self.command = self.make_command()

    def __str__(self):
        return 'Strobe({}, {}, {}, {}, {}, {}, {}, {})'.format(self.condition, self.controller, self.lightsByte, self.amplitude, self.steptime, self.steptimeFactor, self.multiSettingByte, self.hasVariable)
    
    def check_init(self):
        self.check_state(self.amplitude)
        self.check_is_light_controller(self.controller)
    
    def make_command(self):
        command = [110, self.lightsByte, self.amplitude, self.steptime, self.steptimeFactor, self.multiSettingByte]
        if not self.hasVariable:
            return self.clean_bytes(command)
        else:
            return command
        

class ResetEffects(ArduinoEvent):

    def __init__(self, condition, controller, lightAgents):
        super().__init__(condition, controller, False)
        self.lightsByte = self.make_lightsbyte(lightAgents)
        self.check_init()
        self.command = self.make_command()

    def __str__(self):
        return 'ResetEffects({}, {}, {})'.format(self.condition, self.controller, self.lightsByte)
    
    def check_init(self):
        self.check_is_light_controller(self.controller)
    
    def make_command(self):
        command = [190, self.lightsByte]
        if not self.hasVariable:
            return self.clean_bytes(command)
        else:
            return command
        

class RemoveEffect(ArduinoEvent):

    def __init__(self, condition, controller, lightAgents, effectIndex):
        super().__init__(condition, controller, False)
        self.lightsByte = self.make_lightsbyte(lightAgents)
        self.effectIndex = effectIndex
        self.check_init()
        self.command = self.make_command()

    def __str__(self):
        return 'RemoveEffect({}, {}, {}, {})'.format(self.condition, self.controller, self.lightsByte, self.effectIndex)
    
    def check_init(self):
        self.check_is_light_controller(self.controller)
    
    def make_command(self):
        command = [191, self.lightsByte, self.effectIndex]
        if not self.hasVariable:
            return self.clean_bytes(command)
        else:
            return command
    

class MotorSpeed(Event):

    def __init__(self, condition, speed):
        self.type = MOTOR_SPEED_TYPE
        super().__init__(condition, MainController)
        if type(speed) != int or speed < 0:
            self.abort('Invalid speed: ' + str(speed))
        elif speed > MOTOR_MAXIMUM_SPEED:
            self.speed = MOTOR_MAXIMUM_SPEED
        else:
            self.speed = speed


class MotorChangeDirection(Event):

    def __init__(self, condition, direction):
        self.type = MOTOR_DIRECTION_TYPE
        super().__init__(condition, MainController)
        if direction != MOTOR_CLOCKWISE or direction != MOTOR_COUNTERCLOCKWISE:
            self.abort('Invalid direction: ' + str(direction))
        else:
            self.direction = direction


class TriggerAngle(Event):
    def __init__(self, condition, angle):
        self.type = TRIGGER_SET_ANGLE_TYPE
        super().__init__(condition, MainController)
        if type(angle) != int or angle > 180 or angle < 0:
            self.abort('Invalid angle: ' + str(angle))
        else:
            self.angle = angle


class TriggerDetach(Event):
    def __init__(self, condition):
        self.type = TRIGGER_DETACH_TYPE
        super().__init__(condition, MainController)



class Marker(Event):
    def __init__(self, condition):
        self.type = MARKER_TYPE
        super().__init__(condition, MainController)


class TimeReset(Event):

    def __init__(self, condition):
        self.type = TIME_RESET_TYPE
        super().__init__(condition, MainController)


class TimeEventsBlock(Event):

    def __init__(self, condition):
        self.type = TIME_EVENTS_BLOCK_TYPE
        super().__init__(condition, MainController)


class TimeEventsUnblock(Event):

    def __init__(self, condition):
        self.type = TIME_EVENTS_UNBLOCK_TYPE
        super().__init__(condition, MainController)


class TimeEventsClear(Event):

    def __init__(self, condition):
        self.type = TIME_EVENTS_CLEAR_TYPE
        super().__init__(condition, MainController)


class TimeEventsClearToMarker(Event):

    def __init__(self, condition, marker):
        self.type = TIME_EVENTS_CLEAR_TO_MARKER_TYPE
        self.marker = marker
        super().__init__(condition, MainController)


class EventsAdd(Event):

    def __init__(self, condition, events):
        self.type = ADD_EVENTS_TYPE
        if not events or type(events) != dict:
            self.abort('Events in EventsAdd is empty or not a dict')
        self.events = events
        super().__init__(condition, MainController)


class PositionReset(Event):

    def __init__(self, condition):
        self.type = POSITION_RESET_TYPE
        super().__init__(condition, MainController)
