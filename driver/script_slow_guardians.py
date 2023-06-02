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
# Perlin for strobe amplitude also
eventDict['time'].append(ChannelAddEffect(At(0), BottomController, Channel3, 0, 0))

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

eventDict['time'].append(ChannelSetSetting(At(0), TopController, Channel1, 0))

# Vibrato Setup
eventDict['time'].append(SettingStaticLight(At(0), TopController, 1, 0))
eventDict['time'].append(ChannelSetSetting(At(0), TopController, Channel2, 1))
eventDict['time'].append(SettingStaticLight(At(0), TopController, 2, 1))
eventDict['time'].append(ChannelSetSetting(At(0), TopController, Channel3, 2))
eventDict['time'].append(EffectDownVibrato(At(0), TopController, 1, Channel2, Channel3))
eventDict['time'].append(ChannelAddEffect(At(0), TopController, Channel1, 1, 1))


# Strobe Setup
eventDict['time'].append(SettingStaticLight(At(0), TopController, 3, 80))
eventDict['time'].append(ChannelSetSetting(At(0), TopController, Channel4, 3))
eventDict['time'].append(SettingStaticLight(At(0), TopController, 4, 20))
eventDict['time'].append(ChannelSetSetting(At(0), TopController, Channel5, 4))
eventDict['time'].append(EffectStrobe(At(0), TopController, 2, Channel4, Channel5, 1, [Light1,]))


beginning = 0
# Bottom Lights
# 0-7 Fade In
# 5 onwards strobe
# BOTTOM SETTINGS
duration = 1.75
decisteps = 25
eventDict['time'].append(SettingBezierDimm(At(beginning), BottomController, 0, 0, 90, int(duration*100/decisteps), decisteps, 20, 100))
eventDict['time'].append(ChannelSetSetting(At(beginning), BottomController, Channel1, 0))
eventDict['time'].append(SettingBezierDimm(At(beginning), BottomController, 1, 0, 90, int(duration*100/decisteps), decisteps, 20, 100))
eventDict['time'].append(ChannelSetSetting(At(beginning), BottomController, Channel2, 1))

# 4-7 strobe fades in
# 1-1.75
duration = 0.75
decisteps = 15
eventDict['time'].append(SettingBezierDimm(At(beginning+1), BottomController, 2, 0, 30, int(duration*100/decisteps), decisteps, 0, 50))
eventDict['time'].append(ChannelSetSetting(At(beginning+1), BottomController, Channel3, 2))
eventDict['time'].append(SettingStaticLight(At(beginning+1), BottomController, 3, 10))
eventDict['time'].append(ChannelSetSetting(At(beginning+1), BottomController, Channel4, 3))



# 10:30-14
# 2.6-3.5
# Strobe Accelerate, slowly
# Light Fade t oFull Force
duration = 0.88
decisteps = 11
eventDict['time'].append(SettingBezierDimm(At(beginning+2.6), BottomController, 0, 90, 100, int(duration*100/decisteps), decisteps, 0, 100))
eventDict['time'].append(SettingBezierDimm(At(beginning+2.6), BottomController, 1, 90, 100, int(duration*100/decisteps), decisteps, 0, 100))
#amplitude increase
eventDict['time'].append(SettingBezierDimm(At(beginning+2.6), BottomController, 2, 30, 60, int(duration*100/decisteps), decisteps, 0, 50))

#eventDict['time'].append(SettingBezierDimm(At(beginning+2.6), BottomController, 3, 20, 10, int(duration*100/decisteps), decisteps, 0, 100))


# 16-24
# 4-6
# Strobe higher amplitude
duration = 2
decisteps = 10
eventDict['time'].append(SettingBezierDimm(At(beginning+4), BottomController, 2, 60, 100, int(duration*100/decisteps), decisteps, 0, 100))

# 24-25
# 6-6.25
# Strobe slower steptime
duration = 0.25
decisteps = 5
eventDict['time'].append(SettingBezierDimm(At(beginning+6), BottomController, 3, 10, 20, int(duration*100/decisteps), decisteps, 30, 100))

