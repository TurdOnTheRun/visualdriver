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

EffectStrobe1 = 0
EffectStrobe2 = 1
EffectSubtractPercentageVibrato = 2
EffectSubtractPercentagePerlin = 3

# Bottom Setup
eventDict['time'].append(SettingStatic(At(0), BottomController, Setting1, 0))
eventDict['time'].append(SettingStatic(At(0), BottomController, Setting2, 0))
eventDict['time'].append(SettingStatic(At(0), BottomController, Setting3, 0))
eventDict['time'].append(SettingStatic(At(0), BottomController, Setting4, 0))
eventDict['time'].append(SettingSinWave(At(0), BottomController, SettingVibrato, StaticChannel0, StaticChannel100, ChannelVibratoSteptime, StaticChannel0))
eventDict['time'].append(SettingPerlinNoise(At(0), BottomController, SettingPerlin, StaticChannel0, StaticChannel100, ChannelPerlinSteptime, StaticChannel0))


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

eventDict['time'].append(EffectSequencedLightStrobe(At(0), BottomController, EffectStrobe1, ChannelStrobe1Steptime, ChannelStrobe1Darkstep, 1324))
eventDict['time'].append(EffectSequencedLightStrobe(At(0), BottomController, EffectStrobe2, ChannelStrobe2Steptime, ChannelStrobe2Darkstep, 1324))

eventDict['time'].append(EffectSubtractPercentage(At(0), BottomController, EffectSubtractPercentageVibrato, ChannelVibrato))
eventDict['time'].append(EffectSubtractPercentage(At(0), BottomController, EffectSubtractPercentagePerlin, ChannelPerlin))


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

eventDict['time'].append(EffectSequencedLightStrobe(At(0), TopController, EffectStrobe1, ChannelStrobe1Steptime, ChannelStrobe1Darkstep, 1324))
eventDict['time'].append(EffectSequencedLightStrobe(At(0), TopController, EffectStrobe2, ChannelStrobe2Steptime, ChannelStrobe2Darkstep, 1324))

eventDict['time'].append(EffectSubtractPercentage(At(0), TopController, EffectSubtractPercentageVibrato, ChannelVibrato))
eventDict['time'].append(EffectSubtractPercentage(At(0), TopController, EffectSubtractPercentagePerlin, ChannelPerlin))


eventDict['time'].append(LightSetChannel(At(0), TopController, [Light1,], Channel1))
eventDict['time'].append(LightSetChannel(At(0), TopController, [Light2,], Channel2))
eventDict['time'].append(LightSetChannel(At(0), TopController, [Light3,], Channel3))
eventDict['time'].append(LightSetChannel(At(0), TopController, [Light4,], Channel4))

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
# Setup
startTime = beginning + 0.5

eventDict['time'].append(ChannelSetStatic(At(startTime), TopController, ChannelStrobe1Darkstep, 1))
eventDict['time'].append(ChannelSetStatic(At(startTime), BottomController, ChannelStrobe1Darkstep, 1))
eventDict['time'].append(EffectSequencedLightStrobe(At(startTime), TopController, EffectStrobe1, ChannelStrobe1Steptime, ChannelStrobe1Darkstep, 1616))
eventDict['time'].append(EffectSequencedLightStrobe(At(startTime), BottomController, EffectStrobe1, ChannelStrobe1Steptime, ChannelStrobe1Darkstep, 1616))
eventDict['time'].append(EffectSequencedLightStrobe(At(startTime), BottomController, EffectStrobe2, ChannelStrobe2Steptime, ChannelStrobe2Darkstep, 1212))

eventDict['time'].append(ChannelAddEffect(At(startTime), BottomController, Channel1, EffectStrobe2, 0))
eventDict['time'].append(ChannelAddEffect(At(startTime), BottomController, Channel2, EffectStrobe2, 0))

eventDict['time'].append(ChannelSetStatic(At(startTime), BottomController, ChannelStrobe2Darkstep, 1))


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

eventDict['time'].append(SettingBezierDimm(At(startTime), TopController, Setting2, 0, 100, int(dimmduration*10), 10, 0, 100))


# 3.83
# Darkstep Off
startTime = beginning + 3.83
dimmduration = 0.2
eventDict['time'].append(SettingBezierDimm(At(startTime), TopController, Setting2, 100, 0, int(dimmduration*10), 10, 0, 100))
eventDict['time'].append(ChannelAddEffect(At(startTime), BottomController, Channel1, EffectStrobe2, 0))



