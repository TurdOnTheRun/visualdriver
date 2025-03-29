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

music = '/home/maximilian/music/flutebbe/full_240620.mp3'

beginning = 0

#VARIABLES
Setting1 = 0
Setting2 = 1
Setting3 = 2
Setting4 = 3
SettingVibrato = 4
SettingPerlin = 5
SettingSidechain = 6


Channel1 = Channel8
Channel2 = Channel9
Channel3 = Channel10
Channel4 = Channel11
ChannelStrobe1Steptime = Channel12
ChannelStrobe1Darkstep = Channel13
ChannelStrobe2Steptime = Channel14
ChannelStrobe2Darkstep = Channel15
ChannelVibratoSteptime = Channel16
ChannelVibrato = Channel17
ChannelPerlinSteptime = Channel18
ChannelPerlin = Channel19
ChannelSidechain = Channel20

EffectStrobe1 = 0
EffectStrobe2 = 1
EffectSubtractPercentageVibrato = 2
EffectSubtractPercentagePerlin = 3
EffectSidechain = 4

# Bottom Setup
eventDict['time'].append(SettingStatic(At(0), BottomController, Setting1, 0))
eventDict['time'].append(SettingStatic(At(0), BottomController, Setting2, 0))
eventDict['time'].append(SettingStatic(At(0), BottomController, Setting3, 0))
eventDict['time'].append(SettingStatic(At(0), BottomController, Setting4, 0))
eventDict['time'].append(SettingSinWave(At(0), BottomController, SettingVibrato, StaticChannel0, StaticChannel100, ChannelVibratoSteptime, StaticChannel0))
eventDict['time'].append(SettingPerlinNoise(At(0), BottomController, SettingPerlin, StaticChannel0, StaticChannel100, ChannelPerlinSteptime, StaticChannel0))
eventDict['time'].append(SettingStatic(At(0), BottomController, SettingSidechain, 0))


eventDict['time'].append(ChannelSetSetting(At(0), BottomController, Channel1, Setting1))
eventDict['time'].append(ChannelSetSetting(At(0), BottomController, Channel2, Setting2))
eventDict['time'].append(ChannelSetSetting(At(0), BottomController, Channel3, Setting3))
eventDict['time'].append(ChannelSetSetting(At(0), BottomController, Channel4, Setting4))
eventDict['time'].append(ChannelSetStatic(At(0), BottomController, ChannelStrobe1Steptime, 34))
eventDict['time'].append(ChannelSetStatic(At(0), BottomController, ChannelStrobe1Darkstep, 0))
eventDict['time'].append(ChannelSetStatic(At(0), BottomController, ChannelStrobe2Steptime, 34))
eventDict['time'].append(ChannelSetStatic(At(0), BottomController, ChannelStrobe2Darkstep, 0))
eventDict['time'].append(ChannelSetStatic(At(0), BottomController, ChannelVibratoSteptime, 17))
eventDict['time'].append(ChannelSetSetting(At(0), BottomController, ChannelVibrato, SettingVibrato))
eventDict['time'].append(ChannelSetStatic(At(0), BottomController, ChannelPerlinSteptime, 5))
eventDict['time'].append(ChannelSetSetting(At(0), BottomController, ChannelPerlin, SettingPerlin))
eventDict['time'].append(ChannelSetSetting(At(0), BottomController, ChannelSidechain, SettingSidechain))


eventDict['time'].append(EffectSequencedLightStrobe(At(0), BottomController, EffectStrobe1, ChannelStrobe1Steptime, ChannelStrobe1Darkstep, 1324))
eventDict['time'].append(EffectSequencedLightStrobe(At(0), BottomController, EffectStrobe2, ChannelStrobe2Steptime, ChannelStrobe2Darkstep, 1324))

eventDict['time'].append(EffectSubtractPercentage(At(0), BottomController, EffectSubtractPercentageVibrato, ChannelVibrato))
eventDict['time'].append(EffectSubtractPercentage(At(0), BottomController, EffectSubtractPercentagePerlin, ChannelPerlin))

eventDict['time'].append(EffectSubtract(At(0), BottomController, EffectSidechain, ChannelSidechain))


eventDict['time'].append(LightSetChannel(At(0), BottomController, [Light1,], Channel1))
eventDict['time'].append(LightSetChannel(At(0), BottomController, [Light2,], Channel2))
eventDict['time'].append(LightSetChannel(At(0), BottomController, [Light3,], Channel3))
eventDict['time'].append(LightSetChannel(At(0), BottomController, [Light4,], Channel4))


# Top Setup
eventDict['time'].append(SettingStatic(At(0), TopController, Setting1, 0))
eventDict['time'].append(SettingStatic(At(0), TopController, Setting2, 0))
eventDict['time'].append(SettingStatic(At(0), TopController, Setting3, 0))
eventDict['time'].append(SettingStatic(At(0), TopController, Setting4, 0))
eventDict['time'].append(SettingSinWave(At(0), TopController, SettingVibrato, StaticChannel0, StaticChannel100, ChannelVibratoSteptime, StaticChannel0))
eventDict['time'].append(SettingPerlinNoise(At(0), TopController, SettingPerlin, StaticChannel0, StaticChannel100, ChannelPerlinSteptime, StaticChannel0))
eventDict['time'].append(SettingStatic(At(0), TopController, SettingSidechain, 0))


eventDict['time'].append(ChannelSetSetting(At(0), TopController, Channel1, Setting1))
eventDict['time'].append(ChannelSetSetting(At(0), TopController, Channel2, Setting2))
eventDict['time'].append(ChannelSetSetting(At(0), TopController, Channel3, Setting3))
eventDict['time'].append(ChannelSetSetting(At(0), TopController, Channel4, Setting4))
eventDict['time'].append(ChannelSetStatic(At(0), TopController, ChannelStrobe1Steptime, 34))
eventDict['time'].append(ChannelSetStatic(At(0), TopController, ChannelStrobe1Darkstep, 0))
eventDict['time'].append(ChannelSetStatic(At(0), TopController, ChannelStrobe2Steptime, 34))
eventDict['time'].append(ChannelSetStatic(At(0), TopController, ChannelStrobe2Darkstep, 0))
eventDict['time'].append(ChannelSetStatic(At(0), TopController, ChannelVibratoSteptime, 17))
eventDict['time'].append(ChannelSetSetting(At(0), TopController, ChannelVibrato, SettingVibrato))
eventDict['time'].append(ChannelSetStatic(At(0), TopController, ChannelPerlinSteptime, 5))
eventDict['time'].append(ChannelSetSetting(At(0), TopController, ChannelPerlin, SettingPerlin))
eventDict['time'].append(ChannelSetSetting(At(0), TopController, ChannelSidechain, SettingSidechain))


eventDict['time'].append(EffectSequencedLightStrobe(At(0), TopController, EffectStrobe1, ChannelStrobe1Steptime, ChannelStrobe1Darkstep, 1324))
eventDict['time'].append(EffectSequencedLightStrobe(At(0), TopController, EffectStrobe2, ChannelStrobe2Steptime, ChannelStrobe2Darkstep, 1324))

eventDict['time'].append(EffectSubtractPercentage(At(0), TopController, EffectSubtractPercentageVibrato, ChannelVibrato))
eventDict['time'].append(EffectSubtractPercentage(At(0), TopController, EffectSubtractPercentagePerlin, ChannelPerlin))

eventDict['time'].append(EffectSubtract(At(0), TopController, EffectSidechain, ChannelSidechain))


eventDict['time'].append(LightSetChannel(At(0), TopController, [Light1,], Channel1))
eventDict['time'].append(LightSetChannel(At(0), TopController, [Light2,], Channel2))
eventDict['time'].append(LightSetChannel(At(0), TopController, [Light3,], Channel3))
eventDict['time'].append(LightSetChannel(At(0), TopController, [Light4,], Channel4))



# STATE SUMMARY
# 
# TOP                               | BOTTOM
#                                   |
# Settings                          | Settings
# --------------------------------- | ---------------------------------
#   Setting1:            0          |   Setting1:            0
#   Setting2:            0          |   Setting2:            0
#   Setting3:            0          |   Setting3:            0
#   Setting4:            0          |   Setting4:            0
#
#   SettingVibrato:     0 to 100    |   SettingVibrato:     0 to 100
#   SettingPerlin:      0 to 100    |   SettingPerlin:      0 to 100
#
# Static Channels                   | Static Channels
# --------------------------------- | ---------------------------------
#   ChannelStrobe1Steptime: 34      |   ChannelStrobe1Steptime: 34
#   ChannelStrobe1Darkstep: 0       |   ChannelStrobe1Darkstep: 0
#   ChannelStrobe2Steptime: 34      |   ChannelStrobe2Steptime: 34
#   ChannelStrobe2Darkstep: 0       |   ChannelStrobe2Darkstep: 0
#
#   ChannelVibratoSteptime: 17      |   ChannelVibratoSteptime: 17
#   ChannelPerlinSteptime:  5       |   ChannelPerlinSteptime:  5
#
# Effects                           | Effects
# --------------------------------- | ---------------------------------
#   EffectStrobe1:        1324      |   EffectStrobe1:        1324
#   EffectStrobe2:        1324      |   EffectStrobe2:        1324
#
# Light Channels                    | Light Channels
# --------------------------------- | ---------------------------------
#   Channel1:          Setting1, [] |   Channel1:          Setting1, []
#   Channel2:          Setting2, [] |   Channel2:          Setting2, []
#   Channel3:          Setting3, [] |   Channel3:          Setting3, []
#   Channel4:          Setting4, [] |   Channel4:          Setting4, []






# SCRIPT
beginning = 3
eventDict['time'].append(MusicStart(At(beginning), 0))

# 0
# Explosion
# 0-1.2
# Explosion Fades away
startTime = beginning + 0
dimmduration = 1.2
eventDict['time'].append(SettingImpulseToBezierFadeout(At(startTime), TopController, Setting3, 100, 1, 95, 2, int(dimmduration*10), 10, 100, 100))
eventDict['time'].append(SettingImpulseToBezierFadeout(At(startTime), BottomController, Setting1, 100, 1, 95, 2, int(dimmduration*10), 10, 100, 100))
eventDict['time'].append(SettingImpulseToBezierFadeout(At(startTime), BottomController, Setting3, 100, 1, 95, 2, int(dimmduration*10), 10, 100, 100))

# 0.5
# SETUP PART I

#FLUT
#Bottom 1 & 2
#Top 2

#EBBE
#Bottom 4
#Top 4

startTime = beginning + 0.5

eventDict['time'].append(ChannelSetStatic(At(startTime), TopController, ChannelStrobe1Darkstep, 1))
eventDict['time'].append(ChannelSetStatic(At(startTime), BottomController, ChannelStrobe1Darkstep, 1))
eventDict['time'].append(EffectSequencedLightStrobe(At(startTime), TopController, EffectStrobe1, ChannelStrobe1Steptime, ChannelStrobe1Darkstep, 1616))
eventDict['time'].append(EffectSequencedLightStrobe(At(startTime), BottomController, EffectStrobe1, ChannelStrobe1Steptime, ChannelStrobe1Darkstep, 1616))
eventDict['time'].append(EffectSequencedLightStrobe(At(startTime), BottomController, EffectStrobe2, ChannelStrobe2Steptime, ChannelStrobe2Darkstep, 1212))

eventDict['time'].append(ChannelAddEffect(At(startTime), BottomController, Channel1, EffectStrobe2, 0))
eventDict['time'].append(ChannelAddEffect(At(startTime), BottomController, Channel2, EffectStrobe2, 0))

eventDict['time'].append(ChannelSetStatic(At(startTime), BottomController, ChannelStrobe2Darkstep, 1))


# STATE SUMMARY
# 
# TOP                               | BOTTOM
#                                   |
# Settings                          | Settings
# --------------------------------- | ---------------------------------
#   Setting1:            0          |   Setting1:            0
#   Setting2:            0          |   Setting2:            0
#   Setting3:            0          |   Setting3:            0
#   Setting4:            0          |   Setting4:            0
#
#   SettingVibrato:     0 to 100    |   SettingVibrato:     0 to 100
#   SettingPerlin:      0 to 100    |   SettingPerlin:      0 to 100
#
# Static Channels                   | Static Channels
# --------------------------------- | ---------------------------------
#   ChannelStrobe1Steptime: 34      |   ChannelStrobe1Steptime: 34
#   ChannelStrobe1Darkstep: 1       |   ChannelStrobe1Darkstep: 1
#   ChannelStrobe2Steptime: 34      |   ChannelStrobe2Steptime: 34
#   ChannelStrobe2Darkstep: 0       |   ChannelStrobe2Darkstep: 1
#
#   ChannelVibratoSteptime: 17      |   ChannelVibratoSteptime: 17
#   ChannelPerlinSteptime:  5       |   ChannelPerlinSteptime:  5
#
# Effects                           | Effects
# --------------------------------- | ---------------------------------
#   EffectStrobe1:        1616      |   EffectStrobe1:        1616
#   EffectStrobe2:        1324      |   EffectStrobe2:        1212
#
# Light Channels                    | Light Channels
# --------------------------------- | ---------------------------------
#   Channel1:          Setting1, [] |   Channel1:          Setting1, [Strobe2, ]
#   Channel2:          Setting2, [] |   Channel2:          Setting2, [Strobe2, ]
#   Channel3:          Setting3, [] |   Channel3:          Setting3, []
#   Channel4:          Setting4, [] |   Channel4:          Setting4, []


# 0.6 - 2
# Left Strobe Fades In
startTime = beginning + 0.6
dimmduration = 1.4
eventDict['time'].append(SettingBezierDimm(At(startTime), BottomController, Setting1, 0, 100, int(dimmduration*10), 10, 0, 100))
eventDict['time'].append(SettingBezierDimm(At(startTime), BottomController, Setting2, 0, 100, int(dimmduration*10), 10, 0, 100))


# 2.51 - 3.31
# More Intense Strobe Fades In
startTime = beginning + 2.51
dimmduration = 0.8
eventDict['time'].append(ChannelAddEffect(At(startTime), BottomController, Channel1, EffectStrobe1, 0))
eventDict['time'].append(ChannelAddEffect(At(startTime), TopController, Channel2, EffectStrobe1, 0))


# STATE SUMMARY
# 
# TOP                               | BOTTOM
#                                   |
#
# Light Channels                    | Light Channels
# --------------------------------- | ---------------------------------
#   Channel1: Setting1, []          |   Channel1:          Setting1, [Strobe1, ]
#   Channel2: Setting2, [Strobe1]   |   Channel2:          Setting2, [Strobe2, ]
#   Channel3: Setting3, []          |   Channel3:          Setting3, []
#   Channel4: Setting4, []          |   Channel4:          Setting4, []


eventDict['time'].append(SettingBezierDimm(At(startTime), BottomController, Setting2, 100, 0, int(dimmduration/4*10), 10, 0, 100))
eventDict['time'].append(SettingBezierDimm(At(startTime), TopController, Setting2, 0, 100, int(dimmduration*10), 10, 0, 100))

# 3.32
#Tiny right wave
startTime = beginning + 3.32
fadeOutLength = 2.5
# sustainSteptime 0
sustainSteptime = 4
eventDict['time'].append(SettingImpulseToBezierFadeout(At(startTime), BottomController, Setting4, 75, 1, 30, sustainSteptime, int(fadeOutLength*10), 10, 100, 100))



# 3.83
# Darkstep Off
startTime = beginning + 3.83
dimmduration = 0.2
eventDict['time'].append(SettingBezierDimm(At(startTime), BottomController, Setting2, 0, 100, int(dimmduration/4*10), 10, 0, 100))
eventDict['time'].append(SettingBezierDimm(At(startTime), TopController, Setting2, 100, 0, int(dimmduration*10), 10, 0, 100))
eventDict['time'].append(ChannelAddEffect(At(startTime), BottomController, Channel1, EffectStrobe2, 0))

# STATE SUMMARY
# 
# TOP                               | BOTTOM
#                                   |
#
# Light Channels                    | Light Channels
# --------------------------------- | ---------------------------------
#   Channel1: Setting1, []          |   Channel1:          Setting1, [Strobe2, ]
#   Channel2: Setting2, [Strobe1]   |   Channel2:          Setting2, [Strobe2, ]
#   Channel3: Setting3, []          |   Channel3:          Setting3, []
#   Channel4: Setting4, []          |   Channel4:          Setting4, []


# 3.83 - 5.23
# Fade Out
startTime = beginning + 3.83
dimmduration = 2.4
eventDict['time'].append(SettingBezierDimm(At(startTime), BottomController, Setting1, 100, 0, int(dimmduration*10), 10, 0, 100))
eventDict['time'].append(SettingBezierDimm(At(startTime), BottomController, Setting2, 100, 0, int(dimmduration*10), 10, 0, 100))

# 5.26
# Piano with Release until 6.71
startTime = beginning + 5.26
fadeOutLength = 2
# sustainSteptime 0
sustainSteptime = 5
eventDict['time'].append(SettingImpulseToBezierFadeout(At(startTime), BottomController, Setting4, 100, 1, 40, sustainSteptime, int(fadeOutLength*10), 10, 100, 100))


# 6.3
# Darkstep On
startTime = beginning + 6.3
eventDict['time'].append(ChannelAddEffect(At(startTime), BottomController, Channel1, EffectStrobe1, 0))


# STATE SUMMARY
# 
# TOP                               | BOTTOM
#                                   |
#
# Light Channels                    | Light Channels
# --------------------------------- | ---------------------------------
#   Channel1: Setting1, []          |   Channel1:          Setting1, [Strobe1, ]
#   Channel2: Setting2, [Strobe1]   |   Channel2:          Setting2, [Strobe2, ]
#   Channel3: Setting3, []          |   Channel3:          Setting3, []
#   Channel4: Setting4, []          |   Channel4:          Setting4, []

# 6.35 - 7.5
# Darkstep Wave
startTime = beginning + 6.35
dimmduration = 0.6
eventDict['time'].append(SettingBezierDimm(At(startTime), BottomController, Setting1, 0, 100, int(dimmduration*10), 10, 0, 100))
eventDict['time'].append(SettingBezierDimm(At(startTime), TopController, Setting2, 0, 100, int(dimmduration*10), 10, 0, 100))
startTime = startTime + dimmduration
dimmduration = 0.6
eventDict['time'].append(SettingBezierDimm(At(startTime), BottomController, Setting1, 100, 0, int(dimmduration*10), 10, 0, 100))
eventDict['time'].append(SettingBezierDimm(At(startTime), TopController, Setting2, 100, 0, int(dimmduration*10), 10, 0, 100))


