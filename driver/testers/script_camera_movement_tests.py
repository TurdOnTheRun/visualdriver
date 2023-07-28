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
eventDict['time'].append(SettingStaticLight(At(0), BottomController, 0, 100))
eventDict['time'].append(SettingStaticLight(At(0), BottomController, 1, 0))
eventDict['time'].append(ChannelSetSetting(At(0), BottomController, Channel2, 0))
eventDict['time'].append(ChannelSetSetting(At(0), BottomController, Channel3, 1))
eventDict['time'].append(LightSetChannel(At(0), BottomController, [Light1,], Channel2))
eventDict['time'].append(LightSetChannel(At(0), BottomController, [Light2,], Channel3))


# BOTTOM EFFECTS:
eventDict['time'].append(SettingStaticLight(At(0), BottomController, 2, 0)) #amplitude starts at 0
eventDict['time'].append(ChannelSetSetting(At(0), BottomController, Channel1, 2)) #steptime for 25 fps strobe
eventDict['time'].append(EffectStrobe(At(0), BottomController, 0, Channel1, StaticChannel4, 1, [Light1,]))
eventDict['time'].append(ChannelAddEffect(At(0), BottomController, Channel2, 0, 0))
eventDict['time'].append(ChannelAddEffect(At(0), BottomController, Channel3, 0, 0))

eventDict['time'].append(MotorSpeed(At(5), 130))


distance = 0.5
steps = 21
stepdistance = distance/steps

startDistance = 0
light1 = 100
light2 = 0
strobe = 0

steptime = 10

for i in range(steps):
    lightDistance = startDistance + stepdistance*(i+1)
    factor = lightDistance/distance
    if lightDistance > 0.21:
        eventDict['position'].append(MotorSpeed(At(lightDistance), 0))
    print(lightDistance)

    eventDict['position'].append(SettingLinearDimm(At(lightDistance), BottomController, 0, light1, int(100-(factor*100)), steptime))
    light1 = int(100-(factor*100))
    print('light1', light1)
    eventDict['position'].append(SettingLinearDimm(At(lightDistance), BottomController, 1, light2, int(0+(factor*100)), steptime))
    light2 = int(0+(factor*100))
    print('light2', light2)
    
    if lightDistance < distance/2:
        newState = int(0+(factor*100*2))
        if newState > 100:
            newState = 100
        eventDict['position'].append(SettingLinearDimm(At(lightDistance), BottomController, 2, strobe, newState, int(steptime/2)))
        strobe = newState
    else:
        newState = int(0+((1-factor)*100*2))
        if newState < 0:
            newState = 0
        eventDict['position'].append(SettingLinearDimm(At(lightDistance), BottomController, 2, strobe, newState, int(steptime/2)))
        strobe = newState
    print('strobe', strobe)

eventDict['time'].append(SettingStaticLight(At(21), BottomController, 1, 0))



    

vd = VisualDriver(eventDict, usesMotor=True, startTime=0)
vd.start()
