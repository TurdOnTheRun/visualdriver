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

# BOTTOM LIGHTS
eventDict['time'].append(LightSetChannel(At(0), TopController, [Light1, Light2, Light3, Light4], StaticChannel8))
eventDict['time'].append(LightSetChannel(At(0), BottomController, [Light1, Light2,], StaticChannel0))

maxSpeed = 130

eventDict['time'].append(MotorSpeed(At(5), maxSpeed))
eventDict['time'].append(TimeEventsBlock(At(5)))
eventDict['time'].append(LightSetChannel(At(5), TopController, [Light1, Light2, Light3, Light4], StaticChannel0))
eventDict['position'].append(MotorSpeed(At(0.204), 0))
eventDict['position'].append(TimeReset(At(0.5)))
eventDict['position'].append(TimeEventsUnblock(At(0.5)))

vd = VisualDriver(eventDict, usesMotor=True, startTime=0)
vd.start()