# 7.38
#Tiny right wave
startTime = beginning + 7.38
fadeOutLength = 2.5
# sustainSteptime 0
sustainSteptime = 4
eventDict['time'].append(SettingImpulseToBezierFadeout(At(startTime), BottomController, Setting4, 75, 1, 30, sustainSteptime, int(fadeOutLength*10), 10, 100, 100))



# 7.5
# Darkstep Off
startTime = beginning + 7.5
eventDict['time'].append(ChannelAddEffect(At(startTime), BottomController, Channel1, EffectStrobe2, 0))

# STATE SUMMARY
# 
# TOP                               | BOTTOM
#                                   |
#
# Light Channels                    | Light Channels
# --------------------------------- | ---------------------------------
#   Channel1: Setting1, []          |   Channel1:          Setting1, [Strobe2, ]
#   Channel2: Setting2, [Strobe1]   |   Channel2:          Setting2, [Strobe2, ]
#   Channel3: Setting3, []          |   Channel3:          Setting3, []
#   Channel4: Setting4, []          |   Channel4:          Setting4, []

# 7.5 - 9.39
# Strobe Wave
startTime = beginning + 7.5
dimmduration = 0.6
eventDict['time'].append(SettingBezierDimm(At(startTime), BottomController, Setting1, 0, 100, int(dimmduration*10), 10, 0, 100))
eventDict['time'].append(SettingBezierDimm(At(startTime), BottomController, Setting2, 0, 100, int(dimmduration*10), 10, 0, 100))
startTime = startTime + dimmduration
dimmduration = 1.6
eventDict['time'].append(SettingBezierDimm(At(startTime), BottomController, Setting1, 100, 0, int(dimmduration*10), 10, 0, 100))
eventDict['time'].append(SettingBezierDimm(At(startTime), BottomController, Setting2, 100, 0, int(dimmduration*10), 10, 0, 100))

# 9.5
# Right Soft Piano with release until 11.1
startTime = beginning + 9.5
fadeOutLength = 3.5
# sustainSteptime 0
sustainSteptime = 5
eventDict['time'].append(SettingImpulseToBezierFadeout(At(startTime), BottomController, Setting4, 75, 1, 30, sustainSteptime, int(fadeOutLength*10), 10, 100, 100))


# 11.09
# Right Soft-Piano with release until 12.08
startTime = beginning + 11.09
fadeOutLength = 2.3
# sustainSteptime 0
sustainSteptime = 5
eventDict['time'].append(SettingImpulseToBezierFadeout(At(startTime), BottomController, Setting3, 75, 1, 30, sustainSteptime, int(fadeOutLength*10), 10, 100, 100))


# 12.05 - 12.58
# Soft Strobe Fade In
startTime = beginning + 12.05
dimmduration = 0.53
eventDict['time'].append(SettingBezierDimm(At(startTime), BottomController, Setting1, 0, 60, int(dimmduration*10), 10, 0, 100))
eventDict['time'].append(SettingBezierDimm(At(startTime), BottomController, Setting2, 0, 60, int(dimmduration*10), 10, 0, 100))

# 12.58 - 13.43
# Strobe Fade to Full
startTime = beginning + 12.58
dimmduration = 0.85
eventDict['time'].append(SettingBezierDimm(At(startTime), BottomController, Setting1, 60, 80, int(dimmduration*10), 10, 0, 100))
eventDict['time'].append(SettingBezierDimm(At(startTime), BottomController, Setting2, 60, 80, int(dimmduration*10), 10, 0, 100))

# 13.43-14.07
# Strobe Fade Out
startTime = beginning + 13.43
dimmduration = 0.65
eventDict['time'].append(SettingBezierDimm(At(startTime), BottomController, Setting1, 80, 0, int(dimmduration*10), 10, 0, 100))
eventDict['time'].append(SettingBezierDimm(At(startTime), BottomController, Setting2, 80, 0, int(dimmduration*10), 10, 0, 100))

# 14.07 - 15.67
# Strobe Fade In
startTime = beginning + 14
dimmduration = 1
eventDict['time'].append(SettingBezierDimm(At(startTime), BottomController, Setting1, 0, 90, int(dimmduration*10), 10, 0, 100))
eventDict['time'].append(SettingBezierDimm(At(startTime), BottomController, Setting2, 0, 90, int(dimmduration*10), 10, 0, 100))

# 14.07 - 14.73
# Light Darkstep Strobe Wave in background
startTime = beginning + 14.07
dimmduration = 0.35
eventDict['time'].append(SettingBezierDimm(At(startTime), TopController, Setting2, 0, 60, int(dimmduration*10), 10, 0, 100))
startTime = startTime + dimmduration
dimmduration = 0.35
eventDict['time'].append(SettingBezierDimm(At(startTime), TopController, Setting2, 60, 0, int(dimmduration*10), 10, 0, 100))

# 16.06
#Tiny right wave
startTime = beginning + 16.06
fadeOutLength = 2.5
# sustainSteptime 0
sustainSteptime = 4
eventDict['time'].append(SettingImpulseToBezierFadeout(At(startTime), BottomController, Setting4, 75, 1, 30, sustainSteptime, int(fadeOutLength*10), 10, 100, 100))


# 16.29 - 17.44
# Strobe Fade Out
startTime = beginning + 16.29
dimmduration = 4.5
eventDict['time'].append(SettingBezierDimm(At(startTime), BottomController, Setting1, 90, 0, int(dimmduration*10), 10, 50, 100))
eventDict['time'].append(SettingBezierDimm(At(startTime), BottomController, Setting2, 90, 0, int(dimmduration*10), 10, 50, 100))

# 18
# Darkstep On
startTime = beginning + 18
eventDict['time'].append(ChannelAddEffect(At(startTime), BottomController, Channel1, EffectStrobe1, 0))

# STATE SUMMARY
# 
# TOP                               | BOTTOM
#                                   |
#
# Light Channels                    | Light Channels
# --------------------------------- | ---------------------------------
#   Channel1: Setting1, []          |   Channel1:          Setting1, [Strobe1, ]
#   Channel2: Setting2, [Strobe1]   |   Channel2:          Setting2, [Strobe2, ]
#   Channel3: Setting3, []          |   Channel3:          Setting3, []
#   Channel4: Setting4, []          |   Channel4:          Setting4, []

# 18.73 - 20.02
# Strong Left Darkstep Wave
startTime = beginning + 18.73
dimmduration = 1.15
eventDict['time'].append(SettingBezierDimm(At(startTime), BottomController, Setting1, 0, 95, int(dimmduration*10), 10, 0, 100))
eventDict['time'].append(SettingBezierDimm(At(startTime), TopController, Setting2, 0, 95, int(dimmduration*10), 10, 0, 100))
startTime = startTime + dimmduration
dimmduration = 1.15
eventDict['time'].append(SettingBezierDimm(At(startTime), BottomController, Setting1, 95, 0, int(dimmduration*10), 10, 0, 100))
eventDict['time'].append(SettingBezierDimm(At(startTime), TopController, Setting2, 95, 0, int(dimmduration*10), 10, 0, 100))


# 20.03 - 20.95
# Light Left Darkstep Wave
startTime = beginning + 20.03
dimmduration = 0.45
eventDict['time'].append(SettingBezierDimm(At(startTime), BottomController, Setting1, 0, 50, int(dimmduration*10), 10, 0, 100))
eventDict['time'].append(SettingBezierDimm(At(startTime), TopController, Setting2, 0, 50, int(dimmduration*10), 10, 0, 100))
startTime = startTime + dimmduration
dimmduration = 0.45
eventDict['time'].append(SettingBezierDimm(At(startTime), BottomController, Setting1, 50, 0, int(dimmduration*10), 10, 0, 100))
eventDict['time'].append(SettingBezierDimm(At(startTime), TopController, Setting2, 50, 0, int(dimmduration*10), 10, 0, 100))

# 21.03
# Right Piano with release until 22.07
startTime = beginning + 21.03
fadeOutLength = 1.8
# sustainSteptime 0
sustainSteptime = 5
eventDict['time'].append(SettingImpulseToBezierFadeout(At(startTime), BottomController, Setting4, 95, 1, 40, sustainSteptime, int(fadeOutLength*10), 10, 100, 100))


# 22.07
# Right and Top Right Piano with relese until 22.89
startTime = beginning + 22.07
fadeOutLength = 6
# sustainSteptime 0
sustainSteptime = 5
eventDict['time'].append(SettingImpulseToBezierFadeout(At(startTime), TopController, Setting4, 95, 1, 40, sustainSteptime, int(fadeOutLength*10), 10, 100, 100))
eventDict['time'].append(SettingImpulseToBezierFadeout(At(startTime), BottomController, Setting4, 95, 1, 40, sustainSteptime, int(fadeOutLength*10), 10, 100, 100))


# 22.9-24
# Light Strobe Wave
startTime = beginning + 22.9
dimmduration = 0.55
eventDict['time'].append(SettingBezierDimm(At(startTime), BottomController, Setting1, 0, 65, int(dimmduration*10), 10, 0, 100))
eventDict['time'].append(SettingBezierDimm(At(startTime), BottomController, Setting2, 0, 65, int(dimmduration*10), 10, 0, 100))
startTime = startTime + dimmduration
dimmduration = 2
eventDict['time'].append(SettingBezierDimm(At(startTime), BottomController, Setting1, 65, 0, int(dimmduration*10), 10, 50, 100))
eventDict['time'].append(SettingBezierDimm(At(startTime), BottomController, Setting2, 65, 0, int(dimmduration*10), 10, 50, 100))

# 26.05-27
# Light Strobe Wave
startTime = beginning + 26.05
dimmduration = 0.5
eventDict['time'].append(SettingBezierDimm(At(startTime), BottomController, Setting1, 0, 65, int(dimmduration*10), 10, 0, 100))
eventDict['time'].append(SettingBezierDimm(At(startTime), BottomController, Setting2, 0, 65, int(dimmduration*10), 10, 0, 100))
startTime = startTime + dimmduration
dimmduration = 1.5
eventDict['time'].append(SettingBezierDimm(At(startTime), BottomController, Setting1, 65, 0, int(dimmduration*10), 10, 0, 100))
eventDict['time'].append(SettingBezierDimm(At(startTime), BottomController, Setting2, 65, 0, int(dimmduration*10), 10, 0, 100))

# 28
# Top Light Piano with Release until 28.7
startTime = beginning + 28
fadeOutLength = 1.5
# sustainSteptime 0
sustainSteptime = 5
eventDict['time'].append(SettingImpulseToBezierFadeout(At(startTime), TopController, Setting4, 95, 1, 40, sustainSteptime, int(fadeOutLength*10), 10, 100, 100))


# 28.6
# Top And Right Piano with release until 32.7
startTime = beginning + 28.6
fadeOutLength = 6
# sustainSteptime 0
sustainSteptime = 5
eventDict['time'].append(SettingImpulseToBezierFadeout(At(startTime), TopController, Setting4, 95, 1, 40, sustainSteptime, int(fadeOutLength*10), 10, 100, 100))
eventDict['time'].append(SettingImpulseToBezierFadeout(At(startTime), BottomController, Setting4, 95, 1, 40, sustainSteptime, int(fadeOutLength*10), 10, 100, 100))


# 32.78
# Light Piano with Quick release
startTime = beginning + 32.78
fadeOutLength = 1.1
# sustainSteptime 0
sustainSteptime = 5
eventDict['time'].append(SettingImpulseToBezierFadeout(At(startTime), TopController, Setting4, 80, 1, 35, sustainSteptime, int(fadeOutLength*10), 10, 100, 100))


# 33
# Top and Right Piano with release until 40
startTime = beginning + 33
fadeOutLength = 8
# sustainSteptime 0
sustainSteptime = 5
eventDict['time'].append(SettingImpulseToBezierFadeout(At(startTime), TopController, Setting4, 95, 1, 40, sustainSteptime, int(fadeOutLength*10), 10, 100, 100))
eventDict['time'].append(SettingImpulseToBezierFadeout(At(startTime), BottomController, Setting4, 95, 1, 40, sustainSteptime, int(fadeOutLength*10), 10, 100, 100))

# 35.8 - Slight drum hit
# TODO

# 38 - 39.2
# Strong Left Darkstep Wave
startTime = beginning + 38
dimmduration = 0.5
eventDict['time'].append(SettingBezierDimm(At(startTime), BottomController, Setting1, 0, 95, int(dimmduration*10), 10, 0, 100))
eventDict['time'].append(SettingBezierDimm(At(startTime), TopController, Setting2, 0, 95, int(dimmduration*10), 10, 0, 100))
startTime = startTime + dimmduration
dimmduration = 0.8
eventDict['time'].append(SettingBezierDimm(At(startTime), BottomController, Setting1, 95, 0, int(dimmduration*10), 10, 0, 100))
eventDict['time'].append(SettingBezierDimm(At(startTime), TopController, Setting2, 95, 0, int(dimmduration*10), 10, 0, 100))


# 40
# Piano with quick release
startTime = beginning + 40
fadeOutLength = 0.1
# sustainSteptime 0
sustainSteptime = 5
eventDict['time'].append(SettingImpulseToBezierFadeout(At(startTime), BottomController, Setting4, 95, 1, 40, sustainSteptime, int(fadeOutLength*10), 10, 100, 100))


# 40,6
# Piano with quick release
startTime = beginning + 40.6
fadeOutLength = 0.1
# sustainSteptime 0
sustainSteptime = 5
eventDict['time'].append(SettingImpulseToBezierFadeout(At(startTime), BottomController, Setting4, 95, 1, 40, sustainSteptime, int(fadeOutLength*10), 10, 100, 100))

# 41
# Piano with quick release
startTime = beginning + 41
fadeOutLength = 2
# sustainSteptime 0
sustainSteptime = 5
eventDict['time'].append(SettingImpulseToBezierFadeout(At(startTime), TopController, Setting4, 100, 1, 40, sustainSteptime, int(fadeOutLength*10), 10, 90, 100))


# 41 - 42
# Strong Left Darkstep Wave
startTime = beginning + 41
dimmduration = 0.5
eventDict['time'].append(SettingBezierDimm(At(startTime), BottomController, Setting1, 0, 95, int(dimmduration*10), 10, 0, 100))
eventDict['time'].append(SettingBezierDimm(At(startTime), TopController, Setting2, 0, 95, int(dimmduration*10), 10, 0, 100))
startTime = startTime + dimmduration
dimmduration = 0.5
eventDict['time'].append(SettingBezierDimm(At(startTime), BottomController, Setting1, 95, 0, int(dimmduration*10), 10, 0, 100))
eventDict['time'].append(SettingBezierDimm(At(startTime), TopController, Setting2, 95, 0, int(dimmduration*10), 10, 0, 100))



# 41 MOtor On
# 41 - 44 Back Light Fades in
startTime = beginning + 41
dimmduration = 3
eventDict['time'].append(SettingBezierDimm(At(startTime), TopController, Setting3, 0, 95, int(dimmduration*10), 10, 0, 100))

# eventDict['time'].append(MotorSpeed(At(startTime), 90))
# # Bremsfactor 0.0856
# eventDict['position'].append(MotorSpeed(GE(3.25 - 0.0856), 0))

# 42.12 - 42.8
# Strong Left Darkstep Wave
startTime = beginning + 42.12
dimmduration = 0.6
eventDict['time'].append(SettingBezierDimm(At(startTime), BottomController, Setting1, 0, 80, int(dimmduration*10), 10, 0, 100))
eventDict['time'].append(SettingBezierDimm(At(startTime), TopController, Setting2, 0, 80, int(dimmduration*10), 10, 0, 100))
startTime = startTime + dimmduration
dimmduration = 0.2
eventDict['time'].append(SettingBezierDimm(At(startTime), BottomController, Setting1, 80, 0, int(dimmduration*10), 10, 0, 100))
eventDict['time'].append(SettingBezierDimm(At(startTime), TopController, Setting2, 80, 0, int(dimmduration*10), 10, 0, 100))

# 42.8 - 44
# Bassy Fade In


# Part II

#Flut
#Bottom 2
#Top 2

#Glitter Strobe
#Top 1 & 3
#Bottom 1 & 3

#Ebbe
#Bottom 4
#Top 4

#TODO: Sidechain Glitter Strobe from Flut & Ebbe

startTime = beginning + 42.8

eventDict['time'].append(EffectSequencedLightStrobe(At(startTime), TopController, EffectStrobe1, ChannelStrobe1Steptime, ChannelStrobe1Darkstep, 1537))
eventDict['time'].append(EffectSequencedLightStrobe(At(startTime), BottomController, EffectStrobe1, ChannelStrobe1Steptime, ChannelStrobe1Darkstep, 1537))
eventDict['time'].append(EffectSequencedLightStrobe(At(startTime), TopController, EffectStrobe2, ChannelStrobe2Steptime, ChannelStrobe2Darkstep, 2626))
eventDict['time'].append(EffectSequencedLightStrobe(At(startTime), BottomController, EffectStrobe2, ChannelStrobe2Steptime, ChannelStrobe2Darkstep, 2626))

eventDict['time'].append(ChannelAddEffect(At(startTime), BottomController, Channel1, EffectStrobe1, 0))
eventDict['time'].append(ChannelAddEffect(At(startTime), TopController, Channel1, EffectStrobe1, 0))

eventDict['time'].append(ChannelAddEffect(At(startTime), TopController, Channel2, EffectStrobe2, 0))
eventDict['time'].append(ChannelAddEffect(At(startTime), BottomController, Channel2, EffectStrobe2, 0))
eventDict['time'].append(ChannelSetStatic(At(startTime), TopController, ChannelStrobe2Darkstep, 1))

# Temporary for explosion
eventDict['time'].append(ChannelSetStatic(At(startTime), BottomController, ChannelStrobe1Steptime, 34))
eventDict['time'].append(ChannelSetStatic(At(startTime), BottomController, ChannelStrobe1Darkstep, 0)) #off because 5 and 7 are in the strobe effect as well
eventDict['time'].append(ChannelSetStatic(At(startTime), TopController, ChannelStrobe1Darkstep, 0)) 

eventDict['time'].append(LightSetChannel(At(startTime), BottomController, [Light3,], Channel1))

eventDict['time'].append(ChannelAddEffect(At(startTime), TopController, Channel1, EffectSidechain, 1))
eventDict['time'].append(ChannelAddEffect(At(startTime), BottomController, Channel1, EffectSidechain, 1))



