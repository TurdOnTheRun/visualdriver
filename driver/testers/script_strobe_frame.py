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
eventDict['time'].append(ChannelSetChannel(At(0), BottomController, Channel1, StaticChannel10))
eventDict['time'].append(LightSetChannel(At(0), BottomController, [Light1, Light2], Channel1))

# BOTTOM EFFECTS:

eventDict['time'].append(SettingStaticLight(At(0),BottomController, 0, 40))
eventDict['time'].append(ChannelSetSetting(At(0), BottomController, Channel2, 0))
eventDict['time'].append(EffectStrobe(At(0), BottomController, 0, StaticChannel10, Channel2, 1, [Light1,]))
eventDict['time'].append(ChannelAddEffect(At(0), BottomController, Channel1, 0, 0))

eventDict['time'].append(ChannelSetChannel(At(15), BottomController, Channel1, StaticChannel0))

vd = VisualDriver(eventDict, usesMotor=False, startTime=0)
vd.start()
