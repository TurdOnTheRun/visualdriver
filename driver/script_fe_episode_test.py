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
# Settings
# Setting 0: Light
eventDict['time'].append(SettingStaticLight(At(0), BottomController, 0, 0))
# Setting 1: Vibrato Amplitude
eventDict['time'].append(SettingStaticLight(At(0), BottomController, 1, 0))

# Channels
# Channel 1: Lights
eventDict['time'].append(ChannelSetSetting(At(0), BottomController, Channel1, 0))
# Channel 2: Vibrato Amplitude
eventDict['time'].append(ChannelSetSetting(At(0), BottomController, Channel2, 1))

# Effects
# Effect 0: Vibrato
eventDict['time'].append(EffectPerlin(At(0), BottomController, 0, StaticChannel5, StaticChannel5, 1))
eventDict['time'].append(ChannelAddEffect(At(0), BottomController, Channel1, 0, 0))


# TOP LIGHTS
# Settings
# Setting 0: Light
eventDict['time'].append(SettingStaticLight(At(0), TopController, 0, 0))
# Setting 1: Strobe Steptime
eventDict['time'].append(SettingStaticLight(At(0), TopController, 1, 40))
# Setting 2: Vibrato Amplitude
eventDict['time'].append(SettingStaticLight(At(0), TopController, 2, 0))
# Setting 3: Vibrato Steptime
eventDict['time'].append(SettingStaticLight(At(0), TopController, 3, 25))

# Channels
# Channel 1: Lights
eventDict['time'].append(ChannelSetSetting(At(0), TopController, Channel1, 0))
# Channel 2: Strobe Steptime
eventDict['time'].append(ChannelSetSetting(At(0), TopController, Channel2, 1))
# Channel 3: Vibrato Amplitude
eventDict['time'].append(ChannelSetSetting(At(0), TopController, Channel3, 2))
# Channel 4: Vibrato Steptime
eventDict['time'].append(ChannelSetSetting(At(0), TopController, Channel4, 3))

# Effects
# Effect 0: Strobe
eventDict['time'].append(EffectStrobe(At(0), TopController, 0, StaticChannel10, Channel2, 1))
eventDict['time'].append(ChannelAddEffect(At(0), TopController, Channel1, 0, 0))
# Effect 1: Vibrato
eventDict['time'].append(EffectDownVibrato(At(0), TopController, 1, Channel3, Channel4))
eventDict['time'].append(ChannelAddEffect(At(0), TopController, Channel1, 1, 1))


seconds = 1
eventDict['time'].append(LightSetChannel(At(seconds), BottomController, [Light1, Light2, ], Channel1))
eventDict['time'].append(LightSetChannel(At(seconds), TopController, [Light1, Light2, Light4], Channel1))
eventDict['time'].append(SettingBezierDimm(At(seconds), TopController, 0, 0, 100, 10, 40, 0, 100))
seconds += 3
eventDict['time'].append(SettingStaticLight(At(seconds), TopController, 1, 40))
seconds += 3
eventDict['time'].append(SettingStaticLight(At(seconds), TopController, 1, 80))
seconds += 3
eventDict['time'].append(SettingStaticLight(At(seconds), TopController, 1, 40))
seconds += 3
eventDict['time'].append(SettingStaticLight(At(seconds), TopController, 1, 80))
seconds += 3
eventDict['time'].append(SettingLinearDimm(At(seconds), TopController, 2, 0, 70, 10))
eventDict['time'].append(SettingStaticLight(At(seconds), TopController, 1, 40))
seconds += 3
eventDict['time'].append(SettingStaticLight(At(seconds), TopController, 1, 80))
seconds += 3
eventDict['time'].append(SettingStaticLight(At(seconds), TopController, 1, 40))
eventDict['time'].append(SettingLinearDimm(At(seconds), TopController, 2, 70, 0, 10))
seconds += 3
eventDict['time'].append(SettingStaticLight(At(seconds), TopController, 1, 80))
eventDict['time'].append(SettingLinearDimm(At(seconds), TopController, 2, 0, 70, 10))
seconds += 3
eventDict['time'].append(SettingBezierDimm(At(seconds), TopController, 0, 100, 0, 10, 40, 0, 100))
eventDict['time'].append(SettingBezierDimm(At(seconds), BottomController, 0, 0, 100, 10, 40, 0, 100))
seconds += 4
eventDict['time'].append(SettingBezierDimm(At(seconds), TopController, 0, 0, 100, 10, 40, 0, 100))
eventDict['time'].append(SettingBezierDimm(At(seconds), BottomController, 0, 100, 0, 10, 40, 0, 100))
seconds += 4
eventDict['time'].append(SettingBezierDimm(At(seconds), TopController, 0, 100, 0, 10, 40, 0, 100))
eventDict['time'].append(SettingBezierDimm(At(seconds), BottomController, 0, 0, 100, 10, 40, 0, 100))
seconds += 4

