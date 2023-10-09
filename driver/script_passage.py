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

eventDict['time'].append(ChannelSetStatic(At(0), BottomController, Channel3, 100))
eventDict['time'].append(EffectDownVibrato(At(0), BottomController, 0, Channel2, Channel2))
eventDict['time'].append(ChannelAddEffect(At(0), BottomController, Channel3, 0, 0))
eventDict['time'].append(LightSetChannel(At(0), BottomController, [Light1,], Channel3))


eventDict['time'].append(ChannelSetStatic(At(0), BottomController, Channel4, 50))
eventDict['time'].append(EffectUpDown(At(0), BottomController, 1, Channel3, Channel2, 200))

eventDict['time'].append(LightSetChannel(At(5), BottomController, [Light2,], Channel4))
eventDict['time'].append(ChannelAddEffect(At(8), BottomController, Channel4, 1, 0))

eventDict['time'].append(ChannelRemoveEffects(At(20), BottomController, Channel3))
eventDict['time'].append(ChannelRemoveEffects(At(23), BottomController, Channel3))


vd = VisualDriver(eventDict, startTime=0)
vd.start()