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
MessageIndicatorChannel = Channel16 #This needs to be enabled on the Arduinos
SecondIndicatorChannel = Channel17 #This needs to be enabled on the Arduinos

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


eventDict['time'].append(LightSetChannel(At(0), BottomController, [Light4,], MessageIndicatorChannel))
eventDict['time'].append(LightSetChannel(At(0), TopController, [Light3,], MessageIndicatorChannel))


eventDict['time'].append(SettingStatic(At(5), TopController, MainSetting, 30))
eventDict['time'].append(SettingStatic(At(5), BottomController, MainSetting, 30))

eventDict['time'].append(SettingStatic(At(6), TopController, MainSetting, 30))
eventDict['time'].append(SettingStatic(At(6), BottomController, MainSetting, 30))

eventDict['time'].append(SettingStatic(At(7), TopController, MainSetting, 30))
eventDict['time'].append(SettingStatic(At(7), BottomController, MainSetting, 30))

eventDict['time'].append(SettingStatic(At(8), TopController, MainSetting, 30))
eventDict['time'].append(SettingStatic(At(8), BottomController, MainSetting, 30))

eventDict['time'].append(SettingStatic(At(9), TopController, MainSetting, 30))
eventDict['time'].append(SettingStatic(At(9), BottomController, MainSetting, 30))

eventDict['time'].append(SettingStatic(At(10), TopController, MainSetting, 30))
eventDict['time'].append(SettingStatic(At(10), BottomController, MainSetting, 30))

eventDict['time'].append(SettingStatic(At(11), TopController, MainSetting, 30))
eventDict['time'].append(SettingStatic(At(11), BottomController, MainSetting, 30))

eventDict['time'].append(SettingStatic(At(12), TopController, MainSetting, 30))
eventDict['time'].append(SettingStatic(At(12), BottomController, MainSetting, 30))

eventDict['time'].append(SettingStatic(At(13), TopController, MainSetting, 30))
eventDict['time'].append(SettingStatic(At(13), BottomController, MainSetting, 30))

eventDict['time'].append(SettingStatic(At(14), TopController, MainSetting, 30))
eventDict['time'].append(SettingStatic(At(14), BottomController, MainSetting, 30))

eventDict['time'].append(MusicStart(At(15), 0))

vd = VisualDriver(eventDict, startTime=0, isTake=False)
vd.start()