# STATE SUMMARY
# 
# TOP                               | BOTTOM
#                                   |
# Settings                          | Settings
# --------------------------------- | ---------------------------------
#   Setting1:            0          |   Setting1:            0
#   Setting2:            0          |   Setting2:            0
#   Setting3:            95         |   Setting3:            0
#   Setting4:            0          |   Setting4:            0
#
#   SettingVibrato:     0 to 100    |   SettingVibrato:     0 to 100
#   SettingPerlin:      0 to 100    |   SettingPerlin:      0 to 100
#
# Static Channels                   | Static Channels
# --------------------------------- | ---------------------------------
#   ChannelStrobe1Steptime: 34      |   ChannelStrobe1Steptime: 34
#   ChannelStrobe1Darkstep: 1       |   ChannelStrobe1Darkstep: 1
#   ChannelStrobe2Steptime: 34      |   ChannelStrobe2Steptime: 34
#   ChannelStrobe2Darkstep: 1       |   ChannelStrobe2Darkstep: 1
#
#   ChannelVibratoSteptime: 17      |   ChannelVibratoSteptime: 17
#   ChannelPerlinSteptime:  5       |   ChannelPerlinSteptime:  5
#
# Effects                           | Effects
# --------------------------------- | ---------------------------------
#   EffectStrobe1:        1537      |   EffectStrobe1:        1537
#   EffectStrobe2:        2626      |   EffectStrobe2:        2626
#
# Light Channels                    | Light Channels
# --------------------------------- | ---------------------------------
#   Channel1: Setting1, [Strobe1, ] |   Channel1: Setting1, [Strobe1, ]
#   Channel2: Setting2, [Strobe2, ] |   Channel2: Setting2, [Strobe2, ]
#   Channel3: Setting3, []          |   Channel3: Setting3, []
#   Channel4: Setting4, []          |   Channel4: Setting4, []




# 44 In
# Buzzing Explosion
startTime = beginning + 43.9
dimmduration = 0.1
eventDict['time'].append(SettingStatic(At(startTime), TopController, Setting3, 0))
eventDict['time'].append(SettingStatic(At(startTime), BottomController, Setting1, 100))
eventDict['time'].append(SettingStatic(At(startTime), BottomController, Setting3, 100))
startTime = beginning + 45
dimmduration = 2
eventDict['time'].append(SettingBezierDimm(At(startTime), BottomController, Setting1, 30, 0, int(dimmduration*10), 10, 0, 100))
eventDict['time'].append(SettingBezierDimm(At(startTime), BottomController, Setting3, 30, 0, int(dimmduration*10), 10, 0, 100))


# 45-46
# TODO: Distant Tension Fade In, then Fadout until 49

# 46-47.5
# 3 Fire Vibrato Pulses
startTime = beginning + 46
dimmduration = 0.2
eventDict['time'].append(LightSetChannel(At(startTime), TopController, [Light3,], Channel1))

# STATE SUMMARY
# 
# TOP                               | BOTTOM
#
# Light Channels                    | Light Channels
# --------------------------------- | ---------------------------------
#   Channel1: Setting1, [Strobe1, ] |   Channel1: Setting1, [Strobe1, ]
#   Channel2: Setting2, [Strobe2, ] |   Channel2: Setting2, [Strobe2, ]
#   Channel3: Setting3, []          |   Channel3: Setting3, []
#   Channel4: Setting4, []          |   Channel4: Setting4, []

eventDict['time'].append(SettingBezierBeforeFlash(At(startTime), TopController, Setting1, 0, 95, int(dimmduration*10), 10, 0, 100, 100))
# eventDict['time'].append(SettingBezierBeforeFlash(At(startTime), TopController, Setting3, 0, 95, int(dimmduration*10), 10, 0, 100, 100))

startTime = beginning + 46.5
eventDict['time'].append(SettingBezierBeforeFlash(At(startTime), TopController, Setting1, 20, 80, int(dimmduration*10), 10, 0, 100, 100))
# eventDict['time'].append(SettingBezierBeforeFlash(At(startTime), TopController, Setting3, 20, 80, int(dimmduration*10), 10, 0, 100, 100))

startTime = beginning + 47
eventDict['time'].append(SettingBezierBeforeFlash(At(startTime), TopController, Setting1, 10, 95, int(dimmduration*10), 10, 0, 100, 100))
# eventDict['time'].append(SettingBezierBeforeFlash(At(startTime), TopController, Setting3, 10, 95, int(dimmduration*10), 10, 0, 100, 100))

eventDict['time'].append(ChannelSetStatic(At(startTime), BottomController, ChannelStrobe1Darkstep, 1))
eventDict['time'].append(ChannelSetStatic(At(startTime), TopController, ChannelStrobe1Darkstep, 1)) 


# STATE SUMMARY
# 
# TOP                               | BOTTOM
#                                   |
# Static Channels                   | Static Channels
# --------------------------------- | ---------------------------------
#   ChannelStrobe1Steptime: 67      |   ChannelStrobe1Steptime: 67
#   ChannelStrobe1Darkstep: 1       |   ChannelStrobe1Darkstep: 1
#   ChannelStrobe2Steptime: 34      |   ChannelStrobe2Steptime: 34
#   ChannelStrobe2Darkstep: 1       |   ChannelStrobe2Darkstep: 1
#
#   ChannelVibratoSteptime: 17      |   ChannelVibratoSteptime: 17
#   ChannelPerlinSteptime:  5       |   ChannelPerlinSteptime:  5



# 48.5 - 50
startTime = beginning + 46
dimmduration = 2
# Setup Glitter Strobe
eventDict['time'].append(ChannelSetStatic(At(startTime), TopController, ChannelStrobe1Steptime, 67))
eventDict['time'].append(ChannelSetStatic(At(startTime), BottomController, ChannelStrobe1Steptime, 67))
eventDict['time'].append(SettingBezierDimm(At(startTime), BottomController, Setting1, 0, 95, int(dimmduration*10), 10, 0, 20))

startTime = beginning + 48.5
eventDict['time'].append(SettingBezierDimm(At(startTime), TopController, Setting1, 0, 95, int(dimmduration*10), 10, 0, 20))

#Delicate piano
fadeOutLength = 1.5
sustainSteptime = 5
eventDict['time'].append(ChannelSetChannel(At(startTime), TopController, ChannelSidechain, Channel4))
eventDict['time'].append(ChannelSetChannel(At(startTime), BottomController, ChannelSidechain, Channel4))

eventDict['time'].append(SettingImpulseToBezierFadeout(At(startTime), TopController, Setting4, 70, 1, 40, sustainSteptime, int(fadeOutLength*10), 10, 100, 100))
eventDict['time'].append(SettingImpulseToBezierFadeout(At(startTime), BottomController, Setting4, 70, 1, 40, sustainSteptime, int(fadeOutLength*10), 10, 100, 100))

#Delicate piano
startTime = beginning + 50.2
fadeOutLength = 1.5
sustainSteptime = 5
eventDict['time'].append(SettingImpulseToBezierFadeout(At(startTime), TopController, Setting4, 70, 1, 40, sustainSteptime, int(fadeOutLength*10), 10, 100, 100))
eventDict['time'].append(SettingImpulseToBezierFadeout(At(startTime), BottomController, Setting4, 70, 1, 40, sustainSteptime, int(fadeOutLength*10), 10, 100, 100))


#Delicate Piano
startTime = beginning + 50.9
fadeOutLength = 1.5
sustainSteptime = 5
eventDict['time'].append(SettingImpulseToBezierFadeout(At(startTime), TopController, Setting4, 70, 1, 40, sustainSteptime, int(fadeOutLength*10), 10, 100, 100))
eventDict['time'].append(SettingImpulseToBezierFadeout(At(startTime), BottomController, Setting4, 70, 1, 40, sustainSteptime, int(fadeOutLength*10), 10, 100, 100))

#Delicate Piano
startTime = beginning + 52.4
fadeOutLength = 1.5
sustainSteptime = 5
eventDict['time'].append(SettingImpulseToBezierFadeout(At(startTime), TopController, Setting4, 70, 1, 40, sustainSteptime, int(fadeOutLength*10), 10, 100, 100))
eventDict['time'].append(SettingImpulseToBezierFadeout(At(startTime), BottomController, Setting4, 70, 1, 40, sustainSteptime, int(fadeOutLength*10), 10, 100, 100))

#Delicate Piano
startTime = beginning + 54
fadeOutLength = 1.5
sustainSteptime = 5
eventDict['time'].append(SettingImpulseToBezierFadeout(At(startTime), TopController, Setting4, 70, 1, 40, sustainSteptime, int(fadeOutLength*10), 10, 100, 100))
eventDict['time'].append(SettingImpulseToBezierFadeout(At(startTime), BottomController, Setting4, 70, 1, 40, sustainSteptime, int(fadeOutLength*10), 10, 100, 100))

# 54.5 - Chord
startTime = beginning + 54.4
fadeOutLength = 1.5
sustainSteptime = 5
eventDict['time'].append(ChannelSetChannel(At(startTime), TopController, ChannelSidechain, Channel4))
eventDict['time'].append(ChannelSetChannel(At(startTime), BottomController, ChannelSidechain, Channel4))

eventDict['time'].append(SettingImpulseToBezierFadeout(At(startTime), TopController, Setting4, 95, 1, 40, sustainSteptime, int(fadeOutLength*10), 10, 100, 100))
eventDict['time'].append(SettingImpulseToBezierFadeout(At(startTime), BottomController, Setting4, 95, 1, 40, sustainSteptime, int(fadeOutLength*10), 10, 100, 100))

# 56.1 - 56.4
# Flut Fades in Lightly
startTime = beginning + 56.1
dimmduration = 0.3
eventDict['time'].append(ChannelSetChannel(At(startTime), TopController, ChannelSidechain, Channel2))
eventDict['time'].append(ChannelSetChannel(At(startTime), BottomController, ChannelSidechain, Channel2))
eventDict['time'].append(SettingBezierDimm(At(startTime), TopController, Setting2, 0, 40, int(dimmduration*10), 10, 0, 100))
eventDict['time'].append(SettingBezierDimm(At(startTime), BottomController, Setting2, 0, 40, int(dimmduration*10), 10, 0, 100))


# 56.2 - Small Chord
startTime = beginning + 56.2
fadeOutLength = 1
sustainSteptime = 5
eventDict['time'].append(ChannelSetChannel(At(startTime), TopController, ChannelSidechain, Channel4))
eventDict['time'].append(ChannelSetChannel(At(startTime), BottomController, ChannelSidechain, Channel4))
eventDict['time'].append(SettingImpulseToBezierFadeout(At(startTime), TopController, Setting4, 95, 1, 40, sustainSteptime, int(fadeOutLength*10), 10, 100, 100))
eventDict['time'].append(SettingImpulseToBezierFadeout(At(startTime), BottomController, Setting4, 95, 1, 40, sustainSteptime, int(fadeOutLength*10), 10, 100, 100))

# 57.5 - Small Key
startTime = beginning + 57.5
fadeOutLength = 0.5
sustainSteptime = 5
eventDict['time'].append(SettingImpulseToBezierFadeout(At(startTime), TopController, Setting4, 95, 1, 40, sustainSteptime, int(fadeOutLength*10), 10, 100, 100))
# 57.5 - 58
# Flut Amplifies
startTime = beginning + 57.5
dimmduration = 0.5
eventDict['time'].append(ChannelSetChannel(At(startTime), TopController, ChannelSidechain, Channel2))
eventDict['time'].append(ChannelSetChannel(At(startTime), BottomController, ChannelSidechain, Channel2))
eventDict['time'].append(SettingBezierDimm(At(startTime), TopController, Setting2, 40, 70, int(dimmduration*10), 10, 0, 100))
eventDict['time'].append(SettingBezierDimm(At(startTime), BottomController, Setting2, 40, 70, int(dimmduration*10), 10, 0, 100))


# 57.9 - Small Key
startTime = beginning + 57.9
fadeOutLength = 1
sustainSteptime = 5
eventDict['time'].append(ChannelSetChannel(At(startTime), TopController, ChannelSidechain, Channel4))
eventDict['time'].append(ChannelSetChannel(At(startTime), BottomController, ChannelSidechain, Channel4))
eventDict['time'].append(SettingImpulseToBezierFadeout(At(startTime), BottomController, Setting4, 75, 1, 40, sustainSteptime, int(fadeOutLength*10), 10, 100, 100))
eventDict['time'].append(SettingImpulseToBezierFadeout(At(startTime), BottomController, Setting4, 75, 1, 40, sustainSteptime, int(fadeOutLength*10), 10, 100, 100))


# 58 - 58.7
# Flut Deamplifies
startTime = beginning + 58
dimmduration = 0.7
eventDict['time'].append(ChannelSetChannel(At(startTime), TopController, ChannelSidechain, Channel2))
eventDict['time'].append(ChannelSetChannel(At(startTime), BottomController, ChannelSidechain, Channel2))
eventDict['time'].append(SettingBezierDimm(At(startTime), TopController, Setting2, 70, 30, int(dimmduration*10), 10, 0, 100))
eventDict['time'].append(SettingBezierDimm(At(startTime), BottomController, Setting2, 70, 30, int(dimmduration*10), 10, 0, 100))

# 59.55 - Strong Flut
startTime = beginning + 59.55
dimmduration = 0.9
eventDict['time'].append(SettingBezierDimm(At(startTime), TopController, Setting2, 30, 95, int(dimmduration*10), 10, 0, 100))
eventDict['time'].append(SettingBezierDimm(At(startTime), BottomController, Setting2, 30, 95, int(dimmduration*10), 10, 0, 100))
startTime = beginning + 61.35
dimmduration = 0.9
eventDict['time'].append(SettingBezierDimm(At(startTime), TopController, Setting2, 95, 0, int(dimmduration*10), 10, 0, 100))
eventDict['time'].append(SettingBezierDimm(At(startTime), BottomController, Setting2, 95, 0, int(dimmduration*10), 10, 0, 100))

# 65.5 - Small Key
startTime = beginning + 65.5
fadeOutLength = 1
sustainSteptime = 5
eventDict['time'].append(ChannelSetChannel(At(startTime), TopController, ChannelSidechain, Channel4))
eventDict['time'].append(ChannelSetChannel(At(startTime), BottomController, ChannelSidechain, Channel4))
eventDict['time'].append(SettingImpulseToBezierFadeout(At(startTime), TopController, Setting4, 75, 1, 40, sustainSteptime, int(fadeOutLength*10), 10, 100, 100))
eventDict['time'].append(SettingImpulseToBezierFadeout(At(startTime), BottomController, Setting4, 75, 1, 40, sustainSteptime, int(fadeOutLength*10), 10, 100, 100))


# 66 - Small Key
startTime = beginning + 66
fadeOutLength = 1
sustainSteptime = 5
eventDict['time'].append(SettingImpulseToBezierFadeout(At(startTime), TopController, Setting4, 75, 1, 40, sustainSteptime, int(fadeOutLength*10), 10, 100, 100))
eventDict['time'].append(SettingImpulseToBezierFadeout(At(startTime), BottomController, Setting4, 75, 1, 40, sustainSteptime, int(fadeOutLength*10), 10, 100, 100))


# 66.4 - Small Key
startTime = beginning + 66.4
fadeOutLength = 1
sustainSteptime = 5
eventDict['time'].append(SettingImpulseToBezierFadeout(At(startTime), TopController, Setting4, 75, 1, 40, sustainSteptime, int(fadeOutLength*10), 10, 100, 100))
eventDict['time'].append(SettingImpulseToBezierFadeout(At(startTime), BottomController, Setting4, 75, 1, 40, sustainSteptime, int(fadeOutLength*10), 10, 100, 100))

# 66.9 - Small Key
startTime = beginning + 66.9
fadeOutLength = 1
sustainSteptime = 5
eventDict['time'].append(SettingImpulseToBezierFadeout(At(startTime), TopController, Setting4, 75, 1, 40, sustainSteptime, int(fadeOutLength*10), 10, 100, 100))
eventDict['time'].append(SettingImpulseToBezierFadeout(At(startTime), BottomController, Setting4, 75, 1, 40, sustainSteptime, int(fadeOutLength*10), 10, 100, 100))

# 68 - Small Key
startTime = beginning + 68
fadeOutLength = 1
sustainSteptime = 5
eventDict['time'].append(SettingImpulseToBezierFadeout(At(startTime), TopController, Setting4, 75, 1, 40, sustainSteptime, int(fadeOutLength*10), 10, 100, 100))
eventDict['time'].append(SettingImpulseToBezierFadeout(At(startTime), BottomController, Setting4, 75, 1, 40, sustainSteptime, int(fadeOutLength*10), 10, 100, 100))


# 69.4 - One Ebbe Chord (also little pianos)
startTime = beginning + 69.4
fadeOutLength = 1.5
sustainSteptime = 5
eventDict['time'].append(SettingImpulseToBezierFadeout(At(startTime), TopController, Setting4, 95, 1, 40, sustainSteptime, int(fadeOutLength*10), 10, 100, 100))
eventDict['time'].append(SettingImpulseToBezierFadeout(At(startTime), BottomController, Setting4, 95, 1, 40, sustainSteptime, int(fadeOutLength*10), 10, 100, 100))

# 71 - One Ebbe Chord (also little pianos)
startTime = beginning + 71
fadeOutLength = 1
sustainSteptime = 5
eventDict['time'].append(SettingImpulseToBezierFadeout(At(startTime), TopController, Setting4, 95, 1, 40, sustainSteptime, int(fadeOutLength*10), 10, 100, 100))
eventDict['time'].append(SettingImpulseToBezierFadeout(At(startTime), BottomController, Setting4, 95, 1, 40, sustainSteptime, int(fadeOutLength*10), 10, 100, 100))

# 73.5 - Strong Flut
# Flut Amplifies
startTime = beginning + 73.5
dimmduration = 1
eventDict['time'].append(ChannelSetChannel(At(startTime), TopController, ChannelSidechain, Channel2))
eventDict['time'].append(ChannelSetChannel(At(startTime), BottomController, ChannelSidechain, Channel2))
eventDict['time'].append(SettingBezierDimm(At(startTime), TopController, Setting2, 0, 30, int(dimmduration*10), 10, 0, 100))
eventDict['time'].append(SettingBezierDimm(At(startTime), BottomController, Setting2, 0, 30, int(dimmduration*10), 10, 0, 100))
# 74.5 - Strong Flut
startTime = beginning + 74.5
dimmduration = 0.5
eventDict['time'].append(SettingBezierDimm(At(startTime), TopController, Setting2, 30, 95, int(dimmduration*10), 10, 0, 100))
eventDict['time'].append(SettingBezierDimm(At(startTime), BottomController, Setting2, 30, 95, int(dimmduration*10), 10, 0, 100))
startTime = beginning + 76.5
dimmduration = 0.9
eventDict['time'].append(SettingBezierDimm(At(startTime), TopController, Setting2, 95, 0, int(dimmduration*10), 10, 0, 100))
eventDict['time'].append(SettingBezierDimm(At(startTime), BottomController, Setting2, 95, 0, int(dimmduration*10), 10, 0, 100))


