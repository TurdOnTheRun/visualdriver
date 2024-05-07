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

music = '/home/maximilian/music/flutebbe/20240507_full.mp3'


beginning = 0

# BOTTOM VARIABLES
BottomSetting1 = 0
BottomSetting2 = 1
BottomSetting3 = 2
BottomSetting4 = 3
BottomSettingVibrato = 4
BottomSettingPerlin = 5


BottomChannel1 = Channel8
BottomChannel2 = Channel9
BottomChannel3 = Channel10
BottomChannel4 = Channel11
BottomChannelStrobe1Steptime = Channel12
BottomChannelStrobe1Darkstep = Channel13
BottomChannelStrobe2Steptime = Channel14
BottomChannelStrobe2Darkstep = Channel15
BottomChannelVibratoSteptime = Channel16
BottomChannelVibrato = Channel17
BottomChannelPerlinSteptime = Channel18
BottomChannelPerlin = Channel19

BottomEffectStrobe1 = 0
BottomEffectStrobe2 = 1
BottomEffectSubtractPercentageVibrato = 2
BottomEffectSubtractPercentagePerlin = 3

# Bottom Setup
eventDict['time'].append(SettingStatic(At(0), BottomController, BottomSetting1, 0))
eventDict['time'].append(SettingStatic(At(0), BottomController, BottomSetting2, 0))
eventDict['time'].append(SettingStatic(At(0), BottomController, BottomSetting3, 0))
eventDict['time'].append(SettingStatic(At(0), BottomController, BottomSetting4, 0))
eventDict['time'].append(SettingSinWave(At(0), BottomController, BottomSettingVibrato, StaticChannel0, StaticChannel100, BottomChannelVibratoSteptime, StaticChannel0))
eventDict['time'].append(SettingPerlinNoise(At(0), BottomController, BottomSettingPerlin, StaticChannel0, StaticChannel100, BottomChannelPerlinSteptime, StaticChannel0))


eventDict['time'].append(ChannelSetSetting(At(0), BottomController, BottomChannel1, BottomSetting1))
eventDict['time'].append(ChannelSetSetting(At(0), BottomController, BottomChannel2, BottomSetting2))
eventDict['time'].append(ChannelSetSetting(At(0), BottomController, BottomChannel3, BottomSetting3))
eventDict['time'].append(ChannelSetSetting(At(0), BottomController, BottomChannel4, BottomSetting4))
eventDict['time'].append(ChannelSetStatic(At(0), BottomController, BottomChannelStrobe1Steptime, 34))
eventDict['time'].append(ChannelSetStatic(At(0), BottomController, BottomChannelStrobe1Darkstep, 0))
eventDict['time'].append(ChannelSetStatic(At(0), BottomController, BottomChannelStrobe2Steptime, 34))
eventDict['time'].append(ChannelSetStatic(At(0), BottomController, BottomChannelStrobe2Darkstep, 0))
eventDict['time'].append(ChannelSetStatic(At(0), BottomController, BottomChannelVibratoSteptime, 17))
eventDict['time'].append(ChannelSetSetting(At(0), BottomController, BottomChannelVibrato, BottomSettingVibrato))
eventDict['time'].append(ChannelSetStatic(At(0), BottomController, BottomChannelPerlinSteptime, 5))
eventDict['time'].append(ChannelSetSetting(At(0), BottomController, BottomChannelPerlin, BottomSettingPerlin))

eventDict['time'].append(EffectSequencedLightStrobe(At(0), BottomController, BottomEffectStrobe1, BottomChannelStrobe1Steptime, BottomChannelStrobe1Darkstep, 1324))
eventDict['time'].append(EffectSequencedLightStrobe(At(0), BottomController, BottomEffectStrobe2, BottomChannelStrobe2Steptime, BottomChannelStrobe2Darkstep, 1324))

eventDict['time'].append(EffectSubtractPercentage(At(0), BottomController, BottomEffectSubtractPercentageVibrato, BottomChannelVibrato))
eventDict['time'].append(EffectSubtractPercentage(At(0), BottomController, BottomEffectSubtractPercentagePerlin, BottomChannelPerlin))


eventDict['time'].append(LightSetChannel(At(0), BottomController, [Light1,], BottomChannel1))
eventDict['time'].append(LightSetChannel(At(0), BottomController, [Light2,], BottomChannel2))
eventDict['time'].append(LightSetChannel(At(0), BottomController, [Light3,], BottomChannel3))
eventDict['time'].append(LightSetChannel(At(0), BottomController, [Light4,], BottomChannel4))


# TOP VARIABLES
TopSetting1 = 0
TopSetting2 = 1
TopSetting3 = 2
TopSetting4 = 3
TopSettingVibrato = 4
TopSettingPerlin = 5


TopChannel1 = Channel8
TopChannel2 = Channel9
TopChannel3 = Channel10
TopChannel4 = Channel11
TopChannelStrobe1Steptime = Channel12
TopChannelStrobe1Darkstep = Channel13
TopChannelStrobe2Steptime = Channel14
TopChannelStrobe2Darkstep = Channel15
TopChannelVibratoSteptime = Channel16
TopChannelVibrato = Channel17
TopChannelPerlinSteptime = Channel18
TopChannelPerlin = Channel19

TopEffectStrobe1 = 0
TopEffectStrobe2 = 1
TopEffectSubtractPercentageVibrato = 2
TopEffectSubtractPercentagePerlin = 3

# Top Setup
eventDict['time'].append(SettingStatic(At(0), TopController, TopSetting1, 0))
eventDict['time'].append(SettingStatic(At(0), TopController, TopSetting2, 0))
eventDict['time'].append(SettingStatic(At(0), TopController, TopSetting3, 0))
eventDict['time'].append(SettingStatic(At(0), TopController, TopSetting4, 0))
eventDict['time'].append(SettingSinWave(At(0), TopController, TopSettingVibrato, StaticChannel0, StaticChannel100, TopChannelVibratoSteptime, StaticChannel0))
eventDict['time'].append(SettingPerlinNoise(At(0), TopController, TopSettingPerlin, StaticChannel0, StaticChannel100, TopChannelPerlinSteptime, StaticChannel0))


eventDict['time'].append(ChannelSetSetting(At(0), TopController, TopChannel1, TopSetting1))
eventDict['time'].append(ChannelSetSetting(At(0), TopController, TopChannel2, TopSetting2))
eventDict['time'].append(ChannelSetSetting(At(0), TopController, TopChannel3, TopSetting3))
eventDict['time'].append(ChannelSetSetting(At(0), TopController, TopChannel4, TopSetting4))
eventDict['time'].append(ChannelSetStatic(At(0), TopController, TopChannelStrobe1Steptime, 34))
eventDict['time'].append(ChannelSetStatic(At(0), TopController, TopChannelStrobe1Darkstep, 0))
eventDict['time'].append(ChannelSetStatic(At(0), TopController, TopChannelStrobe2Steptime, 34))
eventDict['time'].append(ChannelSetStatic(At(0), TopController, TopChannelStrobe2Darkstep, 0))
eventDict['time'].append(ChannelSetStatic(At(0), TopController, TopChannelVibratoSteptime, 17))
eventDict['time'].append(ChannelSetSetting(At(0), TopController, TopChannelVibrato, TopSettingVibrato))
eventDict['time'].append(ChannelSetStatic(At(0), TopController, TopChannelPerlinSteptime, 5))
eventDict['time'].append(ChannelSetSetting(At(0), TopController, TopChannelPerlin, TopSettingPerlin))

eventDict['time'].append(EffectSequencedLightStrobe(At(0), TopController, TopEffectStrobe1, TopChannelStrobe1Steptime, TopChannelStrobe1Darkstep, 1324))
eventDict['time'].append(EffectSequencedLightStrobe(At(0), TopController, TopEffectStrobe2, TopChannelStrobe2Steptime, TopChannelStrobe2Darkstep, 1324))

eventDict['time'].append(EffectSubtractPercentage(At(0), TopController, TopEffectSubtractPercentageVibrato, TopChannelVibrato))
eventDict['time'].append(EffectSubtractPercentage(At(0), TopController, TopEffectSubtractPercentagePerlin, TopChannelPerlin))


