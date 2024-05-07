from controllers import MainController
from kinectreader import LEFT_WRIST, RIGHT_WRIST
from settings import MOTOR_MAXIMUM_SPEED, MOTOR_CLOCKWISE, MOTOR_COUNTERCLOCKWISE


ARDUINO_COMMUNICATION_START_BYTE = 251
ARDUINO_COMMUNICATION_STOP_BYTE = 252

TIME_RESET_TYPE = 0
ADD_EVENTS_TYPE = 1
POSITION_RESET_TYPE = 2
POSITION_EVENTS_BLOCK_TYPE = 3
POSITION_EVENTS_UNBLOCK_TYPE = 4
TIME_EVENTS_BLOCK_TYPE = 5
TIME_EVENTS_UNBLOCK_TYPE = 6
TIME_EVENTS_CLEAR_TYPE = 7
TIME_EVENTS_CLEAR_TO_MARKER_TYPE = 8
MARKER_TYPE = 9
TRIGGER_SET_ANGLE_TYPE = 10
TRIGGER_DETACH_TYPE = 11
MOTOR_SPEED_TYPE = 12
MOTOR_DIRECTION_TYPE = 13
MUSIC_START_TYPE = 14


class Event:

    def __init__(self, condition, controller=None, hasVariable=False):
        self.condition = condition
        self.controller = controller
        self.hasVariable = hasVariable
        self.type = None
    

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


class ChannelSetStatic(ArduinoEvent):

    def __init__(self, condition, controller, targetChannel, staticState, hasVariable=False):
        super().__init__(condition, controller, hasVariable)
        self.targetChannel = targetChannel
        self.staticState = staticState
        if not hasVariable:
            self.check_init()
        self.command = self.make_command()

    def __str__(self):
        return 'ChannelSetStatic({}, {}, {}, {})'.format(self.condition, self.controller, self.targetChannel, self.staticState)
    
    def check_init(self):
        self.check_state(self.staticState)
        self.check_is_light_controller(self.controller)
    
    def make_command(self):
        command = [162, self.targetChannel.id, self.staticState]
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


class SettingStatic(ArduinoEvent):

    def __init__(self, condition, controller, settingIndex, state, hasVariable=False):
        super().__init__(condition, controller, hasVariable)
        self.settingIndex = settingIndex
        self.state = state
        if not hasVariable:
            self.check_init()
        self.command = self.make_command()

    def __str__(self):
        return 'SettingStatic({}, {}, {}, {}, {})'.format(self.condition, self.controller, self.settingIndex, self.state, self.hasVariable)
    
    def check_init(self):
        self.check_state(self.state)
        self.check_is_light_controller(self.controller)
    
    def make_command(self):
        command = [0, self.settingIndex, self.state]
        if not self.hasVariable:
            return self.clean_bytes(command)
        else:
            return command


class SettingStaticFlash(ArduinoEvent):

    def __init__(self, condition, controller, settingIndex, fromState, toState, onTime, hasVariable=False):
        super().__init__(condition, controller, hasVariable)
        self.settingIndex = settingIndex
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


class SettingBezierBeforeFlash(ArduinoEvent):

    def __init__(self, condition, controller, settingIndex, fromState, toState, steptime, decisteps, y1, y2, flashtime, hasVariable=False):
        self.settingIndex = settingIndex
        self.fromState = fromState
        self.toState = toState
        self.steptime = steptime
        self.decisteps = decisteps
        self.y1 = y1
        self.y2 = y2
        self.flashtime = flashtime
        super().__init__(condition, controller, hasVariable)
        if not hasVariable:
            self.check_init()
        self.command = self.make_command()

    def __str__(self):
        return 'SettingBezierBeforeFlash({}, {}, {}, {}, {}, {}, {}, {}, {}, {}, {})'.format(self.condition, self.controller, self.settingIndex, self.fromState, self.toState, self.steptime, self.decisteps, self.y1, self.y2, self.flashtime, self.hasVariable)
    
    def check_init(self):
        self.check_state(self.fromState)
        self.check_state(self.toState)
        self.check_state(self.y1)
        self.check_state(self.y2)
        self.check_is_light_controller(self.controller)
    
    def make_command(self):
        command = [21, self.settingIndex, self.fromState, self.toState, self.steptime, self.decisteps, self.y1, self.y2, self.flashtime]
        if not self.hasVariable:
            return self.clean_bytes(command)
        else:
            return command