# 25-31
# 6.25-7.75
# strobe softens again
# light goes slightly dimmer
duration = 1.5
decisteps = 30
eventDict['time'].append(SettingBezierDimm(At(beginning+6.25), BottomController, 2, 100, 40, int(duration*100/decisteps), decisteps, 0, 100))
eventDict['time'].append(SettingBezierDimm(At(beginning+6.25), BottomController, 3, 20, 10, int(duration*100/decisteps), decisteps, 0, 60))
eventDict['time'].append(SettingBezierDimm(At(beginning+6.25), BottomController, 0, 100, 90, int(duration*100/decisteps), decisteps, 0, 100))
eventDict['time'].append(SettingBezierDimm(At(beginning+6.25), BottomController, 1, 100, 90, int(duration*100/decisteps), decisteps, 0, 100))

# 28-31
# 7-7.75
# Top Light Fades in
# Vibrato Fade In
duration = 0.75
decisteps = 15
eventDict['time'].append(SettingBezierDimm(At(beginning+7), TopController, 0, 0, 90, int(duration*100/decisteps), decisteps, 0, 100))
eventDict['time'].append(SettingBezierDimm(At(beginning+7), TopController, 1, 0, 40, int(duration*100/decisteps), decisteps, 0, 100))

# 29-33
# 7.25-8.25
# Bottom Fade Down
duration = 0.75
decisteps = 15
eventDict['time'].append(SettingBezierDimm(At(beginning+7.25), BottomController, 0, 90, 20, int(duration*100/decisteps), decisteps, 0, 100))
eventDict['time'].append(SettingBezierDimm(At(beginning+7.25), BottomController, 1, 90, 20, int(duration*100/decisteps), decisteps, 0, 100))

# 31-33
# 7.75-8.25
# Top Fadeout
duration = 0.5
decisteps = 25
eventDict['time'].append(SettingBezierDimm(At(beginning+7.75), TopController, 0, 90, 15, int(duration*100/decisteps), decisteps, 0, 100))
eventDict['time'].append(SettingBezierDimm(At(beginning+7.75), TopController, 1, 40, 5, int(duration*100/decisteps), decisteps, 0, 100))


# 34
# 8.5
# Top Strobe
eventDict['time'].append(ChannelAddEffect(At(beginning+8.5), TopController, Channel1, 2, 2))

# 34-36
# 8.5-9
# And Fade in
duration = 0.5
decisteps = 25
eventDict['time'].append(SettingBezierDimm(At(beginning+8.5), TopController, 0, 15, 90, int(duration*100/decisteps), decisteps, 0, 100))
eventDict['time'].append(SettingBezierDimm(At(beginning+8.5), TopController, 1, 5, 40, int(duration*100/decisteps), decisteps, 0, 100))


# 35-36
# 8.75-9
# Top Strobe increases steptime & amplitude
# Top Reduce Vibrato
duration = 0.25
decisteps = 5
eventDict['time'].append(SettingBezierDimm(At(beginning+8.75), TopController, 3, 80, 90, int(duration*100/decisteps), decisteps, 0, 100))
eventDict['time'].append(SettingBezierDimm(At(beginning+8.75), TopController, 4, 20, 10, int(duration*100/decisteps), decisteps, 0, 60))
eventDict['time'].append(SettingBezierDimm(At(beginning+8.75), TopController, 1, 40, 20, int(duration*100/decisteps), decisteps, 0, 100))

# 37.5 - 39
# 9.375-9.75
# Reduce amplitude
# Reduce steptime to almost nothing
duration = 0.36
decisteps = 9
eventDict['time'].append(SettingBezierDimm(At(beginning+9.375), TopController, 3, 90, 50, int(duration*100/decisteps), decisteps, 0, 100))
#eventDict['time'].append(SettingBezierDimm(At(beginning+9.375), TopController, 4, 20, 2, int(duration*100/decisteps), decisteps, 0, 100))

# 38.5-40
# 9.625-10
# Vibrato Fade In Delicately
duration = 0.38
decisteps = 19
eventDict['time'].append(SettingBezierDimm(At(beginning+9.625), TopController, 1, 20, 40, int(duration*100/decisteps), decisteps, 0, 100))

