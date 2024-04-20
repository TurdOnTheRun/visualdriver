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

music = '/home/maximilian/music/sun_test.mp3'

# 0.40 - 4.40: Left Buzz Fades In
# 4:40 - 7.14: Right Buzz Joins
# 10.00 - 14: Fades Into More Fuzz
# 29.5 - 33: Top Fades in
# 34 - 37: Top Changes To More Crunch
# 53 - 54 Top Changes
# 61 - 63 Top Change. (Maybe mix with Bottom) Starts with Global Effet but Bottom is off --> looks like darkstep. THen bottom fades in.
# 67 - 69 High Note Fade In 
# 73-74 HIgh NOte to more crunch
# 75 - 84 Fade Out

# GLOBAL VARIABLES
GlobalStrobeEffect = 0

# BOTTOM VARIABLES
BottomIntensitySetting = 0
BottomFlashSetting = 1

BottomSetupStrobeEffect = 1
BottomSubtractEffect = 2

BottomChannel = Channel12
BottomStrobeSteptimeChannel = Channel13
BottomStrobeDarkstepChannel = Channel14
BottomFlashChannel = Channel15

# Bottom Setup
eventDict['position'].append(SettingStatic(At(0), BottomController, BottomIntensitySetting, 0))
eventDict['position'].append(ChannelSetSetting(At(0), BottomController, BottomChannel, BottomIntensitySetting))
eventDict['position'].append(LightSetChannel(At(0), BottomController, [Light1, Light2, Light3, Light4], BottomChannel))
eventDict['position'].append(ChannelSetStatic(At(0), BottomController, BottomStrobeSteptimeChannel, 34))
eventDict['position'].append(ChannelSetStatic(At(0), BottomController, BottomStrobeDarkstepChannel, 1))
eventDict['position'].append(EffectSequencedLightStrobe(At(0), BottomController, BottomSetupStrobeEffect, BottomStrobeSteptimeChannel, BottomStrobeDarkstepChannel, 1313))
eventDict['position'].append(EffectSequencedLightStrobe(At(0), BottomController, GlobalStrobeEffect, BottomStrobeSteptimeChannel, BottomStrobeDarkstepChannel, 15372648))

eventDict['position'].append(SettingStatic(At(0), BottomController, BottomFlashSetting, 0))
eventDict['position'].append(ChannelSetSetting(At(0), BottomController, BottomFlashChannel, BottomFlashSetting))
eventDict['position'].append(EffectSubtractPercentage(At(0), BottomController, BottomSubtractEffect, BottomFlashChannel))
eventDict['position'].append(ChannelAddEffect(At(0), BottomController, BottomChannel, BottomSubtractEffect, 2))




# TOP VARIABLES
TopIntensitySetting = 0
TopPerlinSetting =1
TopFlashSetting = 2

TopChannel = Channel13
TopStrobeSteptimeChannel = Channel14
TopStrobeDarkstepChannel = Channel15
TopFlashChannel = Channel16
TopPerlinChannel = Channel17

TopSubtractEffect = 1


# Top Setup
eventDict['position'].append(SettingStatic(At(0), TopController, TopIntensitySetting, 0))

eventDict['position'].append(ChannelSetSetting(At(0), TopController, TopChannel, TopIntensitySetting))
eventDict['position'].append(LightSetChannel(At(0), TopController, [Light1, Light2, Light3, Light4], TopChannel))

eventDict['position'].append(ChannelSetStatic(At(0), TopController, TopStrobeSteptimeChannel, 34))
eventDict['position'].append(ChannelSetStatic(At(0), TopController, TopStrobeDarkstepChannel, 0))
eventDict['position'].append(EffectSequencedLightStrobe(At(0), TopController, GlobalStrobeEffect, TopStrobeSteptimeChannel, TopStrobeDarkstepChannel, 15372648))

eventDict['position'].append(SettingPerlinNoise(At(0), TopController, TopPerlinSetting, StaticChannel0, StaticChannel100, StaticChannel5, StaticChannel0))
eventDict['position'].append(ChannelSetSetting(At(0), TopController, TopPerlinChannel, TopPerlinSetting))

eventDict['position'].append(SettingStatic(At(0), TopController, TopFlashSetting, 0))
eventDict['position'].append(ChannelSetSetting(At(0), TopController, TopFlashChannel, TopFlashSetting))
eventDict['position'].append(EffectSubtractPercentage(At(0), TopController, TopSubtractEffect, TopFlashChannel))
eventDict['position'].append(ChannelAddEffect(At(0), TopController, TopChannel, TopSubtractEffect, 2))


