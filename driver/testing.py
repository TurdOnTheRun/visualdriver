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

# controllers = [BottomController, TopController]

# for controller in controllers:
#     eventDict['time'].append(EffectUpDownVibrato(At(0), controller, 0, StaticChannel5, StaticChannel10))
#     # eventDict['time'].append(EffectStrobe(At(0), controller, 1, StaticChannel10, StaticChannel5, 2, [Light1, Light3]))

#     # Strobe Effect
#     eventDict['time'].append(ChannelSetChannel(At(0), controller, Channel2, StaticChannel5))
#     eventDict['time'].append(ChannelAddEffect(At(0), controller, Channel2, 0, 0))
#     eventDict['time'].append(EffectStrobe(At(0), controller, 1, StaticChannel10, Channel2, 1, [Light1, Light3]))

#     eventDict['time'].append(ChannelSetChannel(At(0), controller, Channel1, StaticChannel10))
#     eventDict['time'].append(ChannelAddEffect(At(0), controller, Channel1, 1, 0))
#     eventDict['time'].append(LightSetChannel(At(0), controller, [Light1, Light2, Light3, Light4], Channel1))

#     # eventDict['time'].append(ChannelAddEffect(At(2), controller, Channel1, 0, 0))
#     # eventDict['time'].append(ChannelAddEffect(At(5), controller, Channel1, 1, 0))


#     # eventDict['time'].append(EffectStrobe(At(10), controller, 1, StaticChannel10, StaticChannel5, 2, [Light1, Light3]))
#     # eventDict['time'].append(ChannelRemoveEffect(At(10), controller, Channel1, 0))

#     # eventDict['time'].append(ChannelAddEffect(At(12), controller, Channel1, 1, 0))


#     eventDict['time'].append(LightSetChannel(At(15), controller, [Light1, Light2, Light3, Light4], StaticChannel0))

# eventDict['time'] = sorted(eventDict['time'], key=lambda event: event.condition.value)



eventDict['time'].append(EffectPerlin(At(0), BottomController, 0, StaticChannel10, StaticChannel2, 10))
eventDict['time'].append(ChannelSetChannel(At(0), BottomController, Channel2, StaticChannel5))
eventDict['time'].append(ChannelAddEffect(At(0), BottomController, Channel2, 0, 0))
eventDict['time'].append(LightSetChannel(At(0), BottomController, [Light1, Light2], Channel2))
eventDict['time'].append(LightSetChannel(At(15), BottomController, [Light1, Light2], StaticChannel0))


vd = VisualDriver(eventDict, startTime=0)
vd.start()