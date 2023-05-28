from controllers import MainController
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


class LightSetChannel(ArduinoEvent):

    def __init__(self, condition, controller, lightAgents, channel, hasVariable=False):
        super().__init__(condition, controller, hasVariable)
        self.lightsByte = self.make_lightsbyte(lightAgents)
        self.channel = channel
        if not hasVariable:
            self.check_init()
        self.command = self.make_command()

    def __str__(self):
        return 'LightSetChannel({}, {}, {}, {})'.format(self.condition, self.controller, self.lightsByte, self.channel)
    
    def check_init(self):
        self.check_is_light_controller(self.controller)
    
    def make_command(self):
        command = [150, self.lightsByte, self.channel.id]
        if not self.hasVariable:
            return self.clean_bytes(command)
        else:
            return command


class ChannelSetSetting(ArduinoEvent):

    def __init__(self, condition, controller, channel, settingIndex, hasVariable=False):
        super().__init__(condition, controller, hasVariable)
        self.channel = channel
        self.setting = settingIndex
        if not hasVariable:
            self.check_init()
        self.command = self.make_command()

    def __str__(self):
        return 'ChannelSetSetting({}, {}, {}, {})'.format(self.condition, self.controller, self.channel, self.setting)
    
    def check_init(self):
        self.check_is_light_controller(self.controller)
    
    def make_command(self):
        command = [160, self.channel.id, self.setting]
        if not self.hasVariable:
            return self.clean_bytes(command)
        else:
            return command
        

class ChannelSetChannel(ArduinoEvent):

    def __init__(self, condition, controller, targetChannel, sourceChannel, hasVariable=False):
        super().__init__(condition, controller, hasVariable)
        self.targetChannel = targetChannel
        self.sourceChannel = sourceChannel
        if not hasVariable:
            self.check_init()
        self.command = self.make_command()

    def __str__(self):
        return 'ChannelSetChannel({}, {}, {}, {})'.format(self.condition, self.controller, self.targetChannel, self.sourceChannel)
    
    def check_init(self):
        self.check_is_light_controller(self.controller)
    
    def make_command(self):
        command = [161, self.targetChannel.id, self.sourceChannel.id]
        if not self.hasVariable:
            return self.clean_bytes(command)
        else:
            return command


class ChannelAddEffect(ArduinoEvent):

    def __init__(self, condition, controller, channel, effectIndex, channelEffectIndex, hasVariable=False):
        super().__init__(condition, controller, hasVariable)
        self.channel = channel
        self.effectIndex = effectIndex
        self.channelEffectIndex = channelEffectIndex
        if not hasVariable:
            self.check_init()
        self.command = self.make_command()

    def __str__(self):
        return 'ChannelAddEffect({}, {}, {}, {}, {})'.format(self.condition, self.controller, self.channel, self.effectIndex, self.channelEffectIndex)
    
    def check_init(self):
        self.check_is_light_controller(self.controller)
    
    def make_command(self):
        command = [170, self.channel.id, self.effectIndex, self.channelEffectIndex]
        if not self.hasVariable:
            return self.clean_bytes(command)
        else:
            return command


class ChannelRemoveEffect(ArduinoEvent):

    def __init__(self, condition, controller, channel, channelEffectIndex, hasVariable=False):
        super().__init__(condition, controller, hasVariable)
        self.channel = channel
        self.channelEffectIndex = channelEffectIndex
        if not hasVariable:
            self.check_init()
        self.command = self.make_command()

    def __str__(self):
        return 'ChannelRemoveEffect({}, {}, {}, {})'.format(self.condition, self.controller, self.channel, self.channelEffectIndex)
    
    def check_init(self):
        self.check_is_light_controller(self.controller)
    
    def make_command(self):
        command = [171, self.channel.id, self.channelEffectIndex]
        if not self.hasVariable:
            return self.clean_bytes(command)
        else:
            return command


