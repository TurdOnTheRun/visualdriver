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
timePerTest = 5

t=0

eventDict['time'].append(SettingStatic(At(t), controll, 0, 80))
eventDict['time'].append(ChannelSetSetting(At(t), controll, Channel10, 0))
eventDict['time'].append(LightSetChannel(At(t), controll, [Light1,], Channel10))

# t += timePerTest
# eventDict['time'].append(SettingStaticFlash(At(t), controll, 0, 100, 30, 255))
# t += timePerTest
# eventDict['time'].append(SettingStaticMachine(At(t), controll, 0, 100, 0, 80, 255, 5))
# t += timePerTest
# eventDict['time'].append(SettingLinearDimm(At(t), controll, 0, 0, 100, 20))
# t += timePerTest
# eventDict['time'].append(SettingBezierDimm(At(t), controll, 0, 100, 0, 20, 10, 1, 100))
# t += timePerTest
# eventDict['time'].append(SettingStatic(At(t), controll, 0, 10))
# t += timePerTest
# eventDict['time'].append(SettingSinWave(At(t), controll, 0, StaticChannel5, StaticChannel80, StaticChannel5, StaticChannel40))
# t += timePerTest
# eventDict['time'].append(SettingLinearWave(At(t), controll, 0, StaticChannel5, StaticChannel80, StaticChannel5, StaticChannel20))
# t += timePerTest
# eventDict['time'].append(SettingLinearSaw(At(t), controll, 0, StaticChannel5, StaticChannel80, StaticChannel5, StaticChannel20))
# t += timePerTest
# eventDict['time'].append(SettingBezierWave(At(t), controll, 0, StaticChannel0, StaticChannel80, StaticChannel5, StaticChannel20, StaticChannel100, StaticChannel0))
# t += timePerTest
# eventDict['time'].append(SettingBezierSaw(At(t), controll, 0, StaticChannel80, StaticChannel0, StaticChannel5, StaticChannel20, StaticChannel100, StaticChannel0))

# t += timePerTest
# eventDict['time'].append(SettingSquareWave(At(t), controll, 0, StaticChannel0, StaticChannel80, StaticChannel100, StaticChannel100, StaticChannel5, StaticChannel5))
# t += timePerTest
# eventDict['time'].append(SettingSquareWave(At(t), controll, 0, StaticChannel80, StaticChannel0, StaticChannel100, StaticChannel20, StaticChannel0, StaticChannel40))
# t += timePerTest
# eventDict['time'].append(SettingSquareWave(At(t), controll, 0, StaticChannel80, StaticChannel0, StaticChannel40, StaticChannel40, StaticChannel0, StaticChannel0))
# t += timePerTest

# t += timePerTest
# eventDict['time'].append(SettingNoise(At(t), controll, 0, StaticChannel0, StaticChannel100, StaticChannel40, StaticChannel0))
# t += timePerTest
# eventDict['time'].append(SettingSeedNoise(At(t), controll, 0, StaticChannel0, StaticChannel100, StaticChannel20, StaticChannel20, StaticChannel40))
# t += timePerTest
# eventDict['time'].append(SettingPerlinNoise(At(t), controll, 0, StaticChannel100, StaticChannel0, StaticChannel20, StaticChannel0))
# t += timePerTest


eventDict['time'].append(ChannelSetStatic(At(t), controll, StaticChannel0, 0))


vd = VisualDriver(eventDict, startTime=0)
vd.start()