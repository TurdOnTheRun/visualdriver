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
# Channel 2: Vibrato amplitude
# Channel 3: Vibrato steptime
# Channel 4: Strobe amplitude
# Channel 5: Strobe steptime

# Setting 0: Lights through Channel 1
# Setting 1: Vibrato amplitude
# Setting 2: Vibrato steptime
# Setting 3: Strobe amplitude
# Setting 4: Strobe steptime

# TOP LIGHTS
eventDict['time'].append(LightSetChannel(At(0), TopController, [Light1, Light2], Channel1))

# TOP EFFECTS
eventDict['time'].append(EffectPerlin(At(0), TopController, 0, StaticChannel1, StaticChannel10, 1, [Light1,]))
eventDict['time'].append(ChannelAddEffect(At(0), TopController, Channel1, 0, 0))
eventDict['time'].append(ChannelAddEffect(At(0), TopController, Channel2, 0, 0))
eventDict['time'].append(ChannelAddEffect(At(0), TopController, Channel3, 0, 0))
eventDict['time'].append(ChannelAddEffect(At(0), TopController, Channel4, 0, 0))

eventDict['time'].append(ChannelSetSetting(At(0), TopController, Channel1, 0))

# Vibrato Setup
eventDict['time'].append(SettingStaticLight(At(0), TopController, 1, 0))
eventDict['time'].append(ChannelSetSetting(At(0), TopController, Channel2, 1))
eventDict['time'].append(SettingStaticLight(At(0), TopController, 2, 4))
eventDict['time'].append(ChannelSetSetting(At(0), TopController, Channel3, 2))
eventDict['time'].append(EffectDownVibrato(At(0), TopController, 1, Channel2, Channel3))
eventDict['time'].append(ChannelAddEffect(At(0), TopController, Channel1, 1, 1))


# Strobe Setup
eventDict['time'].append(SettingStaticLight(At(0), TopController, 3, 80))
eventDict['time'].append(ChannelSetSetting(At(0), TopController, Channel4, 3))
eventDict['time'].append(SettingStaticLight(At(0), TopController, 4, 26))
eventDict['time'].append(ChannelSetSetting(At(0), TopController, Channel5, 4))
eventDict['time'].append(EffectStrobe(At(0), TopController, 2, Channel4, Channel5, 1, []))


beginning = 0
# Bottom Lights
# 0-7 Fade In
# 5 onwards strobe
# BOTTOM SETTINGS
duration = 7
decisteps = 30
eventDict['time'].append(SettingBezierDimm(At(beginning), BottomController, 0, 0, 90, int(duration*100/decisteps), decisteps, 0, 0))
eventDict['time'].append(ChannelSetSetting(At(beginning), BottomController, Channel1, 0))
eventDict['time'].append(SettingBezierDimm(At(beginning), BottomController, 1, 0, 90, int(duration*100/decisteps), decisteps, 0, 0))
eventDict['time'].append(ChannelSetSetting(At(beginning), BottomController, Channel2, 1))

# 4-7 strobe fades in
duration = 3
decisteps = 10
eventDict['time'].append(SettingBezierDimm(At(beginning+4), BottomController, 2, 0, 60, int(duration*100/decisteps), decisteps, 0, 100))
eventDict['time'].append(ChannelSetSetting(At(beginning+4), BottomController, Channel3, 2))
eventDict['time'].append(SettingBezierDimm(At(beginning+4), BottomController, 3, 0, 24, int(duration*100/decisteps), decisteps, 0, 100))
eventDict['time'].append(ChannelSetSetting(At(beginning+4), BottomController, Channel4, 3))

# 10:30-14
# Strobe Accelerate, slowly
# Light Fade t oFull Force
duration = 3.5
decisteps = 10
eventDict['time'].append(SettingBezierDimm(At(beginning+10.5), BottomController, 3, 25, 18, int(duration*100/decisteps), decisteps, 0, 100))
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
eventDict['time'].append(SettingBezierDimm(At(beginning+24), BottomController, 3, 18, 20, int(duration*100/decisteps), decisteps, 0, 100))

# 25-31
# strobe softens again
# light goes slightly dimmer
duration = 6
decisteps = 20
eventDict['time'].append(SettingBezierDimm(At(beginning+25), BottomController, 2, 100, 60, int(duration*100/decisteps), decisteps, 0, 100))
eventDict['time'].append(SettingBezierDimm(At(beginning+25), BottomController, 3, 20, 18, int(duration*100/decisteps), decisteps, 0, 100))
eventDict['time'].append(SettingBezierDimm(At(beginning+25), BottomController, 0, 100, 90, int(duration*100/decisteps), decisteps, 0, 100))
eventDict['time'].append(SettingBezierDimm(At(beginning+25), BottomController, 1, 100, 90, int(duration*100/decisteps), decisteps, 0, 100))

# 28-31
# Top Light Fades in
# Vibrato Fade In
duration = 3
decisteps = 20
eventDict['time'].append(SettingBezierDimm(At(beginning+28), TopController, 0, 0, 90, int(duration*100/decisteps), decisteps, 0, 100))
eventDict['time'].append(SettingBezierDimm(At(beginning+28), TopController, 1, 0, 40, int(duration*100/decisteps), decisteps, 0, 100))

# 29-33
# Bottom Fade Down
duration = 3
decisteps = 20
eventDict['time'].append(SettingBezierDimm(At(beginning+29), BottomController, 0, 90, 20, int(duration*100/decisteps), decisteps, 0, 100))
eventDict['time'].append(SettingBezierDimm(At(beginning+29), BottomController, 1, 90, 20, int(duration*100/decisteps), decisteps, 0, 100))

