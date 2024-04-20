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

music = '/home/maximilian/music/sun_shorter.mp3'




# 1:35
# strobe starts

# 2:55
# Switch to more fine strobe

# 3:48
# hit

# 3:66
# hit

# 3:88
# hit

# 5:70
# hit

# 6:16
# hi

# 6:28
# hit

# 6:64
# hit

# 7:03
# hit

# 8:48
# hit

# 8:76
# hit


# 8:88-9:89
# machine gun


# 9:89
# switch to rough strobe
 

# 11:08
# hit

# 11:96
# hit

# 12:15
# hit

# 12:79
# hit

# 13:37
# hit

# 14:12
# hit

# 17:75
# Switch to not strobe gentle flicker


# GLOBAL VARIABLES
GlobalStrobeEffect = 0

# BOTTOM VARIABLES
BottomIntensitySetting = 0
BottomFlashSetting = 1
BottomIntensitySettingTwo = 2

BottomSetupStrobeEffect = 1
BottomSubtractEffect = 2
BottomStrobeBuildUpEffect = 3

BottomChannel = Channel12
BottomChannelTwo = Channel16
BottomStrobeSteptimeChannel = Channel13
BottomStrobeDarkstepChannel = Channel14
BottomFlashChannel = Channel15

# Bottom Setup
eventDict['position'].append(SettingStatic(At(0), BottomController, BottomIntensitySetting, 0))
eventDict['position'].append(SettingStatic(At(0), BottomController, BottomIntensitySettingTwo, 0))
eventDict['position'].append(ChannelSetSetting(At(0), BottomController, BottomChannel, BottomIntensitySetting))
eventDict['position'].append(ChannelSetSetting(At(0), BottomController, BottomChannelTwo, BottomIntensitySettingTwo))
eventDict['position'].append(LightSetChannel(At(0), BottomController, [Light1, Light2, Light3, Light4], BottomChannel))
eventDict['position'].append(ChannelSetStatic(At(0), BottomController, BottomStrobeSteptimeChannel, 34))
eventDict['position'].append(ChannelSetStatic(At(0), BottomController, BottomStrobeDarkstepChannel, 0))
eventDict['position'].append(EffectSequencedLightStrobe(At(0), BottomController, BottomSetupStrobeEffect, BottomStrobeSteptimeChannel, BottomStrobeDarkstepChannel, 1324))
# eventDict['position'].append(EffectSequencedLightStrobe(At(0), BottomController, BottomStrobeBuildUpEffect, BottomStrobeSteptimeChannel, BottomStrobeDarkstepChannel, 1324))
eventDict['position'].append(EffectSequencedLightStrobe(At(0), BottomController, GlobalStrobeEffect, BottomStrobeSteptimeChannel, BottomStrobeDarkstepChannel, 15372648))

eventDict['position'].append(SettingStatic(At(0), BottomController, BottomFlashSetting, 0))
eventDict['position'].append(ChannelSetSetting(At(0), BottomController, BottomFlashChannel, BottomFlashSetting))
eventDict['position'].append(EffectSubtractPercentage(At(0), BottomController, BottomSubtractEffect, BottomFlashChannel))
eventDict['position'].append(ChannelAddEffect(At(0), BottomController, BottomChannel, BottomSubtractEffect, 2))
eventDict['position'].append(ChannelAddEffect(At(0), BottomController, BottomChannelTwo, BottomSubtractEffect, 2))




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


beginning = 10

# LIGHT SETUP
eventDict['time'].append(ChannelAddEffect(At(beginning-7), BottomController, BottomChannel, BottomSetupStrobeEffect, 0))
eventDict['time'].append(SettingStatic(At(beginning-7), BottomController, BottomIntensitySetting, 90))
eventDict['time'].append(SettingStatic(At(beginning-4), BottomController, BottomIntensitySetting, 0))
# eventDict['time'].append(ChannelSetStatic(At(beginning-4), BottomController, BottomStrobeDarkstepChannel, 1))

# motor
eventDict['time'].append(MotorSpeed(At(beginning-4), 35))

# SCRIPT
eventDict['time'].append(MusicStart(At(beginning), 0))
eventDict['time'].append(SettingStatic(At(beginning), BottomController, BottomIntensitySetting, 20))
eventDict['time'].append(SettingStatic(At(beginning), TopController, TopIntensitySetting, 0))



