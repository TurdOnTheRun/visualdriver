from visualdriver import VisualDriver
from agents import *
from conditions import At
from events import Instant, Vibrato

eventDict = {
    'time': [Instant(At(0), TopAll, 50), Vibrato(At(0), TopAll, 2, 100, 1), Vibrato(At(20), TopAll, 3, 100, 2), Instant(At(25), TopAll, 0)],
    'position': []
}

vd = VisualDriver(eventDict)
vd.start()