# 3.83 - 5.23
# Fade Out
startTime = beginning + 3.83
dimmduration = 2.4
eventDict['time'].append(SettingBezierDimm(At(startTime), BottomController, Setting1, 100, 0, int(dimmduration*10), 10, 0, 100))
eventDict['time'].append(SettingBezierDimm(At(startTime), BottomController, Setting2, 100, 0, int(dimmduration*10), 10, 0, 100))

# 5.26
# Piano with Release until 6.71
startTime = beginning + 5.26
fadeOutLength = 1.5
# sustainSteptime 0
sustainSteptime = 5
eventDict['time'].append(SettingImpulseToBezierFadeout(At(startTime), BottomController, Setting4, 100, 1, 40, sustainSteptime, int(fadeOutLength*10), 10, 100, 100))


# 6.3
# Darkstep On
startTime = beginning + 6.3
eventDict['time'].append(ChannelAddEffect(At(startTime), BottomController, Channel1, EffectStrobe1, 0))

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


# 7.5
# Darkstep Off
startTime = beginning + 7.5
eventDict['time'].append(ChannelAddEffect(At(startTime), BottomController, Channel1, EffectStrobe2, 0))

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
fadeOutLength = 3
# sustainSteptime 0
sustainSteptime = 5
eventDict['time'].append(SettingImpulseToBezierFadeout(At(startTime), BottomController, Setting4, 65, 1, 30, sustainSteptime, int(fadeOutLength*10), 10, 100, 100))


# 11.09
# Top Soft-Piano with release until 12.08
startTime = beginning + 11.09
fadeOutLength = 1.8
# sustainSteptime 0
sustainSteptime = 5
eventDict['time'].append(SettingImpulseToBezierFadeout(At(startTime), TopController, Setting4, 65, 1, 30, sustainSteptime, int(fadeOutLength*10), 10, 100, 100))


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
eventDict['time'].append(SettingBezierDimm(At(startTime), BottomController, Setting1, 0, 40, int(dimmduration*10), 10, 0, 100))
eventDict['time'].append(SettingBezierDimm(At(startTime), TopController, Setting2, 0, 40, int(dimmduration*10), 10, 0, 100))
startTime = startTime + dimmduration
dimmduration = 0.45
eventDict['time'].append(SettingBezierDimm(At(startTime), BottomController, Setting1, 40, 0, int(dimmduration*10), 10, 0, 100))
eventDict['time'].append(SettingBezierDimm(At(startTime), TopController, Setting2, 40, 0, int(dimmduration*10), 10, 0, 100))

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
fadeOutLength = 1.6
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
dimmduration = 3
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
fadeOutLength = 4.8
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
fadeOutLength = 7.8
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
fadeOutLength = 0.1
# sustainSteptime 0
sustainSteptime = 5
eventDict['time'].append(SettingImpulseToBezierFadeout(At(startTime), TopController, Setting4, 95, 1, 40, sustainSteptime, int(fadeOutLength*10), 10, 90, 100))


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
# Bremsfactor 0.0856
# eventDict['position'].append(MotorSpeed(GE(3.25 - 0.0856), 0))

# 42.12 - 42
# Strong Left Darkstep Wave
startTime = beginning + 42.12
dimmduration = 0.6
eventDict['time'].append(SettingBezierDimm(At(startTime), BottomController, Setting1, 0, 80, int(dimmduration*10), 10, 0, 100))
eventDict['time'].append(SettingBezierDimm(At(startTime), TopController, Setting2, 0, 80, int(dimmduration*10), 10, 0, 100))
startTime = startTime + dimmduration
dimmduration = 0.2
eventDict['time'].append(SettingBezierDimm(At(startTime), BottomController, Setting1, 80, 0, int(dimmduration*10), 10, 0, 100))
eventDict['time'].append(SettingBezierDimm(At(startTime), TopController, Setting2, 80, 0, int(dimmduration*10), 10, 0, 100))