# LIGHT SETUP
eventDict['time'].append(MotorSpeed(At(0), 35))

eventDict['position'].append(ChannelAddEffect(At(0), BottomController, BottomChannel, BottomSetupStrobeEffect, 0))
eventDict['position'].append(SettingStatic(At(0), BottomController, BottomIntensitySetting, 90))
eventDict['time'].append(SettingStatic(At(2), BottomController, BottomIntensitySetting, 0))
eventDict['time'].append(ChannelSetStatic(At(2), BottomController, BottomStrobeDarkstepChannel, 1))



beginning = 3
# SCRIPT
eventDict['time'].append(MusicStart(At(beginning), 0))

# 0:50
# Setup
startTime = beginning + 0.5
eventDict['time'].append(ChannelAddEffect(At(startTime), TopController, TopChannel, GlobalStrobeEffect, 0))
eventDict['time'].append(ChannelAddEffect(At(startTime), BottomController, BottomChannel, GlobalStrobeEffect, 0))


# 1:00
# Setup
startTime = beginning + 1
eventDict['time'].append(ChannelSetStatic(At(startTime), TopController, TopStrobeSteptimeChannel, 51))
eventDict['time'].append(ChannelSetStatic(At(startTime), TopController, TopStrobeDarkstepChannel, 0))
eventDict['time'].append(ChannelSetStatic(At(startTime), BottomController, BottomStrobeSteptimeChannel, 51))
eventDict['time'].append(ChannelSetStatic(At(startTime), BottomController, BottomStrobeDarkstepChannel, 0))


# 1:35
# Rough strobe starts
startTime = beginning + 1.35
# eventDict['time'].append(SettingStatic(At(startTime), TopController, TopIntensitySetting, 90))
eventDict['time'].append(SettingStatic(At(startTime), BottomController, BottomIntensitySetting, 90))


# 2:55
# Switch to more fine strobe
startTime = beginning + 2.55
eventDict['time'].append(SettingStatic(At(startTime), TopController, TopIntensitySetting, 90))

# eventDict['time'].append(ChannelSetStatic(At(startTime), TopController, TopStrobeSteptimeChannel, 51))
eventDict['time'].append(ChannelSetStatic(At(startTime), TopController, TopStrobeDarkstepChannel, 1))
# eventDict['time'].append(ChannelSetStatic(At(startTime), BottomController, BottomStrobeSteptimeChannel, 51))
eventDict['time'].append(ChannelSetStatic(At(startTime), BottomController, BottomStrobeDarkstepChannel, 1))


# 7:09
# hit
startTime = beginning + 7.09
eventDict['time'].append(SettingStaticFlash(At(startTime), TopController, TopFlashSetting, 100, 0, 180))
eventDict['time'].append(SettingStaticFlash(At(startTime), BottomController, BottomFlashSetting, 100, 0, 100))

# 7:28
# hit
startTime = beginning + 7.28
eventDict['time'].append(SettingStaticFlash(At(startTime), TopController, TopFlashSetting, 100, 0, 180))
eventDict['time'].append(SettingStaticFlash(At(startTime), BottomController, BottomFlashSetting, 100, 0, 100))

# 7:50
# hit
startTime = beginning + 7.50
eventDict['time'].append(SettingStaticFlash(At(startTime), TopController, TopFlashSetting, 100, 0, 180))
eventDict['time'].append(SettingStaticFlash(At(startTime), BottomController, BottomFlashSetting, 100, 0, 255))

# 9:31
# hit
startTime = beginning + 9.31
eventDict['time'].append(SettingStaticFlash(At(startTime), TopController, TopFlashSetting, 100, 0, 180))
eventDict['time'].append(SettingStaticFlash(At(startTime), BottomController, BottomFlashSetting, 100, 0, 255))


# 9:45
# hi

# 9:77
# hit
startTime = beginning + 9.77
eventDict['time'].append(SettingStaticFlash(At(startTime), TopController, TopFlashSetting, 100, 0, 180))
eventDict['time'].append(SettingStaticFlash(At(startTime), BottomController, BottomFlashSetting, 100, 0, 255))

# 9:89
# hit

# 10:26
# hit
startTime = beginning + 10.26
eventDict['time'].append(SettingStaticFlash(At(startTime), TopController, TopFlashSetting, 100, 0, 180))
eventDict['time'].append(SettingStaticFlash(At(startTime), BottomController, BottomFlashSetting, 100, 0, 255))