eventDict['time'].append(LightSetChannel(At(0), TopController, [Light1,], TopChannel1))
eventDict['time'].append(LightSetChannel(At(0), TopController, [Light2,], TopChannel2))
eventDict['time'].append(LightSetChannel(At(0), TopController, [Light3,], TopChannel3))
eventDict['time'].append(LightSetChannel(At(0), TopController, [Light4,], TopChannel4))


# SCRIPT
beginning = 3
eventDict['time'].append(MusicStart(At(beginning), 0))

# 0
# Explosion
# 0-1.2
# Explosion Fades away
startTime = beginning + 0
dimmduration = 1.2
eventDict['time'].append(SettingImpulseToBezierFadeout(At(startTime), TopController, TopSetting3, 100, 1, 20, 1, int(dimmduration*10), 10, 0, 100))
eventDict['time'].append(SettingImpulseToBezierFadeout(At(startTime), BottomController, BottomSetting1, 100, 1, 20, 1, int(dimmduration*10), 10, 0, 100))
eventDict['time'].append(SettingImpulseToBezierFadeout(At(startTime), BottomController, BottomSetting3, 100, 1, 20, 1, int(dimmduration*10), 10, 0, 100))

# 0.5
# Setup
startTime = beginning + 0.5

eventDict['time'].append(ChannelSetStatic(At(startTime), TopController, TopChannelStrobe1Darkstep, 1))
eventDict['time'].append(ChannelSetStatic(At(startTime), BottomController, TopChannelStrobe1Darkstep, 1))
eventDict['time'].append(EffectSequencedLightStrobe(At(startTime), TopController, TopEffectStrobe1, BottomChannelStrobe1Steptime, BottomChannelStrobe1Darkstep, 1616))
eventDict['time'].append(EffectSequencedLightStrobe(At(startTime), BottomController, BottomEffectStrobe1, BottomChannelStrobe1Steptime, BottomChannelStrobe1Darkstep, 1616))

eventDict['time'].append(EffectSequencedLightStrobe(At(startTime), BottomController, BottomEffectStrobe2, BottomChannelStrobe2Steptime, BottomChannelStrobe2Darkstep, 1212))

eventDict['time'].append(ChannelAddEffect(At(startTime), BottomController, BottomChannel1, BottomEffectStrobe2, 0))
eventDict['time'].append(ChannelAddEffect(At(startTime), BottomController, BottomChannel2, BottomEffectStrobe2, 0))

eventDict['time'].append(ChannelSetStatic(At(startTime), BottomController, TopChannelStrobe2Darkstep, 1))


# 0.6 - 2
# Left Strobe Fades In
startTime = beginning + 0.6
dimmduration = 1.4
eventDict['time'].append(SettingBezierDimm(At(startTime), BottomController, BottomSetting1, 0, 95, int(dimmduration*10), 10, 0, 100))
eventDict['time'].append(SettingBezierDimm(At(startTime), BottomController, BottomSetting2, 0, 95, int(dimmduration*10), 10, 0, 100))


# 2.51 - 3.31
# More Intense Strobe Fades In
startTime = beginning + 2.51
dimmduration = 0.8
eventDict['time'].append(ChannelAddEffect(At(startTime), BottomController, BottomChannel1, BottomEffectStrobe1, 0))
eventDict['time'].append(ChannelAddEffect(At(startTime), TopController, TopChannel2, TopEffectStrobe1, 0))

eventDict['time'].append(SettingBezierDimm(At(startTime), TopController, TopSetting2, 0, 95, int(dimmduration*10), 10, 0, 100))


# 3.83
# Darkstep Off
startTime = beginning + 3.83
dimmduration = 0.2
eventDict['time'].append(SettingBezierDimm(At(startTime), TopController, TopSetting2, 95, 0, int(dimmduration*10), 10, 0, 100))
eventDict['time'].append(ChannelAddEffect(At(startTime), BottomController, BottomChannel1, BottomEffectStrobe2, 0))



# 3.83 - 5.23
# Fade Out
startTime = beginning + 3.83
dimmduration = 1.4
eventDict['time'].append(SettingBezierDimm(At(startTime), BottomController, BottomSetting1, 95, 0, int(dimmduration*10), 10, 0, 100))
eventDict['time'].append(SettingBezierDimm(At(startTime), BottomController, BottomSetting2, 95, 0, int(dimmduration*10), 10, 0, 100))

# 5.26
# Piano with Release until 6.71
startTime = beginning + 5.26
fadeOutLength = 1.5
# sustainSteptime 0
sustainSteptime = 2
eventDict['time'].append(SettingImpulseToBezierFadeout(At(startTime), BottomController, BottomSetting4, 95, 1, 10, sustainSteptime, int(fadeOutLength*10), 10, 0, 100))



# 6.3
# Darkstep On
startTime = beginning + 6.3
eventDict['time'].append(ChannelAddEffect(At(startTime), BottomController, BottomChannel1, BottomEffectStrobe1, 0))

# 6.35 - 7.5
# Darkstep Wave
startTime = beginning + 6.35
dimmduration = 0.6
eventDict['time'].append(SettingBezierDimm(At(startTime), BottomController, BottomSetting1, 0, 95, int(dimmduration*10), 10, 0, 100))
eventDict['time'].append(SettingBezierDimm(At(startTime), TopController, TopSetting2, 0, 95, int(dimmduration*10), 10, 0, 100))
startTime = startTime + dimmduration
dimmduration = 0.6
eventDict['time'].append(SettingBezierDimm(At(startTime), BottomController, BottomSetting1, 95, 0, int(dimmduration*10), 10, 0, 100))
eventDict['time'].append(SettingBezierDimm(At(startTime), TopController, TopSetting2, 95, 0, int(dimmduration*10), 10, 0, 100))


# 7.5
# Darkstep Off
startTime = beginning + 7.5
eventDict['time'].append(ChannelAddEffect(At(startTime), BottomController, BottomChannel1, BottomEffectStrobe2, 0))

# 7.5 - 9.39
# Strobe Wave
startTime = beginning + 7.5
dimmduration = 0.6
eventDict['time'].append(SettingBezierDimm(At(startTime), BottomController, BottomSetting1, 0, 95, int(dimmduration*10), 10, 0, 100))
eventDict['time'].append(SettingBezierDimm(At(startTime), BottomController, BottomSetting2, 0, 95, int(dimmduration*10), 10, 0, 100))
startTime = startTime + dimmduration
dimmduration = 0.6
eventDict['time'].append(SettingBezierDimm(At(startTime), BottomController, BottomSetting1, 95, 0, int(dimmduration*10), 10, 0, 100))
eventDict['time'].append(SettingBezierDimm(At(startTime), BottomController, BottomSetting2, 95, 0, int(dimmduration*10), 10, 0, 100))

# 9.5
# Right Soft Piano with release until 11.1
startTime = beginning + 9.5
fadeOutLength = 1.4
# sustainSteptime 0
sustainSteptime = 2
eventDict['time'].append(SettingImpulseToBezierFadeout(At(startTime), BottomController, BottomSetting4, 65, 1, 20, sustainSteptime, int(fadeOutLength*10), 10, 0, 100))


# 11.09
# Top Soft-Piano with release until 12.08
startTime = beginning + 11.09
fadeOutLength = 0.8
# sustainSteptime 0
sustainSteptime = 2
eventDict['time'].append(SettingImpulseToBezierFadeout(At(startTime), TopController, TopSetting4, 65, 1, 20, sustainSteptime, int(fadeOutLength*10), 10, 0, 100))


# 12.05 - 12.58
# Soft Strobe Fade In
startTime = beginning + 12.05
dimmduration = 0.53
eventDict['time'].append(SettingBezierDimm(At(startTime), BottomController, BottomSetting1, 0, 60, int(dimmduration*10), 10, 0, 100))
eventDict['time'].append(SettingBezierDimm(At(startTime), BottomController, BottomSetting2, 0, 60, int(dimmduration*10), 10, 0, 100))