class SettingBezierAfterFlash(ArduinoEvent):

    def __init__(self, condition, controller, settingIndex, fromState, toState, steptime, decisteps, y1, y2, flashtime, hasVariable=False):
        self.settingIndex = settingIndex
        self.fromState = fromState
        self.toState = toState
        self.steptime = steptime
        self.decisteps = decisteps
        self.y1 = y1
        self.y2 = y2
        self.flashtime = flashtime
        super().__init__(condition, controller, hasVariable)
        if not hasVariable:
            self.check_init()
        self.command = self.make_command()

    def __str__(self):
        return 'SettingBezierAfterFlash({}, {}, {}, {}, {}, {}, {}, {}, {}, {}, {})'.format(self.condition, self.controller, self.settingIndex, self.fromState, self.toState, self.steptime, self.decisteps, self.y1, self.y2, self.flashtime, self.hasVariable)
    
    def check_init(self):
        self.check_state(self.fromState)
        self.check_state(self.toState)
        self.check_state(self.y1)
        self.check_state(self.y2)
        self.check_is_light_controller(self.controller)
    
    def make_command(self):
        command = [22, self.settingIndex, self.fromState, self.toState, self.steptime, self.decisteps, self.y1, self.y2, self.flashtime]
        if not self.hasVariable:
            return self.clean_bytes(command)
        else:
            return command


class SettingImpulseToBezierFadeout(ArduinoEvent):

    def __init__(self, condition, controller, settingIndex, attackState, attackSteptime, sustainState, sustainSteptime, fadeoutSteptime, fadeoutDecisteps, y1, y2, hasVariable=False):
        self.settingIndex = settingIndex
        self.attackState = attackState
        self.attackSteptime = attackSteptime
        self.sustainState = sustainState
        self.sustainSteptime = sustainSteptime
        self.fadeoutSteptime = fadeoutSteptime
        self.fadeoutDecisteps = fadeoutDecisteps
        self.y1 = y1
        self.y2 = y2
        super().__init__(condition, controller, hasVariable)
        if not hasVariable:
            self.check_init()
        self.command = self.make_command()

    def __str__(self):
        return 'SettingImpulseToBezierFadeout({}, {}, {}, {}, {}, {}, {}, {}, {}, {}, {}, {})'.format(self.condition, self.controller, self.settingIndex, self.attackState, self.attackSteptime, self.sustainState, self.sustainSteptime, self.fadeoutSteptime, self.fadeoutDecisteps, self.y1, self.y2, self.hasVariable)
    
    def check_init(self):
        self.check_state(self.attackState)
        self.check_state(self.sustainState)
        self.check_state(self.y1)
        self.check_state(self.y2)
        self.check_is_light_controller(self.controller)
    
    def make_command(self):
        command = [23, self.settingIndex, self.attackState, self.attackSteptime, self.sustainState, self.sustainSteptime, self.fadeoutSteptime, self.fadeoutDecisteps, self.y1, self.y2]
        if not self.hasVariable:
            return self.clean_bytes(command)
        else:
            return command
        

class SettingSinWave(ArduinoEvent):

    def __init__(self, condition, controller, settingIndex, fromChannel, toChannel, steptimeChannel, decistepsChannel, hasVariable=False):
        self.settingIndex = settingIndex
        self.fromChannel = fromChannel
        self.toChannel = toChannel
        self.steptimeChannel = steptimeChannel
        self.decistepsChannel = decistepsChannel
        super().__init__(condition, controller, hasVariable)
        if not hasVariable:
            self.check_init()
        self.command = self.make_command()

    def __str__(self):
        return 'SettingSinWave({}, {}, {}, {}, {}, {}, {}, {})'.format(self.condition, self.controller, self.settingIndex, self.fromChannel, self.toChannel, self.steptimeChannel, self.decistepsChannel, self.hasVariable)
    
    def check_init(self):
        self.check_is_light_controller(self.controller)
    
    def make_command(self):
        command = [30, self.settingIndex, self.fromChannel.id, self.toChannel.id, self.steptimeChannel.id, self.decistepsChannel.id]
        if not self.hasVariable:
            return self.clean_bytes(command)
        else:
            return command


