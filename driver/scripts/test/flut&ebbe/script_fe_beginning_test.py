from visualdriver import VisualDriver
from controllers import * 
from conditions import *
from channels import *
from agents import *
from events import *

eventDict = {
    'position': [],
    'time': []
}

# BOTTOM LIGHTS
eventDict['time'].append(SettingStatic(At(0), BottomController, 0, 0))
eventDict['time'].append(ChannelSetSetting(At(0), BottomController, Channel1, 0))


# TOP LIGHTS
# Settings
# Setting 0: Light
eventDict['time'].append(SettingStatic(At(0), TopController, 0, 0))
# Setting 1: Vibrato Amplitude
eventDict['time'].append(SettingStatic(At(0), TopController, 1, 0))

# Channels
# Channel 1: Lights
eventDict['time'].append(ChannelSetSetting(At(0), TopController, Channel1, 0))
# Channel 2: Vibrato Amplitude
eventDict['time'].append(ChannelSetSetting(At(0), TopController, Channel2, 1))

# Effects
# Effect 0: Vibrato
eventDict['time'].append(EffectDownVibrato(At(0), TopController, 0, Channel2, StaticChannel1))
eventDict['time'].append(ChannelAddEffect(At(0), TopController, Channel1, 0, 0))
# Effect 1: Steptime
eventDict['time'].append(EffectStrobe(At(0), TopController, 1, StaticChannel10, StaticChannel4, 1))


# BOTTOM LIGHTS
# Settings
# Setting 0: Light
eventDict['time'].append(SettingStatic(At(0), BottomController, 0, 0))
# Setting 1: Strobe Steptime
eventDict['time'].append(SettingStatic(At(0), BottomController, 1, 100))

# Channels
# Channel 1: Lights
eventDict['time'].append(ChannelSetSetting(At(0), BottomController, Channel1, 0))
# Channel 2: Strobe Steptime
eventDict['time'].append(ChannelSetSetting(At(0), BottomController, Channel2, 1))

# Effects
# Effect 0: Strobe
eventDict['time'].append(EffectStrobe(At(0), BottomController, 0, StaticChannel9, Channel2, 4))
eventDict['time'].append(ChannelAddEffect(At(0), BottomController, Channel1, 0, 0))



seconds = 1
eventDict['time'].append(LightSetChannel(At(seconds), BottomController, [Light1,], Channel1))
eventDict['time'].append(SettingStatic(At(seconds), BottomController, 0, 100))
seconds += 3
eventDict['time'].append(SettingStatic(At(seconds), BottomController, 1, 50))
seconds += 3
eventDict['time'].append(SettingStatic(At(seconds), BottomController, 1, 25))
seconds += 3
eventDict['time'].append(SettingBezierDimm(At(seconds), BottomController, 1, 80, 25, 40, 7, 0, 100))
seconds += 4
eventDict['time'].append(SettingBezierDimm(At(seconds), BottomController, 1, 25, 80, 40, 7, 0, 50))
seconds += 4
eventDict['time'].append(SettingBezierDimm(At(seconds), BottomController, 1, 80, 25, 40, 7, 50, 0))
seconds += 4

eventDict['time'].append(SettingStatic(At(seconds), BottomController, 0, 0))
eventDict['time'].append(LightSetChannel(At(seconds), TopController, [Light2, ], Channel1))
eventDict['time'].append(SettingLinearDimm(At(seconds), TopController, 0, 0, 100, 25))
seconds += 3
eventDict['time'].append(SettingLinearDimm(At(seconds), TopController, 1, 0, 90, 20))
seconds += 4
eventDict['time'].append(SettingStatic(At(seconds), TopController, 1, 0))
eventDict['time'].append(SettingBezierDimm(At(seconds), TopController, 0, 100, 0, 4, 20, 0, 100))
seconds += .8
eventDict['time'].append(SettingBezierDimm(At(seconds), TopController, 0, 100, 0, 4, 20, 60, 80))
seconds += .8
eventDict['time'].append(SettingBezierDimm(At(seconds), TopController, 0, 100, 0, 4, 20, 90, 90))
seconds += .8
eventDict['time'].append(SettingBezierDimm(At(seconds), TopController, 0, 100, 0, 4, 20, 60, 80))
seconds += .8
eventDict['time'].append(SettingBezierDimm(At(seconds), TopController, 0, 100, 0, 4, 20, 0, 100))
seconds += .8
eventDict['time'].append(SettingBezierDimm(At(seconds), TopController, 0, 100, 0, 4, 20, 90, 90))
seconds += .8
eventDict['time'].append(SettingBezierDimm(At(seconds), TopController, 0, 100, 0, 4, 20, 60, 80))
seconds += .8