# 12.58 - 13.43
# Strobe Fade to Full
startTime = beginning + 12.58
dimmduration = 0.85
eventDict['time'].append(SettingBezierDimm(At(startTime), BottomController, BottomSetting1, 60, 80, int(dimmduration*10), 10, 0, 100))
eventDict['time'].append(SettingBezierDimm(At(startTime), BottomController, BottomSetting2, 60, 80, int(dimmduration*10), 10, 0, 100))

# 13.43-14.07
# Strobe Fade Out
startTime = beginning + 13.43
dimmduration = 0.65
eventDict['time'].append(SettingBezierDimm(At(startTime), BottomController, BottomSetting1, 80, 0, int(dimmduration*10), 10, 0, 100))
eventDict['time'].append(SettingBezierDimm(At(startTime), BottomController, BottomSetting2, 80, 0, int(dimmduration*10), 10, 0, 100))

# 14.07 - 15.67
# Strobe Fade In
startTime = beginning + 14
dimmduration = 1
eventDict['time'].append(SettingBezierDimm(At(startTime), BottomController, BottomSetting1, 0, 90, int(dimmduration*10), 10, 0, 100))
eventDict['time'].append(SettingBezierDimm(At(startTime), BottomController, BottomSetting2, 0, 90, int(dimmduration*10), 10, 0, 100))

# 14.07 - 14.73
# Light Darkstep Strobe Wave in background
startTime = beginning + 14.07
dimmduration = 0.35
eventDict['time'].append(SettingBezierDimm(At(startTime), TopController, TopSetting2, 0, 60, int(dimmduration*10), 10, 0, 100))
startTime = startTime + dimmduration
dimmduration = 0.35
eventDict['time'].append(SettingBezierDimm(At(startTime), TopController, TopSetting2, 60, 0, int(dimmduration*10), 10, 0, 100))

# 16.29 - 17.44
# Strobe Fade Out
startTime = beginning + 16.29
dimmduration = 1.15
eventDict['time'].append(SettingBezierDimm(At(startTime), BottomController, BottomSetting1, 90, 0, int(dimmduration*10), 10, 0, 100))
eventDict['time'].append(SettingBezierDimm(At(startTime), BottomController, BottomSetting2, 90, 0, int(dimmduration*10), 10, 0, 100))

# 18
# Darkstep On
startTime = beginning + 18
eventDict['time'].append(ChannelAddEffect(At(startTime), BottomController, BottomChannel1, BottomEffectStrobe1, 0))

# 18.73 - 20.02
# Strong Left Darkstep Wave
startTime = beginning + 18.73
dimmduration = 1.15
eventDict['time'].append(SettingBezierDimm(At(startTime), BottomController, BottomSetting1, 0, 95, int(dimmduration*10), 10, 0, 100))
eventDict['time'].append(SettingBezierDimm(At(startTime), TopController, TopSetting2, 0, 95, int(dimmduration*10), 10, 0, 100))
startTime = startTime + dimmduration
dimmduration = 1.15
eventDict['time'].append(SettingBezierDimm(At(startTime), BottomController, BottomSetting1, 95, 0, int(dimmduration*10), 10, 0, 100))
eventDict['time'].append(SettingBezierDimm(At(startTime), TopController, TopSetting2, 95, 0, int(dimmduration*10), 10, 0, 100))


# 20.03 - 20.95
# Light Left Darkstep Wave
startTime = beginning + 20.03
dimmduration = 0.45
eventDict['time'].append(SettingBezierDimm(At(startTime), BottomController, BottomSetting1, 0, 40, int(dimmduration*10), 10, 0, 100))
eventDict['time'].append(SettingBezierDimm(At(startTime), TopController, TopSetting2, 0, 40, int(dimmduration*10), 10, 0, 100))
startTime = startTime + dimmduration
dimmduration = 0.45
eventDict['time'].append(SettingBezierDimm(At(startTime), BottomController, BottomSetting1, 40, 0, int(dimmduration*10), 10, 0, 100))
eventDict['time'].append(SettingBezierDimm(At(startTime), TopController, TopSetting2, 40, 0, int(dimmduration*10), 10, 0, 100))

# 21.03
# Right Piano with release until 22.07
startTime = beginning + 21.03
fadeOutLength = 0.8
# sustainSteptime 0
sustainSteptime = 2
eventDict['time'].append(SettingImpulseToBezierFadeout(At(startTime), BottomController, BottomSetting4, 95, 1, 30, sustainSteptime, int(fadeOutLength*10), 10, 0, 100))


# 22.07
# Right and Top Right Piano with relese until 22.89
startTime = beginning + 22.07
fadeOutLength = 0.6
# sustainSteptime 0
sustainSteptime = 2
eventDict['time'].append(SettingImpulseToBezierFadeout(At(startTime), TopController, TopSetting4, 95, 1, 20, sustainSteptime, int(fadeOutLength*10), 10, 0, 100))
eventDict['time'].append(SettingImpulseToBezierFadeout(At(startTime), BottomController, BottomSetting4, 95, 1, 30, sustainSteptime, int(fadeOutLength*10), 10, 0, 100))


# 22.9-24
# Light Strobe Wave
startTime = beginning + 22.9
dimmduration = 0.55
eventDict['time'].append(SettingBezierDimm(At(startTime), BottomController, BottomSetting1, 0, 65, int(dimmduration*10), 10, 0, 100))
eventDict['time'].append(SettingBezierDimm(At(startTime), BottomController, BottomSetting2, 0, 65, int(dimmduration*10), 10, 0, 100))
startTime = startTime + dimmduration
dimmduration = 0.55
eventDict['time'].append(SettingBezierDimm(At(startTime), BottomController, BottomSetting1, 65, 0, int(dimmduration*10), 10, 0, 100))
eventDict['time'].append(SettingBezierDimm(At(startTime), BottomController, BottomSetting2, 65, 0, int(dimmduration*10), 10, 0, 100))

# 26.05-27
# Light Strobe Wave
startTime = beginning + 26.05
dimmduration = 0.5
eventDict['time'].append(SettingBezierDimm(At(startTime), BottomController, BottomSetting1, 0, 65, int(dimmduration*10), 10, 0, 100))
eventDict['time'].append(SettingBezierDimm(At(startTime), BottomController, BottomSetting2, 0, 65, int(dimmduration*10), 10, 0, 100))
startTime = startTime + dimmduration
dimmduration = 0.55
eventDict['time'].append(SettingBezierDimm(At(startTime), BottomController, BottomSetting1, 65, 0, int(dimmduration*10), 10, 0, 100))
eventDict['time'].append(SettingBezierDimm(At(startTime), BottomController, BottomSetting2, 65, 0, int(dimmduration*10), 10, 0, 100))

# 28
# Top Light Piano with Release until 28.7
startTime = beginning + 28
fadeOutLength = 0.5
# sustainSteptime 0
sustainSteptime = 2
eventDict['time'].append(SettingImpulseToBezierFadeout(At(startTime), TopController, TopSetting4, 95, 1, 20, sustainSteptime, int(fadeOutLength*10), 10, 0, 100))


# 28.6
# Top And Right Piano with release until 32.7
startTime = beginning + 28.6
fadeOutLength = 3.8
# sustainSteptime 0
sustainSteptime = 2
eventDict['time'].append(SettingImpulseToBezierFadeout(At(startTime), TopController, TopSetting4, 95, 1, 20, sustainSteptime, int(fadeOutLength*10), 10, 0, 100))
eventDict['time'].append(SettingImpulseToBezierFadeout(At(startTime), BottomController, BottomSetting4, 95, 1, 30, sustainSteptime, int(fadeOutLength*10), 10, 0, 100))


# 32.78
# Light Piano with Quick release
startTime = beginning + 32.78
fadeOutLength = 0.1
# sustainSteptime 0
sustainSteptime = 2
eventDict['time'].append(SettingImpulseToBezierFadeout(At(startTime), TopController, TopSetting4, 80, 1, 20, sustainSteptime, int(fadeOutLength*10), 10, 0, 100))