class ChannelRemoveEffects(ArduinoEvent):

    def __init__(self, condition, controller, channel, hasVariable=False):
        super().__init__(condition, controller, hasVariable)
        self.channel = channel
        if not hasVariable:
            self.check_init()
        self.command = self.make_command()

    def __str__(self):
        return 'ChannelRemoveEffects({}, {}, {})'.format(self.condition, self.controller, self.channel)
    
    def check_init(self):
        self.check_is_light_controller(self.controller)
    
    def make_command(self):
        command = [172, self.channel.id]
        if not self.hasVariable:
            return self.clean_bytes(command)
        else:
            return command


class ChannelsReset(ArduinoEvent):

    def __init__(self, condition, controller):
        super().__init__(condition, controller, False)
        self.check_init()
        self.command = self.make_command()

    def __str__(self):
        return 'ChannelsReset({}, {})'.format(self.condition, self.controller)
    
    def check_init(self):
        self.check_is_light_controller(self.controller)
    
    def make_command(self):
        command = [182,]
        return self.clean_bytes(command)


class SettingStaticLight(ArduinoEvent):

    def __init__(self, condition, controller, settingIndex, state, hasVariable=False):
        super().__init__(condition, controller, hasVariable)
        self.settingIndex = settingIndex
        self.state = state
        if not hasVariable:
            self.check_init()
        self.command = self.make_command()

    def __str__(self):
        return 'SettingStaticLight({}, {}, {}, {}, {})'.format(self.condition, self.controller, self.settingIndex, self.state, self.hasVariable)
    
    def check_init(self):
        self.check_state(self.state)
        self.check_is_light_controller(self.controller)
    
    def make_command(self):
        command = [1, self.settingIndex, self.state]
        if not self.hasVariable:
            return self.clean_bytes(command)
        else:
            return command


class SettingStaticFlash(ArduinoEvent):

    def __init__(self, condition, controller, settingIndex, fromState, toState, onTime, hasVariable=False):
        super().__init__(condition, controller, hasVariable)
        self.settingIndex = self.settingIndex
        self.fromState = fromState
        self.toState = toState
        self.onTime = onTime
        if not hasVariable:
            self.check_init()
        self.command = self.make_command()

    def __str__(self):
        return 'SettingStaticFlash({}, {}, {}, {}, {}, {}, {})'.format(self.condition, self.controller, self.settingIndex, self.fromState, self.toState, self.onTime, self.hasVariable)
    
    def check_init(self):
        self.check_state(self.fromState)
        self.check_state(self.toState)
        self.check_is_light_controller(self.controller)
    
    def make_command(self):
        command = [2, self.settingIndex, self.fromState, self.toState, self.onTime]
        if not self.hasVariable:
            return self.clean_bytes(command)
        else:
            return command


class SettingStaticMachine(ArduinoEvent):

    def __init__(self, condition, controller, settingIndex, onState, offState, onTime, offTime, repetitions, hasVariable=False):
        self.settingIndex = settingIndex
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
        return 'SettingStaticMachine({}, {}, {}, {}, {}, {}, {}, {}, {})'.format(self.condition, self.controller, self.settingIndex, self.onState, self.offState, self.onTime, self.offTime, self.repetitions, self.hasVariable)
    
    def check_init(self):
        self.check_state(self.onState)
        self.check_state(self.offState)
        self.check_is_light_controller(self.controller)
    
    def make_command(self):
        command = [3, self.settingIndex, self.onState, self.offState, self.onTime, self.offTime, self.repetitions]
        if not self.hasVariable:
            return self.clean_bytes(command)
        else:
            return command


