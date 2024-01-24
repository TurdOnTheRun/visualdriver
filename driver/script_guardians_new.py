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
eventDict['time'].append(EffectSequencedLightStrobe(At(0), BottomController, GlobalStrobeEffect, BottomStrobeSteptimeChannel, BottomStrobeDarkstepChannel, 15374628))



# TOP VARIABLES
TopLeftIntensitySetting = 0
TopRightIntensitySetting = 1


TopLeftChannel = Channel16
TopRightChannel = Channel15


TopStrobeSteptimeChannel = Channel13
TopStrobeDarkstepChannel = Channel14
TopStrobeEffect = 0

# Top Setup
eventDict['time'].append(SettingStatic(At(0), TopController, TopLeftIntensitySetting, 0))
eventDict['time'].append(SettingStatic(At(0), TopController, TopRightIntensitySetting, 0))
eventDict['time'].append(ChannelSetSetting(At(0), TopController, TopLeftChannel, TopLeftIntensitySetting))
eventDict['time'].append(ChannelSetSetting(At(0), TopController, TopRightChannel, TopRightIntensitySetting))
eventDict['time'].append(LightSetChannel(At(0), TopController, [Light1, Light2], TopLeftChannel))
eventDict['time'].append(LightSetChannel(At(0), TopController, [Light3, Light4], TopRightChannel))

eventDict['time'].append(ChannelSetStatic(At(0), TopController, TopStrobeSteptimeChannel, 34))
eventDict['time'].append(ChannelSetStatic(At(0), TopController, TopStrobeDarkstepChannel, 0))
eventDict['time'].append(EffectSequencedLightStrobe(At(0), TopController, TopStrobeEffect, TopStrobeSteptimeChannel, TopStrobeDarkstepChannel, 5656))
eventDict['time'].append(EffectSequencedLightStrobe(At(0), TopController, GlobalStrobeEffect, TopStrobeSteptimeChannel, TopStrobeDarkstepChannel, 15374628))

# LIGHT SETUP
eventDict['time'].append(ChannelAddEffect(At(0), BottomController, BottomLeftChannel, BottomStrobeEffect, 0))
eventDict['time'].append(ChannelAddEffect(At(0), BottomController, BottomRightChannel, BottomStrobeEffect, 0))
eventDict['time'].append(SettingStatic(At(0), BottomController, BottomLeftIntensitySetting, 90))
eventDict['time'].append(SettingStatic(At(0), BottomController, BottomRightIntensitySetting, 90))
eventDict['time'].append(SettingStatic(At(2), BottomController, BottomLeftIntensitySetting, 0))
eventDict['time'].append(SettingStatic(At(2), BottomController, BottomRightIntensitySetting, 0))
eventDict['time'].append(ChannelSetStatic(At(2), BottomController, BottomStrobeSteptimeChannel, 51))
eventDict['time'].append(ChannelSetStatic(At(2), BottomController, BottomStrobeDarkstepChannel, 1))

beginning = 3
# SCRIPT

eventDict['time'].append(MusicStart(At(beginning), 0))


# 0.40 - 4.40: Buzz Fades In
startTime = beginning + 0.4
dimmduration = 4
eventDict['time'].append(SettingBezierDimm(At(startTime), BottomController, BottomLeftIntensitySetting, 0, 95, int(dimmduration*10), 10, 100, 100))
eventDict['time'].append(SettingBezierDimm(At(startTime), BottomController, BottomRightIntensitySetting, 0, 95, int(dimmduration*10), 10, 100, 100))

# 4:40 - 7.14: Buzz Intensifies
startTime = beginning + 5
dimmduration = 2
# Reset Strobe and add to Right
eventDict['time'].append(ChannelSetStatic(At(startTime), BottomController, BottomStrobeSteptimeChannel, 67))