# 33
# Top and Right Piano with release until 40
startTime = beginning + 33
fadeOutLength = 6.8
# sustainSteptime 0
sustainSteptime = 3
eventDict['time'].append(SettingImpulseToBezierFadeout(At(startTime), TopController, TopSetting4, 95, 1, 40, sustainSteptime, int(fadeOutLength*10), 10, 0, 100))
eventDict['time'].append(SettingImpulseToBezierFadeout(At(startTime), BottomController, BottomSetting4, 95, 1, 40, sustainSteptime, int(fadeOutLength*10), 10, 0, 100))



# 40
# Piano with quick release
startTime = beginning + 40
fadeOutLength = 0.1
# sustainSteptime 0
sustainSteptime = 2
eventDict['time'].append(SettingImpulseToBezierFadeout(At(startTime), BottomController, BottomSetting4, 95, 1, 30, sustainSteptime, int(fadeOutLength*10), 10, 0, 100))


# 40,6
# Piano with quick release
startTime = beginning + 40.6
fadeOutLength = 0.1
# sustainSteptime 0
sustainSteptime = 2
eventDict['time'].append(SettingImpulseToBezierFadeout(At(startTime), BottomController, BottomSetting4, 95, 1, 30, sustainSteptime, int(fadeOutLength*10), 10, 0, 100))


# 41
# Piano with quick release
startTime = beginning + 41
fadeOutLength = 0.1
# sustainSteptime 0
sustainSteptime = 2
eventDict['time'].append(SettingImpulseToBezierFadeout(At(startTime), TopController, TopSetting4, 95, 1, 20, sustainSteptime, int(fadeOutLength*10), 10, 0, 100))


# 41 MOtor On
# 41 - 44 Back Light Fades in
startTime = beginning + 41
dimmduration = 3
eventDict['time'].append(SettingBezierDimm(At(startTime), TopController, TopSetting3, 0, 95, int(dimmduration*10), 10, 0, 100))

eventDict['time'].append(EffectSequencedLightStrobe(At(startTime), TopController, TopEffectStrobe1, BottomChannelStrobe1Steptime, BottomChannelStrobe1Darkstep, 18361537))
eventDict['time'].append(EffectSequencedLightStrobe(At(startTime), BottomController, BottomEffectStrobe1, BottomChannelStrobe1Steptime, BottomChannelStrobe1Darkstep, 18361537))

eventDict['time'].append(ChannelRemoveEffect(At(startTime), BottomController, BottomChannel2, 0))
eventDict['time'].append(ChannelAddEffect(At(startTime), BottomController, BottomChannel1, BottomEffectStrobe1, 0))
eventDict['time'].append(ChannelAddEffect(At(startTime), BottomController, BottomChannel3, BottomEffectStrobe1, 0))
eventDict['time'].append(ChannelAddEffect(At(startTime), TopController, TopChannel1, BottomEffectStrobe1, 0))
eventDict['time'].append(ChannelAddEffect(At(startTime), TopController, TopChannel2, BottomEffectStrobe1, 0))
eventDict['time'].append(ChannelAddEffect(At(startTime), TopController, TopChannel4, BottomEffectStrobe1, 0))

eventDict['time'].append(MotorSpeed(At(startTime), 90))
eventDict['position'].append(MotorSpeed(At(3.10), 0))


# Part II
# 44
# explosion
startTime = beginning + 44
eventDict['time'].append(LightSetChannel(At(startTime), BottomController, [Light2, Light4], StaticChannel100))


# explosion end
startTime = beginning + 44.1
eventDict['time'].append(LightSetChannel(At(startTime), BottomController, [Light2,], BottomChannel2))
eventDict['time'].append(LightSetChannel(At(startTime), BottomController, [Light4,], BottomChannel4))
eventDict['time'].append(ChannelAddEffect(At(startTime), TopController, TopChannel3, BottomEffectStrobe1, 0))


# 44-48
# Strobe Fade In
startTime = beginning + 44.1
dimmduration = 4
eventDict['time'].append(SettingBezierDimm(At(startTime), TopController, TopSetting1, 0, 95, int(dimmduration*10), 10, 0, 100))
eventDict['time'].append(SettingBezierDimm(At(startTime), TopController, TopSetting2, 0, 95, int(dimmduration*10), 10, 0, 100))
eventDict['time'].append(SettingBezierDimm(At(startTime), TopController, TopSetting3, 0, 95, int(dimmduration*10), 10, 0, 100))
eventDict['time'].append(SettingBezierDimm(At(startTime), TopController, TopSetting4, 0, 95, int(dimmduration*10), 10, 0, 100))

eventDict['time'].append(SettingBezierDimm(At(startTime), BottomController, BottomSetting1, 0, 95, int(dimmduration*10), 10, 0, 100))
eventDict['time'].append(SettingBezierDimm(At(startTime), BottomController, BottomSetting3, 0, 95, int(dimmduration*10), 10, 0, 100))


# 79.5-82.5
# Strobe Fade Out
startTime = beginning + 79.5
dimmduration = 3
eventDict['time'].append(SettingBezierDimm(At(startTime), TopController, TopSetting1, 95, 0, int(dimmduration*10), 10, 0, 100))
eventDict['time'].append(SettingBezierDimm(At(startTime), TopController, TopSetting2, 95, 0, int(dimmduration*10), 10, 0, 100))
eventDict['time'].append(SettingBezierDimm(At(startTime), TopController, TopSetting3, 95, 0, int(dimmduration*10), 10, 0, 100))
eventDict['time'].append(SettingBezierDimm(At(startTime), TopController, TopSetting4, 95, 0, int(dimmduration*10), 10, 0, 100))

eventDict['time'].append(SettingBezierDimm(At(startTime), BottomController, BottomSetting1, 95, 0, int(dimmduration*10), 10, 0, 100))
eventDict['time'].append(SettingBezierDimm(At(startTime), BottomController, BottomSetting3, 95, 0, int(dimmduration*10), 10, 0, 100))

# 81-87.9
# Tinitus
startTime = beginning + 81
dimmduration = 7
eventDict['time'].append(ChannelRemoveEffect(At(startTime), TopController, TopChannel3, 0))
eventDict['time'].append(SettingBezierDimm(At(startTime), TopController, TopSetting3, 0, 95, int(dimmduration*10), 10, 0, 100))


# 82.5
# Remove Effects
startTime = beginning + 79.5
eventDict['time'].append(ChannelRemoveEffect(At(startTime), BottomController, BottomChannel1, 0))
eventDict['time'].append(ChannelRemoveEffect(At(startTime), BottomController, BottomChannel3, 0))
eventDict['time'].append(ChannelRemoveEffect(At(startTime), TopController, TopChannel1, 0))
eventDict['time'].append(ChannelRemoveEffect(At(startTime), TopController, TopChannel2, 0))
eventDict['time'].append(ChannelRemoveEffect(At(startTime), TopController, TopChannel4, 0))



# 88
# PART III

# Setup
# beginning refers to the beginning behind so that when the back moves, the front moves accordingly
# the 0 will be changed as soon as more parts are added
beginning = beginning + 88

startTime = beginning
dimmduration = 0.1
eventDict['time'].append(SettingBezierDimm(At(startTime), TopController, TopSetting3, 95, 0, int(dimmduration*10), 10, 0, 100))


# Bottom
eventDict['time'].append(ChannelAddEffect(At(0), BottomController, BottomChannel1, BottomEffectStrobe1, 0))
eventDict['time'].append(ChannelAddEffect(At(0), BottomController, BottomChannel3, BottomEffectStrobe1, 0))

# Top
eventDict['time'].append(ChannelAddEffect(At(0), TopController, TopChannel4, TopEffectSubtractPercentageVibrato, 0))
# We need a strobe only on 3 (aka 7 as global)
eventDict['time'].append(EffectSequencedLightStrobe(At(0), TopController, TopEffectStrobe1, TopChannelStrobe1Steptime, TopChannelStrobe1Darkstep, 5757))



# 0-0.25
# Bottom Left In
startTime = beginning + 0
dimmduration = 0.25
eventDict['time'].append(SettingBezierDimm(At(startTime), BottomController, BottomSetting1, 0, 95, int(dimmduration*20), 5, 0, 100))

