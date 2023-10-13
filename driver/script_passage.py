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

controll = BottomController

eventDict['time'].append(SettingStaticLight(At(0), controll, 0, 80))
eventDict['time'].append(ChannelSetSetting(At(0), controll, Channel10, 0))
eventDict['time'].append(LightSetChannel(At(0), controll, [Light1,], Channel10))

eventDict['time'].append(SettingStaticFlash(At(3), controll, 0, 100, 30, 255))
eventDict['time'].append(SettingStaticMachine(At(5), controll, 0, 100, 0, 80, 255, 5))
eventDict['time'].append(SettingLinearDimm(At(10), controll, 0, 0, 100, 20))
eventDict['time'].append(SettingBezierDimm(At(13), controll, 0, 100, 0, 20, 10, 1, 100))
eventDict['time'].append(SettingStaticLight(At(16), controll, 0, 10))
eventDict['time'].append(SettingSinWave(At(19), controll, 0, StaticChannel5, StaticChannel80, StaticChannel5, StaticChannel40))


eventDict['time'].append(ChannelSetStatic(At(23), controll, StaticChannel0, 0))


vd = VisualDriver(eventDict, startTime=0)
vd.start()