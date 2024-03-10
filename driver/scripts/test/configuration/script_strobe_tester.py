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

MainSetting = 0
MainChannel = Channel12
SteptimeChannel = Channel13
DarkstepChannel = Channel14
StrobeEffect = 0


# Bottom Light
eventDict['time'].append(SettingStatic(At(0), BottomController, MainSetting, 95))
eventDict['time'].append(SettingStatic(At(0), TopController, MainSetting, 95))


eventDict['time'].append(ChannelSetStatic(At(0), BottomController, DarkstepChannel, 0))
eventDict['time'].append(ChannelSetStatic(At(0), TopController, DarkstepChannel, 0))


eventDict['time'].append(ChannelSetSetting(At(0), BottomController, MainChannel, MainSetting))
eventDict['time'].append(ChannelSetSetting(At(0), TopController, MainChannel, MainSetting))

eventDict['time'].append(ChannelSetStatic(At(0), BottomController, SteptimeChannel, 34))
eventDict['time'].append(ChannelSetStatic(At(0), TopController, SteptimeChannel, 34))

eventDict['time'].append(EffectSequencedLightStrobe(At(0), BottomController, StrobeEffect, SteptimeChannel, DarkstepChannel, 46464646))
eventDict['time'].append(EffectSequencedLightStrobe(At(0), TopController, StrobeEffect, SteptimeChannel, DarkstepChannel, 46464646))

eventDict['time'].append(LightSetChannel(At(0), BottomController, [Light1, Light2, Light3, Light4], MainChannel))
eventDict['time'].append(LightSetChannel(At(0), TopController, [Light1, Light2, Light3, Light4], MainChannel))

eventDict['time'].append(ChannelAddEffect(At(3), BottomController, MainChannel, StrobeEffect, 0))
eventDict['time'].append(ChannelAddEffect(At(3), TopController, MainChannel, StrobeEffect, 0))

eventDict['time'].append(ChannelSetStatic(At(13), BottomController, MainChannel, 0))


vd = VisualDriver(eventDict, startTime=0, isTake=False)
vd.start()