class SettingLinearWave(ArduinoEvent):

    def __init__(self, condition, controller, settingIndex, fromChannel, toChannel, steptimeChannel, hasVariable=False):
        self.settingIndex = settingIndex
        self.fromChannel = fromChannel
        self.toChannel = toChannel
        self.steptimeChannel = steptimeChannel
        super().__init__(condition, controller, hasVariable)
        if not hasVariable:
            self.check_init()
        self.command = self.make_command()

    def __str__(self):
        return 'SettingLinearWave({}, {}, {}, {}, {}, {}, {})'.format(self.condition, self.controller, self.settingIndex, self.fromChannel, self.toChannel, self.steptimeChannel, self.hasVariable)
    
    def check_init(self):
        self.check_is_light_controller(self.controller)
    
    def make_command(self):
        command = [40, self.settingIndex, self.fromChannel.id, self.toChannel.id, self.steptimeChannel.id]
        if not self.hasVariable:
            return self.clean_bytes(command)
        else:
            return command


class SettingLinearSaw(ArduinoEvent):

    def __init__(self, condition, controller, settingIndex, fromChannel, toChannel, steptimeChannel, hasVariable=False):
        self.settingIndex = settingIndex
        self.fromChannel = fromChannel
        self.toChannel = toChannel
        self.steptimeChannel = steptimeChannel
        super().__init__(condition, controller, hasVariable)
        if not hasVariable:
            self.check_init()
        self.command = self.make_command()

    def __str__(self):
        return 'SettingLinearSaw({}, {}, {}, {}, {}, {}, {})'.format(self.condition, self.controller, self.settingIndex, self.fromChannel, self.toChannel, self.steptimeChannel, self.hasVariable)
    
    def check_init(self):
        self.check_is_light_controller(self.controller)
    
    def make_command(self):
        command = [41, self.settingIndex, self.fromChannel.id, self.toChannel.id, self.steptimeChannel.id]
        if not self.hasVariable:
            return self.clean_bytes(command)
        else:
            return command


class SettingBezierWave(ArduinoEvent):

    def __init__(self, condition, controller, settingIndex, fromChannel, toChannel, steptimeChannel, decistepsChannel, y1Channel, y2Channel, hasVariable=False):
        self.settingIndex = settingIndex
        self.fromChannel = fromChannel
        self.toChannel = toChannel
        self.steptimeChannel = steptimeChannel
        self.decistepsChannel = decistepsChannel
        self.y1Channel = y1Channel
        self.y2Channel = y2Channel
        super().__init__(condition, controller, hasVariable)
        if not hasVariable:
            self.check_init()
        self.command = self.make_command()

    def __str__(self):
        return 'SettingBezierWave({}, {}, {}, {}, {}, {}, {}, {}, {}, {})'.format(self.condition, self.controller, self.settingIndex, self.fromChannel, self.toChannel, self.steptimeChannel, self.decistepsChannel, self.y1Channel, self.y2Channel, self.hasVariable)
    
    def check_init(self):
        self.check_is_light_controller(self.controller)
    
    def make_command(self):
        command = [50, self.settingIndex, self.fromChannel.id, self.toChannel.id, self.steptimeChannel.id, self.decistepsChannel.id, self.y1Channel.id, self.y2Channel.id]
        if not self.hasVariable:
            return self.clean_bytes(command)
        else:
            return command


class SettingBezierSaw(ArduinoEvent):

    def __init__(self, condition, controller, settingIndex, fromChannel, toChannel, steptimeChannel, decistepsChannel, y1Channel, y2Channel, hasVariable=False):
        self.settingIndex = settingIndex
        self.fromChannel = fromChannel
        self.toChannel = toChannel
        self.steptimeChannel = steptimeChannel
        self.decistepsChannel = decistepsChannel
        self.y1Channel = y1Channel
        self.y2Channel = y2Channel
        super().__init__(condition, controller, hasVariable)
        if not hasVariable:
            self.check_init()
        self.command = self.make_command()

    def __str__(self):
        return 'SettingBezierSaw({}, {}, {}, {}, {}, {}, {}, {}, {}, {})'.format(self.condition, self.controller, self.settingIndex, self.fromChannel, self.toChannel, self.steptimeChannel, self.decistepsChannel, self.y1Channel, self.y2Channel, self.hasVariable)
    
    def check_init(self):
        self.check_is_light_controller(self.controller)
    
    def make_command(self):
        command = [51, self.settingIndex, self.fromChannel.id, self.toChannel.id, self.steptimeChannel.id, self.decistepsChannel.id, self.y1Channel.id, self.y2Channel.id]
        if not self.hasVariable:
            return self.clean_bytes(command)
        else:
            return command


