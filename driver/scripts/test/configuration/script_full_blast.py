from visualdriver import VisualDriver
from controllers import * 
from conditions import *
from channels import *
from agents import *
from events import *
from settings import *

# 10 Seconds all left lights at 100
# 10 Seconds all right lights at 100
# 10 Seconds all top lights at 100

eventDict = {
    'position': [],
    'time': []
}

steptime = 10

t=0

eventDict['time'].append(LightSetChannel(At(t), BottomController, [Light1,Light2], StaticChannel100))

t+=steptime
eventDict['time'].append(LightSetChannel(At(t), BottomController, [Light1,Light2], StaticChannel0))
eventDict['time'].append(LightSetChannel(At(t), BottomController, [Light3,Light4], StaticChannel100))

t+=steptime
eventDict['time'].append(LightSetChannel(At(t), BottomController, [Light1,Light2], StaticChannel0))
eventDict['time'].append(LightSetChannel(At(t), BottomController, [Light3,Light4], StaticChannel0))
eventDict['time'].append(LightSetChannel(At(t), TopController, [Light1,Light2,Light3,Light4], StaticChannel100))

t+=steptime
eventDict['time'].append(LightSetChannel(At(t), BottomController, [Light1,Light2], StaticChannel0))
eventDict['time'].append(LightSetChannel(At(t), BottomController, [Light3,Light4], StaticChannel0))
eventDict['time'].append(LightSetChannel(At(t), TopController, [Light1,Light2,Light3,Light4], StaticChannel0))


vd = VisualDriver(eventDict, startTime=0, usesTrigger=False)
vd.start()