# Part II
# 44
# explosion
startTime = beginning + 44
fadeOutLength = 0.2
sustainSteptime = 5
eventDict['time'].append(SettingImpulseToBezierFadeout(At(startTime), BottomController, Setting1, 100, 1, 99, sustainSteptime, int(fadeOutLength*10), 10, 90, 100))
eventDict['time'].append(SettingImpulseToBezierFadeout(At(startTime), BottomController, Setting3, 100, 1, 99, sustainSteptime, int(fadeOutLength*10), 10, 90, 100))


# explosion end
startTime = beginning + 44.1

eventDict['time'].append(ChannelSetStatic(At(startTime), TopController, ChannelStrobe1Steptime, 67))
eventDict['time'].append(ChannelSetStatic(At(startTime), BottomController, ChannelStrobe1Steptime, 67))


eventDict['time'].append(EffectSequencedLightStrobe(At(startTime), TopController, EffectStrobe1, ChannelStrobe1Steptime, ChannelStrobe1Darkstep, 1537))
eventDict['time'].append(EffectSequencedLightStrobe(At(startTime), BottomController, EffectStrobe1, ChannelStrobe1Steptime, ChannelStrobe1Darkstep, 1537))

eventDict['time'].append(ChannelRemoveEffect(At(startTime), BottomController, Channel2, 0))
eventDict['time'].append(ChannelAddEffect(At(startTime), BottomController, Channel1, EffectStrobe1, 0))
eventDict['time'].append(ChannelAddEffect(At(startTime), BottomController, Channel3, EffectStrobe1, 0))
eventDict['time'].append(ChannelAddEffect(At(startTime), TopController, Channel1, EffectStrobe1, 0))
eventDict['time'].append(ChannelAddEffect(At(startTime), TopController, Channel3, EffectStrobe1, 0))

#Setup of Flut and Ebbe from jeweilige Top position
eventDict['time'].append(ChannelRemoveEffect(At(startTime), TopController, Channel2, 0))
eventDict['time'].append(ChannelRemoveEffect(At(startTime), TopController, Channel4, 0))
eventDict['time'].append(EffectSequencedLightStrobe(At(startTime), TopController, EffectStrobe2, ChannelStrobe2Steptime, ChannelStrobe2Darkstep, 2626))
eventDict['time'].append(ChannelAddEffect(At(startTime), TopController, Channel2, EffectStrobe2, 0))



# 44-48
# Strobe Fade In
startTime = beginning + 44.1
dimmduration = 4
eventDict['time'].append(SettingBezierDimm(At(startTime), TopController, Setting1, 0, 100, int(dimmduration*10), 10, 0, 100))
eventDict['time'].append(SettingBezierDimm(At(startTime), TopController, Setting3, 0, 100, int(dimmduration*10), 10, 0, 100))
eventDict['time'].append(SettingBezierDimm(At(startTime), BottomController, Setting1, 0, 100, int(dimmduration*10), 10, 0, 100))
eventDict['time'].append(SettingBezierDimm(At(startTime), BottomController, Setting3, 0, 100, int(dimmduration*10), 10, 0, 100))


# 79.5-82.5
# Strobe Fade Out
startTime = beginning + 79.5
dimmduration = 3
eventDict['time'].append(SettingBezierDimm(At(startTime), TopController, Setting1, 100, 0, int(dimmduration*10), 10, 0, 100))
eventDict['time'].append(SettingBezierDimm(At(startTime), TopController, Setting2, 100, 0, int(dimmduration*10), 10, 0, 100))
eventDict['time'].append(SettingBezierDimm(At(startTime), TopController, Setting3, 100, 0, int(dimmduration*10), 10, 0, 100))
eventDict['time'].append(SettingBezierDimm(At(startTime), TopController, Setting4, 100, 0, int(dimmduration*10), 10, 0, 100))
eventDict['time'].append(SettingBezierDimm(At(startTime), BottomController, Setting1, 100, 0, int(dimmduration*10), 10, 0, 100))
eventDict['time'].append(SettingBezierDimm(At(startTime), BottomController, Setting3, 100, 0, int(dimmduration*10), 10, 0, 100))

# 81-87.9
# Tinitus
startTime = beginning + 81
dimmduration = 7
eventDict['time'].append(ChannelRemoveEffect(At(startTime), TopController, Channel3, 0))
eventDict['time'].append(SettingBezierDimm(At(startTime), TopController, Setting3, 0, 95, int(dimmduration*10), 10, 0, 100))