class SettingSquareWave(ArduinoEvent):

    def __init__(self, condition, controller, settingIndex, fromChannel, toChannel, fromSteptimeChannel, toSteptimeChannel, fromSteptimeFactorChannel, toSteptimeFactorChannel, hasVariable=False):
        self.settingIndex = settingIndex
        self.fromChannel = fromChannel
        self.toChannel = toChannel
        self.fromSteptimeChannel = fromSteptimeChannel
        self.toSteptimeChannel = toSteptimeChannel
        self.fromSteptimeFactorChannel = fromSteptimeFactorChannel
        self.toSteptimeFactorChannel = toSteptimeFactorChannel
        super().__init__(condition, controller, hasVariable)
        if not hasVariable:
            self.check_init()
        self.command = self.make_command()

    def __str__(self):
        return 'SettingSquareWave({}, {}, {}, {}, {}, {}, {}, {}, {}, {})'.format(self.condition, self.controller, self.settingIndex, self.fromChannel, self.toChannel, self.fromSteptimeChannel, self.toSteptimeChannel, self.fromSteptimeFactorChannel, self.toSteptimeFactorChannel, self.hasVariable)
    
    def check_init(self):
        self.check_is_light_controller(self.controller)
    
    def make_command(self):
        command = [60, self.settingIndex, self.fromChannel.id, self.toChannel.id, self.fromSteptimeChannel.id, self.toSteptimeChannel.id, self.fromSteptimeFactorChannel.id, self.toSteptimeFactorChannel.id]
        if not self.hasVariable:
            return self.clean_bytes(command)
        else:
            return command


class SettingNoise(ArduinoEvent):

    def __init__(self, condition, controller, settingIndex, fromChannel, toChannel, steptimeChannel, steptimeFactorChannel, hasVariable=False):
        self.settingIndex = settingIndex
        self.fromChannel = fromChannel
        self.toChannel = toChannel
        self.steptimeChannel = steptimeChannel
        self.steptimeFactorChannel = steptimeFactorChannel
        super().__init__(condition, controller, hasVariable)
        if not hasVariable:
            self.check_init()
        self.command = self.make_command()

    def __str__(self):
        return 'SettingNoise({}, {}, {}, {}, {}, {}, {}, {})'.format(self.condition, self.controller, self.settingIndex, self.fromChannel, self.toChannel, self.steptimeChannel, self.steptimeFactorChannel, self.hasVariable)
    
    def check_init(self):
        self.check_is_light_controller(self.controller)
    
    def make_command(self):
        command = [70, self.settingIndex, self.fromChannel.id, self.toChannel.id, self.steptimeChannel.id, self.steptimeFactorChannel.id]
        if not self.hasVariable:
            return self.clean_bytes(command)
        else:
            return command


class SettingSeedNoise(ArduinoEvent):

    def __init__(self, condition, controller, settingIndex, fromChannel, toChannel, steptimeChannel, steptimeFactorChannel, seedChannel, hasVariable=False):
        self.settingIndex = settingIndex
        self.fromChannel = fromChannel
        self.toChannel = toChannel
        self.steptimeChannel = steptimeChannel
        self.steptimeFactorChannel = steptimeFactorChannel
        self.seedChannel = seedChannel
        super().__init__(condition, controller, hasVariable)
        if not hasVariable:
            self.check_init()
        self.command = self.make_command()

    def __str__(self):
        return 'SettingSeedNoise({}, {}, {}, {}, {}, {}, {}, {}, {})'.format(self.condition, self.controller, self.settingIndex, self.fromChannel, self.toChannel, self.steptimeChannel, self.steptimeFactorChannel, self.seedChannel, self.hasVariable)
    
    def check_init(self):
        self.check_is_light_controller(self.controller)
    
    def make_command(self):
        command = [71, self.settingIndex, self.fromChannel.id, self.toChannel.id, self.steptimeChannel.id, self.steptimeFactorChannel.id, self.seedChannel.id]
        if not self.hasVariable:
            return self.clean_bytes(command)
        else:
            return command