# 10.00 - 14: Fades Into More Fuzz
startTime = beginning + 12
eventDict['time'].append(ChannelSetStatic(At(startTime), BottomController, BottomStrobeSteptimeChannel, 51))
startTime = beginning + 13
eventDict['time'].append(ChannelSetStatic(At(startTime), BottomController, BottomStrobeSteptimeChannel, 34))
startTime = beginning + 14
eventDict['time'].append(ChannelSetStatic(At(startTime), BottomController, BottomStrobeDarkstepChannel, 0))
eventDict['time'].append(ChannelSetStatic(At(startTime), BottomController, BottomStrobeSteptimeChannel, 51))
startTime = beginning + 15
eventDict['time'].append(ChannelSetStatic(At(startTime), BottomController, BottomStrobeSteptimeChannel, 34))


# TODO: Perlin Vibrato over all of Bottom Starting at 25

# 29.5 - 33: Top Fades in
# Bottom Prep
startTime = beginning + 28.5
dimmduration = 2.5
eventDict['time'].append(SettingBezierDimm(At(startTime), TopController, TopLeftIntensitySetting, 0, 95, int(dimmduration*10), 10, 0, 100))
eventDict['time'].append(SettingBezierDimm(At(startTime), BottomController, BottomLeftIntensitySetting, 95, 8, int(dimmduration*10), 10, 0, 100))
eventDict['time'].append(SettingBezierDimm(At(startTime), BottomController, BottomRightIntensitySetting, 95, 8, int(dimmduration*10), 10, 0, 100))


# 34 - 37: Top Changes To More Crunch
startTime = beginning + 34
dimmduration = 0.5

eventDict['time'].append(ChannelAddEffect(At(startTime), TopController, TopLeftChannel, TopStrobeEffect, 0))
eventDict['time'].append(SettingBezierDimm(At(startTime), BottomController, BottomLeftIntensitySetting, 8, 0, int(dimmduration*10), 10, 0, 100))
eventDict['time'].append(SettingBezierDimm(At(startTime), BottomController, BottomRightIntensitySetting, 8, 0, int(dimmduration*10), 10, 0, 100))

startTime = beginning + 35.5
eventDict['time'].append(ChannelSetStatic(At(startTime), TopController, TopStrobeSteptimeChannel, 34))
eventDict['time'].append(ChannelSetStatic(At(startTime), TopController, TopStrobeDarkstepChannel, 1))

startTime = beginning + 37.8
eventDict['time'].append(ChannelSetStatic(At(startTime), TopController, TopStrobeDarkstepChannel, 0))
eventDict['time'].append(ChannelAddEffect(At(startTime), TopController, TopRightChannel, TopStrobeEffect, 0))
eventDict['time'].append(EffectSequencedLightStrobe(At(startTime), TopController, TopStrobeEffect, TopStrobeSteptimeChannel, TopStrobeDarkstepChannel, 5768))

# Fade In Top Right
# 38-41
startTime = beginning + 38
dimmduration = 3
eventDict['time'].append(SettingBezierDimm(At(startTime), TopController, TopRightIntensitySetting, 0, 95, int(dimmduration*10), 10, 0, 100))

# Switch to Global Strobe
# 43
startTime = beginning + 43
eventDict['time'].append(ChannelSetStatic(At(startTime), BottomController, BottomStrobeSteptimeChannel, 34))
eventDict['time'].append(ChannelSetStatic(At(startTime), BottomController, BottomStrobeDarkstepChannel, 0))
eventDict['time'].append(ChannelSetStatic(At(startTime), TopController, TopStrobeDarkstepChannel, 0))
eventDict['time'].append(ChannelAddEffect(At(startTime), TopController, TopLeftChannel, GlobalStrobeEffect, 0))
eventDict['time'].append(ChannelAddEffect(At(startTime), TopController, TopRightChannel, GlobalStrobeEffect, 0))
eventDict['time'].append(ChannelAddEffect(At(startTime), BottomController, BottomLeftChannel, GlobalStrobeEffect, 0))
eventDict['time'].append(ChannelAddEffect(At(startTime), BottomController, BottomRightChannel, GlobalStrobeEffect, 0))


# Bottom Fades Im
# 46.5 - 48
startTime = beginning + 46.5
dimmduration = 1.5
strength = 60
eventDict['time'].append(SettingBezierDimm(At(startTime), BottomController, BottomLeftIntensitySetting, 0, strength, int(dimmduration*10), 10, 0, 100))
eventDict['time'].append(SettingBezierDimm(At(startTime), BottomController, BottomRightIntensitySetting, 0, strength, int(dimmduration*10), 10, 0, 100))