# 79 - Small Key
startTime = beginning + 79
eventDict['time'].append(ChannelSetChannel(At(startTime), TopController, ChannelSidechain, Channel4))
eventDict['time'].append(ChannelSetChannel(At(startTime), BottomController, ChannelSidechain, Channel4))
fadeOutLength = 0.6
sustainSteptime = 5
eventDict['time'].append(SettingImpulseToBezierFadeout(At(startTime), TopController, Setting4, 75, 1, 40, sustainSteptime, int(fadeOutLength*10), 10, 100, 100))
eventDict['time'].append(SettingImpulseToBezierFadeout(At(startTime), BottomController, Setting4, 75, 1, 40, sustainSteptime, int(fadeOutLength*10), 10, 100, 100))


# 80 - Small Key
startTime = beginning + 80
fadeOutLength = 0.5
sustainSteptime = 5
eventDict['time'].append(SettingImpulseToBezierFadeout(At(startTime), TopController, Setting4, 75, 1, 40, sustainSteptime, int(fadeOutLength*10), 10, 100, 100))
eventDict['time'].append(SettingImpulseToBezierFadeout(At(startTime), BottomController, Setting4, 75, 1, 40, sustainSteptime, int(fadeOutLength*10), 10, 100, 100))

# 80.4 - Small Key
startTime = beginning + 80.4
fadeOutLength = 0.5
sustainSteptime = 5
eventDict['time'].append(SettingImpulseToBezierFadeout(At(startTime), TopController, Setting4, 75, 1, 40, sustainSteptime, int(fadeOutLength*10), 10, 100, 100))
eventDict['time'].append(SettingImpulseToBezierFadeout(At(startTime), BottomController, Setting4, 75, 1, 40, sustainSteptime, int(fadeOutLength*10), 10, 100, 100))

# 80.9 - Chord
startTime = beginning + 80.9
fadeOutLength = 0.5
sustainSteptime = 5
eventDict['time'].append(SettingImpulseToBezierFadeout(At(startTime), TopController, Setting4, 95, 1, 40, sustainSteptime, int(fadeOutLength*10), 10, 100, 100))
eventDict['time'].append(SettingImpulseToBezierFadeout(At(startTime), BottomController, Setting4, 95, 1, 40, sustainSteptime, int(fadeOutLength*10), 10, 100, 100))

# 81.6 - Small Key
startTime = beginning + 81.6
fadeOutLength = 0.5
sustainSteptime = 5
eventDict['time'].append(SettingImpulseToBezierFadeout(At(startTime), TopController, Setting4, 75, 1, 40, sustainSteptime, int(fadeOutLength*10), 10, 100, 100))
eventDict['time'].append(SettingImpulseToBezierFadeout(At(startTime), BottomController, Setting4, 75, 1, 40, sustainSteptime, int(fadeOutLength*10), 10, 100, 100))

# 82.2 - Small Key
startTime = beginning + 82.2
fadeOutLength = 0.5
sustainSteptime = 5
eventDict['time'].append(SettingImpulseToBezierFadeout(At(startTime), TopController, Setting4, 75, 1, 40, sustainSteptime, int(fadeOutLength*10), 10, 100, 100))
eventDict['time'].append(SettingImpulseToBezierFadeout(At(startTime), BottomController, Setting4, 75, 1, 40, sustainSteptime, int(fadeOutLength*10), 10, 100, 100))


# 83 - Chord
startTime = beginning + 83
fadeOutLength = 0.5
sustainSteptime = 5
eventDict['time'].append(SettingImpulseToBezierFadeout(At(startTime), TopController, Setting4, 85, 1, 40, sustainSteptime, int(fadeOutLength*10), 10, 100, 100))
eventDict['time'].append(SettingImpulseToBezierFadeout(At(startTime), BottomController, Setting4, 85, 1, 40, sustainSteptime, int(fadeOutLength*10), 10, 100, 100))

# 84 - Chord
startTime = beginning + 84
fadeOutLength = 1
sustainSteptime = 5
eventDict['time'].append(SettingImpulseToBezierFadeout(At(startTime), TopController, Setting4, 95, 1, 40, sustainSteptime, int(fadeOutLength*10), 10, 100, 100))
eventDict['time'].append(SettingImpulseToBezierFadeout(At(startTime), BottomController, Setting4, 95, 1, 40, sustainSteptime, int(fadeOutLength*10), 10, 100, 100))

# 86.6 - Small Key
startTime = beginning + 87
fadeOutLength = 0.5
sustainSteptime = 5
eventDict['time'].append(SettingImpulseToBezierFadeout(At(startTime), TopController, Setting4, 75, 1, 40, sustainSteptime, int(fadeOutLength*10), 10, 100, 100))
eventDict['time'].append(SettingImpulseToBezierFadeout(At(startTime), BottomController, Setting4, 75, 1, 40, sustainSteptime, int(fadeOutLength*10), 10, 100, 100))


# 79.5-82.5
# Strobe Fade Out
startTime = beginning + 79.5
dimmduration = 3
eventDict['time'].append(SettingBezierDimm(At(startTime), TopController, Setting1, 95, 0, int(dimmduration*10), 10, 0, 100))
eventDict['time'].append(SettingBezierDimm(At(startTime), BottomController, Setting1, 95, 0, int(dimmduration*10), 10, 0, 100))
eventDict['time'].append(SettingBezierDimm(At(startTime), BottomController, Setting3, 95, 0, int(dimmduration*10), 10, 0, 100))

# 81-87.9
# Tinitus
startTime = beginning + 78
dimmduration = 10
eventDict['time'].append(LightSetChannel(At(startTime), TopController, [Light3], Channel3))
# STATE SUMMARY
# 
# TOP                               | BOTTOM
#
# Light Channels                    | Light Channels
# --------------------------------- | ---------------------------------
#   Channel1: Setting1, [Strobe1, ] |   Channel1: Setting1, [Strobe1, ]
#   Channel2: Setting2, [Strobe2, ] |   Channel2: Setting2, [Strobe2, ]
#   Channel3: Setting3, []          |   Channel3: Setting3, []
#   Channel4: Setting4, []          |   Channel4: Setting4, []
eventDict['time'].append(SettingBezierDimm(At(startTime), TopController, Setting3, 0, 95, int(dimmduration*10), 10, 0, 100))


# 82.5
# Remove Effects
startTime = beginning + 82.5
eventDict['time'].append(ChannelRemoveEffects(At(startTime), BottomController, Channel1))
eventDict['time'].append(ChannelRemoveEffects(At(startTime), TopController, Channel1))
eventDict['time'].append(ChannelRemoveEffect(At(startTime), TopController, Channel2, 0))

# STATE SUMMARY
# 
# TOP                               | BOTTOM
#
# Light Channels                    | Light Channels
# --------------------------------- | ---------------------------------
#   Channel1: Setting1, []          |   Channel1: Setting1, []
#   Channel2: Setting2, []          |   Channel2: Setting2, [Strobe2, ]
#   Channel3: Setting3, []          |   Channel3: Setting3, []
#   Channel4: Setting4, []          |   Channel4: Setting4, []



# 88
# PART III

# Setup
# beginning refers to the beginning behind so that when the back moves, the front moves accordingly
# the 0 will be changed as soon as more parts are added
originalBeginning = beginning
beginning = beginning + 88

startTime = beginning
dimmduration = 0.1
eventDict['time'].append(SettingBezierDimm(At(startTime), TopController, Setting3, 95, 0, int(dimmduration*10), 10, 0, 100))

eventDict['time'].append(ChannelSetStatic(At(startTime), TopController, ChannelStrobe1Steptime, 34))
eventDict['time'].append(ChannelSetStatic(At(startTime), BottomController, ChannelStrobe1Steptime, 34))

# Bottom
eventDict['time'].append(ChannelSetStatic(At(startTime), BottomController, ChannelStrobe1Darkstep, 0))
eventDict['time'].append(ChannelAddEffect(At(startTime), BottomController, Channel1, EffectStrobe1, 0))
eventDict['time'].append(ChannelAddEffect(At(startTime), BottomController, Channel3, EffectStrobe1, 0))
eventDict['time'].append(LightSetChannel(At(startTime), BottomController, [Light3,], Channel3))


# Top
eventDict['time'].append(ChannelAddEffect(At(startTime), TopController, Channel4, EffectSubtractPercentageVibrato, 0))
# We need a strobe only on 3 (aka 7 as global)
eventDict['time'].append(EffectSequencedLightStrobe(At(startTime), TopController, EffectStrobe1, ChannelStrobe1Steptime, ChannelStrobe1Darkstep, 5757))


# STATE SUMMARY
# 
# TOP                               | BOTTOM
#                                   |
# Settings                          | Settings
# --------------------------------- | ---------------------------------
#   Setting1:            0          |   Setting1:            0
#   Setting2:            0          |   Setting2:            0
#   Setting3:            0          |   Setting3:            0
#   Setting4:            0          |   Setting4:            0
#
#   SettingVibrato:     0 to 100    |   SettingVibrato:     0 to 100
#   SettingPerlin:      0 to 100    |   SettingPerlin:      0 to 100
#
# Static Channels                   | Static Channels
# --------------------------------- | ---------------------------------
#   ChannelStrobe1Steptime: 34      |   ChannelStrobe1Steptime: 34
#   ChannelStrobe1Darkstep: 1       |   ChannelStrobe1Darkstep: 0
#   ChannelStrobe2Steptime: 34      |   ChannelStrobe2Steptime: 34
#   ChannelStrobe2Darkstep: 1       |   ChannelStrobe2Darkstep: 1
#
#   ChannelVibratoSteptime: 17      |   ChannelVibratoSteptime: 17
#   ChannelPerlinSteptime:  5       |   ChannelPerlinSteptime:  5
#
# Effects                           | Effects
# --------------------------------- | ---------------------------------
#   EffectStrobe1:        5757      |   EffectStrobe1:        1537
#   EffectStrobe2:        2626      |   EffectStrobe2:        2626
#
# Light Channels                    | Light Channels
# --------------------------------- | ---------------------------------
#   Channel1: Setting1, []          |   Channel1: Setting1, [Strobe1,]
#   Channel2: Setting2, []          |   Channel2: Setting2, [Strobe2, ]
#   Channel3: Setting3, []          |   Channel3: Setting3, [Strobe1,]
#   Channel4: Setting4, [Vibrato]   |   Channel4: Setting4, []


# 0-0.25
# Bottom Left In
startTime = beginning + 0
dimmduration = 0.25
eventDict['time'].append(SettingBezierDimm(At(startTime), BottomController, Setting1, 0, 100, int(dimmduration*20), 5, 0, 100))

# 0.25
# Right Joins
startTime = beginning + 0.25
dimmduration = 0
eventDict['time'].append(SettingBezierDimm(At(startTime), BottomController, Setting3, 0, 100, int(dimmduration*20), 5, 0, 100))

# 1.06 - 2.16
# Fade Down
startTime = beginning + 1.06
dimmduration = 1.1
eventDict['time'].append(SettingBezierDimm(At(startTime), BottomController, Setting3, 100, 10, int(dimmduration*20), 5, 0, 100))
eventDict['time'].append(SettingBezierDimm(At(startTime), BottomController, Setting3, 100, 10, int(dimmduration*20), 5, 0, 100))

# 2.43 - 3.97
# Right Fades In
startTime = beginning + 2.43
dimmduration = 1.55
eventDict['time'].append(SettingBezierDimm(At(startTime), BottomController, Setting3, 10, 100, int(dimmduration*20), 5, 0, 100))

# 4.06 - 5.85
# Both Fade Down
startTime = beginning + 4.05
dimmduration = 1.8
eventDict['time'].append(SettingBezierDimm(At(startTime), BottomController, Setting3, 100, 0, int(dimmduration*20), 5, 0, 100))

# 5.2
# Background Vibrato Appears Lightly
startTime = beginning + 5.2
dimmduration = 0.5
eventDict['time'].append(SettingBezierDimm(At(startTime), TopController, Setting4, 0, 80, int(dimmduration*20), 5, 0, 100))

# 6.32 - 7.6
# Right Fades In
startTime = beginning + 6.3
dimmduration = 1.3
eventDict['time'].append(SettingBezierDimm(At(startTime), BottomController, Setting3, 0, 100, int(dimmduration*20), 5, 0, 100))

# 7.76
# Right Off
startTime = beginning + 7.76
dimmduration = 0
eventDict['time'].append(SettingBezierDimm(At(startTime), BottomController, Setting3, 100, 0, int(dimmduration*20), 5, 0, 100))

# 8.58 - 9.4
# Left Fades In
startTime = beginning + 8.6
dimmduration = 0.8
eventDict['time'].append(SettingBezierDimm(At(startTime), BottomController, Setting1, 0, 100, int(dimmduration*20), 5, 0, 100))

# 9.51 - 9.7
# Right Joins Lightly
startTime = beginning + 9.50
dimmduration = 0.2
eventDict['time'].append(SettingBezierDimm(At(startTime), BottomController, Setting3, 0, 60, int(dimmduration*20), 5, 0, 100))
# 9.51 - 12.3
# Top Fades Out
startTime = beginning + 9.50
dimmduration = 2.8
eventDict['time'].append(SettingBezierDimm(At(startTime), TopController, Setting4, 80, 0, int(dimmduration*10), 10, 0, 100))

# 11.7 - 12.6
# Right full blast
# Left down
startTime = beginning + 11.70
dimmduration = 0.9
eventDict['time'].append(SettingBezierDimm(At(startTime), BottomController, Setting1, 100, 40, int(dimmduration*20), 5, 0, 100))
eventDict['time'].append(SettingBezierDimm(At(startTime), BottomController, Setting3, 60, 100, int(dimmduration*20), 5, 0, 100))

# 12.6 - 12.9
# Both Down
startTime = beginning + 12.60
dimmduration = 0.3
eventDict['time'].append(SettingBezierDimm(At(startTime), BottomController, Setting1, 40, 0, int(dimmduration*20), 5, 0, 100))
eventDict['time'].append(SettingBezierDimm(At(startTime), BottomController, Setting3, 100, 0, int(dimmduration*20), 5, 0, 100))

# 12.9 - 13.18
# Right Up
startTime = beginning + 12.9
dimmduration = 0.25
eventDict['time'].append(SettingBezierDimm(At(startTime), BottomController, Setting3, 0, 100, int(dimmduration*20), 5, 0, 100))

# 13.18 - 13.68
# Right Down
startTime = beginning + 13.18
dimmduration = 0.5
eventDict['time'].append(SettingBezierDimm(At(startTime), BottomController, Setting3, 100, 0, int(dimmduration*20), 5, 0, 100))

# 13.3
# Light Quicker Top Pulse
startTime = beginning + 13.3
eventDict['time'].append(ChannelSetStatic(At(startTime), TopController, ChannelVibratoSteptime, 9))

# STATE SUMMARY
# 
# TOP                               | BOTTOM
#                                   |
# Static Channels                   | Static Channels
# --------------------------------- | ---------------------------------
#
#   ChannelVibratoSteptime: 9       |   ChannelVibratoSteptime: 17
#   ChannelPerlinSteptime:  5       |   ChannelPerlinSteptime:  5
#


eventDict['time'].append(SettingStatic(At(startTime), TopController, Setting4, 30))


# 14.07 - 14.87
# Left Wave
startTime = beginning + 14.07
dimmduration = 0.4
eventDict['time'].append(SettingBezierDimm(At(startTime), BottomController, Setting1, 0, 100, int(dimmduration*20), 5, 0, 100))
startTime = startTime + dimmduration
dimmduration = 0.4
eventDict['time'].append(SettingBezierDimm(At(startTime), BottomController, Setting1, 100, 0, int(dimmduration*20), 5, 0, 100))


# 14.85 - 16.00
# Right Wave
startTime = beginning + 14.85
dimmduration = 0.55
eventDict['time'].append(SettingBezierDimm(At(startTime), BottomController, Setting3, 0, 100, int(dimmduration*20), 5, 0, 100))
startTime = startTime + dimmduration
dimmduration = 0.60
eventDict['time'].append(SettingBezierDimm(At(startTime), BottomController, Setting3, 100, 0, int(dimmduration*20), 5, 0, 100))

# 15.6
# Top Vibrato gets slower again
# startTime = beginning + 15.6
# eventDict['time'].append(ChannelSetStatic(At(startTime), TopController, ChannelVibratoSteptime, 17))
 

# 16 - 16.75
# Small Left Wave
startTime = beginning + 16
dimmduration = 0.35
eventDict['time'].append(SettingBezierDimm(At(startTime), BottomController, Setting1, 0, 70, int(dimmduration*20), 5, 0, 100))
startTime = startTime + dimmduration
dimmduration = 0.40
eventDict['time'].append(SettingBezierDimm(At(startTime), BottomController, Setting1, 70, 0, int(dimmduration*20), 5, 0, 100))

# 17.45 - 18.00
# Both Fade in Lightly
startTime = beginning + 17.45
dimmduration = 0.55
eventDict['time'].append(SettingBezierDimm(At(startTime), BottomController, Setting1, 0, 70, int(dimmduration*20), 5, 0, 100))
eventDict['time'].append(SettingBezierDimm(At(startTime), BottomController, Setting3, 0, 70, int(dimmduration*20), 5, 0, 100))

# 18.50 - 18.9
# Darkstep On and go to fully
startTime = beginning + 18.5
dimmduration = 0.40
eventDict['time'].append(ChannelSetStatic(At(startTime), BottomController, ChannelStrobe1Darkstep, 1))


# STATE SUMMARY
# 
# TOP                               | BOTTOM
#                                   |
#
# Static Channels                   | Static Channels
# --------------------------------- | ---------------------------------
#   ChannelStrobe1Steptime: 34      |   ChannelStrobe1Steptime: 34
#   ChannelStrobe1Darkstep: 1       |   ChannelStrobe1Darkstep: 1