class SettingPerlinNoise(ArduinoEvent):

    def __init__(self, condition, controller, settingIndex, fromChannel, toChannel, steptimeChannel, steptimeFactorChannel, hasVariable=False):
        self.settingIndex = settingIndex
        self.fromChannel = fromChannel
        self.toChannel = toChannel
        self.steptimeChannel = steptimeChannel
        self.steptimeFactorChannel = steptimeFactorChannel
        super().__init__(condition, controller, hasVariable)
        if not hasVariable:
            self.check_init()
        self.command = self.make_command()

    def __str__(self):
        return 'SettingPerlinNoise({}, {}, {}, {}, {}, {}, {}, {})'.format(self.condition, self.controller, self.settingIndex, self.fromChannel, self.toChannel, self.steptimeChannel, self.steptimeFactorChannel, self.hasVariable)
    
    def check_init(self):
        self.check_is_light_controller(self.controller)
    
    def make_command(self):
        command = [72, self.settingIndex, self.fromChannel.id, self.toChannel.id, self.steptimeChannel.id, self.steptimeFactorChannel.id]
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

class EffectNone(ArduinoEvent):

    def __init__(self, condition, controller, effectIndex, hasVariable=False):
        super().__init__(condition, controller, hasVariable)
        self.effectIndex = effectIndex
        if not hasVariable:
            self.check_init()
        self.command = self.make_command()

    def __str__(self):
        return 'EffectNone({}, {}, {}, {})'.format(self.condition, self.controller, self.effectIndex, self.hasVariable)
    
    def check_init(self):
        self.check_is_light_controller(self.controller)
    
    def make_command(self):
        command = [100, self.effectIndex]
        if not self.hasVariable:
            return self.clean_bytes(command)
        else:
            return command


class EffectInverse(ArduinoEvent):

    def __init__(self, condition, controller, effectIndex, hasVariable=False):
        super().__init__(condition, controller, hasVariable)
        self.effectIndex = effectIndex
        if not hasVariable:
            self.check_init()
        self.command = self.make_command()

    def __str__(self):
        return 'EffectInverse({}, {}, {}, {})'.format(self.condition, self.controller, self.effectIndex, self.hasVariable)
    
    def check_init(self):
        self.check_is_light_controller(self.controller)
    
    def make_command(self):
        command = [101, self.effectIndex]
        if not self.hasVariable:
            return self.clean_bytes(command)
        else:
            return command


class EffectLastOrZero(ArduinoEvent):

    def __init__(self, condition, controller, effectIndex, hasVariable=False):
        super().__init__(condition, controller, hasVariable)
        self.effectIndex = effectIndex
        if not hasVariable:
            self.check_init()
        self.command = self.make_command()

    def __str__(self):
        return 'EffectLastOrZero({}, {}, {}, {})'.format(self.condition, self.controller, self.effectIndex, self.hasVariable)
    
    def check_init(self):
        self.check_is_light_controller(self.controller)
    
    def make_command(self):
        command = [102, self.effectIndex]
        if not self.hasVariable:
            return self.clean_bytes(command)
        else:
            return command

class EffectAdd(ArduinoEvent):

    def __init__(self, condition, controller, effectIndex, inputChannel, hasVariable=False):
        super().__init__(condition, controller, hasVariable)
        self.effectIndex = effectIndex
        self.inputChannel = inputChannel
        if not hasVariable:
            self.check_init()
        self.command = self.make_command()

    def __str__(self):
        return 'EffectAdd({}, {}, {}, {}, {})'.format(self.condition, self.controller, self.effectIndex, self.inputChannel, self.hasVariable)
    
    def check_init(self):
        self.check_is_light_controller(self.controller)
    
    def make_command(self):
        command = [110, self.effectIndex, self.inputChannel.id]
        if not self.hasVariable:
            return self.clean_bytes(command)
        else:
            return command


class EffectSubtract(ArduinoEvent):

    def __init__(self, condition, controller, effectIndex, inputChannel, hasVariable=False):
        super().__init__(condition, controller, hasVariable)
        self.effectIndex = effectIndex
        self.inputChannel = inputChannel
        if not hasVariable:
            self.check_init()
        self.command = self.make_command()

    def __str__(self):
        return 'EffectSubtract({}, {}, {}, {}, {})'.format(self.condition, self.controller, self.effectIndex, self.inputChannel, self.hasVariable)
    
    def check_init(self):
        self.check_is_light_controller(self.controller)
    
    def make_command(self):
        command = [111, self.effectIndex, self.inputChannel.id]
        if not self.hasVariable:
            return self.clean_bytes(command)
        else:
            return command


