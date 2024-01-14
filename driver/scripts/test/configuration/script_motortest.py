from visualdriver import VisualDriver
from controllers import * 
from conditions import *
from channels import *
from agents import *
from events import *
from settings import *

eventDict = {
    'position': [],
    'time': []
}

t=0
eventDict['time'].append(MotorSpeed(At(t), 50))

# t+=8
# eventDict['time'].append(MotorSpeed(At(t), 90))

eventDict['position'].append(MotorSpeed(At(0.5), 0))


vd = VisualDriver(eventDict, startTime=0, usesMotor=True)
vd.start()