# 31-33
# Top Fadeout
duration = 2
decisteps = 20
eventDict['time'].append(SettingBezierDimm(At(beginning+31), TopController, 0, 90, 15, int(duration*100/decisteps), decisteps, 0, 100))

# 34
# Top Strobe
eventDict['time'].append(ChannelAddEffect(At(beginning+34), TopController, Channel1, 2, 2))

# 34-36
# And Fade in
duration = 2
decisteps = 20
eventDict['time'].append(SettingBezierDimm(At(beginning+34), TopController, 0, 15, 90, int(duration*100/decisteps), decisteps, 0, 100))

# 35-36
# Top Strobe increases steptime & amplitude
# Top Reduce Vibrato
duration = 1
decisteps = 10
eventDict['time'].append(SettingBezierDimm(At(beginning+35), TopController, 3, 80, 90, int(duration*100/decisteps), decisteps, 0, 100))
eventDict['time'].append(SettingBezierDimm(At(beginning+35), TopController, 4, 26, 28, int(duration*100/decisteps), decisteps, 0, 100))
eventDict['time'].append(SettingBezierDimm(At(beginning+35), TopController, 1, 40, 20, int(duration*100/decisteps), decisteps, 0, 100))

# 37.5 - 39
# Reduce amplitude
# Reduce steptime to almost nothing
duration = 1.5
decisteps = 10
eventDict['time'].append(SettingBezierDimm(At(beginning+37.5), TopController, 3, 90, 60, int(duration*100/decisteps), decisteps, 0, 100))
eventDict['time'].append(SettingBezierDimm(At(beginning+37.5), TopController, 4, 28, 10, int(duration*100/decisteps), decisteps, 0, 100))

# 38.5-40
# Vibrato Fade In Delicately
duration = 1.5
decisteps = 10
eventDict['time'].append(SettingBezierDimm(At(beginning+38.5), TopController, 1, 20, 40, int(duration*100/decisteps), decisteps, 0, 100))

# 43 - 53
# Top Strobe Increase steptime
duration = 10
decisteps = 30
eventDict['time'].append(SettingBezierDimm(At(beginning+43), TopController, 4, 10, 25, int(duration*100/decisteps), decisteps, 0, 100))

# 44-45
# Vibrato Fade Out
duration = 1
decisteps = 10
eventDict['time'].append(SettingBezierDimm(At(beginning+44), TopController, 1, 40, 10, int(duration*100/decisteps), decisteps, 0, 100))

# 53 - 55
# Top Strobe Increase amplitude
duration = 2
decisteps = 10
eventDict['time'].append(SettingBezierDimm(At(beginning+53), TopController, 3, 60, 90, int(duration*100/decisteps), decisteps, 0, 100))

# 60-61
# Vibrato Fade In
duration = 1
decisteps = 10
eventDict['time'].append(SettingBezierDimm(At(beginning+60), TopController, 1, 10, 40, int(duration*100/decisteps), decisteps, 0, 100))

# 62 Vibrato Off
duration = 1
decisteps = 10
eventDict['time'].append(SettingStaticLight(At(beginning+62), TopController, 1, 0))

# 62-65
# Bottom Fade In
# Top Fade Out
duration = 3
decisteps = 20
eventDict['time'].append(SettingBezierDimm(At(beginning+62), BottomController, 0, 20, 50, int(duration*100/decisteps), decisteps, 0, 100))
eventDict['time'].append(SettingBezierDimm(At(beginning+62), BottomController, 1, 20, 50, int(duration*100/decisteps), decisteps, 0, 100))
eventDict['time'].append(SettingBezierDimm(At(beginning+62), TopController, 0, 90, 15, int(duration*100/decisteps), decisteps, 0, 100))

# 67 - 68
# Bottom Fade OUt
# Top Fade In (Maybe Only Single light)
duration = 1
decisteps = 10
eventDict['time'].append(SettingBezierDimm(At(beginning+67), BottomController, 0, 50, 20, int(duration*100/decisteps), decisteps, 0, 100))
eventDict['time'].append(SettingBezierDimm(At(beginning+67), BottomController, 1, 50, 20, int(duration*100/decisteps), decisteps, 0, 100))
eventDict['time'].append(SettingBezierDimm(At(beginning+67), TopController, 0, 15, 40, int(duration*100/decisteps), decisteps, 0, 100))

# 73-75
# Bottom Fade In
# Top Fade OUt Completely
duration = 2
decisteps = 10
eventDict['time'].append(SettingBezierDimm(At(beginning+73), BottomController, 0, 20, 60, int(duration*100/decisteps), decisteps, 0, 100))
eventDict['time'].append(SettingBezierDimm(At(beginning+73), BottomController, 1, 20, 60, int(duration*100/decisteps), decisteps, 0, 100))
eventDict['time'].append(SettingBezierDimm(At(beginning+73), TopController, 0, 50, 0, int(duration*100/decisteps), decisteps, 0, 100))

# 75 - 84
# Bottom Fade Out Completely
duration = 9
decisteps = 30
eventDict['time'].append(SettingBezierDimm(At(beginning+75), BottomController, 0, 60, 0, int(duration*100/decisteps), decisteps, 0, 100))
eventDict['time'].append(SettingBezierDimm(At(beginning+75), BottomController, 1, 60, 0, int(duration*100/decisteps), decisteps, 0, 100))


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

eventDict['time'].append(LightSetChannel(At(86), TopController, [Light1, Light2, Light3, Light4], StaticChannel0))

vd = VisualDriver(eventDict, music=music, usesMotor=False, startTime=0)
vd.start()