class EffectAddPercentage(ArduinoEvent):

    def __init__(self, condition, controller, effectIndex, inputChannel, hasVariable=False):
        super().__init__(condition, controller, hasVariable)
        self.effectIndex = effectIndex
        self.inputChannel = inputChannel
        if not hasVariable:
            self.check_init()
        self.command = self.make_command()

    def __str__(self):
        return 'EffectAddPercentage({}, {}, {}, {}, {})'.format(self.condition, self.controller, self.effectIndex, self.inputChannel, self.hasVariable)
    
    def check_init(self):
        self.check_is_light_controller(self.controller)
    
    def make_command(self):
        command = [112, self.effectIndex, self.inputChannel.id]
        if not self.hasVariable:
            return self.clean_bytes(command)
        else:
            return command


class EffectSubtractPercentage(ArduinoEvent):

    def __init__(self, condition, controller, effectIndex, inputChannel, hasVariable=False):
        super().__init__(condition, controller, hasVariable)
        self.effectIndex = effectIndex
        self.inputChannel = inputChannel
        if not hasVariable:
            self.check_init()
        self.command = self.make_command()

    def __str__(self):
        return 'EffectSubtractPercentage({}, {}, {}, {}, {})'.format(self.condition, self.controller, self.effectIndex, self.inputChannel, self.hasVariable)
    
    def check_init(self):
        self.check_is_light_controller(self.controller)
    
    def make_command(self):
        command = [113, self.effectIndex, self.inputChannel.id]
        if not self.hasVariable:
            return self.clean_bytes(command)
        else:
            return command


class EffectPercentage(ArduinoEvent):

    def __init__(self, condition, controller, effectIndex, inputChannel, hasVariable=False):
        super().__init__(condition, controller, hasVariable)
        self.effectIndex = effectIndex
        self.inputChannel = inputChannel
        if not hasVariable:
            self.check_init()
        self.command = self.make_command()

    def __str__(self):
        return 'EffectPercentage({}, {}, {}, {}, {})'.format(self.condition, self.controller, self.effectIndex, self.inputChannel, self.hasVariable)
    
    def check_init(self):
        self.check_is_light_controller(self.controller)
    
    def make_command(self):
        command = [114, self.effectIndex, self.inputChannel.id]
        if not self.hasVariable:
            return self.clean_bytes(command)
        else:
            return command


class EffectSequencedLightStrobe(ArduinoEvent):

    def __init__(self, condition, controller, effectIndex, steptimeChannel, darkstepChannel, sequence, hasVariable=False):
        super().__init__(condition, controller, hasVariable)
        self.effectIndex = effectIndex
        self.steptimeChannel = steptimeChannel
        self.darkstepChannel = darkstepChannel
        reversed = str(sequence)[::-1]
        sequence = int(reversed)
        if sequence < 0 or sequence > 999999999:
            self.abort("The sequence is not valid: %s", str(sequence))
        sequenceBytes = sequence.to_bytes(4, byteorder="big")
        self.byte1 = sequenceBytes[0]
        self.byte2 = sequenceBytes[1]
        self.byte3 = sequenceBytes[2]
        self.byte4 = sequenceBytes[3]

        if not hasVariable:
            self.check_init()
        self.command = self.make_command()

    def __str__(self):
        return 'EffectSequencedLightStrobe({}, {}, {}, {}, {}, {}, {}, {}, {}, {})'.format(self.condition, self.controller, self.effectIndex, self.steptimeChannel, self.darkstepChannel, self.byte1, self.byte2, self.byte3, self.byte4, self.hasVariable)
    
    def check_init(self):
        self.check_is_light_controller(self.controller)
    
    def make_command(self):
        command = [120, self.effectIndex, self.steptimeChannel.id, self.darkstepChannel.id, self.byte1, self.byte2, self.byte3, self.byte4]
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