# 0.25
# Right Joins
startTime = beginning + 0.25
dimmduration = 0
eventDict['time'].append(SettingBezierDimm(At(startTime), BottomController, BottomSetting3, 0, 95, int(dimmduration*20), 5, 0, 100))

# 1.06 - 2.16
# Fade Down
startTime = beginning + 1.06
dimmduration = 1.1
eventDict['time'].append(SettingBezierDimm(At(startTime), BottomController, BottomSetting3, 95, 10, int(dimmduration*20), 5, 0, 100))
eventDict['time'].append(SettingBezierDimm(At(startTime), BottomController, BottomSetting3, 95, 10, int(dimmduration*20), 5, 0, 100))

# 2.43 - 3.97
# Right Fades In
startTime = beginning + 2.43
dimmduration = 1.55
eventDict['time'].append(SettingBezierDimm(At(startTime), BottomController, BottomSetting3, 10, 95, int(dimmduration*20), 5, 0, 100))

# 4.06 - 5.85
# Both Fade Down
startTime = beginning + 4.05
dimmduration = 1.8
eventDict['time'].append(SettingBezierDimm(At(startTime), BottomController, BottomSetting3, 95, 0, int(dimmduration*20), 5, 0, 100))

# 5.2
# Background Vibrato Appears Lightly
startTime = beginning + 5.2
dimmduration = 0.5
eventDict['time'].append(SettingBezierDimm(At(startTime), TopController, TopSetting4, 0, 80, int(dimmduration*20), 5, 0, 100))

# 6.32 - 7.6
# Right Fades In
startTime = beginning + 6.3
dimmduration = 1.3
eventDict['time'].append(SettingBezierDimm(At(startTime), BottomController, BottomSetting3, 0, 95, int(dimmduration*20), 5, 0, 100))

# 7.76
# Right Off
startTime = beginning + 7.76
dimmduration = 0
eventDict['time'].append(SettingBezierDimm(At(startTime), BottomController, BottomSetting3, 95, 0, int(dimmduration*20), 5, 0, 100))

# 8.58 - 9.4
# Left Fades In
startTime = beginning + 8.6
dimmduration = 0.8
eventDict['time'].append(SettingBezierDimm(At(startTime), BottomController, BottomSetting1, 0, 95, int(dimmduration*20), 5, 0, 100))

# 9.51 - 9.7
# Right Joins Lightly
startTime = beginning + 9.50
dimmduration = 0.2
eventDict['time'].append(SettingBezierDimm(At(startTime), BottomController, BottomSetting3, 0, 60, int(dimmduration*20), 5, 0, 100))
# 9.51 - 12.3
# Top Fades Out
startTime = beginning + 9.50
dimmduration = 2.8
eventDict['time'].append(SettingBezierDimm(At(startTime), TopController, TopSetting4, 80, 0, int(dimmduration*10), 10, 0, 100))

# 11.7 - 12.6
# Right full blast
# Left down
startTime = beginning + 11.70
dimmduration = 0.9
eventDict['time'].append(SettingBezierDimm(At(startTime), BottomController, BottomSetting1, 95, 40, int(dimmduration*20), 5, 0, 100))
eventDict['time'].append(SettingBezierDimm(At(startTime), BottomController, BottomSetting3, 60, 95, int(dimmduration*20), 5, 0, 100))

# 12.6 - 12.9
# Both Down
startTime = beginning + 12.60
dimmduration = 0.3
eventDict['time'].append(SettingBezierDimm(At(startTime), BottomController, BottomSetting1, 40, 0, int(dimmduration*20), 5, 0, 100))
eventDict['time'].append(SettingBezierDimm(At(startTime), BottomController, BottomSetting3, 95, 0, int(dimmduration*20), 5, 0, 100))

# 12.9 - 13.18
# Right Up
startTime = beginning + 12.9
dimmduration = 0.25
eventDict['time'].append(SettingBezierDimm(At(startTime), BottomController, BottomSetting3, 0, 95, int(dimmduration*20), 5, 0, 100))

# 13.18 - 13.68
# Right Down
startTime = beginning + 13.18
dimmduration = 0.5
eventDict['time'].append(SettingBezierDimm(At(startTime), BottomController, BottomSetting3, 95, 0, int(dimmduration*20), 5, 0, 100))

# 13.3
# Light Quicker Top Pulse
startTime = beginning + 13.3
eventDict['time'].append(ChannelSetStatic(At(startTime), TopController, TopChannelVibratoSteptime, 9))
eventDict['time'].append(SettingStatic(At(startTime), TopController, TopSetting4, 30))


# 14.07 - 14.87
# Left Wave
startTime = beginning + 14.07
dimmduration = 0.4
eventDict['time'].append(SettingBezierDimm(At(startTime), BottomController, BottomSetting1, 0, 95, int(dimmduration*20), 5, 0, 100))
startTime = startTime + dimmduration
dimmduration = 0.4
eventDict['time'].append(SettingBezierDimm(At(startTime), BottomController, BottomSetting1, 95, 0, int(dimmduration*20), 5, 0, 100))


# 14.85 - 16.00
# Right Wave
startTime = beginning + 14.85
dimmduration = 0.55
eventDict['time'].append(SettingBezierDimm(At(startTime), BottomController, BottomSetting3, 0, 95, int(dimmduration*20), 5, 0, 100))
startTime = startTime + dimmduration
dimmduration = 0.60
eventDict['time'].append(SettingBezierDimm(At(startTime), BottomController, BottomSetting3, 95, 0, int(dimmduration*20), 5, 0, 100))

# 15.6
# Top Vibrato gets slower again
# startTime = beginning + 15.6
# eventDict['time'].append(ChannelSetStatic(At(startTime), TopController, TopChannelVibratoSteptime, 17))
 

# 16 - 16.75
# Small Left Wave
startTime = beginning + 16
dimmduration = 0.35
eventDict['time'].append(SettingBezierDimm(At(startTime), BottomController, BottomSetting1, 0, 70, int(dimmduration*20), 5, 0, 100))
startTime = startTime + dimmduration
dimmduration = 0.40
eventDict['time'].append(SettingBezierDimm(At(startTime), BottomController, BottomSetting1, 70, 0, int(dimmduration*20), 5, 0, 100))

# 17.45 - 18.00
# Both Fade in Lightly
startTime = beginning + 17.45
dimmduration = 0.55
eventDict['time'].append(SettingBezierDimm(At(startTime), BottomController, BottomSetting1, 0, 70, int(dimmduration*20), 5, 0, 100))
eventDict['time'].append(SettingBezierDimm(At(startTime), BottomController, BottomSetting3, 0, 70, int(dimmduration*20), 5, 0, 100))

# 18.50 - 18.9
# Darkstep On and go to fully
startTime = beginning + 18.5
dimmduration = 0.40
eventDict['time'].append(ChannelSetStatic(At(startTime), BottomController, BottomChannelStrobe1Darkstep, 1))
eventDict['time'].append(SettingBezierDimm(At(startTime), BottomController, BottomSetting1, 70, 95, int(dimmduration*20), 5, 0, 100))
eventDict['time'].append(SettingBezierDimm(At(startTime), BottomController, BottomSetting3, 70, 95, int(dimmduration*20), 5, 0, 100))

# 19.84 - 20.90
# Fade Down
startTime = beginning + 19.85
dimmduration = 1.05
eventDict['time'].append(SettingBezierDimm(At(startTime), BottomController, BottomSetting1, 95, 0, int(dimmduration*20), 5, 0, 100))
eventDict['time'].append(SettingBezierDimm(At(startTime), BottomController, BottomSetting3, 95, 0, int(dimmduration*20), 5, 0, 100))

# 20.9 - 22.5
# Right Wave
startTime = beginning + 21
dimmduration = 0.75
eventDict['time'].append(ChannelSetStatic(At(startTime), BottomController, BottomChannelStrobe1Darkstep, 0))
eventDict['time'].append(SettingBezierDimm(At(startTime), BottomController, BottomSetting3, 0, 95, int(dimmduration*20), 5, 0, 100))
startTime = startTime + dimmduration
dimmduration = 0.75
eventDict['time'].append(SettingBezierDimm(At(startTime), BottomController, BottomSetting3, 95, 0, int(dimmduration*20), 5, 0, 100))