# 10:64
# hit
startTime = beginning + 10.64
eventDict['time'].append(SettingStaticFlash(At(startTime), TopController, TopFlashSetting, 100, 0, 180))
eventDict['time'].append(SettingStaticFlash(At(startTime), BottomController, BottomFlashSetting, 100, 0, 255))


# 13:65
# switch to rough strobe
startTime = beginning + 13.65
eventDict['time'].append(ChannelSetStatic(At(startTime), TopController, TopStrobeSteptimeChannel, 34))
# eventDict['time'].append(ChannelSetStatic(At(startTime), TopController, TopStrobeDarkstepChannel, 0))
eventDict['time'].append(ChannelSetStatic(At(startTime), BottomController, BottomStrobeSteptimeChannel, 34))
# eventDict['time'].append(ChannelSetStatic(At(startTime), BottomController, BottomStrobeDarkstepChannel, 0))


# 17:97
# hit
startTime = beginning + 17.97
eventDict['time'].append(SettingStaticFlash(At(startTime), TopController, TopFlashSetting, 100, 0, 180))
eventDict['time'].append(SettingStaticFlash(At(startTime), BottomController, BottomFlashSetting, 100, 0, 255))

# 18:82
# hit
startTime = beginning + 18.82
eventDict['time'].append(SettingStaticFlash(At(startTime), TopController, TopFlashSetting, 100, 0, 180))
eventDict['time'].append(SettingStaticFlash(At(startTime), BottomController, BottomFlashSetting, 100, 0, 255))

# 19:03
# hit
startTime = beginning + 19.03
eventDict['time'].append(SettingStaticFlash(At(startTime), TopController, TopFlashSetting, 100, 0, 180))
eventDict['time'].append(SettingStaticFlash(At(startTime), BottomController, BottomFlashSetting, 100, 0, 255))

# 19:25
# hit
startTime = beginning + 19.25
eventDict['time'].append(SettingStaticFlash(At(startTime), TopController, TopFlashSetting, 100, 0, 180))
eventDict['time'].append(SettingStaticFlash(At(startTime), BottomController, BottomFlashSetting, 100, 0, 255))

# 19:66
# hit
startTime = beginning + 19.66
eventDict['time'].append(SettingStaticFlash(At(startTime), TopController, TopFlashSetting, 100, 0, 180))
eventDict['time'].append(SettingStaticFlash(At(startTime), BottomController, BottomFlashSetting, 100, 0, 255))

# 20:13
# hit
startTime = beginning + 20.13
eventDict['time'].append(SettingStaticFlash(At(startTime), TopController, TopFlashSetting, 100, 0, 180))
eventDict['time'].append(SettingStaticFlash(At(startTime), BottomController, BottomFlashSetting, 100, 0, 255))

# 20:23
# hit
startTime = beginning + 20.23
eventDict['time'].append(SettingStaticFlash(At(startTime), TopController, TopFlashSetting, 100, 0, 180))
eventDict['time'].append(SettingStaticFlash(At(startTime), BottomController, BottomFlashSetting, 100, 0, 255))

# 20:60
# hit
startTime = beginning + 20.6
eventDict['time'].append(SettingStaticFlash(At(startTime), TopController, TopFlashSetting, 100, 0, 180))
eventDict['time'].append(SettingStaticFlash(At(startTime), BottomController, BottomFlashSetting, 100, 0, 255))

# 20:99
# hit
startTime = beginning + 20.99
eventDict['time'].append(SettingStaticFlash(At(startTime), TopController, TopFlashSetting, 100, 0, 180))
eventDict['time'].append(SettingStaticFlash(At(startTime), BottomController, BottomFlashSetting, 100, 0, 255))

# 21:34
# Switch to not strobe gentle flicker
startTime = beginning + 21.34
eventDict['time'].append(ChannelRemoveEffect(At(startTime), TopController, TopChannel, 0))
eventDict['time'].append(EffectSubtractPercentage(At(0), TopController, TopSubtractEffect, TopPerlinChannel))

eventDict['time'].append(SettingStatic(At(startTime), TopController, TopIntensitySetting, 30))
eventDict['time'].append(SettingStatic(At(startTime), BottomController, BottomIntensitySetting, 0))


# 28
# End
startTime = beginning + 28
eventDict['time'].append(SettingStatic(At(startTime), TopController, TopIntensitySetting, 0))
eventDict['time'].append(MotorSpeed(At(startTime), 0))



vd = VisualDriver(eventDict, music=music, usesMotor=False, startTime=0, isTake=False)
vd.start()