# Set Strobe steptime to 40ms and new amplitude
eventDict['time'].append(SettingStatic(At(seconds), BottomController, 1, 4))
eventDict['time'].append(EffectStrobe(At(seconds), BottomController, 0, StaticChannel10, Channel2, 10, [Light1,]))
eventDict['time'].append(LightSetChannel(At(seconds), BottomController, [Light1, Light2], Channel1))
eventDict['time'].append(SettingLinearDimm(At(seconds), BottomController, 0, 0, 100, 5))
seconds += 8
eventDict['time'].append(LightSetChannel(At(seconds), BottomController, [Light1, ], StaticChannel0))
seconds += 8

# Top Vibrato Off
eventDict['time'].append(SettingStatic(At(seconds), TopController, 1, 0))
eventDict['time'].append(LightSetChannel(At(seconds), TopController, [Light2,], StaticChannel0))
eventDict['time'].append(SettingBezierDimm(At(seconds), TopController, 0, 0, 100, 20, 20, 0, 100))
eventDict['time'].append(SettingBezierDimm(At(seconds), BottomController, 0, 100, 0, 20, 20, 0, 100))
eventDict['time'].append(LightSetChannel(At(seconds), TopController, [Light4, ], Channel1))
seconds += 6
eventDict['time'].append(SettingLinearDimm(At(seconds), TopController, 1, 0, 90, 20))
seconds += 4
eventDict['time'].append(SettingBezierDimm(At(seconds), TopController, 0, 100, 0, 15, 20, 0, 100))
eventDict['time'].append(SettingBezierDimm(At(seconds), BottomController, 0, 0, 100, 15, 20, 0, 100))
eventDict['time'].append(ChannelAddEffect(At(seconds), TopController, Channel1, 1, 1))
eventDict['time'].append(SettingStatic(At(seconds), TopController, 1, 0))
seconds += 8
eventDict['time'].append(SettingBezierDimm(At(seconds), TopController, 0, 0, 100, 7, 10, 0, 100))
eventDict['time'].append(SettingBezierDimm(At(seconds), BottomController, 0, 100, 0, 7, 10, 0, 100))
seconds += 2
eventDict['time'].append(SettingBezierDimm(At(seconds), TopController, 0, 100, 0, 7, 10, 0, 100))
eventDict['time'].append(SettingBezierDimm(At(seconds), BottomController, 0, 0, 100, 7, 10, 0, 100))
seconds += 2
eventDict['time'].append(SettingBezierDimm(At(seconds), TopController, 0, 0, 100, 7, 10, 0, 100))
eventDict['time'].append(SettingBezierDimm(At(seconds), BottomController, 0, 100, 0, 7, 10, 0, 100))
seconds += 2
eventDict['time'].append(SettingBezierDimm(At(seconds), TopController, 0, 100, 0, 7, 10, 0, 100))
eventDict['time'].append(SettingBezierDimm(At(seconds), BottomController, 0, 0, 100, 7, 10, 0, 100))
seconds += 2
eventDict['time'].append(SettingStatic(At(seconds), BottomController, 1, 8))
seconds += 3
eventDict['time'].append(SettingStatic(At(seconds), BottomController, 1, 4))
seconds += 3
eventDict['time'].append(SettingStatic(At(seconds), BottomController, 1, 8))
seconds += 3
eventDict['time'].append(SettingStatic(At(seconds), BottomController, 1, 4))
seconds += 4

eventDict['time'].append(SettingStatic(At(seconds), BottomController, 0, 0))
seconds += 1
eventDict['time'].append(SettingStatic(At(seconds), BottomController, 0, 0))


vd = VisualDriver(eventDict, usesMotor=False, startTime=0)
vd.start()
