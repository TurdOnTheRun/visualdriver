from visualdriver import VisualDriver
from agents import *
from events import kinectTest, leftCenterRight

eventDict = leftCenterRight(30, (Bottom1, 100, 100), (TopAll, 90, 40), (Bottom2, 100, 100), 1)
vd = VisualDriver(eventDict, music='/home/maximilian/Downloads/sound.wav')
vd.start()
