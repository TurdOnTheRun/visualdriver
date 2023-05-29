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

music = '/home/maximilian/music/guardians.mp3'

# BOTTOM:
# Channel 1: Light 1
# Channel 2: Light 2
# Channel 3: Strobe Amplitude
# Channel 4: Strobe Steptime

# Setting 0: Light 1 through Channel 1
# Setting 1: Light 2 through Channel 2
# Setting 2: Strobe Amplitude throufh Channel 3
# Setting 3: Strobe Steptime through Channel 4

# Effect 0: Perlin at 100

# BOTTOM LIGHTS
eventDict['time'].append(LightSetChannel(At(0), BottomController, [Light1], Channel1))
eventDict['time'].append(LightSetChannel(At(0), BottomController, [Light2], Channel2))

# BOTTOM EFFECTS:
eventDict['time'].append(EffectPerlin(At(0), BottomController, 0, StaticChannel1, StaticChannel10, 1, [Light1,]))
eventDict['time'].append(ChannelAddEffect(At(0), BottomController, Channel1, 0, 0))
eventDict['time'].append(ChannelAddEffect(At(0), BottomController, Channel2, 0, 0))
# Perlin for steptime and amplitude also
eventDict['time'].append(ChannelAddEffect(At(0), BottomController, Channel3, 0, 0))
eventDict['time'].append(ChannelAddEffect(At(0), BottomController, Channel4, 0, 0))

eventDict['time'].append(EffectStrobe(At(0), BottomController, 1, Channel3, Channel4, 1, [Light1,]))
eventDict['time'].append(ChannelAddEffect(At(0), BottomController, Channel1, 1, 1))
eventDict['time'].append(ChannelAddEffect(At(0), BottomController, Channel2, 1, 1))


# TOP
# Channel 1: Light 1 and Light 2

# TOP LIGHTS
eventDict['time'].append(LightSetChannel(At(0), TopController, [Light1, Light2], Channel1))

# TOP EFFECTS
eventDict['time'].append(EffectPerlin(At(0), TopController, 0, StaticChannel1, StaticChannel10, 1, [Light1,]))
eventDict['time'].append(ChannelAddEffect(At(0), TopController, Channel1, 0, 0))
eventDict['time'].append(ChannelSetSetting(At(0), TopController, Channel1, 0))


beginning = 0
# Bottom Lights
# 0-6 Fade In
# 5 onwards strobe
# BOTTOM SETTINGS
duration = 7
decisteps = 30
eventDict['time'].append(SettingBezierDimm(At(beginning), BottomController, 0, 0, 90, int(duration*100/decisteps), decisteps, 0, 1))
eventDict['time'].append(ChannelSetSetting(At(beginning), BottomController, Channel1, 0))
eventDict['time'].append(SettingBezierDimm(At(beginning), BottomController, 1, 0, 90, int(duration*100/decisteps), decisteps, 0, 1))
eventDict['time'].append(ChannelSetSetting(At(beginning), BottomController, Channel2, 1))

# 4-7 strobe fades in
duration = 3
decisteps = 10
eventDict['time'].append(SettingBezierDimm(At(beginning+4), BottomController, 2, 0, 60, int(duration*100/decisteps), decisteps, 0, 100))
eventDict['time'].append(ChannelSetSetting(At(beginning+4), BottomController, Channel3, 2))
eventDict['time'].append(SettingBezierDimm(At(beginning+4), BottomController, 3, 0, 25, int(duration*100/decisteps), decisteps, 0, 100))
eventDict['time'].append(ChannelSetSetting(At(beginning+4), BottomController, Channel4, 3))

# 10:30-14
# Strobe Accelerate, slowly
# Light Fade t oFull Force
duration = 3.5
decisteps = 10
eventDict['time'].append(SettingBezierDimm(At(beginning+10.5), BottomController, 3, 25, 20, int(duration*100/decisteps), decisteps, 0, 100))
eventDict['time'].append(SettingBezierDimm(At(beginning+10.5), BottomController, 0, 90, 100, int(duration*100/decisteps), decisteps, 0, 100))
eventDict['time'].append(SettingBezierDimm(At(beginning+10.5), BottomController, 1, 90, 100, int(duration*100/decisteps), decisteps, 0, 100))

# 16-24
# Strobe higher amplitude
duration = 8
decisteps = 10
eventDict['time'].append(SettingBezierDimm(At(beginning+16), BottomController, 2, 60, 100, int(duration*100/decisteps), decisteps, 0, 100))

# 24-25
# Strobe slower steptime
duration = 1
decisteps = 10
eventDict['time'].append(SettingBezierDimm(At(beginning+24), BottomController, 3, 20, 22, int(duration*100/decisteps), decisteps, 0, 100))

# 28-31
# Top Light Fades in
duration = 3
decisteps = 20
eventDict['time'].append(SettingBezierDimm(At(beginning+28), TopController, 0, 0, 80, int(duration*100/decisteps), decisteps, 0, 100))

# eventDict['time'].append(EffectUpDownVibrato(At(0), TopController, 0, StaticChannel5, StaticChannel10))
# # eventDict['time'].append(EffectStrobe(At(0), controller, 1, StaticChannel10, StaticChannel5, 2, [Light1, Light3]))

# # Strobe Effect
# eventDict['time'].append(ChannelSetChannel(At(0), TopController, Channel2, StaticChannel5))
# eventDict['time'].append(ChannelAddEffect(At(0), TopController, Channel2, 0, 0))
# eventDict['time'].append(EffectStrobe(At(0), TopController, 1, StaticChannel10, Channel2, 1, [Light1, Light3]))

# eventDict['time'].append(ChannelSetChannel(At(0), TopController, Channel1, StaticChannel10))
# eventDict['time'].append(ChannelAddEffect(At(0), TopController, Channel1, 1, 0))
# eventDict['time'].append(LightSetChannel(At(0), TopController, [Light1, Light2, Light3, Light4], Channel1))

# # eventDict['time'].append(ChannelAddEffect(At(2), controller, Channel1, 0, 0))
# # eventDict['time'].append(ChannelAddEffect(At(5), controller, Channel1, 1, 0))


# # eventDict['time'].append(EffectStrobe(At(10), controller, 1, StaticChannel10, StaticChannel5, 2, [Light1, Light3]))
# # eventDict['time'].append(ChannelRemoveEffect(At(10), controller, Channel1, 0))

# # eventDict['time'].append(ChannelAddEffect(At(12), controller, Channel1, 1, 0))

eventDict['time'].append(LightSetChannel(At(35), TopController, [Light1, Light2, Light3, Light4], StaticChannel0))

vd = VisualDriver(eventDict, music=music, usesMotor=False, startTime=0)
vd.start()