class SettingLinearDimm(ArduinoEvent):

    def __init__(self, condition, controller, settingIndex, fromState, toState, steptime, hasVariable=False):
        self.settingIndex = settingIndex
        self.fromState = fromState
        self.toState = toState
        self.steptime = steptime
        super().__init__(condition, controller, hasVariable)
        if not hasVariable:
            self.check_init()
        self.command = self.make_command()

    def __str__(self):
        return 'SettingLinearDimm({}, {}, {}, {}, {}, {}, {})'.format(self.condition, self.controller, self.settingIndex, self.fromState, self.toState, self.steptime, self.hasVariable)
    
    def check_init(self):
        self.check_state(self.fromState)
        self.check_state(self.toState)
        self.check_is_light_controller(self.controller)
    
    def make_command(self):
        command = [10, self.settingIndex, self.fromState, self.toState, self.steptime]
        if not self.hasVariable:
            return self.clean_bytes(command)
        else:
            return command


class SettingBezierDimm(ArduinoEvent):

    def __init__(self, condition, controller, settingIndex, fromState, toState, steptime, decisteps, y1, y2, hasVariable=False):
        self.settingIndex = settingIndex
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
        return 'SettingBezierDimm({}, {}, {}, {}, {}, {}, {}, {}, {}, {})'.format(self.condition, self.controller, self.settingIndex, self.fromState, self.toState, self.steptime, self.decisteps, self.y1, self.y2, self.hasVariable)
    
    def check_init(self):
        self.check_state(self.fromState)
        self.check_state(self.toState)
        self.check_state(self.y1)
        self.check_state(self.y2)
        self.check_is_light_controller(self.controller)
    
    def make_command(self):
        command = [20, self.settingIndex, self.fromState, self.toState, self.steptime, self.decisteps, self.y1, self.y2]
        if not self.hasVariable:
            return self.clean_bytes(command)
        else:
            return command


class SettingsReset(ArduinoEvent):

    def __init__(self, condition, controller):
        super().__init__(condition, controller, False)
        self.check_init()
        self.command = self.make_command()

    def __str__(self):
        return 'SettingsReset({}, {})'.format(self.condition, self.controller)
    
    def check_init(self):
        self.check_is_light_controller(self.controller)
    
    def make_command(self):
        command = [180,]
        return self.clean_bytes(command)


# EFFECTS

class EffectUpVibrato(ArduinoEvent):

    def __init__(self, condition, controller, effectIndex, amplitudeChannel, steptimeChannel, hasVariable=False):
        super().__init__(condition, controller, hasVariable)
        self.effectIndex = effectIndex
        self.amplitudeChannel = amplitudeChannel
        self.steptimeChannel = steptimeChannel
        if not hasVariable:
            self.check_init()
        self.command = self.make_command()

    def __str__(self):
        return 'EffectUpVibrato({}, {}, {}, {}, {}, {})'.format(self.condition, self.controller, self.effectIndex, self.amplitudeChannel, self.steptimeChannel, self.hasVariable)
    
    def check_init(self):
        self.check_is_light_controller(self.controller)
    
    def make_command(self):
        command = [60, self.effectIndex, self.amplitudeChannel.id, self.steptimeChannel.id]
        if not self.hasVariable:
            return self.clean_bytes(command)
        else:
            return command


class EffectDownVibrato(ArduinoEvent):

    def __init__(self, condition, controller, effectIndex, amplitudeChannel, steptimeChannel, hasVariable=False):
        super().__init__(condition, controller, hasVariable)
        self.effectIndex = effectIndex
        self.amplitudeChannel = amplitudeChannel
        self.steptimeChannel = steptimeChannel
        if not hasVariable:
            self.check_init()
        self.command = self.make_command()

    def __str__(self):
        return 'EffectDownVibrato({}, {}, {}, {}, {}, {})'.format(self.condition, self.controller, self.effectIndex, self.amplitudeChannel, self.steptimeChannel, self.hasVariable)
    
    def check_init(self):
        self.check_is_light_controller(self.controller)
    
    def make_command(self):
        command = [61, self.effectIndex, self.amplitudeChannel.id, self.steptimeChannel.id]
        if not self.hasVariable:
            return self.clean_bytes(command)
        else:
            return command


