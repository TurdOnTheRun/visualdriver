from visualdriver import VisualDriver
from controllers import * 
from agents import *
from events import *

eventDict = {
    'position': [],
    'time': []
}

eventDict['time'].append(StaticLight(At(0), TopController, [Light1, Light2, Light3, Light4], 20))
eventDict['time'].append(StaticLight(At(0), BottomController, [Light1, Light2], 20))


eventDict['time'].append(StaticFlash(At(4), TopController, [Light1, Light2, Light3, Light4], 100, 30, 200))
eventDict['time'].append(StaticFlash(At(4), BottomController, [Light1, Light2], 100, 30, 200))


eventDict['time'].append(StaticMachine(At(8), TopController, [Light1, Light2, Light3, Light4], 50, 0, 200, 100, 50))
eventDict['time'].append(StaticMachine(At(8), BottomController, [Light1, Light2], 50, 0, 200, 100, 50))


eventDict['time'].append(LinearDimm(At(12), TopController, [Light1, Light2, Light3, Light4], 0, 50, 6))
eventDict['time'].append(LinearDimm(At(12), BottomController, [Light1, Light2], 0, 50, 6))


eventDict['time'].append(BezierDimm(At(16), TopController, [Light1, Light2, Light3, Light4], 0, 100, 30, 80, 20))
eventDict['time'].append(BezierDimm(At(16), BottomController, [Light1, Light2], 0, 100, 30, 80, 20))


eventDict['time'].append(StaticLight(At(20), TopController, [Light1, Light2, Light3, Light4], 50))
eventDict['time'].append(StaticLight(At(20), BottomController, [Light1, Light2], 50))


eventDict['time'].append(UpDownVibrato(At(20), TopController, [Light1, Light2, Light3, Light4], 50, 10))
eventDict['time'].append(UpDownVibrato(At(20), BottomController, [Light1, Light2], 50, 10))


eventDict['time'].append(Strobe(At(24), TopController, [Light1, Light2, Light3, Light4], 100, 130, 1, [Light1, Light3]))
eventDict['time'].append(Strobe(At(24), BottomController, [Light1, Light2], 100, 130, 1, [Light1,]))


eventDict['time'].append(RemoveEffect(At(28), TopController, [Light1, Light2], 1))
eventDict['time'].append(RemoveEffect(At(28), BottomController, [Light1, ], 1))


eventDict['time'].append(RemoveEffect(At(32), TopController, [Light3, Light4], 1))
eventDict['time'].append(RemoveEffect(At(32), BottomController, [Light2,], 1))


eventDict['time'].append(ResetEffects(At(36), TopController,  [Light1, Light2, Light3, Light4]))
eventDict['time'].append(ResetEffects(At(36), BottomController,  [Light1, Light2]))


eventDict['time'].append(StaticLight(At(36), TopController, [Light1, Light2, Light3, Light4], 20))
eventDict['time'].append(StaticLight(At(36), BottomController, [Light1, Light2], 20))


vd = VisualDriver(eventDict, startTime=0)
vd.start()