# 22
# Top Vibrato Faster Again
startTime = beginning + 22
eventDict['time'].append(ChannelSetStatic(At(startTime), TopController, TopChannelVibratoSteptime, 9))


# 23.1 - 24
# Small Right Wave
startTime = beginning + 23
dimmduration = 0.5
eventDict['time'].append(SettingBezierDimm(At(startTime), BottomController, BottomSetting3, 0, 60, int(dimmduration*20), 5, 0, 100))
startTime = startTime + dimmduration
dimmduration = 0.5
eventDict['time'].append(SettingBezierDimm(At(startTime), BottomController, BottomSetting3, 60, 0, int(dimmduration*20), 5, 0, 100))

# 24.5 - 25.3
# Small Right Wave
startTime = beginning + 24.3
dimmduration = 0.5
eventDict['time'].append(SettingBezierDimm(At(startTime), BottomController, BottomSetting3, 0, 60, int(dimmduration*20), 5, 0, 100))
startTime = startTime + dimmduration
dimmduration = 0.5
eventDict['time'].append(SettingBezierDimm(At(startTime), BottomController, BottomSetting3, 60, 0, int(dimmduration*20), 5, 0, 100))

# 25.3 - 26.3
# Small Left Wave
startTime = beginning + 25.3
dimmduration = 0.5
eventDict['time'].append(SettingBezierDimm(At(startTime), BottomController, BottomSetting1, 0, 60, int(dimmduration*20), 5, 0, 100))
startTime = startTime + dimmduration
dimmduration = 0.5
eventDict['time'].append(SettingBezierDimm(At(startTime), BottomController, BottomSetting1, 60, 0, int(dimmduration*20), 5, 0, 100))

# 26.45 - 27
# Tiny Left Wave
startTime = beginning + 26.45
dimmduration = 0.25
eventDict['time'].append(SettingBezierDimm(At(startTime), BottomController, BottomSetting1, 0, 40, int(dimmduration*20), 5, 0, 100))
startTime = startTime + dimmduration
dimmduration = 0.30
eventDict['time'].append(SettingBezierDimm(At(startTime), BottomController, BottomSetting1, 40, 0, int(dimmduration*20), 5, 0, 100))

# 27.8 - 28.9
# Both Fade in Lightly
startTime = beginning + 27.8
dimmduration = 1
eventDict['time'].append(SettingBezierDimm(At(startTime), BottomController, BottomSetting1, 0, 60, int(dimmduration*20), 5, 0, 100))
eventDict['time'].append(SettingBezierDimm(At(startTime), BottomController, BottomSetting3, 0, 60, int(dimmduration*20), 5, 0, 100))

# 28..9 - 29.3
# Darkstep On and go to fully
startTime = beginning + 28.9
dimmduration = 0.4
eventDict['time'].append(ChannelSetStatic(At(startTime), BottomController, BottomChannelStrobe1Darkstep, 1))
eventDict['time'].append(SettingBezierDimm(At(startTime), BottomController, BottomSetting1, 60, 95, int(dimmduration*20), 5, 0, 100))
eventDict['time'].append(SettingBezierDimm(At(startTime), BottomController, BottomSetting3, 60, 95, int(dimmduration*20), 5, 0, 100))

# 29.3
# Darkstep Off
startTime = beginning + 29.3
eventDict['time'].append(ChannelSetStatic(At(startTime), BottomController, BottomChannelStrobe1Darkstep, 0))

# 30.9 - 31.5
# Fade Down
startTime = beginning + 30.9
dimmduration = 0.6
eventDict['time'].append(SettingBezierDimm(At(startTime), BottomController, BottomSetting1, 95, 0, int(dimmduration*20), 5, 0, 100))
eventDict['time'].append(SettingBezierDimm(At(startTime), BottomController, BottomSetting3, 95, 0, int(dimmduration*20), 5, 0, 100))

# 31.8 - 32.8
# Right Wave
startTime = beginning + 31.8
dimmduration = 0.5
eventDict['time'].append(SettingBezierDimm(At(startTime), BottomController, BottomSetting3, 0, 95, int(dimmduration*20), 5, 0, 100))
startTime = startTime + dimmduration
dimmduration = 0.5
eventDict['time'].append(SettingBezierDimm(At(startTime), BottomController, BottomSetting3, 95, 0, int(dimmduration*20), 5, 0, 100))

# 33.4 - 33.9
# Top Small Strobe Wave
startTime = beginning + 33
# Replace Vibrato with strobe
# eventDict['time'].append(ChannelAddEffect(At(0), TopController, TopChannel3, TopEffectStrobe1, 0))
startTime = beginning + 33.4
dimmduration = 0.25
eventDict['time'].append(SettingBezierDimm(At(startTime), BottomController, BottomSetting3, 0, 90, int(dimmduration*20), 5, 0, 100))
startTime = startTime + dimmduration
dimmduration = 0.25
eventDict['time'].append(SettingBezierDimm(At(startTime), BottomController, BottomSetting3, 90, 0, int(dimmduration*20), 5, 0, 100))


# 34.3 - 35.3
# Wave that stays high
startTime = beginning + 34.3
dimmduration = 0.5
eventDict['time'].append(SettingBezierDimm(At(startTime), BottomController, BottomSetting1, 0, 95, int(dimmduration*20), 5, 0, 100))
startTime = startTime + dimmduration
dimmduration = 0.5
eventDict['time'].append(SettingBezierDimm(At(startTime), BottomController, BottomSetting1, 95, 40, int(dimmduration*20), 5, 0, 100))

# 35.3 - 36.90
# Another Small Wave, Long Fadeout
startTime = beginning + 35.3
dimmduration = 0.6
eventDict['time'].append(SettingBezierDimm(At(startTime), BottomController, BottomSetting1, 40, 80, int(dimmduration*20), 5, 0, 100))
startTime = startTime + dimmduration
dimmduration = 1.3
eventDict['time'].append(SettingBezierDimm(At(startTime), BottomController, BottomSetting1, 80, 0, int(dimmduration*10), 10, 0, 100))

# 37.2-38.1
# Darstep On Wave
startTime = beginning + 37.2
dimmduration = 0.45
eventDict['time'].append(ChannelSetStatic(At(startTime), BottomController, BottomChannelStrobe1Darkstep, 0))
eventDict['time'].append(SettingBezierDimm(At(startTime), BottomController, BottomSetting1, 0, 95, int(dimmduration*20), 5, 0, 100))
eventDict['time'].append(SettingBezierDimm(At(startTime), BottomController, BottomSetting3, 0, 95, int(dimmduration*20), 5, 0, 100))
startTime = startTime + dimmduration
dimmduration = 0.45
eventDict['time'].append(SettingBezierDimm(At(startTime), BottomController, BottomSetting1, 95, 0, int(dimmduration*20), 5, 0, 100))
eventDict['time'].append(SettingBezierDimm(At(startTime), BottomController, BottomSetting3, 95, 0, int(dimmduration*20), 5, 0, 100))

# 38.4 - 40.5
# Top Strobe Wave
startTime = beginning + 38.4
dimmduration = 0.7
eventDict['time'].append(SettingBezierDimm(At(startTime), BottomController, BottomSetting1, 0, 90, int(dimmduration*20), 5, 0, 100))
startTime = startTime + dimmduration
dimmduration = 1.4
eventDict['time'].append(SettingBezierDimm(At(startTime), BottomController, BottomSetting1, 90, 0, int(dimmduration*20), 5, 0, 100))

# 40.7 - 42
# Right Wave
startTime = beginning + 40
eventDict['time'].append(ChannelSetStatic(At(startTime), BottomController, BottomChannelStrobe1Darkstep, 0))
startTime = beginning + 40.7
dimmduration = 0.6
eventDict['time'].append(SettingBezierDimm(At(startTime), BottomController, BottomSetting3, 0, 95, int(dimmduration*20), 5, 0, 100))
startTime = startTime + dimmduration
dimmduration = 0.7
eventDict['time'].append(SettingBezierDimm(At(startTime), BottomController, BottomSetting3, 95, 0, int(dimmduration*20), 5, 0, 100))

