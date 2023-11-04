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


light1Channel = Channel10
light2Channel = Channel13
noiseBottomChannel = Channel11
noiseTopChannel = Channel12
waveTopChannel = Channel14
waveBottomChannel = Channel15
eventDict['time'].append(SettingStaticLight(At(t), controll, 0, 80))
eventDict['time'].append(ChannelSetSetting(At(t), controll, light1Channel, 0))
eventDict['time'].append(LightSetChannel(At(t), controll, [Light1,], light1Channel))
# eventDict['time'].append(SettingNoise(At(t), controll, 1, StaticChannel0, StaticChannel20, StaticChannel40, StaticChannel0))
# eventDict['time'].append(SettingNoise(At(t), controll, 2, StaticChannel0, StaticChannel20, StaticChannel40, StaticChannel0))
# eventDict['time'].append(ChannelSetSetting(At(t), controll, noiseBottomChannel, 1))
# eventDict['time'].append(ChannelSetSetting(At(t), controll, noiseTopChannel, 2))
# eventDict['time'].append(ChannelSetStatic(At(t), controll, waveBottomChannel, 0))
# eventDict['time'].append(ChannelSetStatic(At(t), controll, waveTopChannel, 80))
# eventDict['time'].append(EffectAdd(At(t), controll, 0, noiseTopChannel))
# eventDict['time'].append(EffectSubtract(At(t), controll, 1, noiseBottomChannel))
# eventDict['time'].append(ChannelAddEffect(At(t), controll, waveTopChannel, 0,0))
# eventDict['time'].append(ChannelAddEffect(At(t), controll, waveBottomChannel, 1,0))

eventDict['time'].append(EffectInverse(At(t), controll, 2))
eventDict['time'].append(ChannelAddEffect(At(t), controll, light2Channel, 2, 0))
eventDict['time'].append(ChannelSetChannel(At(t), controll, light2Channel, light1Channel))
eventDict['time'].append(LightSetChannel(At(t), controll, [Light2,], light2Channel))


eventDict['time'].append(SettingSquareWave(At(t), controll, 0, StaticChannel0, StaticChannel100, StaticChannel40, StaticChannel40, StaticChannel0, StaticChannel0))

t += 30




eventDict['time'].append(ChannelSetStatic(At(t), controll, StaticChannel0, 0))



vd = VisualDriver(eventDict, startTime=0)
vd.start()