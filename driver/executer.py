from visualdriver import VisualDriver
from agents import *
from events import leftCenterRight

eventDict = leftCenterRight(60, (Bottom1, 100, 200), (TopAll, 90, 80), (Bottom2, 100, 200), 2)
vd = VisualDriver(eventDict)
vd.start()