eventDict['time'].append(SettingStaticLight(At(seconds), TopController, 0, 0))









# seconds = 1
# eventDict['time'].append(LightSetChannel(At(seconds), BottomController, [Light1, Light2], Channel1))
# eventDict['time'].append(SettingStaticLight(At(seconds), BottomController, 0, 100))
# seconds += 3
# eventDict['time'].append(SettingStaticLight(At(seconds), BottomController, 1, 50))
# seconds += 3
# eventDict['time'].append(SettingStaticLight(At(seconds), BottomController, 1, 25))
# seconds += 3
# eventDict['time'].append(SettingBezierDimm(At(seconds), BottomController, 1, 80, 25, 40, 7, 0,100))
# seconds += 6
# eventDict['time'].append(SettingBezierDimm(At(seconds), BottomController, 1, 25, 80, 40, 7, 0,50))
# seconds += 6
# eventDict['time'].append(SettingBezierDimm(At(seconds), BottomController, 1, 80, 25, 40, 7, 50,0))
# seconds += 6
# eventDict['time'].append(SettingBezierDimm(At(seconds), BottomController, 1, 80, 25, 40, 7, 100,0))
# seconds += 6

# eventDict['time'].append(SettingStaticLight(At(seconds), BottomController, 0, 0))
# eventDict['time'].append(LightSetChannel(At(seconds), TopController, [Light2, ], Channel1))
# eventDict['time'].append(SettingLinearDimm(At(seconds), TopController, 0, 0, 100, 25))
# seconds += 2
# eventDict['time'].append(SettingLinearDimm(At(seconds), TopController, 1, 0, 90, 20))
# seconds += 4
# eventDict['time'].append(LightSetChannel(At(seconds), TopController, [Light1, Light2, Light4], Channel1))
# seconds += 6
# eventDict['time'].append(SettingLinearDimm(At(seconds), TopController, 0, 100, 0, 5))

# # Set Strobe steptime to 40ms and new amplitude
# eventDict['time'].append(SettingStaticLight(At(seconds), BottomController, 1, 4))
# eventDict['time'].append(EffectStrobe(At(seconds), BottomController, 0, StaticChannel10, Channel2, 10, [Light1,]))
# eventDict['time'].append(LightSetChannel(At(seconds), BottomController, [Light1, Light2], Channel1))
# eventDict['time'].append(SettingLinearDimm(At(seconds), BottomController, 0, 0, 100, 5))
# seconds += 8
# eventDict['time'].append(LightSetChannel(At(seconds), BottomController, [Light1, ], StaticChannel0))
# seconds += 8

# # Top Vibrato Off
# eventDict['time'].append(SettingStaticLight(At(seconds), TopController, 1, 0))
# eventDict['time'].append(LightSetChannel(At(seconds), TopController, [Light1, Light2, Light4], StaticChannel0))
# eventDict['time'].append(SettingBezierDimm(At(seconds), TopController, 0, 0, 100, 20, 20, 0, 100))
# eventDict['time'].append(SettingBezierDimm(At(seconds), BottomController, 0, 100, 0, 20, 20, 0, 100))
# eventDict['time'].append(LightSetChannel(At(seconds), TopController, [Light3, ], Channel1))
# seconds += 6
# eventDict['time'].append(SettingLinearDimm(At(seconds), TopController, 1, 0, 90, 20))
# seconds += 4
# eventDict['time'].append(SettingBezierDimm(At(seconds), TopController, 0, 100, 0, 15, 20, 0, 100))
# eventDict['time'].append(SettingBezierDimm(At(seconds), BottomController, 0, 0, 100, 15, 20, 0, 100))
# seconds += 8
# eventDict['time'].append(SettingStaticLight(At(seconds), BottomController, 1, 8))
# seconds += 3
# eventDict['time'].append(SettingStaticLight(At(seconds), BottomController, 1, 4))
# seconds += 3
# eventDict['time'].append(SettingStaticLight(At(seconds), BottomController, 1, 8))
# seconds += 3
# eventDict['time'].append(SettingStaticLight(At(seconds), BottomController, 1, 4))
# seconds += 4

# eventDict['time'].append(SettingStaticLight(At(seconds), BottomController, 0, 0))
# seconds += 1
# eventDict['time'].append(SettingStaticLight(At(seconds), BottomController, 0, 0))








vd = VisualDriver(eventDict, usesMotor=False, startTime=0)
vd.start()
