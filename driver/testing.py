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

eventDict['time'].append(ChannelSetChannel(At(0), TopController, Channel1, StaticChannel6))
eventDict['time'].append(LightSetChannel(At(0), TopController, [Light1, Light2, Light3, Light4], Channel1))

eventDict['time'].append(EffectUpDownVibrato(At(5), TopController, 0, StaticChannel5, StaticChannel5))
eventDict['time'].append(ChannelAddEffect(At(5), TopController, Channel1, 0, 0))

eventDict['time'].append(EffectStrobe(At(10), TopController, 1, StaticChannel10, StaticChannel5, 2, [Light1, Light3]))
eventDict['time'].append(ChannelRemoveEffect(At(10), TopController, Channel1, 0))

eventDict['time'].append(ChannelAddEffect(At(12), TopController, Channel1, 1, 0))
eventDict['time'].append(LightSetChannel(At(15), TopController, [Light1, Light2, Light3, Light4], StaticChannel0))


vd = VisualDriver(eventDict, startTime=0)
vd.start()