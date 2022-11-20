from visualdriver import VisualDriver
from agents import *
from events import kinectTest, leftCenterRight

eventDict = kinectTest(60, TopAll, 1)
vd = VisualDriver(eventDict, usesKinect=True, music='/home/maximilian/Downloads/sound.wav')
vd.start()