class EffectUpDownVibrato(ArduinoEvent):

    def __init__(self, condition, controller, effectIndex, amplitudeChannel, steptimeChannel, hasVariable=False):
        super().__init__(condition, controller, hasVariable)
        self.effectIndex = effectIndex
        self.amplitudeChannel = amplitudeChannel
        self.steptimeChannel = steptimeChannel
        if not hasVariable:
            self.check_init()
        self.command = self.make_command()

    def __str__(self):
        return 'EffectUpDownVibrato({}, {}, {}, {}, {}, {})'.format(self.condition, self.controller, self.effectIndex, self.amplitudeChannel, self.steptimeChannel, self.hasVariable)
    
    def check_init(self):
        self.check_is_light_controller(self.controller)
    
    def make_command(self):
        command = [62, self.effectIndex, self.amplitudeChannel.id, self.steptimeChannel.id]
        if not self.hasVariable:
            return self.clean_bytes(command)
        else:
            return command


class EffectStrobe(ArduinoEvent):

    def __init__(self, condition, controller, effectIndex,  amplitudeChannel, steptimeChannel, steptimeFactor, mutliSettingAgents=[], hasVariable=False):
        super().__init__(condition, controller, hasVariable)
        self.effectIndex = effectIndex
        self.amplitudeChannel = amplitudeChannel
        self.steptimeChannel = steptimeChannel
        self.steptimeFactor = steptimeFactor
        self.multiSettingByte = self.make_lightsbyte(mutliSettingAgents)
        if not hasVariable:
            self.check_init()
        self.command = self.make_command()

    def __str__(self):
        return 'EffectStrobe({}, {}, {}, {}, {}, {}, {}, {})'.format(self.condition, self.controller, self.effectIndex, self.amplitudeChannel, self.steptimeChannel, self.steptimeFactor, self.multiSettingByte, self.hasVariable)
    
    def check_init(self):
        self.check_is_light_controller(self.controller)
    
    def make_command(self):
        command = [70, self.effectIndex, self.amplitudeChannel.id, self.steptimeChannel.id, self.steptimeFactor, self.multiSettingByte]
        if not self.hasVariable:
            return self.clean_bytes(command)
        else:
            return command


class EffectPerlin(ArduinoEvent):

    def __init__(self, condition, controller, effectIndex, amplitudeChannel, steptimeChannel, octaves, bias, mutliSettingAgents=[], hasVariable=False):
        super().__init__(condition, controller, hasVariable)
        self.effectIndex = effectIndex
        self.amplitudeChannel = amplitudeChannel
        self.steptimeChannel = steptimeChannel
        self.octaves = octaves
        self.bias = bias
        self.multiSettingByte = self.make_lightsbyte(mutliSettingAgents)
        if not hasVariable:
            self.check_init()
        self.command = self.make_command()

    def __str__(self):
        return 'EffectPerlin({}, {}, {}, {}, {}, {}, {}, {}, {})'.format(self.condition, self.controller, self.effectIndex, self.amplitudeChannel, self.steptimeChannel, self.octaves, self.bias, self.multiSettingByte, self.hasVariable)
    
    def check_init(self):
        self.check_is_light_controller(self.controller)
    
    def make_command(self):
        command = [80, self.effectIndex, self.amplitudeChannel.id, self.steptimeChannel.id, self.octaves, self.bias, self.multiSettingByte]
        if not self.hasVariable:
            return self.clean_bytes(command)
        else:
            return command


class EffectsReset(ArduinoEvent):

    def __init__(self, condition, controller):
        super().__init__(condition, controller, False)
        self.check_init()
        self.command = self.make_command()

    def __str__(self):
        return 'EffectsReset({}, {})'.format(self.condition, self.controller)
    
    def check_init(self):
        self.check_is_light_controller(self.controller)
    
    def make_command(self):
        command = [181,]
        return self.clean_bytes(command)


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