# 41.3 - 42.6
# Top Strobe Wave
startTime = beginning + 41.3
dimmduration = 0.5
eventDict['time'].append(SettingBezierDimm(At(startTime), BottomController, BottomSetting1, 0, 90, int(dimmduration*20), 5, 0, 100))
startTime = startTime + dimmduration
dimmduration = 0.8
eventDict['time'].append(SettingBezierDimm(At(startTime), BottomController, BottomSetting1, 90, 0, int(dimmduration*20), 5, 0, 100))

# 44.8 - 46.2
# Top Wave and Bottom Darkstep Wave
startTime = beginning + 44
eventDict['time'].append(ChannelSetStatic(At(startTime), BottomController, BottomChannelStrobe1Darkstep, 1))
startTime = beginning + 44.8
dimmduration = 0.7
eventDict['time'].append(SettingBezierDimm(At(startTime), BottomController, BottomSetting1, 0, 95, int(dimmduration*20), 5, 0, 100))
eventDict['time'].append(SettingBezierDimm(At(startTime), BottomController, BottomSetting3, 0, 95, int(dimmduration*20), 5, 0, 100))
eventDict['time'].append(SettingBezierDimm(At(startTime), TopController, TopSetting4, 0, 95, int(dimmduration*20), 5, 0, 100))
startTime = startTime + dimmduration
dimmduration = 0.7
eventDict['time'].append(SettingBezierDimm(At(startTime), BottomController, BottomSetting1, 95, 0, int(dimmduration*20), 5, 0, 100))
eventDict['time'].append(SettingBezierDimm(At(startTime), BottomController, BottomSetting3, 95, 0, int(dimmduration*20), 5, 0, 100))
# eventDict['time'].append(SettingBezierDimm(At(startTime), TopController, TopSetting3, 95, 0, int(dimmduration*20), 5, 0, 100))

# 46
# Start Turn
startTime = beginning + 46
eventDict['time'].append(MotorSpeed(At(startTime), 80))
eventDict['position'].append(MotorSpeed(At(3.62), 0))


# Setup Ebbe
ebbemove = 5.43
# 50
startTime = beginning + 50 + ebbemove
eventDict['time'].append(ChannelRemoveEffect(At(startTime), BottomController, BottomChannel1, 0))
eventDict['time'].append(ChannelRemoveEffect(At(startTime), BottomController, BottomChannel3, 0))
startTime = beginning + 50
dimmduration = 2
eventDict['time'].append(SettingBezierDimm(At(startTime), TopController, TopSetting4, 95, 0, int(dimmduration*20), 5, 0, 100))

eventDict['time'].append(ChannelAddEffect(At(startTime), TopController, TopChannel2, TopEffectSubtractPercentagePerlin, 0))


# 52
# Top

startTime = beginning + 52 + ebbemove
fadeOutLength = 1.8
eventDict['time'].append(ChannelRemoveEffect(At(startTime), TopController, TopChannel4, 0))

# sustainSteptime 
sustainSteptime = 3
eventDict['time'].append(SettingImpulseToBezierFadeout(At(startTime), TopController, TopSetting4, 95, 1, 20, sustainSteptime, int(fadeOutLength*10), 10, 0, 100))


# 53
# Right
startTime = beginning + 53 + ebbemove
fadeOutLength = 1.8
# sustainSteptime 
sustainSteptime = 3
eventDict['time'].append(SettingImpulseToBezierFadeout(At(startTime), BottomController, BottomSetting3, 95, 1, 20, sustainSteptime, int(fadeOutLength*10), 10, 0, 100))


# 56.1
# Top
startTime = beginning + 56.1 + ebbemove
fadeOutLength = 1.8
# sustainSteptime 
sustainSteptime = 3
eventDict['time'].append(SettingImpulseToBezierFadeout(At(startTime), TopController, TopSetting4, 95, 1, 20, sustainSteptime, int(fadeOutLength*10), 10, 0, 100))


# 56.1 - 62
# Fade In String Aura in Backgrounf
startTime = beginning + 56.1 + ebbemove
dimmduration = 4.9
eventDict['time'].append(SettingBezierDimm(At(startTime), TopController, TopSetting2, 0, 100, int(dimmduration*10), 10, 0, 100))


# 57.1
# Right
startTime = beginning + 57.1 + ebbemove
fadeOutLength = 1.8
# sustainSteptime 
sustainSteptime = 3
eventDict['time'].append(SettingImpulseToBezierFadeout(At(startTime), BottomController, BottomSetting3, 95, 1, 20, sustainSteptime, int(fadeOutLength*10), 10, 0, 100))


# 62 - 63.6
# Fade Out String Aura in Background
startTime = beginning + 62 + ebbemove
dimmduration = 2.3
eventDict['time'].append(SettingBezierDimm(At(startTime), TopController, TopSetting2, 100, 0, int(dimmduration*10), 10, 0, 100))

# 63.8
# Top
startTime = beginning + 63.8 + ebbemove
fadeOutLength = 1.8
# sustainSteptime 
sustainSteptime = 3
eventDict['time'].append(SettingImpulseToBezierFadeout(At(startTime), TopController, TopSetting4, 95, 1, 20, sustainSteptime, int(fadeOutLength*10), 10, 0, 100))


# 64.8
# Right
startTime = beginning + 64.8 + ebbemove
fadeOutLength = 1.8
# sustainSteptime 
sustainSteptime = 3
eventDict['time'].append(SettingImpulseToBezierFadeout(At(startTime), BottomController, BottomSetting3, 95, 1, 20, sustainSteptime, int(fadeOutLength*10), 10, 0, 100))



# 64.9
# Light Left
startTime = beginning + 64.9 + ebbemove
fadeOutLength = 1.8
# sustainSteptime 
sustainSteptime = 3
eventDict['time'].append(SettingImpulseToBezierFadeout(At(startTime), BottomController, BottomSetting1, 70, 1, 20, sustainSteptime, int(fadeOutLength*10), 10, 0, 100))

# 67.5
# Top
startTime = beginning + 67.5 + ebbemove
fadeOutLength = 1.8
# sustainSteptime 
sustainSteptime = 3
eventDict['time'].append(SettingImpulseToBezierFadeout(At(startTime), TopController, TopSetting4, 95, 1, 20, sustainSteptime, int(fadeOutLength*10), 10, 0, 100))


# 68.6
# Left
startTime = beginning + 68.6 + ebbemove
fadeOutLength = 1.8
# sustainSteptime 
sustainSteptime = 3
eventDict['time'].append(SettingImpulseToBezierFadeout(At(startTime), BottomController, BottomSetting3, 95, 1, 20, sustainSteptime, int(fadeOutLength*10), 10, 0, 100))

# 69.6
# Right
startTime = beginning + 69.6 + ebbemove
fadeOutLength = 1.8
# sustainSteptime 
sustainSteptime = 3
eventDict['time'].append(SettingImpulseToBezierFadeout(At(startTime), BottomController, BottomSetting3, 95, 1, 20, sustainSteptime, int(fadeOutLength*10), 10, 0, 100))


# 70 - 75
# Fade In String Aura
startTime = beginning + 70 + ebbemove
dimmduration = 5
eventDict['time'].append(SettingBezierDimm(At(startTime), TopController, TopSetting2, 0, 100, int(dimmduration*10), 10, 0, 100))

# 72
# Right
startTime = beginning + 72 + ebbemove
fadeOutLength = 1.8
# sustainSteptime 
sustainSteptime = 3
eventDict['time'].append(SettingImpulseToBezierFadeout(At(startTime), BottomController, BottomSetting3, 95, 1, 20, sustainSteptime, int(fadeOutLength*10), 10, 0, 100))


# 75.4 76.4
# Fade Out String Aura
startTime = beginning + 75.4 + ebbemove
dimmduration = 3
eventDict['time'].append(SettingBezierDimm(At(startTime), TopController, TopSetting2, 100, 0, int(dimmduration*10), 10, 0, 100))

