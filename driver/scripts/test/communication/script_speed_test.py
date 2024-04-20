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
eventDict['time'].append(SettingStatic(At(0), BottomController, MainSetting, 30))
eventDict['time'].append(SettingStatic(At(0), TopController, MainSetting, 0))

eventDict['time'].append(ChannelSetSetting(At(0), BottomController, MainChannel, MainSetting))
eventDict['time'].append(ChannelSetSetting(At(0), TopController, MainChannel, MainSetting))

eventDict['time'].append(ChannelSetStatic(At(0), BottomController, DarkstepChannel, 0))
eventDict['time'].append(ChannelSetStatic(At(0), TopController, DarkstepChannel, 0))

eventDict['time'].append(ChannelSetStatic(At(0), BottomController, SteptimeChannel, 67))
eventDict['time'].append(ChannelSetStatic(At(0), TopController, SteptimeChannel, 67))

eventDict['time'].append(LightSetChannel(At(0), BottomController, [Light3,], MainChannel))
eventDict['time'].append(LightSetChannel(At(0), TopController, [Light3,], MainChannel))


eventDict['time'].append(SettingStatic(At(3), BottomController, MainSetting, 0))

# 3
eventDict['time'].append(SettingStatic(At(4), TopController, MainSetting, 30))
eventDict['time'].append(SettingStatic(At(4), BottomController, MainSetting, 30))


# 5
eventDict['time'].append(SettingStatic(At(7), TopController, MainSetting, 0))
eventDict['time'].append(SettingStatic(At(7), BottomController, MainSetting, 0))
eventDict['time'].append(SettingStaticFlash(At(8), TopController, MainSetting, 30, 0, 255))
eventDict['time'].append(SettingStaticFlash(At(8), BottomController, MainSetting, 30, 0, 255))

# 7
eventDict['time'].append(SettingStatic(At(9), TopController, MainSetting, 0))
eventDict['time'].append(SettingStatic(At(9), BottomController, MainSetting, 0))
eventDict['time'].append(SettingStaticMachine(At(10), TopController, MainSetting, 30, 0, 255, 1, 1))
eventDict['time'].append(SettingStaticMachine(At(10), BottomController, MainSetting, 30, 0, 255, 1, 1))

# 8
eventDict['time'].append(SettingStatic(At(11), TopController, MainSetting, 0))
eventDict['time'].append(SettingStatic(At(11), BottomController, MainSetting, 0))
eventDict['time'].append(SettingBezierDimm(At(12), TopController, MainSetting, 0, 30, 0, 0, 100, 100))
eventDict['time'].append(SettingBezierDimm(At(12), BottomController, MainSetting, 0, 30, 0, 0, 100, 100))

# 9
eventDict['time'].append(SettingStatic(At(13), TopController, MainSetting, 0))
eventDict['time'].append(SettingStatic(At(13), BottomController, MainSetting, 0))
eventDict['time'].append(SettingBezierAfterFlash(At(14), TopController, MainSetting, 30, 0, 0, 0, 100, 100, 50))
eventDict['time'].append(SettingBezierAfterFlash(At(14), BottomController, MainSetting, 30, 0, 0, 0, 100, 100, 50))

eventDict['time'].append(SettingStatic(At(15), TopController, MainSetting, 0))
eventDict['time'].append(SettingStatic(At(15), BottomController, MainSetting, 0))


vd = VisualDriver(eventDict, startTime=0, isTake=False)
vd.start()