# 82.5
# Remove Effects
startTime = beginning + 82.5
eventDict['time'].append(ChannelRemoveEffect(At(startTime), BottomController, Channel1, 0))
eventDict['time'].append(ChannelRemoveEffect(At(startTime), BottomController, Channel3, 0))
eventDict['time'].append(ChannelRemoveEffect(At(startTime), TopController, Channel1, 0))
eventDict['time'].append(ChannelRemoveEffect(At(startTime), TopController, Channel2, 0))
eventDict['time'].append(ChannelRemoveEffect(At(startTime), TopController, Channel4, 0))



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
eventDict['time'].append(ChannelAddEffect(At(startTime), BottomController, Channel1, EffectStrobe1, 0))
eventDict['time'].append(ChannelAddEffect(At(startTime), BottomController, Channel3, EffectStrobe1, 0))

# Top
eventDict['time'].append(ChannelAddEffect(At(startTime), TopController, Channel4, EffectSubtractPercentageVibrato, 0))
# We need a strobe only on 3 (aka 7 as global)
eventDict['time'].append(EffectSequencedLightStrobe(At(startTime), TopController, EffectStrobe1, ChannelStrobe1Steptime, ChannelStrobe1Darkstep, 5757))



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
eventDict['time'].append(SettingBezierDimm(At(startTime), BottomController, Setting3, 0, 100, int(dimmduration*20), 5, 0, 100))
startTime = startTime + dimmduration
dimmduration = 0.75
eventDict['time'].append(SettingBezierDimm(At(startTime), BottomController, Setting3, 100, 0, int(dimmduration*20), 5, 0, 100))

# 22
# Top Vibrato Faster Again
startTime = beginning + 22
eventDict['time'].append(ChannelSetStatic(At(startTime), TopController, ChannelVibratoSteptime, 9))


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
eventDict['time'].append(SettingBezierDimm(At(startTime), BottomController, Setting1, 70, 100, int(dimmduration*20), 5, 0, 100))
eventDict['time'].append(SettingBezierDimm(At(startTime), BottomController, Setting3, 70, 100, int(dimmduration*20), 5, 0, 100))

# 29.3
# Darkstep Off
startTime = beginning + 29.3
eventDict['time'].append(ChannelSetStatic(At(startTime), BottomController, ChannelStrobe1Darkstep, 0))

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
# Bremsfactor 0.074
# eventDict['position'].append(MotorSpeed(LE(2.75 + 0.074), 0))


# Setup Ebbe
ebbemove = 5.43
# 50
startTime = beginning + 50 + ebbemove
eventDict['time'].append(ChannelRemoveEffect(At(startTime), BottomController, Channel1, 0))
eventDict['time'].append(ChannelRemoveEffect(At(startTime), BottomController, Channel3, 0))
startTime = beginning + 50
dimmduration = 3.5
eventDict['time'].append(SettingBezierDimm(At(startTime), TopController, Setting4, 100, 0, int(dimmduration*20), 5, 0, 100))

eventDict['time'].append(ChannelAddEffect(At(startTime), TopController, Channel2, EffectSubtractPercentagePerlin, 0))

# sustainSteptime 
sustainSteptime = 5
fadeOutLength = 2
eventDict['time'].append(SettingImpulseToBezierFadeout(At(startTime), BottomController, Setting3, 70, 1, 20, sustainSteptime, int(fadeOutLength*10), 10, 0, 100))



startTime = beginning + 50.58 + ebbemove
# sustainSteptime 
sustainSteptime = 5
fadeOutLength = 2
eventDict['time'].append(SettingImpulseToBezierFadeout(At(startTime), TopController, Setting4, 100, 1, 40, sustainSteptime, int(fadeOutLength*10), 10, 100, 100))




# 52
# Top

startTime = beginning + 52 + ebbemove
fadeOutLength = 2.8
eventDict['time'].append(ChannelRemoveEffect(At(startTime), TopController, Channel4, 0))

# sustainSteptime 
sustainSteptime = 5
eventDict['time'].append(SettingImpulseToBezierFadeout(At(startTime), TopController, Setting4, 100, 1, 40, sustainSteptime, int(fadeOutLength*10), 10, 100, 100))