# 76.4
# Top
startTime = beginning + 76.4 + ebbemove
fadeOutLength = 1.8
# sustainSteptime 
sustainSteptime = 3
eventDict['time'].append(SettingImpulseToBezierFadeout(At(startTime), TopController, TopSetting4, 95, 1, 20, sustainSteptime, int(fadeOutLength*10), 10, 0, 100))


# 77.7
# Right
startTime = beginning + 77.7 + ebbemove
fadeOutLength = 1.8
# sustainSteptime 
sustainSteptime = 3
eventDict['time'].append(SettingImpulseToBezierFadeout(At(startTime), BottomController, BottomSetting3, 95, 1, 20, sustainSteptime, int(fadeOutLength*10), 10, 0, 100))


# 78.9
# Light Left
startTime = beginning + 78.9 + ebbemove
fadeOutLength = 1.8
# sustainSteptime 
sustainSteptime = 3
eventDict['time'].append(SettingImpulseToBezierFadeout(At(startTime), BottomController, BottomSetting1, 70, 1, 20, sustainSteptime, int(fadeOutLength*10), 10, 0, 100))


# 80.13
# Super Light Right
startTime = beginning + 80.13 + ebbemove
fadeOutLength = 1.8
# sustainSteptime 0
sustainSteptime = 3
eventDict['time'].append(SettingImpulseToBezierFadeout(At(startTime), BottomController, BottomSetting3, 50, 1, 10, sustainSteptime, int(fadeOutLength*10), 10, 0, 100))


# 82.9-85.8
# Fade In string Aura
startTime = beginning + 82 + ebbemove
dimmduration = 3.5
eventDict['time'].append(SettingBezierDimm(At(startTime), TopController, TopSetting2, 0, 100, int(dimmduration*10), 10, 0, 100))

# 84.5
# Top
startTime = beginning + 84.5 + ebbemove
fadeOutLength = 1.8
# sustainSteptime 
sustainSteptime = 3
eventDict['time'].append(SettingImpulseToBezierFadeout(At(startTime), TopController, TopSetting4, 95, 1, 20, sustainSteptime, int(fadeOutLength*10), 10, 0, 100))


# 85.8 - 87.2
# Fade Out String Aura but not Fully
startTime = beginning + 85.8 + ebbemove
dimmduration = 1.4
eventDict['time'].append(SettingBezierDimm(At(startTime), TopController, TopSetting2, 100, 0, int(dimmduration*10), 10, 0, 100))

# 85.9
# Left Light
startTime = beginning + 85.9 + ebbemove
fadeOutLength = 1.8
# sustainSteptime 
sustainSteptime = 3
eventDict['time'].append(SettingImpulseToBezierFadeout(At(startTime), BottomController, BottomSetting1, 70, 1, 20, sustainSteptime, int(fadeOutLength*10), 10, 0, 100))

# 86.2
# Right Light
startTime = beginning + 86.2 + ebbemove
fadeOutLength = 1.8
# sustainSteptime 
sustainSteptime = 3
eventDict['time'].append(SettingImpulseToBezierFadeout(At(startTime), BottomController, BottomSetting3, 70, 1, 20, sustainSteptime, int(fadeOutLength*10), 10, 0, 100))


# 86.9
# Top
startTime = beginning + 86.8 + ebbemove
fadeOutLength = 1.8
# sustainSteptime 
sustainSteptime = 3
eventDict['time'].append(SettingImpulseToBezierFadeout(At(startTime), TopController, TopSetting4, 95, 1, 20, sustainSteptime, int(fadeOutLength*10), 10, 0, 100))


# 87.2 - 89
# Fade In String Aura
startTime = beginning + 87.2 + ebbemove
dimmduration = 1.8
eventDict['time'].append(SettingBezierDimm(At(startTime), TopController, TopSetting2, 0, 100, int(dimmduration*10), 10, 0, 100))

# 88.3
# Right
startTime = beginning + 88.3 + ebbemove
fadeOutLength = 1.8
# sustainSteptime 
sustainSteptime = 3
eventDict['time'].append(SettingImpulseToBezierFadeout(At(startTime), BottomController, BottomSetting3, 95, 1, 20, sustainSteptime, int(fadeOutLength*10), 10, 0, 100))


# 88.7
# Left
startTime = beginning + 88.7 + ebbemove
fadeOutLength = 1.8
# sustainSteptime 
sustainSteptime = 3
eventDict['time'].append(SettingImpulseToBezierFadeout(At(startTime), BottomController, BottomSetting1, 95, 1, 20, sustainSteptime, int(fadeOutLength*10), 10, 0, 100))

# 89 - 92.5
# Fade Out String Aura
startTime = beginning + 89 + ebbemove
dimmduration = 3.5
eventDict['time'].append(SettingBezierDimm(At(startTime), TopController, TopSetting2, 100, 0, int(dimmduration*10), 10, 0, 100))

# 89.8
# Top
startTime = beginning + 89.8 + ebbemove
fadeOutLength = 1.8
# sustainSteptime 
sustainSteptime = 3
eventDict['time'].append(SettingImpulseToBezierFadeout(At(startTime), TopController, TopSetting4, 95, 1, 20, sustainSteptime, int(fadeOutLength*10), 10, 0, 100))


# 91.2
# Light Right
startTime = beginning + 91.2 + ebbemove
fadeOutLength = 1.8
# sustainSteptime 
sustainSteptime = 3
eventDict['time'].append(SettingImpulseToBezierFadeout(At(startTime), BottomController, BottomSetting3, 70, 1, 20, sustainSteptime, int(fadeOutLength*10), 10, 0, 100))


# 91.8
# Light Left
startTime = beginning + 91.8 + ebbemove
fadeOutLength = 1.8
# sustainSteptime 
sustainSteptime = 3
eventDict['time'].append(SettingImpulseToBezierFadeout(At(startTime), BottomController, BottomSetting1, 95, 1, 20, sustainSteptime, int(fadeOutLength*10), 10, 0, 100))

# 93.5
# Top
startTime = beginning + 93 + ebbemove
fadeOutLength = 1.8
# sustainSteptime 
sustainSteptime = 3
eventDict['time'].append(SettingImpulseToBezierFadeout(At(startTime), TopController, TopSetting4, 95, 1, 20, sustainSteptime, int(fadeOutLength*10), 10, 0, 100))


# 94.2 - 100.8
# Aura Fade In
startTime = beginning + 94.2 + ebbemove
dimmduration = 6.6
eventDict['time'].append(SettingBezierDimm(At(startTime), TopController, TopSetting2, 0, 100, int(dimmduration*10), 10, 0, 100))

# 96.25
# Super Light Left
startTime = beginning + 96.25 + ebbemove
fadeOutLength = 1.8
# sustainSteptime 
sustainSteptime = 3
eventDict['time'].append(SettingImpulseToBezierFadeout(At(startTime), BottomController, BottomSetting1, 50, 1, 10, sustainSteptime, int(fadeOutLength*10), 10, 0, 100))

# 96.5
# Super Ligth Right
startTime = beginning + 96.5 + ebbemove
fadeOutLength = 1.8
# sustainSteptime 
sustainSteptime = 3
eventDict['time'].append(SettingImpulseToBezierFadeout(At(startTime), BottomController, BottomSetting3, 50, 1, 10, sustainSteptime, int(fadeOutLength*10), 10, 0, 100))


# 106 - 109
# Aura Fade OUt
startTime = beginning + 106 + ebbemove
dimmduration = 3
eventDict['time'].append(SettingBezierDimm(At(startTime), TopController, TopSetting2, 100, 0, int(dimmduration*10), 10, 0, 100))


startTime = beginning + 115 + ebbemove
dimmduration = 0.2
eventDict['time'].append(SettingBezierDimm(At(startTime), BottomController, BottomSetting3, 0, 60, int(dimmduration*10), 10, 0, 100))


vd = VisualDriver(eventDict, music=music, usesMotor=True, startTime=0, isTake=False)
vd.start()