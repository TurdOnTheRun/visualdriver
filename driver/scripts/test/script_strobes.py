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
eventDict['time'].append(ChannelSetChannel(At(0), BottomController, Channel1, StaticChannel8))
eventDict['time'].append(LightSetChannel(At(0), BottomController, [Light1, Light2], Channel1))

# BOTTOM EFFECTS:
eventDict['time'].append(EffectPerlin(At(0), BottomController, 0, StaticChannel1, StaticChannel10, 1, [Light1,]))
eventDict['time'].append(ChannelAddEffect(At(0), BottomController, Channel1, 0, 0))
eventDict['time'].append(ChannelAddEffect(At(0), BottomController, Channel2, 0, 0))

eventDict['time'].append(SettingStaticLight(At(0),BottomController,1,0))
eventDict['time'].append(ChannelSetSetting(At(0), BottomController, Channel2, 1))
eventDict['time'].append(EffectStrobe(At(0), BottomController, 1, StaticChannel9, Channel2, 1, [Light1,]))


beginning = 0


duration = 4
decisteps = 20
eventDict['time'].append(ChannelAddEffect(At(beginning+4), BottomController, Channel1, 1, 1))
eventDict['time'].append(SettingBezierDimm(At(beginning+4), BottomController, 1, 0, 10, int(duration*100/decisteps), decisteps, 0, 100))

duration = 4
decisteps = 20
eventDict['time'].append(SettingBezierDimm(At(beginning+12), BottomController, 1, 10, 20, int(duration*100/decisteps), decisteps, 0, 100))

duration = 4
decisteps = 20
eventDict['time'].append(SettingBezierDimm(At(beginning+20), BottomController, 1, 20, 30, int(duration*100/decisteps), decisteps, 0, 100))

duration = 4
decisteps = 20
eventDict['time'].append(SettingBezierDimm(At(beginning+28), BottomController, 1, 30, 40, int(duration*100/decisteps), decisteps, 0, 100))

duration = 4
decisteps = 20
eventDict['time'].append(SettingBezierDimm(At(beginning+36), BottomController, 1, 40, 50, int(duration*100/decisteps), decisteps, 0, 100))

duration = 4
decisteps = 20
eventDict['time'].append(SettingBezierDimm(At(beginning+44), BottomController, 1, 50, 60, int(duration*100/decisteps), decisteps, 0, 100))


eventDict['time'].append(LightSetChannel(At(52), BottomController, [Light1, Light2], StaticChannel0))

vd = VisualDriver(eventDict, usesMotor=False, startTime=0)
vd.start()
