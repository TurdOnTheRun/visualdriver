from visualdriver import VisualDriver
from controllers import * 
from conditions import *
from channels import *
from agents import *
from events import *
from settings import *

eventDict = {
    'position': [],
    'time': []
}

music = '/home/maximilian/music/guardians.mp3'

# 0.40 - 4.40: Left Buzz Fades In
# 4:40 - 7.14: Left Buzz Joins
# 10.00 - 14: Fades Into More Fuzz
# 29.5 - 33: Top Fades in
# 33.8 - 37: Top Changes To More Crunch
# 53 - 54 Top Changes
# 61 - 63 Top Change. (Maybe mix with Bottom)
# 67 - 69 High Note Fade In 
# 73-74 HIgh NOte to more crunch
# 75 - 84 Fade Out

# BOTTOM

BottomStrengthSetting = 0
BottomStrengthChannel = Channel16
BottomStrobeChannel = Channel11
BottomStrobeSetting = 1

BottomOneChannel = Channel12
BottomTwoChannel = Channel13
BottomThreeChannel = Channel14
BottomFourChannel = Channel15

BottomInverseEffect = 0

# Bottom Light
eventDict['time'].append(SettingStatic(At(0), BottomController, BottomStrengthSetting, 100))
eventDict['time'].append(ChannelSetSetting(At(0), BottomController, BottomStrengthChannel, BottomStrengthSetting))
eventDict['time'].append(SettingSquareWave(At(0), BottomController, BottomStrobeSetting, StaticChannel0, BottomStrengthChannel, StaticChannel40, StaticChannel40, StaticChannel0, StaticChannel0))

eventDict['time'].append(EffectInverse(At(0), BottomController, BottomInverseEffect))
eventDict['time'].append(ChannelAddEffect(At(0), BottomController, BottomThreeChannel, BottomInverseEffect, 0))

eventDict['time'].append(ChannelSetSetting(At(0), BottomController, BottomOneChannel, BottomStrobeSetting))
# eventDict['time'].append(ChannelSetSetting(At(0), BottomController, BottomTwoChannel, BottomStrobeSetting))
eventDict['time'].append(ChannelSetSetting(At(0), BottomController, BottomThreeChannel, BottomStrobeSetting))
# eventDict['time'].append(ChannelSetSetting(At(0), BottomController, BottomFourChannel, BottomStrobeSetting))

eventDict['time'].append(LightSetChannel(At(0), BottomController, [Light1], BottomOneChannel))
eventDict['time'].append(LightSetChannel(At(0), BottomController, [Light3], BottomThreeChannel))


# Top

TopStrengthSetting = 0
TopStrengthChannel = Channel16
TopStrobeChannel = Channel11
TopStrobeSetting = 1

TopOneChannel = Channel12
TopTwoChannel = Channel13
TopThreeChannel = Channel14
TopFourChannel = Channel15

TopInverseEffect = 0

eventDict['time'].append(SettingStatic(At(0), TopController, TopStrengthSetting, 0))
eventDict['time'].append(ChannelSetSetting(At(0), TopController, TopStrengthChannel, TopStrengthSetting))
eventDict['time'].append(SettingSquareWave(At(0), TopController, TopStrobeSetting, StaticChannel0, TopStrengthChannel, StaticChannel40, StaticChannel40, StaticChannel0, StaticChannel0))

eventDict['time'].append(EffectInverse(At(0), TopController, TopInverseEffect))
# eventDict['time'].append(ChannelAddEffect(At(0), TopController, TopThreeChannel, TopInverseEffect, 0))

eventDict['time'].append(ChannelSetSetting(At(0), TopController, TopOneChannel, TopStrobeSetting))
# eventDict['time'].append(ChannelSetSetting(At(0), TopController, TopTwoChannel, TopStrobeSetting))
eventDict['time'].append(ChannelSetSetting(At(0), TopController, TopThreeChannel, TopStrobeSetting))
# eventDict['time'].append(ChannelSetSetting(At(0), TopController, TopFourChannel, TopStrobeSetting))

eventDict['time'].append(LightSetChannel(At(0), TopController, [Light1], TopOneChannel))
eventDict['time'].append(LightSetChannel(At(0), TopController, [Light3], TopThreeChannel))

eventDict['time'].append(MotorSpeed(At(0), 90))

eventDict['position'].append(EffectNone(At(1.5), BottomController, BottomInverseEffect))
eventDict['position'].append(SettingStatic(At(1.5), BottomController, BottomStrengthSetting, 0))
eventDict['position'].append(ChannelAddEffect(At(1.5), TopController, TopThreeChannel, TopInverseEffect, 0))
eventDict['position'].append(SettingStatic(At(1.5), TopController, TopStrengthSetting, 100))


eventDict['position'].append(MotorSpeed(At(3), 0))



vd = VisualDriver(eventDict, music=None, usesMotor=False, startTime=0, isTake=False)
vd.start()