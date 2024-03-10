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

# GLOBAL VARIABLES
GlobalStrobeEffect = 2

# BOTTOM VARIABLES
BottomLeftIntensitySetting = 0
BottomRightIntensitySetting = 1

BottomLeftChannel = Channel16
BottomRightChannel = Channel12

BottomStrobeSteptimeChannel = Channel13
BottomStrobeDarkstepChannel = Channel14

BottomStrobeEffect = 0


# Bottom Setup
eventDict['time'].append(SettingStatic(At(0), BottomController, BottomLeftIntensitySetting, 0))
eventDict['time'].append(SettingStatic(At(0), BottomController, BottomRightIntensitySetting, 0))

eventDict['time'].append(ChannelSetSetting(At(0), BottomController, BottomLeftChannel, BottomLeftIntensitySetting))
eventDict['time'].append(ChannelSetSetting(At(0), BottomController, BottomRightChannel, BottomRightIntensitySetting))

eventDict['time'].append(LightSetChannel(At(0), BottomController, [Light1, Light2], BottomLeftChannel))
eventDict['time'].append(LightSetChannel(At(0), BottomController, [Light3, Light4], BottomRightChannel))

eventDict['time'].append(ChannelSetStatic(At(0), BottomController, BottomStrobeSteptimeChannel, 34))
eventDict['time'].append(ChannelSetStatic(At(0), BottomController, BottomStrobeDarkstepChannel, 0))
eventDict['time'].append(EffectSequencedLightStrobe(At(0), BottomController, BottomStrobeEffect, BottomStrobeSteptimeChannel, BottomStrobeDarkstepChannel, 1423))

# LIGHT SETUP
eventDict['time'].append(ChannelAddEffect(At(0), BottomController, BottomLeftChannel, BottomStrobeEffect, 0))
eventDict['time'].append(ChannelAddEffect(At(0), BottomController, BottomRightChannel, BottomStrobeEffect, 0))
eventDict['time'].append(SettingStatic(At(0), BottomController, BottomLeftIntensitySetting, 90))
eventDict['time'].append(SettingStatic(At(0), BottomController, BottomRightIntensitySetting, 90))
eventDict['time'].append(SettingStatic(At(2), BottomController, BottomLeftIntensitySetting, 0))
eventDict['time'].append(SettingStatic(At(2), BottomController, BottomRightIntensitySetting, 0))
eventDict['time'].append(ChannelSetStatic(At(2), BottomController, BottomStrobeSteptimeChannel, 67))
eventDict['time'].append(ChannelSetStatic(At(2), BottomController, BottomStrobeDarkstepChannel, 1))

beginning = 3
# SCRIPT


# 0.40 - 4.40: Buzz Fades In
startTime = beginning + 0
eventDict['time'].append(SettingStatic(At(startTime), BottomController, BottomLeftIntensitySetting, 95))
eventDict['time'].append(SettingStatic(At(startTime), BottomController, BottomRightIntensitySetting, 95))

# 4:40 - 7.14: Buzz Intensifies
startTime = beginning + 5
eventDict['time'].append(ChannelSetStatic(At(startTime), BottomController, BottomStrobeDarkstepChannel, 0))

# 10.00 - 14: Fades Into More Fuzz
startTime = beginning + 10
eventDict['time'].append(ChannelSetStatic(At(startTime), BottomController, BottomStrobeDarkstepChannel, 1))
eventDict['time'].append(ChannelSetStatic(At(startTime), BottomController, BottomStrobeSteptimeChannel, 51))
startTime = beginning + 15
eventDict['time'].append(ChannelSetStatic(At(startTime), BottomController, BottomStrobeSteptimeChannel, 34))
startTime = beginning + 20
eventDict['time'].append(ChannelSetStatic(At(startTime), BottomController, BottomStrobeDarkstepChannel, 0))
eventDict['time'].append(ChannelSetStatic(At(startTime), BottomController, BottomStrobeSteptimeChannel, 51))
startTime = beginning + 25
eventDict['time'].append(ChannelSetStatic(At(startTime), BottomController, BottomStrobeSteptimeChannel, 34))

startTime = beginning + 33
eventDict['time'].append(ChannelSetStatic(At(startTime), BottomController, BottomStrobeDarkstepChannel, 0))


vd = VisualDriver(eventDict, usesMotor=False, startTime=0, isTake=False)
vd.start()