#Gets crunchier
# 53
startTime = beginning + 53
eventDict['time'].append(ChannelSetStatic(At(startTime), TopController, TopStrobeDarkstepChannel, 1))
eventDict['time'].append(ChannelSetStatic(At(startTime), BottomController, BottomStrobeDarkstepChannel, 1))

#Bottom Fades Down
# 55 - 56
startTime = beginning + 55
dimmduration = 1
eventDict['time'].append(SettingBezierDimm(At(startTime), BottomController, BottomLeftIntensitySetting, strength, 30, int(dimmduration*10), 10, 0, 100))
eventDict['time'].append(SettingBezierDimm(At(startTime), BottomController, BottomRightIntensitySetting, strength, 30, int(dimmduration*10), 10, 0, 100))

#Top Fades Down & Bottom Up
# 61 - 62
startTime = beginning + 61
dimmduration = 1
eventDict['time'].append(SettingBezierDimm(At(startTime), TopController, TopLeftIntensitySetting, 95, 30, int(dimmduration*10), 10, 0, 100))
eventDict['time'].append(SettingBezierDimm(At(startTime), TopController, TopRightIntensitySetting, 95, 30, int(dimmduration*10), 10, 0, 100))
eventDict['time'].append(SettingBezierDimm(At(startTime), BottomController, BottomLeftIntensitySetting, 30, 95, int(dimmduration*10), 10, 0, 100))
eventDict['time'].append(SettingBezierDimm(At(startTime), BottomController, BottomRightIntensitySetting, 30, 95, int(dimmduration*10), 10, 0, 100))

# Bottom Fades Down & Top Up
startTime = beginning + 67.3
dimmduration = 0.5
eventDict['time'].append(SettingBezierDimm(At(startTime), TopController, TopLeftIntensitySetting, 30, 95, int(dimmduration*10), 10, 0, 100))
eventDict['time'].append(SettingBezierDimm(At(startTime), TopController, TopRightIntensitySetting, 30, 95, int(dimmduration*10), 10, 0, 100))
eventDict['time'].append(SettingBezierDimm(At(startTime), BottomController, BottomLeftIntensitySetting, 95, 30, int(dimmduration*10), 10, 0, 100))
eventDict['time'].append(SettingBezierDimm(At(startTime), BottomController, BottomRightIntensitySetting, 95, 30, int(dimmduration*10), 10, 0, 100))

# Bottom Fades Down & Top Up
startTime = beginning + 73.5
dimmduration = 0.5
eventDict['time'].append(SettingBezierDimm(At(startTime), TopController, TopLeftIntensitySetting, 95, 0, int(dimmduration*10), 10, 0, 100))
eventDict['time'].append(SettingBezierDimm(At(startTime), TopController, TopRightIntensitySetting, 95, 0, int(dimmduration*10), 10, 0, 100))
eventDict['time'].append(SettingBezierDimm(At(startTime), BottomController, BottomLeftIntensitySetting, 30, 95, int(dimmduration*10), 10, 0, 100))
eventDict['time'].append(SettingBezierDimm(At(startTime), BottomController, BottomRightIntensitySetting, 30, 95, int(dimmduration*10), 10, 0, 100))

#Fade Out
# 75 - 83
startTime = beginning + 75
dimmduration = 9
eventDict['time'].append(SettingBezierDimm(At(startTime), BottomController, BottomLeftIntensitySetting, 95, 0, int(dimmduration*5), 20, 0, 100))
eventDict['time'].append(SettingBezierDimm(At(startTime), BottomController, BottomRightIntensitySetting, 95, 0, int(dimmduration*5), 20, 0, 100))

# eventDict['time'].append(MotorSpeed(At(0), 90))


eventDict['time'].append(ChannelSetStatic(At(beginning+85), BottomController, BottomStrobeDarkstepChannel, 0))


# eventDict['position'].append(MotorSpeed(At(3), 0))



vd = VisualDriver(eventDict, music=music, usesMotor=False, startTime=0, isTake=False)
vd.start()