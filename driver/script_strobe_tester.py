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


# BOTTOM

BottomMainSetting = 0
BottomMainChannel = Channel12
BottomSteptimeChannel = Channel13
BottomStrobeEffect = 0


# Bottom Light
eventDict['time'].append(SettingStatic(At(0), BottomController, BottomMainSetting, 95))
eventDict['time'].append(ChannelSetSetting(At(0), BottomController, BottomMainChannel, BottomMainSetting))
eventDict['time'].append(ChannelSetStatic(At(0), BottomController, BottomSteptimeChannel, 100))
eventDict['time'].append(EffectSequencedLightStrobe(At(0), BottomController, BottomStrobeEffect, BottomSteptimeChannel, 43431212))
eventDict['time'].append(ChannelAddEffect(At(0), BottomController, BottomMainChannel, BottomStrobeEffect, 0))
eventDict['time'].append(LightSetChannel(At(0), BottomController, [Light1, Light2, Light3, Light4], BottomMainChannel))

eventDict['time'].append(ChannelSetStatic(At(10), BottomController, BottomMainChannel, 0))


vd = VisualDriver(eventDict, startTime=0, isTake=False)
vd.start()