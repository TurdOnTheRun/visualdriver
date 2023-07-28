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

maxSpeed = 180

eventDict['time'].append(MotorSpeed(At(2), maxSpeed))
eventDict['time'].append(TimeEventsBlock(At(2)))
eventDict['position'].append(MotorDirection(At(1.5-0.25), MOTOR_COUNTERCLOCKWISE))
eventDict['position'].append(MotorDirection(LE(0.25+0.25), MOTOR_CLOCKWISE))
eventDict['position'].append(MotorDirection(At(1.5-0.25), MOTOR_CLOCKWISE))
eventDict['position'].append(TimeEventsUnblock(At(1.5-0.25)))
eventDict['time'].append(TimeReset(At(2)))
eventDict['time'].append(MotorSpeed(At(0), 0))
eventDict['time'].append(LightSetChannel(At(4), TopController, [Light1, Light2, Light3, Light4], StaticChannel8))



vd = VisualDriver(eventDict, usesMotor=True, startTime=0)
vd.start()