eventDict['time'].append(SettingBezierDimm(At(startTime), BottomController, Setting1, 70, 100, int(dimmduration*20), 5, 0, 100))
eventDict['time'].append(SettingBezierDimm(At(startTime), BottomController, Setting3, 70, 100, int(dimmduration*20), 5, 0, 100))

# 19.84 - 20.90
# Fade Down
startTime = beginning + 19.85
dimmduration = 1.05
eventDict['time'].append(SettingBezierDimm(At(startTime), BottomController, Setting1, 100, 0, int(dimmduration*20), 5, 0, 100))
eventDict['time'].append(SettingBezierDimm(At(startTime), BottomController, Setting3, 100, 0, int(dimmduration*20), 5, 0, 100))

# 20.9 - 22.5
# Right Wave
startTime = beginning + 21
dimmduration = 0.75
eventDict['time'].append(ChannelSetStatic(At(startTime), BottomController, ChannelStrobe1Darkstep, 0))

# STATE SUMMARY
# 
# TOP                               | BOTTOM
#
# Static Channels                   | Static Channels
# --------------------------------- | ---------------------------------
#   ChannelStrobe1Steptime: 34      |   ChannelStrobe1Steptime: 34
#   ChannelStrobe1Darkstep: 1       |   ChannelStrobe1Darkstep: 0


eventDict['time'].append(SettingBezierDimm(At(startTime), BottomController, Setting3, 0, 100, int(dimmduration*20), 5, 0, 100))
startTime = startTime + dimmduration
dimmduration = 0.75
eventDict['time'].append(SettingBezierDimm(At(startTime), BottomController, Setting3, 100, 0, int(dimmduration*20), 5, 0, 100))

# 22
# Top Vibrato Faster Again
startTime = beginning + 22
eventDict['time'].append(ChannelSetStatic(At(startTime), TopController, ChannelVibratoSteptime, 9))

# STATE SUMMARY
# 
# TOP                               | BOTTOM
#                                   |
# Static Channels                   | Static Channels
# --------------------------------- | ---------------------------------
#
#   ChannelVibratoSteptime: 9       |   ChannelVibratoSteptime: 17
#   ChannelPerlinSteptime:  5       |   ChannelPerlinSteptime:  5


# 23.1 - 24
# Small Right Wave
startTime = beginning + 23
dimmduration = 0.5
eventDict['time'].append(SettingBezierDimm(At(startTime), BottomController, Setting3, 0, 70, int(dimmduration*20), 5, 0, 100))
startTime = startTime + dimmduration
dimmduration = 0.5
eventDict['time'].append(SettingBezierDimm(At(startTime), BottomController, Setting3, 70, 0, int(dimmduration*20), 5, 0, 100))

# 24.5 - 25.3
# Small Right Wave
startTime = beginning + 24.3
dimmduration = 0.5
eventDict['time'].append(SettingBezierDimm(At(startTime), BottomController, Setting3, 0, 70, int(dimmduration*20), 5, 0, 100))
startTime = startTime + dimmduration
dimmduration = 0.5
eventDict['time'].append(SettingBezierDimm(At(startTime), BottomController, Setting3, 70, 0, int(dimmduration*20), 5, 0, 100))

# 25.3 - 26.3
# Small Left Wave
startTime = beginning + 25.3
dimmduration = 0.5
eventDict['time'].append(SettingBezierDimm(At(startTime), BottomController, Setting1, 0, 70, int(dimmduration*20), 5, 0, 100))
startTime = startTime + dimmduration
dimmduration = 0.5
eventDict['time'].append(SettingBezierDimm(At(startTime), BottomController, Setting1, 70, 0, int(dimmduration*20), 5, 0, 100))

# 26.45 - 27
# Tiny Left Wave
startTime = beginning + 26.45
dimmduration = 0.25
eventDict['time'].append(SettingBezierDimm(At(startTime), BottomController, Setting1, 0, 50, int(dimmduration*20), 5, 0, 100))
startTime = startTime + dimmduration
dimmduration = 0.30
eventDict['time'].append(SettingBezierDimm(At(startTime), BottomController, Setting1, 50, 0, int(dimmduration*20), 5, 0, 100))

# 27.8 - 28.9
# Both Fade in Lightly
startTime = beginning + 27.8
dimmduration = 1
eventDict['time'].append(SettingBezierDimm(At(startTime), BottomController, Setting1, 0, 70, int(dimmduration*20), 5, 0, 100))
eventDict['time'].append(SettingBezierDimm(At(startTime), BottomController, Setting3, 0, 70, int(dimmduration*20), 5, 0, 100))

# 28..9 - 29.3
# Darkstep On and go to fully
startTime = beginning + 28.9
dimmduration = 0.4
eventDict['time'].append(ChannelSetStatic(At(startTime), BottomController, ChannelStrobe1Darkstep, 1))

# STATE SUMMARY
# 
# TOP                               | BOTTOM
#
# Static Channels                   | Static Channels
# --------------------------------- | ---------------------------------
#   ChannelStrobe1Steptime: 34      |   ChannelStrobe1Steptime: 34
#   ChannelStrobe1Darkstep: 1       |   ChannelStrobe1Darkstep: 1

eventDict['time'].append(SettingBezierDimm(At(startTime), BottomController, Setting1, 70, 100, int(dimmduration*20), 5, 0, 100))
eventDict['time'].append(SettingBezierDimm(At(startTime), BottomController, Setting3, 70, 100, int(dimmduration*20), 5, 0, 100))

# 29.3
# Darkstep Off
startTime = beginning + 29.3
eventDict['time'].append(ChannelSetStatic(At(startTime), BottomController, ChannelStrobe1Darkstep, 0))


# STATE SUMMARY
# 
# TOP                               | BOTTOM
#
# Static Channels                   | Static Channels
# --------------------------------- | ---------------------------------
#   ChannelStrobe1Steptime: 34      |   ChannelStrobe1Steptime: 34
#   ChannelStrobe1Darkstep: 1       |   ChannelStrobe1Darkstep: 0

# 30.9 - 31.5
# Fade Down
startTime = beginning + 30.9
dimmduration = 0.6
eventDict['time'].append(SettingBezierDimm(At(startTime), BottomController, Setting1, 100, 0, int(dimmduration*20), 5, 0, 100))
eventDict['time'].append(SettingBezierDimm(At(startTime), BottomController, Setting3, 100, 0, int(dimmduration*20), 5, 0, 100))

# 31.8 - 32.8
# Right Wave
startTime = beginning + 31.8
dimmduration = 0.5
eventDict['time'].append(SettingBezierDimm(At(startTime), BottomController, Setting3, 0, 100, int(dimmduration*20), 5, 0, 100))
startTime = startTime + dimmduration
dimmduration = 0.5
eventDict['time'].append(SettingBezierDimm(At(startTime), BottomController, Setting3, 100, 0, int(dimmduration*20), 5, 0, 100))

# 33.4 - 33.9
# Top Small Strobe Wave
startTime = beginning + 33
# Replace Vibrato with strobe
# eventDict['time'].append(ChannelAddEffect(At(0), TopController, Channel3, EffectStrobe1, 0))
startTime = beginning + 33.4
dimmduration = 0.25
eventDict['time'].append(SettingBezierDimm(At(startTime), BottomController, Setting3, 0, 90, int(dimmduration*20), 5, 0, 100))
startTime = startTime + dimmduration
dimmduration = 0.25
eventDict['time'].append(SettingBezierDimm(At(startTime), BottomController, Setting3, 90, 0, int(dimmduration*20), 5, 0, 100))


# 34.3 - 35.3
# Wave that stays high
startTime = beginning + 34.3
dimmduration = 0.5
eventDict['time'].append(SettingBezierDimm(At(startTime), BottomController, Setting1, 0, 100, int(dimmduration*20), 5, 0, 100))
startTime = startTime + dimmduration
dimmduration = 0.5
eventDict['time'].append(SettingBezierDimm(At(startTime), BottomController, Setting1, 100, 50, int(dimmduration*20), 5, 0, 100))

# 35.3 - 36.90
# Another Small Wave, Long Fadeout
startTime = beginning + 35.3
dimmduration = 0.6
eventDict['time'].append(SettingBezierDimm(At(startTime), BottomController, Setting1, 50, 90, int(dimmduration*20), 5, 0, 100))
startTime = startTime + dimmduration
dimmduration = 1.3
eventDict['time'].append(SettingBezierDimm(At(startTime), BottomController, Setting1, 90, 0, int(dimmduration*10), 10, 0, 100))

# 37.2-38.1
# Darstep On Wave
startTime = beginning + 37.2
dimmduration = 0.45
eventDict['time'].append(ChannelSetStatic(At(startTime), BottomController, ChannelStrobe1Darkstep, 0))


# STATE SUMMARY
# 
# TOP                               | BOTTOM
#
# Static Channels                   | Static Channels
# --------------------------------- | ---------------------------------
#   ChannelStrobe1Steptime: 34      |   ChannelStrobe1Steptime: 34
#   ChannelStrobe1Darkstep: 1       |   ChannelStrobe1Darkstep: 0

eventDict['time'].append(SettingBezierDimm(At(startTime), BottomController, Setting1, 0, 100, int(dimmduration*20), 5, 0, 100))
eventDict['time'].append(SettingBezierDimm(At(startTime), BottomController, Setting3, 0, 100, int(dimmduration*20), 5, 0, 100))
startTime = startTime + dimmduration
dimmduration = 0.45
eventDict['time'].append(SettingBezierDimm(At(startTime), BottomController, Setting1, 100, 0, int(dimmduration*20), 5, 0, 100))
eventDict['time'].append(SettingBezierDimm(At(startTime), BottomController, Setting3, 100, 0, int(dimmduration*20), 5, 0, 100))

# 38.4 - 40.5
# Top Strobe Wave
startTime = beginning + 38.4
dimmduration = 0.7
eventDict['time'].append(SettingBezierDimm(At(startTime), BottomController, Setting1, 0, 95, int(dimmduration*20), 5, 0, 100))
startTime = startTime + dimmduration
dimmduration = 1.4
eventDict['time'].append(SettingBezierDimm(At(startTime), BottomController, Setting1, 95, 0, int(dimmduration*20), 5, 0, 100))

# 40.7 - 42
# Right Wave
startTime = beginning + 40
eventDict['time'].append(ChannelSetStatic(At(startTime), BottomController, ChannelStrobe1Darkstep, 0))


# STATE SUMMARY
# 
# TOP                               | BOTTOM
#
# Static Channels                   | Static Channels
# --------------------------------- | ---------------------------------
#   ChannelStrobe1Steptime: 34      |   ChannelStrobe1Steptime: 34
#   ChannelStrobe1Darkstep: 1       |   ChannelStrobe1Darkstep: 0


startTime = beginning + 40.7
dimmduration = 0.6
eventDict['time'].append(SettingBezierDimm(At(startTime), BottomController, Setting3, 0, 100, int(dimmduration*20), 5, 0, 100))
startTime = startTime + dimmduration
dimmduration = 0.7
eventDict['time'].append(SettingBezierDimm(At(startTime), BottomController, Setting3, 100, 0, int(dimmduration*20), 5, 0, 100))

# 41.3 - 42.6
# Top Strobe Wave
startTime = beginning + 41.3
dimmduration = 0.5
eventDict['time'].append(SettingBezierDimm(At(startTime), BottomController, Setting1, 0, 95, int(dimmduration*20), 5, 0, 100))
startTime = startTime + dimmduration
dimmduration = 0.8
eventDict['time'].append(SettingBezierDimm(At(startTime), BottomController, Setting1, 95, 0, int(dimmduration*20), 5, 0, 100))

# 44.8 - 46.2
# Top Wave and Bottom Darkstep Wave
startTime = beginning + 44
eventDict['time'].append(ChannelSetStatic(At(startTime), BottomController, ChannelStrobe1Darkstep, 1))


# STATE SUMMARY
# 
# TOP                               | BOTTOM
#
# Static Channels                   | Static Channels
# --------------------------------- | ---------------------------------
#   ChannelStrobe1Steptime: 34      |   ChannelStrobe1Steptime: 34
#   ChannelStrobe1Darkstep: 1       |   ChannelStrobe1Darkstep: 1


startTime = beginning + 44.8
dimmduration = 0.7
eventDict['time'].append(SettingBezierDimm(At(startTime), BottomController, Setting1, 0, 100, int(dimmduration*20), 5, 0, 100))
eventDict['time'].append(SettingBezierDimm(At(startTime), BottomController, Setting3, 0, 100, int(dimmduration*20), 5, 0, 100))
eventDict['time'].append(SettingBezierDimm(At(startTime), TopController, Setting4, 0, 100, int(dimmduration*20), 5, 0, 100))
startTime = startTime + dimmduration
dimmduration = 0.7
eventDict['time'].append(SettingBezierDimm(At(startTime), BottomController, Setting1, 100, 0, int(dimmduration*20), 5, 0, 100))
eventDict['time'].append(SettingBezierDimm(At(startTime), BottomController, Setting3, 100, 0, int(dimmduration*20), 5, 0, 100))
# eventDict['time'].append(SettingBezierDimm(At(startTime), TopController, Setting3, 95, 0, int(dimmduration*20), 5, 0, 100))

# 46
# Start Turn
startTime = beginning + 46
# eventDict['time'].append(MotorDirection(At(startTime), MOTOR_COUNTERCLOCKWISE))
# eventDict['time'].append(MotorSpeed(At(startTime), 80))
# # Bremsfactor 0.074
# eventDict['position'].append(MotorSpeed(LE(2.75 + 0.074), 0))

startTime = beginning + 50
dimmduration = 4.5
eventDict['time'].append(SettingBezierDimm(At(startTime), TopController, Setting4, 100, 0, int(dimmduration*20), 5, 0, 100))

# Setup Ebbe
ebbemove = 5.43
# 50
startTime = beginning + 50
eventDict['time'].append(ChannelRemoveEffect(At(startTime), BottomController, Channel1, 0))
eventDict['time'].append(ChannelRemoveEffect(At(startTime), BottomController, Channel3, 0))

eventDict['time'].append(ChannelAddEffect(At(startTime), TopController, Channel2, EffectSubtractPercentagePerlin, 0))


# STATE SUMMARY
# 
# TOP                               | BOTTOM
#                                   |
# Settings                          | Settings
# --------------------------------- | ---------------------------------
#   Setting1:            0          |   Setting1:            0
#   Setting2:            0          |   Setting2:            0
#   Setting3:            0          |   Setting3:            0
#   Setting4:            0          |   Setting4:            0
#
#   SettingVibrato:     0 to 100    |   SettingVibrato:     0 to 100
#   SettingPerlin:      0 to 100    |   SettingPerlin:      0 to 100
#
# Static Channels                   | Static Channels
# --------------------------------- | ---------------------------------
#   ChannelStrobe1Steptime: 34      |   ChannelStrobe1Steptime: 34
#   ChannelStrobe1Darkstep: 1       |   ChannelStrobe1Darkstep: 1
#   ChannelStrobe2Steptime: 34      |   ChannelStrobe2Steptime: 34
#   ChannelStrobe2Darkstep: 1       |   ChannelStrobe2Darkstep: 1
#
#   ChannelVibratoSteptime: 9       |   ChannelVibratoSteptime: 17
#   ChannelPerlinSteptime:  5       |   ChannelPerlinSteptime:  5
#
# Effects                           | Effects
# --------------------------------- | ---------------------------------
#   EffectStrobe1:        5757      |   EffectStrobe1:        1537
#   EffectStrobe2:        2626      |   EffectStrobe2:        2626
#
# Light Channels                    | Light Channels
# --------------------------------- | ---------------------------------
#   Channel1: Setting1, []          |   Channel1: Setting1, []
#   Channel2: Setting2, [Perlin]    |   Channel2: Setting2, [Strobe2, ]
#   Channel3: Setting3, []          |   Channel3: Setting3, []
#   Channel4: Setting4, [Vibrato]   |   Channel4: Setting4, []


# Light Top
startTime = beginning + 46.5 + ebbemove
eventDict['time'].append(ChannelRemoveEffect(At(startTime), TopController, Channel4, 0))

# STATE SUMMARY
# 
# TOP                               | BOTTOM
#
# Light Channels                    | Light Channels
# --------------------------------- | ---------------------------------
#   Channel1: Setting1, []          |   Channel1: Setting1, []
#   Channel2: Setting2, [Perlin]    |   Channel2: Setting2, [Strobe2, ]
#   Channel3: Setting3, []          |   Channel3: Setting3, []
#   Channel4: Setting4, []          |   Channel4: Setting4, []
fadeOutLength = 2.8
# sustainSteptime 
sustainSteptime = 4
eventDict['time'].append(SettingImpulseToBezierFadeout(At(startTime), TopController, Setting4, 70, 1, 30, sustainSteptime, int(fadeOutLength*10), 10, 100, 100))



# sustainSteptime
startTime = beginning + 49.5 + ebbemove
sustainSteptime = 5
fadeOutLength = 2
eventDict['time'].append(SettingImpulseToBezierFadeout(At(startTime), BottomController, Setting3, 80, 1, 20, sustainSteptime, int(fadeOutLength*10), 10, 0, 100))



startTime = beginning + 50.58 + ebbemove
sustainSteptime = 5
fadeOutLength = 2
eventDict['time'].append(SettingImpulseToBezierFadeout(At(startTime), TopController, Setting4, 100, 1, 40, sustainSteptime, int(fadeOutLength*10), 10, 100, 100))




# 52
# Top

startTime = beginning + 52 + ebbemove
fadeOutLength = 2.8
# sustainSteptime 
sustainSteptime = 5
eventDict['time'].append(SettingImpulseToBezierFadeout(At(startTime), TopController, Setting4, 100, 1, 40, sustainSteptime, int(fadeOutLength*10), 10, 100, 100))


# 53
# Right
startTime = beginning + 53 + ebbemove
fadeOutLength = 3.5
# sustainSteptime 
sustainSteptime = 5
eventDict['time'].append(SettingImpulseToBezierFadeout(At(startTime), BottomController, Setting3, 100, 1, 40, sustainSteptime, int(fadeOutLength*10), 10, 100, 100))


# 56.1
# Top
startTime = beginning + 56.1 + ebbemove
fadeOutLength = 2.8
# sustainSteptime 
sustainSteptime = 5
eventDict['time'].append(SettingImpulseToBezierFadeout(At(startTime), TopController, Setting4, 100, 1, 40, sustainSteptime, int(fadeOutLength*10), 10, 100, 100))


