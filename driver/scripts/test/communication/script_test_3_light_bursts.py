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
MessageIndicatorChannel = Channel16
SecondIndicatorChannel = Channel17

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
eventDict['time'].append(LightSetChannel(At(0), TopController, [Light4,], MainChannel))


eventDict['time'].append(SettingStatic(At(4), BottomController, MainSetting, 0))
eventDict['time'].append(SettingStatic(At(4), TopController, MainSetting, 0)) #This improves performance of top light for some reason. It removes the huge delay on the first Setting


eventDict['time'].append(SettingStaticMachine(At(5), TopController, MainSetting, 30, 0, 125, 125, 3))
eventDict['time'].append(SettingStaticMachine(At(5), BottomController, MainSetting, 30, 0, 125, 125, 3))

eventDict['time'].append(SettingStaticMachine(At(7), TopController, MainSetting, 30, 0, 125, 125, 3))
eventDict['time'].append(SettingStaticMachine(At(7), BottomController, MainSetting, 30, 0, 125, 125, 3))

eventDict['time'].append(SettingStaticMachine(At(9), TopController, MainSetting, 30, 0, 125, 125, 3))
eventDict['time'].append(SettingStaticMachine(At(9), BottomController, MainSetting, 30, 0, 125, 125, 3))

eventDict['time'].append(SettingStatic(At(11), TopController, MainSetting, 0))
eventDict['time'].append(SettingStatic(At(11), BottomController, MainSetting, 0))


vd = VisualDriver(eventDict, startTime=0, isTake=False)
vd.start()