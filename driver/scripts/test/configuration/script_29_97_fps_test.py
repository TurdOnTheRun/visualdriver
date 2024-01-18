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

# music = '/home/maximilian/music/guardians.mp3'

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

BottomStrengthChannel = Channel16
BottomStrobeChannel = Channel11
BottomStrobeSetting = 1

BottomOneChannel = Channel12
BottomTwoChannel = Channel13
BottomThreeChannel = Channel14
BottomFourChannel = Channel15

BottomInverseEffect = 0

# Bottom Light
eventDict['time'].append(ChannelSetStatic(At(0), BottomController, BottomStrengthChannel, 100))
eventDict['time'].append(ChannelSetStatic(At(0), BottomController, BottomStrobeChannel, 34))
eventDict['time'].append(SettingSquareWave(At(0), BottomController, BottomStrobeSetting, StaticChannel0, BottomStrengthChannel, BottomStrobeChannel, BottomStrobeChannel, StaticChannel0, StaticChannel0))

eventDict['time'].append(EffectInverse(At(0), BottomController, BottomInverseEffect))
eventDict['time'].append(ChannelAddEffect(At(0), BottomController, BottomThreeChannel, BottomInverseEffect, 0))

eventDict['time'].append(ChannelSetSetting(At(0), BottomController, BottomOneChannel, BottomStrobeSetting))
# eventDict['time'].append(ChannelSetSetting(At(0), BottomController, BottomTwoChannel, BottomStrobeSetting))
eventDict['time'].append(ChannelSetSetting(At(0), BottomController, BottomThreeChannel, BottomStrobeSetting))
# eventDict['time'].append(ChannelSetSetting(At(0), BottomController, BottomFourChannel, BottomStrobeSetting))

eventDict['time'].append(LightSetChannel(At(0), BottomController, [Light1], BottomOneChannel))
eventDict['time'].append(LightSetChannel(At(0), BottomController, [Light3], BottomThreeChannel))


eventDict['time'].append(ChannelSetStatic(At(180), BottomController, BottomStrengthChannel, 0))


vd = VisualDriver(eventDict, music=None, startTime=0, isTake=False)
vd.start()