# 56.1 - 62
# Fade In String Aura in Backgrounf
startTime = beginning + 56.1 + ebbemove
dimmduration = 4.9
eventDict['time'].append(SettingBezierDimm(At(startTime), TopController, Setting2, 0, 100, int(dimmduration*10), 10, 0, 100))


# 57.1
# Right
startTime = beginning + 57.1 + ebbemove
fadeOutLength = 3.5
# sustainSteptime 
sustainSteptime = 5
eventDict['time'].append(SettingImpulseToBezierFadeout(At(startTime), BottomController, Setting3, 100, 1, 40, sustainSteptime, int(fadeOutLength*10), 10, 100, 100))


# 62 - 63.6
# Fade Out String Aura in Background
startTime = beginning + 62 + ebbemove
dimmduration = 2.3
eventDict['time'].append(SettingBezierDimm(At(startTime), TopController, Setting2, 100, 0, int(dimmduration*10), 10, 0, 100))

# 63.8
# Top
startTime = beginning + 63.8 + ebbemove
fadeOutLength = 2.8
# sustainSteptime 
sustainSteptime = 5
eventDict['time'].append(SettingImpulseToBezierFadeout(At(startTime), TopController, Setting4, 100, 1, 40, sustainSteptime, int(fadeOutLength*10), 10, 100, 100))


# 64.8
# Right
startTime = beginning + 64.8 + ebbemove
fadeOutLength = 3.5
# sustainSteptime 
sustainSteptime = 5
eventDict['time'].append(SettingImpulseToBezierFadeout(At(startTime), BottomController, Setting3, 100, 1, 40, sustainSteptime, int(fadeOutLength*10), 10, 100, 100))



# 64.9
# Light Left
startTime = beginning + 64.9 + ebbemove
fadeOutLength = 2.8
# sustainSteptime 
sustainSteptime = 4
eventDict['time'].append(SettingImpulseToBezierFadeout(At(startTime), BottomController, Setting1, 80, 1, 30, sustainSteptime, int(fadeOutLength*10), 10, 100, 100))

# 67.5
# Top
startTime = beginning + 67.5 + ebbemove
fadeOutLength = 2.8
# sustainSteptime 
sustainSteptime = 5
eventDict['time'].append(SettingImpulseToBezierFadeout(At(startTime), TopController, Setting4, 100, 1, 40, sustainSteptime, int(fadeOutLength*10), 10, 100, 100))


# 68.6
# Left
startTime = beginning + 68.6 + ebbemove
fadeOutLength = 2.8
# sustainSteptime 
sustainSteptime = 5
eventDict['time'].append(SettingImpulseToBezierFadeout(At(startTime), BottomController, Setting1, 100, 1, 40, sustainSteptime, int(fadeOutLength*10), 10, 100, 100))

# 69.6
# Right
startTime = beginning + 69.6 + ebbemove
fadeOutLength = 2.8
# sustainSteptime 
sustainSteptime = 5
eventDict['time'].append(SettingImpulseToBezierFadeout(At(startTime), BottomController, Setting3, 100, 1, 40, sustainSteptime, int(fadeOutLength*10), 10, 100, 100))


# 70 - 75
# Fade In String Aura
startTime = beginning + 70 + ebbemove
dimmduration = 5
eventDict['time'].append(SettingBezierDimm(At(startTime), TopController, Setting2, 0, 100, int(dimmduration*10), 10, 0, 100))

# 72
# Right
startTime = beginning + 72 + ebbemove
fadeOutLength = 2.8
# sustainSteptime 
sustainSteptime = 5
eventDict['time'].append(SettingImpulseToBezierFadeout(At(startTime), BottomController, Setting3, 100, 1, 40, sustainSteptime, int(fadeOutLength*10), 10, 100, 100))


# 75.4 76.4
# Fade Out String Aura
startTime = beginning + 75.4 + ebbemove
dimmduration = 3
eventDict['time'].append(SettingBezierDimm(At(startTime), TopController, Setting2, 100, 0, int(dimmduration*10), 10, 0, 100))

# 76.4
# Top
startTime = beginning + 76.4 + ebbemove
fadeOutLength = 2.8
# sustainSteptime 
sustainSteptime = 5
eventDict['time'].append(SettingImpulseToBezierFadeout(At(startTime), TopController, Setting4, 100, 1, 40, sustainSteptime, int(fadeOutLength*10), 10, 100, 100))


# 77.7
# Right
startTime = beginning + 77.7 + ebbemove
fadeOutLength = 3
# sustainSteptime 
sustainSteptime = 5
eventDict['time'].append(SettingImpulseToBezierFadeout(At(startTime), BottomController, Setting3, 100, 1, 40, sustainSteptime, int(fadeOutLength*10), 10, 100, 100))


# 78.9
# Light Left
startTime = beginning + 78.9 + ebbemove
fadeOutLength = 3
# sustainSteptime 
sustainSteptime = 4
eventDict['time'].append(SettingImpulseToBezierFadeout(At(startTime), BottomController, Setting1, 80, 1, 30, sustainSteptime, int(fadeOutLength*10), 10, 100, 100))


# 80.13
# Super Light Right
startTime = beginning + 80.13 + ebbemove
fadeOutLength = 3.5
# sustainSteptime 0
sustainSteptime = 3
eventDict['time'].append(SettingImpulseToBezierFadeout(At(startTime), BottomController, Setting3, 60, 1, 20, sustainSteptime, int(fadeOutLength*10), 10, 100, 100))


# 82.9-85.8
# Fade In string Aura
startTime = beginning + 82 + ebbemove
dimmduration = 3.5
eventDict['time'].append(SettingBezierDimm(At(startTime), TopController, Setting2, 0, 100, int(dimmduration*10), 10, 0, 100))

# 84.5
# Top
startTime = beginning + 84.5 + ebbemove
fadeOutLength = 2.8
# sustainSteptime 
sustainSteptime = 5
eventDict['time'].append(SettingImpulseToBezierFadeout(At(startTime), TopController, Setting4, 100, 1, 40, sustainSteptime, int(fadeOutLength*10), 10, 100, 100))


# 85.8 - 87.2
# Fade Out String Aura but not Fully
startTime = beginning + 85.8 + ebbemove
dimmduration = 1.4
eventDict['time'].append(SettingBezierDimm(At(startTime), TopController, Setting2, 100, 0, int(dimmduration*10), 10, 0, 100))

# 85.9
# Left Light
startTime = beginning + 85.9 + ebbemove
fadeOutLength = 2.8
# sustainSteptime 
sustainSteptime = 4
eventDict['time'].append(SettingImpulseToBezierFadeout(At(startTime), BottomController, Setting1, 80, 1, 30, sustainSteptime, int(fadeOutLength*10), 10, 90, 100))

# 86.2
# Right Light
startTime = beginning + 86.2 + ebbemove
fadeOutLength = 2.8
# sustainSteptime 
sustainSteptime = 4
eventDict['time'].append(SettingImpulseToBezierFadeout(At(startTime), BottomController, Setting3, 80, 1, 30, sustainSteptime, int(fadeOutLength*10), 10, 90, 100))


# 86.9
# Top
startTime = beginning + 86.8 + ebbemove
fadeOutLength = 2.8
# sustainSteptime 
sustainSteptime = 5
eventDict['time'].append(SettingImpulseToBezierFadeout(At(startTime), TopController, Setting4, 100, 1, 40, sustainSteptime, int(fadeOutLength*10), 10, 100, 100))


# 87.2 - 89
# Fade In String Aura
startTime = beginning + 87.2 + ebbemove
dimmduration = 2.8
eventDict['time'].append(SettingBezierDimm(At(startTime), TopController, Setting2, 0, 100, int(dimmduration*10), 10, 0, 100))

# 88.3
# Right
startTime = beginning + 88.3 + ebbemove
fadeOutLength = 2.8
# sustainSteptime 
sustainSteptime = 5
eventDict['time'].append(SettingImpulseToBezierFadeout(At(startTime), BottomController, Setting3, 100, 1, 40, sustainSteptime, int(fadeOutLength*10), 10, 100, 100))


# 88.7
# Left
startTime = beginning + 88.7 + ebbemove
fadeOutLength = 2.8
# sustainSteptime 
sustainSteptime = 5
eventDict['time'].append(SettingImpulseToBezierFadeout(At(startTime), BottomController, Setting1, 100, 1, 40, sustainSteptime, int(fadeOutLength*10), 10, 100, 100))

# 89 - 92.5
# Fade Out String Aura
startTime = beginning + 89 + ebbemove
dimmduration = 3.5
eventDict['time'].append(SettingBezierDimm(At(startTime), TopController, Setting2, 100, 0, int(dimmduration*10), 10, 0, 100))

# 89.8
# Top
startTime = beginning + 89.8 + ebbemove
fadeOutLength = 2.8
# sustainSteptime 
sustainSteptime = 5
eventDict['time'].append(SettingImpulseToBezierFadeout(At(startTime), TopController, Setting4, 100, 1, 40, sustainSteptime, int(fadeOutLength*10), 10, 100, 100))


# 91.2
# Light Right
startTime = beginning + 91.2 + ebbemove
fadeOutLength = 2.8
# sustainSteptime 
sustainSteptime = 5
eventDict['time'].append(SettingImpulseToBezierFadeout(At(startTime), BottomController, Setting3, 80, 1, 30, sustainSteptime, int(fadeOutLength*10), 10, 90, 100))


# 91.8
# Light Left
startTime = beginning + 91.6 + ebbemove
fadeOutLength = 2.8
# sustainSteptime 
sustainSteptime = 5
eventDict['time'].append(SettingImpulseToBezierFadeout(At(startTime), BottomController, Setting1, 100, 1, 40, sustainSteptime, int(fadeOutLength*10), 10, 100, 100))

# 93.5
# Top
startTime = beginning + 93 + ebbemove
fadeOutLength = 4
# sustainSteptime 
sustainSteptime = 5
eventDict['time'].append(SettingImpulseToBezierFadeout(At(startTime), TopController, Setting4, 100, 1, 40, sustainSteptime, int(fadeOutLength*10), 10, 100, 100))


# 94.2 - 100.8
# Aura Fade In
startTime = beginning + 94.2 + ebbemove
dimmduration = 6.6
eventDict['time'].append(SettingBezierDimm(At(startTime), TopController, Setting2, 0, 100, int(dimmduration*10), 10, 0, 100))

# 96.25
# Super Light Left
startTime = beginning + 96 + ebbemove
fadeOutLength = 2.8
# sustainSteptime 
sustainSteptime = 5
eventDict['time'].append(SettingImpulseToBezierFadeout(At(startTime), BottomController, Setting1, 60, 1, 15, sustainSteptime, int(fadeOutLength*10), 10, 100, 100))

# 96.5
# Super Ligth Right
startTime = beginning + 96.2 + ebbemove
fadeOutLength = 2.8
# sustainSteptime 
sustainSteptime = 3
eventDict['time'].append(SettingImpulseToBezierFadeout(At(startTime), BottomController, Setting3, 60, 1, 15, sustainSteptime, int(fadeOutLength*10), 10, 100, 100))


# 106 - 109
# Aura Fade OUt
startTime = beginning + 100 + ebbemove
dimmduration = 8
eventDict['time'].append(SettingBezierDimm(At(startTime), TopController, Setting2, 100, 0, int(dimmduration*10), 10, 0, 100))


# 196
# Start Part IV
# Setup

beginning = originalBeginning
startTime = beginning + 196

eventDict['time'].append(ChannelSetStatic(At(startTime), BottomController, ChannelStrobe1Darkstep, 0))
eventDict['time'].append(EffectSequencedLightStrobe(At(startTime), BottomController, EffectStrobe1, ChannelStrobe1Steptime, ChannelStrobe1Darkstep, 2424))
eventDict['time'].append(ChannelAddEffect(At(startTime), BottomController, Channel2, EffectStrobe1, 0))
eventDict['time'].append(ChannelAddEffect(At(startTime), BottomController, Channel4, EffectStrobe1, 0))

eventDict['time'].append(ChannelAddEffect(At(startTime), BottomController, Channel1, EffectSidechain, 1))
eventDict['time'].append(ChannelAddEffect(At(startTime), BottomController, Channel3, EffectSidechain, 1))


eventDict['time'].append(ChannelSetSetting(At(startTime), BottomController, ChannelSidechain, SettingSidechain))


startTime = beginning + 212 #moved it to where top ist first used to prolong aura fade out from part III (time events are sorted at the end)
eventDict['time'].append(LightSetChannel(At(startTime), TopController, [Light1,Light3], Channel1))
eventDict['time'].append(LightSetChannel(At(startTime), TopController, [Light2,Light4], Channel2))
eventDict['time'].append(ChannelSetStatic(At(startTime), TopController, ChannelStrobe1Steptime, 80))
eventDict['time'].append(ChannelSetStatic(At(startTime), TopController, ChannelStrobe1Darkstep, 1))
eventDict['time'].append(EffectSequencedLightStrobe(At(startTime), TopController, EffectStrobe1, ChannelStrobe1Steptime, ChannelStrobe1Darkstep, 6868))
eventDict['time'].append(ChannelAddEffect(At(startTime), TopController, Channel2, EffectStrobe1, 0))

eventDict['time'].append(ChannelAddEffect(At(startTime), BottomController, Channel2, EffectSidechain, 1))
eventDict['time'].append(ChannelAddEffect(At(startTime), BottomController, Channel4, EffectSidechain, 1))


# STATE SUMMARY
# 
# TOP                               | BOTTOM
#                                   |
# Settings                          | Settings
# --------------------------------- | ---------------------------------
#   Setting1:            0          |   Setting1:            0
#   Setting2:            0          |   Setting2:            0
#   Setting3:            0          |   Setting3:            0
#   Setting4:            0          |   Setting4:            0
#
#   SettingVibrato:     0 to 100    |   SettingVibrato:     0 to 100
#   SettingPerlin:      0 to 100    |   SettingPerlin:      0 to 100
#
# Static Channels                   | Static Channels
# --------------------------------- | ---------------------------------
#   ChannelStrobe1Steptime: 100     |   ChannelStrobe1Steptime: 34
#   ChannelStrobe1Darkstep: 0       |   ChannelStrobe1Darkstep: 0
#   ChannelStrobe2Steptime: 34      |   ChannelStrobe2Steptime: 34
#   ChannelStrobe2Darkstep: 1       |   ChannelStrobe2Darkstep: 1
#
#   ChannelVibratoSteptime: 9       |   ChannelVibratoSteptime: 17
#   ChannelPerlinSteptime:  5       |   ChannelPerlinSteptime:  5
#
# Effects                           | Effects
# --------------------------------- | ---------------------------------
#   EffectStrobe1:        6868      |   EffectStrobe1:        2424
#   EffectStrobe2:        2626      |   EffectStrobe2:        2626
#
# Light Channels                    | Light Channels
# --------------------------------- | ---------------------------------
#   Channel1: Setting1, []          |   Channel1: Setting1, []
#   Channel2: Setting2, [Strobe1]   |   Channel2: Setting2, [Strobe1, ]
#   Channel3: Setting3, []          |   Channel3: Setting3, []
#   Channel4: Setting4, []          |   Channel4: Setting4, [Strobe1, ]



# eventDict['time'].append(MotorSpeed(At(startTime), 10))

startTime = beginning + 197
# eventDict['time'].append(MotorSpeed(At(startTime), 20))

startTime = beginning + 198
# eventDict['time'].append(MotorSpeed(At(startTime), 30))

startTime = beginning + 198
# eventDict['time'].append(MotorSpeed(At(startTime), 45))

loopPianofadeOutLength = 0.3
loopPianosustainSteptime = 3

# 196.63
# 6 Pianos spaced by 0.25
startTime = beginning + 196.63
left = True
for i in range(6):
    if left:
        sett = Setting1
    else:
        sett = Setting3
    eventDict['time'].append(SettingImpulseToBezierFadeout(At(startTime), BottomController, sett, 70, 1, 20, loopPianosustainSteptime, int(loopPianofadeOutLength*20), 5, 0, 100))
    startTime += 0.25
    left = not left

# 198.68
# 2 Pianos spaced by 0.25
startTime = beginning + 198.68
left = True
for i in range(2):
    if left:
        sett = Setting1
    else:
        sett = Setting3
    eventDict['time'].append(SettingImpulseToBezierFadeout(At(startTime), BottomController, sett, 70, 1, 20, loopPianosustainSteptime, int(loopPianofadeOutLength*20), 5, 70, 100))
    startTime += 0.25
    left = not left

# 199.71
# 2 Pianos spaced by 0.25
startTime = beginning + 199.71
left = True
for i in range(2):
    if left:
        sett = Setting1
    else:
        sett = Setting3
    eventDict['time'].append(SettingImpulseToBezierFadeout(At(startTime), BottomController, sett, 70, 1, 20, loopPianosustainSteptime, int(loopPianofadeOutLength*20), 5, 70, 100))
    startTime += 0.25
    left = not left

# 200.72
# 6 Pianos
startTime = beginning + 200.72
left = True
for i in range(6):
    if left:
        sett = Setting1
    else:
        sett = Setting3
    eventDict['time'].append(SettingImpulseToBezierFadeout(At(startTime), BottomController, sett, 70, 1, 20, loopPianosustainSteptime, int(loopPianofadeOutLength*20), 5, 70, 100))
    startTime += 0.25
    left = not left

# 202.75
# 6 Pianos
startTime = beginning + 202.75
left = True
for i in range(6):
    if left:
        sett = Setting1
    else:
        sett = Setting3
    eventDict['time'].append(SettingImpulseToBezierFadeout(At(startTime), BottomController, sett, 70, 1, 10, loopPianosustainSteptime, int(loopPianofadeOutLength*20), 5, 70, 100))
    startTime += 0.25
    left = not left

# 204.5
# Continuous Pianos
startTime = beginning + 204.5
left = True
for i in range(32):
    if left:
        sett = Setting1
    else:
        sett = Setting3
    eventDict['time'].append(SettingImpulseToBezierFadeout(At(startTime), BottomController, sett, 80, 1, 10, loopPianosustainSteptime, int(loopPianofadeOutLength*20), 5, 70, 100))
    startTime += 0.25
    left = not left