# 53
# Right
startTime = beginning + 53 + ebbemove
fadeOutLength = 2.8
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
fadeOutLength = 2.8
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
fadeOutLength = 2.8
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
eventDict['time'].append(SettingImpulseToBezierFadeout(At(startTime), BottomController, Setting3, 100, 1, 40, sustainSteptime, int(fadeOutLength*10), 10, 100, 100))

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
fadeOutLength = 2.8
# sustainSteptime 
sustainSteptime = 5
eventDict['time'].append(SettingImpulseToBezierFadeout(At(startTime), BottomController, Setting3, 100, 1, 40, sustainSteptime, int(fadeOutLength*10), 10, 100, 100))


# 78.9
# Light Left
startTime = beginning + 78.9 + ebbemove
fadeOutLength = 2.8
# sustainSteptime 
sustainSteptime = 4
eventDict['time'].append(SettingImpulseToBezierFadeout(At(startTime), BottomController, Setting1, 80, 1, 30, sustainSteptime, int(fadeOutLength*10), 10, 100, 100))


# 80.13
# Super Light Right
startTime = beginning + 80.13 + ebbemove
fadeOutLength = 2.8
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
startTime = beginning + 91.8 + ebbemove
fadeOutLength = 2.8
# sustainSteptime 
sustainSteptime = 5
eventDict['time'].append(SettingImpulseToBezierFadeout(At(startTime), BottomController, Setting1, 100, 1, 40, sustainSteptime, int(fadeOutLength*10), 10, 100, 100))

# 93.5
# Top
startTime = beginning + 93 + ebbemove
fadeOutLength = 2.8
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
startTime = beginning + 96.25 + ebbemove
fadeOutLength = 2.8
# sustainSteptime 
sustainSteptime = 5
eventDict['time'].append(SettingImpulseToBezierFadeout(At(startTime), BottomController, Setting1, 60, 1, 15, sustainSteptime, int(fadeOutLength*10), 10, 100, 100))

# 96.5
# Super Ligth Right
startTime = beginning + 96.5 + ebbemove
fadeOutLength = 2.8
# sustainSteptime 
sustainSteptime = 3
eventDict['time'].append(SettingImpulseToBezierFadeout(At(startTime), BottomController, Setting3, 60, 1, 15, sustainSteptime, int(fadeOutLength*10), 10, 100, 100))


# 106 - 109
# Aura Fade OUt
startTime = beginning + 106 + ebbemove
dimmduration = 3
eventDict['time'].append(SettingBezierDimm(At(startTime), TopController, Setting2, 100, 0, int(dimmduration*10), 10, 0, 100))


# 196
# Start Part IV
# Setup
beginning = originalBeginning
startTime = beginning + 196

loopPianofadeOutLength = 0.3
loopPianosustainSteptime = 3

eventDict['time'].append(EffectSequencedLightStrobe(At(startTime), BottomController, EffectStrobe1, ChannelStrobe1Steptime, ChannelStrobe1Darkstep, 2424))
eventDict['time'].append(ChannelAddEffect(At(startTime), BottomController, Channel2, EffectStrobe1, 0))
eventDict['time'].append(ChannelAddEffect(At(startTime), BottomController, Channel4, EffectStrobe1, 0))
# eventDict['time'].append(MotorSpeed(At(startTime), 10))

startTime = beginning + 197
# eventDict['time'].append(MotorSpeed(At(startTime), 20))

startTime = beginning + 198
# eventDict['time'].append(MotorSpeed(At(startTime), 30))

startTime = beginning + 198
# eventDict['time'].append(MotorSpeed(At(startTime), 45))

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
eventDict['time'].append(LightSetChannel(At(startTime), TopController, [Light1,Light3], Channel1))
eventDict['time'].append(LightSetChannel(At(startTime), TopController, [Light2,Light4], Channel2))
eventDict['time'].append(ChannelSetStatic(At(startTime), TopController, ChannelStrobe1Steptime, 100))
eventDict['time'].append(ChannelSetStatic(At(startTime), TopController, ChannelStrobe1Darkstep, 0))
eventDict['time'].append(EffectSequencedLightStrobe(At(startTime), TopController, EffectStrobe1, ChannelStrobe1Steptime, ChannelStrobe1Darkstep, 6868))
eventDict['time'].append(ChannelAddEffect(At(startTime), TopController, Channel2, EffectStrobe1, 0))
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
startTime = beginning + 198.71
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