# # 0:78
# # Setup
startTime = beginning + 0.78
eventDict['time'].append(ChannelAddEffect(At(startTime), TopController, TopChannel, GlobalStrobeEffect, 0))
eventDict['time'].append(ChannelAddEffect(At(startTime), BottomController, BottomChannel, GlobalStrobeEffect, 0))



# 1:00
# Setup
startTime = beginning + 1



# 1:35
# Explosion
startTime = beginning + 1.35
eventDict['time'].append(LightSetChannel(At(startTime), BottomController, [Light1, Light2, Light3, Light4], StaticChannel100))
eventDict['time'].append(SettingStatic(At(beginning), BottomController, BottomIntensitySetting, 0))



# 1:40
# Rough strobe starts
startTime = beginning + 1.43
eventDict['time'].append(LightSetChannel(At(startTime), BottomController, [Light1,Light2, Light3, Light4], BottomChannel))
eventDict['time'].append(SettingStatic(At(startTime), TopController, TopIntensitySetting, 95))


# 2:55
# Switch to more fine strobe
startTime = beginning + 2.55
dimmduration = 5.5
eventDict['time'].append(SettingBezierDimm(At(startTime), BottomController, BottomIntensitySetting, 0, 65, int(dimmduration*10), 10, 0, 50))


# # 3:48
# # hit
# startTime = beginning + 3.48
# eventDict['time'].append(SettingStaticFlash(At(startTime), TopController, TopFlashSetting, 100, 0, 190))
# eventDict['time'].append(SettingStaticFlash(At(startTime), BottomController, BottomFlashSetting, 100, 0, 190))

# # 3:66
# # hit
# startTime = beginning + 3.66
# eventDict['time'].append(SettingStaticFlash(At(startTime), TopController, TopFlashSetting, 100, 0, 190))
# eventDict['time'].append(SettingStaticFlash(At(startTime), BottomController, BottomFlashSetting, 100, 0, 190))

# # 3:88
# # hit
# startTime = beginning + 3.88
# eventDict['time'].append(SettingStaticFlash(At(startTime), TopController, TopFlashSetting, 100, 0, 190))
# eventDict['time'].append(SettingStaticFlash(At(startTime), BottomController, BottomFlashSetting, 100, 0, 190))

# # 5:70
# # hit
# startTime = beginning + 5.70
# eventDict['time'].append(SettingStaticFlash(At(startTime), TopController, TopFlashSetting, 100, 0, 210))
# eventDict['time'].append(SettingStaticFlash(At(startTime), BottomController, BottomFlashSetting, 100, 0, 210))

# # 6:16
# # hit
# startTime = beginning + 6.16
# eventDict['time'].append(SettingStaticFlash(At(startTime), TopController, TopFlashSetting, 100, 0, 210))
# eventDict['time'].append(SettingStaticFlash(At(startTime), BottomController, BottomFlashSetting, 100, 0, 210))

# # 6:28
# # hit
# startTime = beginning + 6.28
# eventDict['time'].append(SettingStaticFlash(At(startTime), TopController, TopFlashSetting, 100, 0, 210))
# eventDict['time'].append(SettingStaticFlash(At(startTime), BottomController, BottomFlashSetting, 100, 0, 210))

# # 6:64
# # hit
# startTime = beginning + 6.64
# eventDict['time'].append(SettingStaticFlash(At(startTime), TopController, TopFlashSetting, 100, 0, 210))
# eventDict['time'].append(SettingStaticFlash(At(startTime), BottomController, BottomFlashSetting, 100, 0, 210))

# # 7:03
# # hit
# startTime = beginning + 7.03
# eventDict['time'].append(SettingStaticFlash(At(startTime), TopController, TopFlashSetting, 100, 0, 210))
# eventDict['time'].append(SettingStaticFlash(At(startTime), BottomController, BottomFlashSetting, 100, 0, 210))

# # 8:48
# # hit
# startTime = beginning + 8.48
# eventDict['time'].append(SettingStaticFlash(At(startTime), TopController, TopFlashSetting, 100, 0, 210))
# eventDict['time'].append(SettingStaticFlash(At(startTime), BottomController, BottomFlashSetting, 100, 0, 210))

# # 8:76
# # hit
# startTime = beginning + 8.76
# eventDict['time'].append(SettingStaticFlash(At(startTime), TopController, TopFlashSetting, 100, 0, 210))
# eventDict['time'].append(SettingStaticFlash(At(startTime), BottomController, BottomFlashSetting, 100, 0, 210))

