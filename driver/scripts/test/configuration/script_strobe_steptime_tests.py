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

# BOTTOM

BottomStrengthChannel = Channel16
BottomStrobeSteptimeChannel = Channel11
BottomStrobeSetting = 1

BottomOneChannel = Channel12
BottomThreeChannel = Channel14

BottomInverseEffect = 0

# Bottom Light
eventDict['time'].append(ChannelSetStatic(At(0), BottomController, BottomStrengthChannel, 100))
eventDict['time'].append(ChannelSetStatic(At(0), BottomController, BottomStrobeSteptimeChannel, 34))
eventDict['time'].append(SettingSquareWave(At(0), BottomController, BottomStrobeSetting, StaticChannel0, BottomStrengthChannel, BottomStrobeSteptimeChannel, BottomStrobeSteptimeChannel, StaticChannel0, StaticChannel0))

eventDict['time'].append(EffectInverse(At(0), BottomController, BottomInverseEffect))
eventDict['time'].append(ChannelAddEffect(At(0), BottomController, BottomThreeChannel, BottomInverseEffect, 0))

eventDict['time'].append(ChannelSetSetting(At(0), BottomController, BottomOneChannel, BottomStrobeSetting))
eventDict['time'].append(ChannelSetSetting(At(0), BottomController, BottomThreeChannel, BottomStrobeSetting))
eventDict['time'].append(LightSetChannel(At(0), BottomController, [Light1], BottomOneChannel))
eventDict['time'].append(LightSetChannel(At(0), BottomController, [Light3], BottomThreeChannel))

time = 0
duration = 2

time += duration
# eventDict['time'].append(ChannelSetStatic(At(time), BottomController, BottomStrengthChannel, 0))
eventDict['time'].append(ChannelSetStatic(At(time), BottomController, BottomStrobeSteptimeChannel, 42))
time += 1
eventDict['time'].append(ChannelSetStatic(At(time), BottomController, BottomStrengthChannel, 100))

time += duration
# eventDict['time'].append(ChannelSetStatic(At(time), BottomController, BottomStrengthChannel, 0))
eventDict['time'].append(ChannelSetStatic(At(time), BottomController, BottomStrobeSteptimeChannel, 51))
time += 1
eventDict['time'].append(ChannelSetStatic(At(time), BottomController, BottomStrengthChannel, 100))

time += duration
# eventDict['time'].append(ChannelSetStatic(At(time), BottomController, BottomStrengthChannel, 0))
eventDict['time'].append(ChannelSetStatic(At(time), BottomController, BottomStrobeSteptimeChannel, 59))
time += 1
eventDict['time'].append(ChannelSetStatic(At(time), BottomController, BottomStrengthChannel, 100))

time += duration
# eventDict['time'].append(ChannelSetStatic(At(time), BottomController, BottomStrengthChannel, 0))
eventDict['time'].append(ChannelSetStatic(At(time), BottomController, BottomStrobeSteptimeChannel, 67))
time += 1
eventDict['time'].append(ChannelSetStatic(At(time), BottomController, BottomStrengthChannel, 100))

time += duration
eventDict['time'].append(ChannelSetStatic(At(time), BottomController, BottomStrengthChannel, 0))

vd = VisualDriver(eventDict, music=None, startTime=0, isTake=False)
vd.start()