# 212.98
# Chord
startTime = beginning + 212.98
fadeOutLength = 1.8
# sustainSteptime 
sustainSteptime = 5
eventDict['time'].append(SettingImpulseToBezierFadeout(At(startTime), TopController, Setting1, 100, 1, 40, sustainSteptime, int(fadeOutLength*10), 10, 100, 100))
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


# 216.96
# Pulsating Appears Lightly
startTime = beginning + 216.96
dimmduration = 1
eventDict['time'].append(SettingBezierDimm(At(startTime), TopController, Setting2, 0, 60, int(dimmduration*10), 10, 0, 100))

# 220.91
# Chord
startTime = beginning + 220.91
fadeOutLength = 1.8
# sustainSteptime 
sustainSteptime = 5
eventDict['time'].append(SettingImpulseToBezierFadeout(At(startTime), TopController, Setting1, 100, 1, 40, sustainSteptime, int(fadeOutLength*10), 10, 100, 100))
# eventDict['time'].append(MotorSpeed(At(startTime), 70))


# 224.91
# Chord
startTime = beginning + 224.91
fadeOutLength = 1.8
# sustainSteptime 
sustainSteptime = 5
eventDict['time'].append(SettingImpulseToBezierFadeout(At(startTime), TopController, Setting1, 100, 1, 40, sustainSteptime, int(fadeOutLength*10), 10, 100, 100))



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



# 232.95
# Chord
startTime = beginning + 232.95
fadeOutLength = 1.8
# sustainSteptime 
sustainSteptime = 3
eventDict['time'].append(SettingImpulseToBezierFadeout(At(startTime), TopController, Setting1, 100, 1, 40, sustainSteptime, int(fadeOutLength*10), 10, 100, 100))



# 236.93
# Soft Chord
startTime = beginning + 236.93
fadeOutLength = 1.8
# sustainSteptime 
sustainSteptime = 5
eventDict['time'].append(SettingImpulseToBezierFadeout(At(startTime), TopController, Setting1, 80, 1, 30, sustainSteptime, int(fadeOutLength*10), 10, 100, 100))


# 240.95
# Soft Chord
startTime = beginning + 240.95
fadeOutLength = 1.8
# sustainSteptime 
sustainSteptime = 5
eventDict['time'].append(SettingImpulseToBezierFadeout(At(startTime), TopController, Setting1, 80, 1, 30, sustainSteptime, int(fadeOutLength*10), 10, 100, 100))
# eventDict['time'].append(MotorSpeed(At(startTime), 90))


# 244.89
# Chord
startTime = beginning + 244.89
fadeOutLength = 1.8
# sustainSteptime 
sustainSteptime = 5
eventDict['time'].append(SettingImpulseToBezierFadeout(At(startTime), TopController, Setting1, 80, 1, 30, sustainSteptime, int(fadeOutLength*10), 10, 100, 100))
# eventDict['time'].append(MotorSpeed(At(startTime), 100))


# 244.89 - 247.91
# Wave
# Strobe from left and right
startTime = beginning + 244.89
dimmduration = 1.5
eventDict['time'].append(SettingBezierDimm(At(startTime), BottomController, Setting2, 0, 80, int(dimmduration*10), 10, 0, 100))
eventDict['time'].append(SettingBezierDimm(At(startTime), BottomController, Setting4, 0, 80, int(dimmduration*10), 10, 0, 100))
startTime = startTime + dimmduration
eventDict['time'].append(SettingBezierDimm(At(startTime), BottomController, Setting2, 80, 0, int(dimmduration*10), 10, 0, 100))
eventDict['time'].append(SettingBezierDimm(At(startTime), BottomController, Setting4, 80, 0, int(dimmduration*10), 10, 0, 100))

# 246.6 - 250.65
# Pulsating becomes full on intense
startTime = beginning + 246.6
dimmduration = 4
eventDict['time'].append(SettingBezierDimm(At(startTime), TopController, Setting2, 60, 95, int(dimmduration*10), 10, 0, 100))

# 248
startTime = beginning + 248
# eventDict['time'].append(MotorSpeed(At(startTime), 110))

# 254.45 - 257.34
# Fade In Strobe from left and right
startTime = beginning + 246.6
dimmduration = 3
eventDict['time'].append(SettingBezierDimm(At(startTime), BottomController, Setting2, 0, 90, int(dimmduration*10), 10, 0, 100))
eventDict['time'].append(SettingBezierDimm(At(startTime), BottomController, Setting4, 0, 90, int(dimmduration*10), 10, 0, 100))


