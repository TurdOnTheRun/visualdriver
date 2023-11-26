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

t=0
eventDict['time'].append(ChannelSetStatic(At(t), TopController, Channel11, 70))
eventDict['time'].append(LightSetChannel(At(t), TopController, [Light1, Light2, Light3, Light4], Channel11))

t+=3
eventDict['time'].append(LightSetChannel(At(t), TopController, [Light1, Light2, Light3, Light4], StaticChannel0))
eventDict['time'].append(LightSetChannel(At(t), BottomController, [Light1, Light2], StaticChannel80))

t+=3
eventDict['time'].append(LightSetChannel(At(t), BottomController, [Light1, Light2], StaticChannel0))


vd = VisualDriver(eventDict, startTime=0)
vd.start()