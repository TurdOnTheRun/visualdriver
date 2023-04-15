from visualdriver import VisualDriver
from controllers import * 
from agents import *
from events import *

eventDict = {
    'position': [],
    'time': []
}

#Right Light: 
#0 - 3:75
#4:34 - 8:01
#8:35 - 11:53
#12:00 - 14:76
#15:23 -  18
#18 - low steady until 29

eventDict['time'].append(StaticLight(At(0), TopController, [Light1, Light2, Light3, Light4], 20))

eventDict['time'].append(StaticFlash(At(2), TopController, [Light1, Light2, Light3, Light4], 100, 30, 200))

eventDict['time'].append(StaticMachine(At(4), TopController, [Light1, Light2, Light3, Light4], 50, 0, 200, 100, 50))

eventDict['time'].append(LinearDimm(At(6), TopController, [Light1, Light2, Light3, Light4], 0, 50, 6))

eventDict['time'].append(BezierDimm(At(9), TopController, [Light1, Light2, Light3, Light4], 0, 100, 30, 80, 20))

eventDict['time'].append(StaticLight(At(12), TopController, [Light1, Light2, Light3, Light4], 50))

eventDict['time'].append(UpDownVibrato(At(12), TopController, [Light1, Light2, Light3, Light4], 50, 10))

eventDict['time'].append(Strobe(At(16), TopController, [Light1, Light2, Light3, Light4], 100, 130, 1, [Light1, Light3]))

vd = VisualDriver(eventDict, startTime=0)
vd.start()