# 257.34 = 260.45
# Fade Out Strobe from left and right
startTime = beginning + 257.34
dimmduration = 3
eventDict['time'].append(SettingBezierDimm(At(startTime), BottomController, Setting2, 90, 0, int(dimmduration*10), 10, 0, 100))
eventDict['time'].append(SettingBezierDimm(At(startTime), BottomController, Setting4, 90, 0, int(dimmduration*10), 10, 0, 100))

# 260.95 - 262.4
# Wave Strobe from left and right
startTime = beginning + 260.95
dimmduration = 0.25
eventDict['time'].append(SettingBezierDimm(At(startTime), BottomController, Setting2, 0, 80, int(dimmduration*10), 10, 0, 100))
eventDict['time'].append(SettingBezierDimm(At(startTime), BottomController, Setting4, 0, 80, int(dimmduration*10), 10, 0, 100))
startTime = startTime + dimmduration
eventDict['time'].append(SettingBezierDimm(At(startTime), BottomController, Setting2, 80, 0, int(dimmduration*10), 10, 0, 100))
eventDict['time'].append(SettingBezierDimm(At(startTime), BottomController, Setting4, 80, 0, int(dimmduration*10), 10, 0, 100))

# 262.44-263.4
# Fade In Strobe from left and right
startTime = beginning + 262.44
dimmduration = 1
eventDict['time'].append(SettingBezierDimm(At(startTime), BottomController, Setting2, 0, 60, int(dimmduration*10), 10, 0, 100))
eventDict['time'].append(SettingBezierDimm(At(startTime), BottomController, Setting4, 0, 60, int(dimmduration*10), 10, 0, 100))

# 264.65 - 268.14
# Fade Out Strobe from left and right
startTime = beginning + 264.65
dimmduration = 3.5
eventDict['time'].append(SettingBezierDimm(At(startTime), BottomController, Setting2, 60, 0, int(dimmduration*10), 10, 0, 100))
eventDict['time'].append(SettingBezierDimm(At(startTime), BottomController, Setting4, 60, 0, int(dimmduration*10), 10, 0, 100))
# eventDict['time'].append(MotorSpeed(At(startTime), 80))


# 268 - 279.54
# Fade Out Everything
startTime = beginning + 268
dimmduration = 10
eventDict['time'].append(SettingBezierDimm(At(startTime), TopController, Setting2, 95, 0, int(dimmduration*10), 10, 0, 100))
# eventDict['time'].append(MotorSpeed(At(startTime), 60))

# 270.27
# Piano Loop becomes every second 


# PART V
# Breakfactor: 0.0625
# eventDict['position'].append(MotorSpeed(LE(-1.5 + 0.0625), 0))


# 276
# Random Light for Ending
startTime = beginning + 276
dimmduration = 3.5
eventDict['time'].append(SettingBezierDimm(At(startTime), BottomController, Setting2, 0, 90, int(dimmduration*10), 10, 0, 100))
eventDict['time'].append(SettingBezierDimm(At(startTime), BottomController, Setting4, 0, 90, int(dimmduration*10), 10, 0, 100))

# 301 - 316
# Direction Change
# Gradually accelarte to 80
# 301: 40

startTime = beginning + 301

# 315.5:
# Direction Change
startTime = beginning + 315
# eventDict['time'].append(MotorDirection(At(startTime), MOTOR_CLOCKWISE))
# eventDict['time'].append(MotorSpeed(At(startTime), 90))

# 331:
# Direction Change
startTime = beginning + 330.5
# eventDict['time'].append(MotorDirection(At(startTime), MOTOR_COUNTERCLOCKWISE))
# eventDict['time'].append(MotorSpeed(At(startTime), 110))

# 354:
# Motor Off
startTime = beginning + 354
# eventDict['time'].append(MotorSpeed(At(startTime), 0))
# eventDict['time'].append(MotorDirection(At(startTime), MOTOR_CLOCKWISE))


startTime = startTime + 2

eventDict['time'].append(SettingStatic(At(startTime), BottomController, Setting4, 0))




eventDict['time'] = sorted(eventDict['time'], key=lambda x: x.condition.value, reverse=False)

vd = VisualDriver(eventDict, music=music, usesMotor=True, startTime=0, isTake=False)
vd.start()