class NowDeltaIncrease(ArduinoEvent):

    def __init__(self, condition, controller, delta, hasVariable=False):
        super().__init__(condition, controller, hasVariable)
        self.delta = delta
        if not hasVariable:
            self.check_init()
        self.command = self.make_command()

    def __str__(self):
        return 'NowDeltaIncrease({}, {}, {}, {})'.format(self.condition, self.controller, self.delta, self.hasVariable)
    
    def check_init(self):
        self.check_is_light_controller(self.controller)
    
    def make_command(self):
        command = [190, self.delta]
        if not self.hasVariable:
            return self.clean_bytes(command)
        else:
            return command


class NowDeltaDecrease(ArduinoEvent):

    def __init__(self, condition, controller, delta, hasVariable=False):
        super().__init__(condition, controller, hasVariable)
        self.delta = delta
        if not hasVariable:
            self.check_init()
        self.command = self.make_command()

    def __str__(self):
        return 'NowDeltaDecrease({}, {}, {}, {})'.format(self.condition, self.controller, self.delta, self.hasVariable)
    
    def check_init(self):
        self.check_is_light_controller(self.controller)
    
    def make_command(self):
        command = [191, self.delta]
        if not self.hasVariable:
            return self.clean_bytes(command)
        else:
            return command


class MotorSpeed(Event):

    def __init__(self, condition, speed):
        super().__init__(condition, MainController)
        self.type = MOTOR_SPEED_TYPE
        if type(speed) != int or speed < 0:
            self.abort('Invalid speed: ' + str(speed))
        elif speed > MOTOR_MAXIMUM_SPEED:
            self.speed = MOTOR_MAXIMUM_SPEED
        else:
            self.speed = speed


class MotorDirection(Event):

    def __init__(self, condition, direction):
        super().__init__(condition, MainController)
        self.type = MOTOR_DIRECTION_TYPE
        if direction != MOTOR_CLOCKWISE and direction != MOTOR_COUNTERCLOCKWISE:
            self.abort('Invalid direction: ' + str(direction))
        else:
            self.direction = direction


class MusicStart(Event):

    def __init__(self, condition, startTime):
        super().__init__(condition, MainController)
        self.type = MUSIC_START_TYPE
        if type(startTime) != int or startTime < 0:
            self.abort('Invalid startTime: ' + str(startTime))
        self.startTime = startTime


class TriggerAngle(Event):
    def __init__(self, condition, angle):
        super().__init__(condition, MainController)
        self.type = TRIGGER_SET_ANGLE_TYPE
        if type(angle) != int or angle > 180 or angle < 0:
            self.abort('Invalid angle: ' + str(angle))
        else:
            self.angle = angle


class TriggerDetach(Event):
    def __init__(self, condition):
        super().__init__(condition, MainController)
        self.type = TRIGGER_DETACH_TYPE


class Marker(Event):
    def __init__(self, condition):
        super().__init__(condition, MainController)
        self.type = MARKER_TYPE


class TimeReset(Event):

    def __init__(self, condition):
        super().__init__(condition, MainController)
        self.type = TIME_RESET_TYPE


class TimeEventsBlock(Event):

    def __init__(self, condition):
        super().__init__(condition, MainController)
        self.type = TIME_EVENTS_BLOCK_TYPE


class TimeEventsUnblock(Event):

    def __init__(self, condition):
        super().__init__(condition, MainController)
        self.type = TIME_EVENTS_UNBLOCK_TYPE


class TimeEventsClear(Event):

    def __init__(self, condition):
        super().__init__(condition, MainController)
        self.type = TIME_EVENTS_CLEAR_TYPE


class TimeEventsClearToMarker(Event):

    def __init__(self, condition, marker):
        super().__init__(condition, MainController)
        self.type = TIME_EVENTS_CLEAR_TO_MARKER_TYPE
        self.marker = marker

class EventsAdd(Event):

    def __init__(self, condition, events):
        super().__init__(condition, MainController)
        self.type = ADD_EVENTS_TYPE
        if not events or type(events) != dict:
            self.abort('Events in EventsAdd is empty or not a dict')
        self.events = events


class PositionReset(Event):

    def __init__(self, condition):
        super().__init__(condition, MainController)
        self.type = POSITION_RESET_TYPE


class PositionEventsBlock(Event):

    def __init__(self, condition):
        super().__init__(condition, MainController)
        self.type = POSITION_EVENTS_BLOCK_TYPE


class PositionEventsUnblock(Event):

    def __init__(self, condition):
        super().__init__(condition, MainController)
        self.type = POSITION_EVENTS_UNBLOCK_TYPE
