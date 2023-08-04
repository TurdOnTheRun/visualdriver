from visualdriver import VisualDriver
from controllers import * 
from conditions import *
from channels import *
from agents import *
from events import *

# Simple Lighting Tests
# Execute Twice: Once frontal view and once side view

eventDict = {
    'position': [],
    'time': []
}

# BOTTOM LIGHTS
eventDict['time'].append(LightSetChannel(At(0), TopController, [Light1, Light2, Light3, Light4], StaticChannel8))
eventDict['time'].append(LightSetChannel(At(0), BottomController, [Light1, Light2,], StaticChannel0))

maxSpeed = 180
position = 0.5

secs = 3
eventDict['time'].append(LightSetChannel(At(secs), TopController, [Light1, Light2, Light3, Light4], StaticChannel0))

secs += 1
eventDict['time'].append(LightSetChannel(At(secs), TopController, [Light1, ], StaticChannel10))
secs += 3
eventDict['time'].append(LightSetChannel(At(secs), TopController, [Light1, ], StaticChannel0))
eventDict['time'].append(LightSetChannel(At(secs), TopController, [Light2, ], StaticChannel10))
secs += 3
eventDict['time'].append(LightSetChannel(At(secs), TopController, [Light2, ], StaticChannel0))
eventDict['time'].append(LightSetChannel(At(secs), TopController, [Light3, ], StaticChannel10))
secs += 3
eventDict['time'].append(LightSetChannel(At(secs), TopController, [Light3, ], StaticChannel0))
eventDict['time'].append(LightSetChannel(At(secs), TopController, [Light4, ], StaticChannel10))
secs += 3
eventDict['time'].append(LightSetChannel(At(secs), TopController, [Light1, Light2, Light3, Light4], StaticChannel0))
eventDict['time'].append(LightSetChannel(At(secs), TopController, [Light1, Light2, ], StaticChannel10))
secs += 3
eventDict['time'].append(LightSetChannel(At(secs), TopController, [Light1, Light2, ], StaticChannel0))
eventDict['time'].append(LightSetChannel(At(secs), TopController, [Light2, Light3, ], StaticChannel10))
secs += 3
eventDict['time'].append(LightSetChannel(At(secs), TopController, [Light2, Light3, ], StaticChannel0))
eventDict['time'].append(LightSetChannel(At(secs), TopController, [Light3, Light4, ], StaticChannel10))
secs += 3
eventDict['time'].append(LightSetChannel(At(secs), TopController, [Light3, Light4, ], StaticChannel0))
eventDict['time'].append(LightSetChannel(At(secs), TopController, [Light4, Light1, ], StaticChannel10))
secs += 3
eventDict['time'].append(LightSetChannel(At(secs), TopController, [Light4, Light1, ], StaticChannel0))
eventDict['time'].append(LightSetChannel(At(secs), TopController, [Light1, Light3, ], StaticChannel10))
secs += 3
eventDict['time'].append(LightSetChannel(At(secs), TopController, [Light1, Light3, ], StaticChannel0))
eventDict['time'].append(LightSetChannel(At(secs), TopController, [Light2, Light4, ], StaticChannel10))
secs += 3
eventDict['time'].append(LightSetChannel(At(secs), TopController, [Light2, Light4, ], StaticChannel0))
eventDict['time'].append(LightSetChannel(At(secs), BottomController, [Light1, ], StaticChannel10))
secs += 3
eventDict['time'].append(LightSetChannel(At(secs), BottomController, [Light1, ], StaticChannel0))
eventDict['time'].append(LightSetChannel(At(secs), BottomController, [Light2, ], StaticChannel10))
secs += 3
eventDict['time'].append(LightSetChannel(At(secs), BottomController, [Light1, ], StaticChannel10))
secs += 3
eventDict['time'].append(LightSetChannel(At(secs), TopController, [Light1, ], StaticChannel10))
secs += 3
eventDict['time'].append(LightSetChannel(At(secs), TopController, [Light1, ], StaticChannel0))
eventDict['time'].append(LightSetChannel(At(secs), TopController, [Light2, Light3], StaticChannel10))
secs += 3
eventDict['time'].append(LightSetChannel(At(secs), TopController, [Light1, Light3], StaticChannel0))
eventDict['time'].append(LightSetChannel(At(secs), BottomController, [Light2, Light1], StaticChannel0))


vd = VisualDriver(eventDict, usesMotor=False, startTime=0)
vd.start()
