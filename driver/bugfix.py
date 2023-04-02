from visualdriver import VisualDriver
from agents import *
from events import *

music = None
eventDict = {
    'position': [],
    'time': []
}


eventDict['time'].append(Linear(At(4), Bottom2, 100, int(5*10)))
eventDict['time'].append(Linear(At(10), Bottom2, 0, int(1)))
eventDict['time'].append(InstantBezier(At(12), Bottom2, 0, 0, int(1), 100, 100, 100, 100))
vd = VisualDriver(eventDict, music=music)
vd.start()