# 8:88-9:89
# machine gun
startTime = beginning + 8.88
# eventDict['time'].append(ChannelSetStatic(At(startTime), TopController, TopStrobeDarkstepChannel, 1))
# eventDict['time'].append(ChannelSetStatic(At(startTime), BottomController, BottomStrobeSteptimeChannel, 51))
# eventDict['time'].append(ChannelSetStatic(At(startTime), BottomController, BottomStrobeDarkstepChannel, 1))
eventDict['time'].append(SettingStaticMachine(At(startTime), TopController, TopFlashSetting, 100, 35, 65, 50, 12))
eventDict['time'].append(SettingStaticMachine(At(startTime), BottomController, BottomFlashSetting, 100, 35, 65, 50, 12))


# 9:89
# switch to rough strobe
startTime = beginning + 9.89
eventDict['time'].append(LightSetChannel(At(startTime), BottomController, [Light1, Light2, Light3, Light4], StaticChannel100))
eventDict['time'].append(SettingStatic(At(startTime), TopController, TopIntensitySetting, 0))
eventDict['time'].append(ChannelAddEffect(At(startTime), BottomController, BottomChannel, BottomSetupStrobeEffect, 0))
eventDict['time'].append(ChannelSetStatic(At(startTime), BottomController, BottomStrobeDarkstepChannel, 1))


# switch to rough strobe
startTime = beginning + 10.02
eventDict['time'].append(SettingStatic(At(startTime), BottomController, BottomFlashSetting, 0))
eventDict['time'].append(SettingStatic(At(startTime), BottomController, BottomIntensitySetting, 97))
eventDict['time'].append(LightSetChannel(At(startTime), BottomController, [Light1, Light2, Light3, Light4], BottomChannel))
eventDict['time'].append(SettingStatic(At(startTime), TopController, TopFlashSetting, 0))



# # 11:08
# # hit
startTime = beginning + 11.08
eventDict['time'].append(SettingStaticFlash(At(startTime), BottomController, BottomFlashSetting, 100, 0, 250))

# # 11:96
# # hit
# startTime = beginning + 11.96
# eventDict['time'].append(SettingStaticFlash(At(startTime), BottomController, BottomFlashSetting, 100, 0, 250))

# # 12:15
# # hit
# startTime = beginning + 12.15
# eventDict['time'].append(SettingStaticFlash(At(startTime), BottomController, BottomFlashSetting, 100, 0, 250))

# # 12:79
# # hit
# startTime = beginning + 12.79
# eventDict['time'].append(SettingStaticFlash(At(startTime), BottomController, BottomFlashSetting, 100, 0, 250))

# # 13:37
# # hit
# startTime = beginning + 13.37
# eventDict['time'].append(SettingStaticFlash(At(startTime), BottomController, BottomFlashSetting, 100, 0, 250))

# # 14:12
# # hit
# startTime = beginning + 14.12
# eventDict['time'].append(SettingStaticFlash(At(startTime), BottomController, BottomFlashSetting, 100, 0, 250))

# 14:75-17:00
# increase
startTime = beginning + 14.75
dimmduration = 2.25
# eventDict['time'].append(SettingBezierDimm(At(startTime), TopController, TopIntensitySetting, 95, 100, int(dimmduration*100), 1, 0, 100))
eventDict['time'].append(SettingBezierDimm(At(startTime), BottomController, BottomIntensitySetting, 97, 100, int(dimmduration*100), 1, 0, 100))
# Prepare Top
eventDict['time'].append(ChannelRemoveEffect(At(startTime), TopController, TopChannel, 0))
eventDict['time'].append(EffectSubtractPercentage(At(startTime), TopController, TopSubtractEffect, TopPerlinChannel))


# 17:75
# Switch to not strobe gentle flicker
startTime = beginning + 17.5
dimmduration = 0.3
eventDict['time'].append(SettingBezierDimm(At(startTime), BottomController, BottomIntensitySetting, 100, 0, int(dimmduration*100), 1, 0, 100))

startTime = beginning + 17.75
eventDict['time'].append(SettingStatic(At(startTime), TopController, TopIntensitySetting, 30))


# 24
# End
startTime = beginning + 24
eventDict['time'].append(SettingStatic(At(startTime), TopController, TopIntensitySetting, 0))
eventDict['time'].append(MotorSpeed(At(startTime), 90))


eventDict['position'].append(MotorSpeed(At(0.9), 0))


vd = VisualDriver(eventDict, music=music, usesMotor=True, startTime=0, isTake=False)
vd.start()