# Wave
# Strobe from left and right
startTime = beginning + 206.5
dimmduration = 6
eventDict['time'].append(SettingBezierDimm(At(startTime), BottomController, Setting2, 0, 70, int(dimmduration*10), 10, 0, 100))
eventDict['time'].append(SettingBezierDimm(At(startTime), BottomController, Setting4, 0, 70, int(dimmduration*10), 10, 0, 100))
startTime = startTime + dimmduration
dimmduration = 3
eventDict['time'].append(SettingBezierDimm(At(startTime), BottomController, Setting2, 70, 10, int(dimmduration*10), 10, 0, 100))
eventDict['time'].append(SettingBezierDimm(At(startTime), BottomController, Setting4, 70, 10, int(dimmduration*10), 10, 0, 100))
startTime = startTime + dimmduration
dimmduration = 0.5
eventDict['time'].append(SettingBezierDimm(At(startTime), BottomController, Setting2, 10, 50, int(dimmduration*10), 10, 0, 100))
eventDict['time'].append(SettingBezierDimm(At(startTime), BottomController, Setting4, 10, 50, int(dimmduration*10), 10, 0, 100))
startTime = startTime + dimmduration
dimmduration = 0.5
eventDict['time'].append(SettingBezierDimm(At(startTime), BottomController, Setting2, 50, 0, int(dimmduration*10), 10, 0, 100))
eventDict['time'].append(SettingBezierDimm(At(startTime), BottomController, Setting4, 50, 0, int(dimmduration*10), 10, 0, 100))

# 212.98
# Chord
startTime = beginning + 212.98
fadeOutLength = 1.8
# sustainSteptime 
sustainSteptime = 5
eventDict['time'].append(SettingImpulseToBezierFadeout(At(startTime), TopController, Setting1, 100, 1, 40, sustainSteptime, int(fadeOutLength*10), 10, 100, 100))
eventDict['time'].append(SettingImpulseToBezierFadeout(At(startTime), BottomController, SettingSidechain, 100, 1, 40, sustainSteptime, int(fadeOutLength*10), 10, 100, 100))
# eventDict['time'].append(MotorSpeed(At(startTime), 60))



startTime = beginning + 212.98
left = True
for i in range(48):
    if left:
        sett = Setting1
    else:
        sett = Setting3
    eventDict['time'].append(SettingImpulseToBezierFadeout(At(startTime), BottomController, sett, 100, 1, 40, loopPianosustainSteptime, int(loopPianofadeOutLength*20), 5, 80, 100))
    startTime += 0.25
    left = not left

# 216.96
# Chord
startTime = beginning + 216.96
fadeOutLength = 1.8
# sustainSteptime 
sustainSteptime = 5
eventDict['time'].append(SettingImpulseToBezierFadeout(At(startTime), TopController, Setting1, 100, 1, 40, sustainSteptime, int(fadeOutLength*10), 10, 100, 100))
eventDict['time'].append(SettingImpulseToBezierFadeout(At(startTime), BottomController, SettingSidechain, 100, 1, 40, sustainSteptime, int(fadeOutLength*10), 10, 100, 100))


# 216.96
# Pulsating Appears Lightly
startTime = beginning + 216.96
dimmduration = 1
eventDict['time'].append(SettingBezierDimm(At(startTime), TopController, Setting2, 0, 60, int(dimmduration*10), 10, 0, 100))

# Wave
# Strobe from left and right
startTime = beginning + 220
dimmduration = 13
eventDict['time'].append(SettingBezierDimm(At(startTime), BottomController, Setting2, 0, 70, int(dimmduration*10), 10, 0, 100))
eventDict['time'].append(SettingBezierDimm(At(startTime), BottomController, Setting4, 0, 70, int(dimmduration*10), 10, 0, 100))
startTime = startTime + dimmduration
dimmduration = 7
eventDict['time'].append(SettingBezierDimm(At(startTime), BottomController, Setting2, 70, 0, int(dimmduration*10), 10, 0, 100))
eventDict['time'].append(SettingBezierDimm(At(startTime), BottomController, Setting4, 70, 0, int(dimmduration*10), 10, 0, 100))


# 220.91
# Chord
startTime = beginning + 220.91
fadeOutLength = 1.8
# sustainSteptime 
sustainSteptime = 5
eventDict['time'].append(SettingImpulseToBezierFadeout(At(startTime), TopController, Setting1, 100, 1, 40, sustainSteptime, int(fadeOutLength*10), 10, 100, 100))
eventDict['time'].append(SettingImpulseToBezierFadeout(At(startTime), BottomController, SettingSidechain, 100, 1, 40, sustainSteptime, int(fadeOutLength*10), 10, 100, 100))
# eventDict['time'].append(MotorSpeed(At(startTime), 70))


# 224.91
# Chord
startTime = beginning + 224.91
fadeOutLength = 1.8
# sustainSteptime 
sustainSteptime = 5
eventDict['time'].append(SettingImpulseToBezierFadeout(At(startTime), TopController, Setting1, 100, 1, 40, sustainSteptime, int(fadeOutLength*10), 10, 100, 100))
eventDict['time'].append(SettingImpulseToBezierFadeout(At(startTime), BottomController, SettingSidechain, 100, 1, 40, sustainSteptime, int(fadeOutLength*10), 10, 100, 100))



startTime = beginning + 224.91
left = True
for i in range(182):
    if left:
        sett = Setting1
    else:
        sett = Setting3
    eventDict['time'].append(SettingImpulseToBezierFadeout(At(startTime), BottomController, sett, 70, 1, 30, loopPianosustainSteptime, int(loopPianofadeOutLength*20), 5, 80, 100))
    startTime += 0.25
    left = not left

# 228.95
# Chord
startTime = beginning + 228.95
fadeOutLength = 1.8
# sustainSteptime 
sustainSteptime = 5
eventDict['time'].append(SettingImpulseToBezierFadeout(At(startTime), TopController, Setting1, 100, 1, 40, sustainSteptime, int(fadeOutLength*10), 10, 100, 100))
eventDict['time'].append(SettingImpulseToBezierFadeout(At(startTime), BottomController, SettingSidechain, 100, 1, 40, sustainSteptime, int(fadeOutLength*10), 10, 100, 100))



# 232.95
# Chord
startTime = beginning + 232.95
fadeOutLength = 1.8
# sustainSteptime 
sustainSteptime = 3
eventDict['time'].append(SettingImpulseToBezierFadeout(At(startTime), TopController, Setting1, 100, 1, 40, sustainSteptime, int(fadeOutLength*10), 10, 100, 100))
eventDict['time'].append(SettingImpulseToBezierFadeout(At(startTime), BottomController, SettingSidechain, 100, 1, 40, sustainSteptime, int(fadeOutLength*10), 10, 100, 100))



# 236.93
# Soft Chord
startTime = beginning + 236.93
fadeOutLength = 1.8
# sustainSteptime 
sustainSteptime = 5
eventDict['time'].append(SettingImpulseToBezierFadeout(At(startTime), TopController, Setting1, 80, 1, 30, sustainSteptime, int(fadeOutLength*10), 10, 100, 100))
eventDict['time'].append(SettingImpulseToBezierFadeout(At(startTime), BottomController, SettingSidechain, 80, 1, 40, sustainSteptime, int(fadeOutLength*10), 10, 100, 100))


# 240.95
# Soft Chord
startTime = beginning + 240.95
fadeOutLength = 1.8
# sustainSteptime 
sustainSteptime = 5
eventDict['time'].append(SettingImpulseToBezierFadeout(At(startTime), TopController, Setting1, 80, 1, 30, sustainSteptime, int(fadeOutLength*10), 10, 100, 100))
eventDict['time'].append(SettingImpulseToBezierFadeout(At(startTime), BottomController, SettingSidechain, 80, 1, 40, sustainSteptime, int(fadeOutLength*10), 10, 100, 100))
# eventDict['time'].append(MotorSpeed(At(startTime), 90))


# 244.89
# Chord
startTime = beginning + 244.89
fadeOutLength = 1.8
# sustainSteptime 
sustainSteptime = 5
eventDict['time'].append(SettingImpulseToBezierFadeout(At(startTime), TopController, Setting1, 90, 1, 30, sustainSteptime, int(fadeOutLength*10), 10, 100, 100))
eventDict['time'].append(SettingImpulseToBezierFadeout(At(startTime), BottomController, SettingSidechain, 90, 1, 40, sustainSteptime, int(fadeOutLength*10), 10, 100, 100))

# eventDict['time'].append(MotorSpeed(At(startTime), 100))


# 244.89 - 247.91
# Wave
# Strobe from left and right
startTime = beginning + 244.89
dimmduration = 1.5
eventDict['time'].append(SettingBezierDimm(At(startTime), BottomController, Setting2, 0, 70, int(dimmduration*10), 10, 0, 100))
eventDict['time'].append(SettingBezierDimm(At(startTime), BottomController, Setting4, 0, 70, int(dimmduration*10), 10, 0, 100))
startTime = startTime + dimmduration
eventDict['time'].append(SettingBezierDimm(At(startTime), BottomController, Setting2, 70, 0, int(dimmduration*10), 10, 0, 100))
eventDict['time'].append(SettingBezierDimm(At(startTime), BottomController, Setting4, 70, 0, int(dimmduration*10), 10, 0, 100))

# 246.6 - 250.65
# Pulsating becomes full on intense
startTime = beginning + 246.6
dimmduration = 4
eventDict['time'].append(SettingBezierDimm(At(startTime), TopController, Setting2, 60, 95, int(dimmduration*10), 10, 0, 100))

eventDict['time'].append(ChannelSetStatic(At(startTime), BottomController, ChannelStrobe2Steptime, 80))
eventDict['time'].append(ChannelSetStatic(At(startTime), BottomController, ChannelStrobe2Darkstep, 0))
eventDict['time'].append(SettingSquareWave(At(startTime), BottomController, SettingSidechain, StaticChannel0, StaticChannel51, ChannelStrobe2Steptime, ChannelStrobe2Steptime, StaticChannel0, StaticChannel0))

# 248
startTime = beginning + 248
# eventDict['time'].append(MotorSpeed(At(startTime), 110))

# 254.45 - 257.34
# Fade In Strobe from left and right
startTime = beginning + 246.6
dimmduration = 3
eventDict['time'].append(SettingBezierDimm(At(startTime), BottomController, Setting2, 0, 80, int(dimmduration*10), 10, 0, 100))
eventDict['time'].append(SettingBezierDimm(At(startTime), BottomController, Setting4, 0, 80, int(dimmduration*10), 10, 0, 100))


# 257.34 = 260.45
# Fade Out Strobe from left and right
startTime = beginning + 257.34
dimmduration = 3
eventDict['time'].append(SettingBezierDimm(At(startTime), BottomController, Setting2, 80, 0, int(dimmduration*10), 10, 0, 100))
eventDict['time'].append(SettingBezierDimm(At(startTime), BottomController, Setting4, 80, 0, int(dimmduration*10), 10, 0, 100))

# 260.95 - 262.4
# Wave Strobe from left and right
startTime = beginning + 260.95
dimmduration = 0.25
eventDict['time'].append(SettingBezierDimm(At(startTime), BottomController, Setting2, 0, 70, int(dimmduration*10), 10, 0, 100))
eventDict['time'].append(SettingBezierDimm(At(startTime), BottomController, Setting4, 0, 70, int(dimmduration*10), 10, 0, 100))
startTime = startTime + dimmduration
eventDict['time'].append(SettingBezierDimm(At(startTime), BottomController, Setting2, 70, 0, int(dimmduration*10), 10, 0, 100))
eventDict['time'].append(SettingBezierDimm(At(startTime), BottomController, Setting4, 70, 0, int(dimmduration*10), 10, 0, 100))

# 262.44-263.4
# Fade In Strobe from left and right
startTime = beginning + 262.44
dimmduration = 1
eventDict['time'].append(SettingBezierDimm(At(startTime), BottomController, Setting2, 0, 50, int(dimmduration*10), 10, 0, 100))
eventDict['time'].append(SettingBezierDimm(At(startTime), BottomController, Setting4, 0, 50, int(dimmduration*10), 10, 0, 100))

# 264.65 - 268.14
# Fade Out Strobe from left and right
startTime = beginning + 264.65
dimmduration = 3.5
eventDict['time'].append(SettingBezierDimm(At(startTime), BottomController, Setting2, 50, 0, int(dimmduration*10), 10, 0, 100))
eventDict['time'].append(SettingBezierDimm(At(startTime), BottomController, Setting4, 50, 0, int(dimmduration*10), 10, 0, 100))
# eventDict['time'].append(MotorSpeed(At(startTime), 80))


# 268 - 279.54
# Fade Out Everything
startTime = beginning + 268
dimmduration = 10
eventDict['time'].append(SettingBezierDimm(At(startTime), TopController, Setting2, 95, 0, int(dimmduration*10), 10, 0, 100))
# eventDict['time'].append(MotorSpeed(At(startTime), 60))

eventDict['time'].append(LightSetChannel(At(startTime), TopController, [Light1,], Channel1))
eventDict['time'].append(LightSetChannel(At(startTime), TopController, [Light3,], Channel3))

# 272 Piano every second

startTime = beginning + 272
strength = 70
fadeOutLength = 0.5
for i in range(4):
    eventDict['time'].append(SettingImpulseToBezierFadeout(At(startTime), TopController, Setting1, strength, 1, 30, loopPianosustainSteptime, int(loopPianofadeOutLength*20), 5, 80, 100))
    startTime += 1


# 276.5 - 279.5 Piano Fades Out
startTime = beginning + 276
for i in range(6):
    eventDict['time'].append(SettingImpulseToBezierFadeout(At(startTime), TopController, Setting1, strength, 1, 30, loopPianosustainSteptime, int(loopPianofadeOutLength*20), 5, 80, 100))
    startTime += 1
    strength -= 10


# PART V
# Breakfactor: 0.0625
# eventDict['position'].append(MotorSpeed(LE(-1.5 + 0.0625), 0))

# Faint Flut Bottom 3 & 4
# Present Flut Top 2, Bottom 3
# Ebbe Pianos Top 4, Bottom 1

# Vibrato Pulse Weak Top 1 and Strong Top 3

beginning = originalBeginning
startTime = beginning + 278

eventDict['time'].append(LightSetChannel(At(startTime), TopController, [Light2,], Channel2))
eventDict['time'].append(LightSetChannel(At(startTime), TopController, [Light4,], Channel4))

eventDict['time'].append(EffectSequencedLightStrobe(At(startTime), BottomController, EffectStrobe1, ChannelStrobe1Steptime, ChannelStrobe1Darkstep, 3434))
eventDict['time'].append(EffectSequencedLightStrobe(At(startTime), BottomController, EffectStrobe2, ChannelStrobe2Steptime, ChannelStrobe2Darkstep, 6363))
eventDict['time'].append(EffectSequencedLightStrobe(At(startTime), TopController, EffectStrobe2, ChannelStrobe2Steptime, ChannelStrobe2Darkstep, 6363))

eventDict['time'].append(ChannelSetStatic(At(startTime), BottomController, ChannelStrobe1Darkstep, 1))
eventDict['time'].append(ChannelSetStatic(At(startTime), BottomController, ChannelStrobe2Steptime, 34))
eventDict['time'].append(ChannelSetStatic(At(startTime), BottomController, ChannelStrobe2Darkstep,1))

eventDict['time'].append(ChannelSetStatic(At(startTime), TopController, ChannelStrobe1Steptime, 34))
eventDict['time'].append(ChannelSetStatic(At(startTime), TopController, ChannelStrobe1Darkstep, 1))

eventDict['time'].append(ChannelRemoveEffects(At(startTime), BottomController, Channel1))
eventDict['time'].append(ChannelRemoveEffects(At(startTime), BottomController, Channel2))
eventDict['time'].append(ChannelRemoveEffects(At(startTime), BottomController, Channel3))
eventDict['time'].append(ChannelRemoveEffects(At(startTime), BottomController, Channel4))

eventDict['time'].append(ChannelAddEffect(At(startTime), BottomController, Channel3, EffectStrobe1, 0))
eventDict['time'].append(ChannelAddEffect(At(startTime), BottomController, Channel4, EffectStrobe1, 0))
eventDict['time'].append(ChannelRemoveEffect(At(startTime), BottomController, Channel1, 0))
eventDict['time'].append(ChannelRemoveEffect(At(startTime), BottomController, Channel2, 0))

eventDict['time'].append(ChannelAddEffect(At(startTime), TopController, Channel2, EffectStrobe2, 0))
eventDict['time'].append(ChannelAddEffect(At(startTime), TopController, Channel1, EffectSubtractPercentagePerlin, 0))
eventDict['time'].append(ChannelAddEffect(At(startTime), TopController, Channel3, EffectSubtractPercentageVibrato, 0))


# STATE SUMMARY
# 
# TOP                               | BOTTOM
#                                   |
# Settings                          | Settings
# --------------------------------- | ---------------------------------
#   Setting1:            0          |   Setting1:            0
#   Setting2:            0          |   Setting2:            0
#   Setting3:            0          |   Setting3:            0
#   Setting4:            0          |   Setting4:            0
#
#   SettingVibrato:     0 to 100    |   SettingVibrato:     0 to 100
#   SettingPerlin:      0 to 100    |   SettingPerlin:      0 to 100
#
# Static Channels                   | Static Channels
# --------------------------------- | ---------------------------------
#   ChannelStrobe1Steptime: 34      |   ChannelStrobe1Steptime: 34
#   ChannelStrobe1Darkstep: 1       |   ChannelStrobe1Darkstep: 1
#   ChannelStrobe2Steptime: 34      |   ChannelStrobe2Steptime: 34
#   ChannelStrobe2Darkstep: 1       |   ChannelStrobe2Darkstep: 1
#
#   ChannelVibratoSteptime: 9       |   ChannelVibratoSteptime: 17
#   ChannelPerlinSteptime:  5       |   ChannelPerlinSteptime:  5
#
# Effects                           | Effects
# --------------------------------- | ---------------------------------
#   EffectStrobe1:        6868      |   EffectStrobe1:        3434
#   EffectStrobe2:        6363      |   EffectStrobe2:        6363
#
# Light Channels                    | Light Channels
# --------------------------------- | ---------------------------------
#   Channel1: Setting1, [Perlin, ]  |   Channel1: Setting1, []
#   Channel2: Setting2, [Strobe2, ] |   Channel2: Setting2, []
#   Channel3: Setting3, []          |   Channel3: Setting3, [Strobe1, ]
#   Channel4: Setting4, []          |   Channel4: Setting4, [Strobe1, ]


