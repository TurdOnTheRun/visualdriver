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

controll = TopController
lights = [Light1,]
timePerTest = 5

t=0


lightChannel = Channel10
# eventDict['time'].append(SettingStaticLight(At(t), controll, 0, 0))
eventDict['time'].append(SettingStaticLight(At(t), BottomController, 0, 0))

# eventDict['time'].append(ChannelSetSetting(At(t), controll, lightChannel, 0))
eventDict['time'].append(ChannelSetSetting(At(t), BottomController, lightChannel, 0))

# eventDict['time'].append(LightSetChannel(At(t), controll, lights, lightChannel))
eventDict['time'].append(LightSetChannel(At(t), BottomController, [Light2,Light1], lightChannel))
# eventDict['time'].append(SettingStaticLight(At(t), controll, 0, 80))
eventDict['time'].append(SettingStaticLight(At(t), BottomController, 0, 70))
eventDict['time'].append(TriggerAngle(At(t), TRIGGER_SONY_DOWN))
t=0.5
eventDict['time'].append(TriggerAngle(At(t), TRIGGER_SONY_UP))


vd = VisualDriver(eventDict, startTime=0, usesTrigger=True)
vd.start()