# 43-53
# 10.75-13.25
# Top Strobe Increase steptime
duration = 2.5
decisteps = 50
#amplitude instead
eventDict['time'].append(SettingBezierDimm(At(beginning+9.375), TopController, 3, 50, 70, int(duration*100/decisteps), decisteps, 0, 100))

#eventDict['time'].append(SettingBezierDimm(At(beginning+10.75), TopController, 4, 2, 10, int(duration*100/decisteps), decisteps, 100, 100))

# 44-45
# 11-11.25
# Vibrato Fade Out
duration = 0.25
decisteps = 5
eventDict['time'].append(SettingBezierDimm(At(beginning+11), TopController, 1, 40, 10, int(duration*100/decisteps), decisteps, 0, 100))

# 53 - 55
# 13.25-13.75
# Top Strobe Increase amplitude
duration = 0.5
decisteps = 10
eventDict['time'].append(SettingBezierDimm(At(beginning+13.25), TopController, 3, 70, 100, int(duration*100/decisteps), decisteps, 0, 100))

# 60-61
# 15-15.25
# Vibrato Fade In
duration = 0.25
decisteps = 10
eventDict['time'].append(SettingBezierDimm(At(beginning+15), TopController, 1, 10, 40, int(duration*100/decisteps), decisteps, 0, 100))

# 62 Vibrato Off
# 15.5
eventDict['time'].append(SettingStaticLight(At(beginning+15.5), TopController, 1, 0))

# 62-65
# 15.5-16.25
# Bottom Fade In
# Top Fade Out
duration = 0.75
decisteps = 25
eventDict['time'].append(SettingBezierDimm(At(beginning+15.5), BottomController, 0, 20, 50, int(duration*100/decisteps), decisteps, 0, 100))
eventDict['time'].append(SettingBezierDimm(At(beginning+15.5), BottomController, 1, 20, 50, int(duration*100/decisteps), decisteps, 0, 100))
eventDict['time'].append(SettingBezierDimm(At(beginning+15.5), TopController, 0, 90, 15, int(duration*100/decisteps), decisteps, 0, 100))

# 67 - 68
# 16.75-17
# Bottom Fade OUt
# Top Fade In (Maybe Only Single light)
duration = 0.25
decisteps = 5
eventDict['time'].append(SettingBezierDimm(At(beginning+16.75), BottomController, 0, 50, 20, int(duration*100/decisteps), decisteps, 0, 100))
eventDict['time'].append(SettingBezierDimm(At(beginning+16.75), BottomController, 1, 50, 20, int(duration*100/decisteps), decisteps, 0, 100))
eventDict['time'].append(SettingBezierDimm(At(beginning+16.75), TopController, 0, 15, 40, int(duration*100/decisteps), decisteps, 0, 100))

# 73-75
# 18.25-18.75
# Bottom Fade In
# Top Fade OUt Completely
duration = 0.5
decisteps = 10
eventDict['time'].append(SettingBezierDimm(At(beginning+18.25), BottomController, 0, 20, 60, int(duration*100/decisteps), decisteps, 0, 100))
eventDict['time'].append(SettingBezierDimm(At(beginning+18.25), BottomController, 1, 20, 60, int(duration*100/decisteps), decisteps, 0, 100))
eventDict['time'].append(SettingBezierDimm(At(beginning+18.25), BottomController, 2, 40, 60, int(duration*100/decisteps), decisteps, 0, 100))
eventDict['time'].append(SettingBezierDimm(At(beginning+18.25), TopController, 0, 50, 0, int(duration*100/decisteps), decisteps, 0, 100))

# 75 - 84
# 18.75 - 21.75
# Bottom Fade Out Completely
duration = 3
decisteps = 50
eventDict['time'].append(SettingBezierDimm(At(beginning+18.75), BottomController, 0, 60, 0, int(duration*100/decisteps), decisteps, 0, 100))
eventDict['time'].append(SettingBezierDimm(At(beginning+18.75), BottomController, 1, 60, 0, int(duration*100/decisteps), decisteps, 0, 100))


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

eventDict['time'].append(LightSetChannel(At(23), TopController, [Light1, Light2, Light3, Light4], StaticChannel0))

vd = VisualDriver(eventDict, music=music, usesMotor=False, startTime=0)
vd.start()