# 279 - Vibrato Perline Pulse Weak
startTime = beginning + 279
dimmduration = 0.1
eventDict['time'].append(SettingBezierDimm(At(startTime), TopController, Setting1, 0, 50, int(dimmduration*10), 10, 0, 100))

# 280.6 - 282 Light Faint Flut Fade In (no darkstep)
startTime = beginning + 280.6
dimmduration = 1.5
eventDict['time'].append(SettingBezierDimm(At(startTime), BottomController, Setting1, 0, 50, int(dimmduration*10), 10, 0, 100))
eventDict['time'].append(SettingBezierDimm(At(startTime), BottomController, Setting3, 0, 50, int(dimmduration*10), 10, 0, 100))

# 280.8 Piano Key
startTime = beginning + 280.8
fadeOutLength = 2.8
# sustainSteptime 
sustainSteptime = 5
eventDict['time'].append(SettingImpulseToBezierFadeout(At(startTime), BottomController, Setting1, 100, 1, 40, sustainSteptime, int(fadeOutLength*10), 10, 100, 100))


# 282.8 Piano Key
startTime = beginning + 282.8
fadeOutLength = 2.8
# sustainSteptime 
sustainSteptime = 5
eventDict['time'].append(SettingImpulseToBezierFadeout(At(startTime), TopController, Setting4, 100, 1, 40, sustainSteptime, int(fadeOutLength*10), 10, 100, 100))


# 282.3 - 283 Faint Darkstep Flut Fade In
startTime = beginning + 282.3
dimmduration = 0.8
eventDict['time'].append(SettingBezierDimm(At(startTime), BottomController, Setting1, 0, 80, int(dimmduration*10), 10, 0, 100))
eventDict['time'].append(SettingBezierDimm(At(startTime), BottomController, Setting3, 0, 80, int(dimmduration*10), 10, 0, 100))

# 283 - 285.5  Faint Darkstep Flut Fade Out
startTime = beginning + 283
dimmduration = 2.5
eventDict['time'].append(SettingBezierDimm(At(startTime), BottomController, Setting1, 80, 0, int(dimmduration*10), 10, 0, 100))
eventDict['time'].append(SettingBezierDimm(At(startTime), BottomController, Setting3, 80, 0, int(dimmduration*10), 10, 0, 100))

# 283.9 Light Piano Key
startTime = beginning + 283.9
fadeOutLength = 2.8
# sustainSteptime 
sustainSteptime = 5
eventDict['time'].append(SettingImpulseToBezierFadeout(At(startTime), TopController, Setting4, 70, 1, 40, sustainSteptime, int(fadeOutLength*10), 10, 100, 100))


# 284.8 Piano Key
startTime = beginning + 284.8
fadeOutLength = 2.8
# sustainSteptime 
sustainSteptime = 5
eventDict['time'].append(SettingImpulseToBezierFadeout(At(startTime), BottomController, Setting1, 100, 1, 40, sustainSteptime, int(fadeOutLength*10), 10, 100, 100))


# 286.4 - 288.5 Faint Flut Wave
startTime = beginning + 286.4
dimmduration = 1
eventDict['time'].append(SettingBezierDimm(At(startTime), BottomController, Setting1, 0, 80, int(dimmduration*10), 10, 0, 100))
eventDict['time'].append(SettingBezierDimm(At(startTime), BottomController, Setting3, 0, 80, int(dimmduration*10), 10, 0, 100))
startTime = beginning + 287
dimmduration = 1
eventDict['time'].append(SettingBezierDimm(At(startTime), BottomController, Setting1, 80, 0, int(dimmduration*10), 10, 0, 100))
eventDict['time'].append(SettingBezierDimm(At(startTime), BottomController, Setting3, 80, 0, int(dimmduration*10), 10, 0, 100))

# 287.8 Very Light Key
startTime = beginning + 287.8
fadeOutLength = 2.8
# sustainSteptime 
sustainSteptime = 5
eventDict['time'].append(SettingImpulseToBezierFadeout(At(startTime), BottomController, Setting1, 60, 1, 40, sustainSteptime, int(fadeOutLength*10), 10, 100, 100))


# 288.5 - 291 Stronger Faint Flut Wave
startTime = beginning + 288.5
dimmduration = 1
eventDict['time'].append(SettingBezierDimm(At(startTime), BottomController, Setting1, 0, 95, int(dimmduration*10), 10, 0, 100))
eventDict['time'].append(SettingBezierDimm(At(startTime), BottomController, Setting3, 0, 95, int(dimmduration*10), 10, 0, 100))
startTime = beginning + 290
dimmduration = 1
eventDict['time'].append(SettingBezierDimm(At(startTime), BottomController, Setting1, 95, 0, int(dimmduration*10), 10, 0, 100))
eventDict['time'].append(SettingBezierDimm(At(startTime), BottomController, Setting3, 95, 0, int(dimmduration*10), 10, 0, 100))

# 288.8 Light Key
startTime = beginning + 288.8
fadeOutLength = 2.8
# sustainSteptime 
sustainSteptime = 5
eventDict['time'].append(SettingImpulseToBezierFadeout(At(startTime), TopController, Setting4, 80, 1, 40, sustainSteptime, int(fadeOutLength*10), 10, 100, 100))


# 289 Vibrato Pulse Fast and Stronger
startTime = beginning + 289
dimmduration = 0.1
eventDict['time'].append(SettingBezierDimm(At(startTime), TopController, Setting1, 50, 0, int(dimmduration*10), 10, 0, 100))
eventDict['time'].append(SettingBezierDimm(At(startTime), TopController, Setting3, 0, 70, int(dimmduration*10), 10, 0, 100))


# 289.3 Light Key
startTime = beginning + 289.3
fadeOutLength = 2.8
# sustainSteptime 
sustainSteptime = 5
eventDict['time'].append(SettingImpulseToBezierFadeout(At(startTime), BottomController, Setting1, 80, 1, 40, sustainSteptime, int(fadeOutLength*10), 10, 100, 100))


# 292 - 293 Present Flut Wave (Darkstep)
eventDict['time'].append(ChannelAddEffect(At(startTime), BottomController, Channel3, EffectStrobe2, 0))


# STATE SUMMARY
# 
# TOP                               | BOTTOM
#                                   |
#
# Light Channels                    | Light Channels
# --------------------------------- | ---------------------------------
#   Channel1: Setting1, [Perlin, ]  |   Channel1: Setting1, []
#   Channel2: Setting2, [Strobe2, ] |   Channel2: Setting2, []
#   Channel3: Setting3, []          |   Channel3: Setting3, [Strobe2, ]
#   Channel4: Setting4, []          |   Channel4: Setting4, [Strobe1, ]

startTime = beginning + 292
dimmduration = 0.5
eventDict['time'].append(SettingBezierDimm(At(startTime), TopController, Setting2, 0, 95, int(dimmduration*10), 10, 0, 100))
eventDict['time'].append(SettingBezierDimm(At(startTime), BottomController, Setting3, 0, 95, int(dimmduration*10), 10, 0, 100))
startTime = beginning + 292.5
dimmduration = 0.5
eventDict['time'].append(SettingBezierDimm(At(startTime), TopController, Setting2, 95, 0, int(dimmduration*10), 10, 0, 100))
eventDict['time'].append(SettingBezierDimm(At(startTime), BottomController, Setting3, 95, 0, int(dimmduration*10), 10, 0, 100))


# 292.5 Vibrato Pulse Slower
startTime = beginning + 292.5
eventDict['time'].append(ChannelSetStatic(At(startTime), TopController, ChannelVibratoSteptime, 17))


# STATE SUMMARY
# 
# TOP                               | BOTTOM
#                                   |
# Static Channels                   | Static Channels
# --------------------------------- | ---------------------------------
#
#   ChannelVibratoSteptime: 17       |   ChannelVibratoSteptime: 17
#   ChannelPerlinSteptime:  5        |   ChannelPerlinSteptime:  5


# 293 - 295 Vibrato Stronger
startTime = beginning + 293
dimmduration = 2
eventDict['time'].append(SettingBezierDimm(At(startTime), TopController, Setting3, 70, 85, int(dimmduration*10), 10, 0, 100))

# 294 - 296 Present Flut Wave  (Darkstep)
startTime = beginning + 294
dimmduration = 1
eventDict['time'].append(SettingBezierDimm(At(startTime), TopController, Setting2, 0, 95, int(dimmduration*10), 10, 0, 100))
eventDict['time'].append(SettingBezierDimm(At(startTime), BottomController, Setting3, 0, 95, int(dimmduration*10), 10, 0, 100))
startTime = beginning + 295
dimmduration = 1
eventDict['time'].append(SettingBezierDimm(At(startTime), TopController, Setting2, 95, 0, int(dimmduration*10), 10, 0, 100))
eventDict['time'].append(SettingBezierDimm(At(startTime), BottomController, Setting3, 95, 0, int(dimmduration*10), 10, 0, 100))

# 296.8 Double Key
startTime = beginning + 296.8
fadeOutLength = 2.8
# sustainSteptime 
sustainSteptime = 5
eventDict['time'].append(SettingImpulseToBezierFadeout(At(startTime), TopController, Setting4, 100, 1, 40, sustainSteptime, int(fadeOutLength*10), 10, 100, 100))
eventDict['time'].append(SettingImpulseToBezierFadeout(At(startTime), BottomController, Setting1, 100, 1, 40, sustainSteptime, int(fadeOutLength*10), 10, 100, 100))


# 297.45 Piano Key
startTime = beginning + 297.45
fadeOutLength = 2.8
# sustainSteptime 
sustainSteptime = 5
eventDict['time'].append(SettingImpulseToBezierFadeout(At(startTime), BottomController, Setting1, 100, 1, 40, sustainSteptime, int(fadeOutLength*10), 10, 100, 100))


# 298 - 301 Vibrato Maximum
startTime = beginning + 298
dimmduration = 3
eventDict['time'].append(SettingBezierDimm(At(startTime), TopController, Setting3, 85, 95, int(dimmduration*10), 10, 0, 100))

# 300.8 Double Piano Key
startTime = beginning + 300.8
fadeOutLength = 2.8
# sustainSteptime 
sustainSteptime = 5
eventDict['time'].append(SettingImpulseToBezierFadeout(At(startTime), TopController, Setting4, 100, 1, 40, sustainSteptime, int(fadeOutLength*10), 10, 100, 100))
fadeOutLength = 0.5
eventDict['time'].append(SettingImpulseToBezierFadeout(At(startTime), BottomController, Setting1, 100, 1, 40, sustainSteptime, int(fadeOutLength*10), 10, 100, 100))

# 301 - 303.5 Vibrato Fade Out (Switch to Perlin)
startTime = beginning + 301
dimmduration = 2.5
eventDict['time'].append(SettingBezierDimm(At(startTime), TopController, Setting3, 95, 0, int(dimmduration*10), 10, 0, 100))
eventDict['time'].append(SettingBezierDimm(At(startTime), TopController, Setting1, 0, 40, int(dimmduration*10), 10, 0, 100))


#Part VI

beginning = originalBeginning
startTime = beginning + 301.5

# eventDict['time'].append(LightSetChannel(At(startTime), TopController, [Light2,], Channel2))
# eventDict['time'].append(LightSetChannel(At(startTime), TopController, [Light4,], Channel4))

eventDict['time'].append(EffectSequencedLightStrobe(At(startTime), BottomController, EffectStrobe1, ChannelStrobe1Steptime, ChannelStrobe1Darkstep, 1368))
eventDict['time'].append(EffectSequencedLightStrobe(At(startTime), TopController, EffectStrobe1, ChannelStrobe1Steptime, ChannelStrobe1Darkstep, 1368))
eventDict['time'].append(EffectSequencedLightStrobe(At(startTime), BottomController, EffectStrobe2, ChannelStrobe2Steptime, ChannelStrobe2Darkstep, 1324))

eventDict['time'].append(ChannelSetStatic(At(startTime), BottomController, ChannelStrobe1Darkstep, 0))
eventDict['time'].append(ChannelSetStatic(At(startTime), TopController, ChannelStrobe1Darkstep, 0))

eventDict['time'].append(ChannelSetStatic(At(startTime), BottomController, ChannelStrobe2Darkstep, 1))

eventDict['time'].append(ChannelAddEffect(At(startTime), BottomController, Channel1, EffectStrobe1, 0))
eventDict['time'].append(ChannelAddEffect(At(startTime), BottomController, Channel2, EffectStrobe2, 0))
eventDict['time'].append(LightSetChannel(At(startTime), BottomController, [Light1, Light3], Channel1))
eventDict['time'].append(LightSetChannel(At(startTime), BottomController, [Light2, Light4], Channel2))

eventDict['time'].append(ChannelAddEffect(At(startTime), TopController, Channel2, EffectStrobe1, 0))
eventDict['time'].append(LightSetChannel(At(startTime), TopController, [Light2, Light4], Channel2))

# eventDict['time'].append(ChannelAddEffect(At(startTime), BottomController, Channel1, EffectSubtractPercentageVibrato, 1))
# eventDict['time'].append(ChannelAddEffect(At(startTime), BottomController, Channel2, EffectSubtractPercentageVibrato, 1))
eventDict['time'].append(ChannelAddEffect(At(startTime), TopController, Channel2, EffectSubtractPercentageVibrato, 1))



# STATE SUMMARY
# 
# TOP                               | BOTTOM
#                                   |
# Settings                          | Settings
# --------------------------------- | ---------------------------------
#   Setting1:            0          |   Setting1:            0
#   Setting2:            0          |   Setting2:            0
#   Setting3:            0          |   Setting3:            0
#   Setting4:            0          |   Setting4:            0
#
#   SettingVibrato:     0 to 100    |   SettingVibrato:     0 to 100
#   SettingPerlin:      0 to 100    |   SettingPerlin:      0 to 100
#
# Static Channels                   | Static Channels
# --------------------------------- | ---------------------------------
#   ChannelStrobe1Steptime: 34      |   ChannelStrobe1Steptime: 34
#   ChannelStrobe1Darkstep: 0       |   ChannelStrobe1Darkstep: 0
#   ChannelStrobe2Steptime: 34      |   ChannelStrobe2Steptime: 34
#   ChannelStrobe2Darkstep: 1       |   ChannelStrobe2Darkstep: 1
#
#   ChannelVibratoSteptime: 17      |   ChannelVibratoSteptime: 17
#   ChannelPerlinSteptime:  5       |   ChannelPerlinSteptime:  5
#
# Effects                           | Effects
# --------------------------------- | ---------------------------------
#   EffectStrobe1:        1368      |   EffectStrobe1:        1368
#   EffectStrobe2:        6363      |   EffectStrobe2:        1324
#
# Light Channels                    | Light Channels
# --------------------------------- | ---------------------------------
#   Channel1: Setting1, [Perlin, ]  |   Channel1: Setting1, [Strobe1,]
#   Channel2: Setting2, [Strobe1, ] |   Channel2: Setting2, [Strobe2,]
#   Channel3: Setting3, []          |   Channel3: Setting3, [Strobe2, ]
#   Channel4: Setting4, []          |   Channel4: Setting4, [Strobe1, ]

# 301 - 316
# Direction Change
# Gradually accelarte to 80
# 301: 40

#302 - 314 Finer Strobe Fades In
startTime = beginning + 304
dimmduration = 10
eventDict['time'].append(SettingBezierDimm(At(startTime), TopController, Setting2, 0, 95, int(dimmduration*1), 100, 0, 40))
eventDict['time'].append(SettingBezierDimm(At(startTime), BottomController, Setting1, 0, 95, int(dimmduration*1), 100, 0, 40))
eventDict['time'].append(SettingBezierDimm(At(startTime), TopController, Setting1, 40, 0, int(dimmduration*1), 100, 0, 40))


# 315.5:
# Direction Change
startTime = beginning + 315
# eventDict['time'].append(MotorDirection(At(startTime), MOTOR_CLOCKWISE))
# eventDict['time'].append(MotorSpeed(At(startTime), 90))

#316 Strobe Off
startTime = beginning + 316
eventDict['time'].append(SettingStatic(At(startTime), TopController, Setting2, 0))
eventDict['time'].append(SettingStatic(At(startTime), BottomController, Setting1, 0))

#316 Strobe On
startTime = beginning + 316.8
eventDict['time'].append(ChannelSetStatic(At(startTime), BottomController, ChannelStrobe1Darkstep, 1))
eventDict['time'].append(ChannelSetStatic(At(startTime), TopController, ChannelStrobe1Darkstep, 1))
eventDict['time'].append(SettingStatic(At(startTime), TopController, Setting2, 95))
eventDict['time'].append(SettingStatic(At(startTime), BottomController, Setting1, 95))

# 331:
# Direction Change
startTime = beginning + 330.5
# eventDict['time'].append(MotorDirection(At(startTime), MOTOR_COUNTERCLOCKWISE))
# eventDict['time'].append(MotorSpeed(At(startTime), 110))

# 331: Silence with eerie sound
startTime = beginning + 332
eventDict['time'].append(SettingStatic(At(startTime), TopController, Setting2, 0))
eventDict['time'].append(SettingStatic(At(startTime), BottomController, Setting1, 0))
dimmduration = 1.5
eventDict['time'].append(SettingBezierDimm(At(startTime), TopController, Setting1, 0, 95, int(dimmduration*1), 100, 90, 90))
eventDict['time'].append(LightSetChannel(At(startTime), BottomController, [Light1, Light2, Light3, Light4], Channel2))

# 333: Blast Strobe
startTime = beginning + 333.8
eventDict['time'].append(SettingStatic(At(startTime), TopController, Setting1, 0))
eventDict['time'].append(SettingStatic(At(startTime), BottomController, Setting2, 95))

#345.5 Fadeout, only tinitus remains
startTime = beginning + 345.9
eventDict['time'].append(SettingStatic(At(startTime), BottomController, Setting2, 0))
dimmduration = 3.5
eventDict['time'].append(SettingBezierDimm(At(startTime), TopController, Setting1, 95, 35, int(dimmduration*1), 100, 20, 100))



# 354:
# Motor Off
startTime = beginning + 354
# eventDict['time'].append(MotorSpeed(At(startTime), 0))
# eventDict['time'].append(MotorDirection(At(startTime), MOTOR_CLOCKWISE))


startTime = startTime + 2

eventDict['time'].append(SettingStatic(At(startTime), BottomController, Setting4, 0))




eventDict['time'] = sorted(eventDict['time'], key=lambda x: x.condition.value, reverse=False)

vd = VisualDriver(eventDict, music=music, usesMotor=False, startTime=298, isTake=False)
vd.start()