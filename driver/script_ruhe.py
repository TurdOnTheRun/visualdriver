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

music = '/home/maximilian/music/ruhe.mp3'

# D is back Top
# F is Left Bottom
# A is Right Bottom

t=2

topLightSetting1 = 0
topLightChannel1 = Channel10
topLightSetting2 = 1
topLightChannel2 = Channel11
topLightSetting2 = 2
topLightChannel2 = Channel12
topLightSetting3 = 3
topLightChannel3 = Channel13
topLightSetting4 = 4
topLightChannel4 = Channel14

leftLightSetting = 0
leftLightChannel = Channel10
rightLightSetting = 1
rightLightChannel = Channel11

eventDict['time'].append(SettingStatic(At(0), TopController, topLightSetting1, 0))
eventDict['time'].append(ChannelSetSetting(At(0), TopController, topLightChannel1, topLightSetting1))
eventDict['time'].append(LightSetChannel(At(0), TopController, [Light3,], topLightChannel1))

eventDict['time'].append(SettingStatic(At(0), TopController, topLightSetting2, 0))
eventDict['time'].append(ChannelSetSetting(At(0), TopController, topLightChannel2, topLightSetting2))
eventDict['time'].append(LightSetChannel(At(0), TopController, [Light2,], topLightChannel2))

eventDict['time'].append(SettingStatic(At(0), TopController, topLightSetting3, 0))
eventDict['time'].append(ChannelSetSetting(At(0), TopController, topLightChannel3, topLightSetting3))
eventDict['time'].append(LightSetChannel(At(0), TopController, [Light1,], topLightChannel3))

eventDict['time'].append(SettingStatic(At(0), TopController, topLightSetting4, 0))
eventDict['time'].append(ChannelSetSetting(At(0), TopController, topLightChannel4, topLightSetting4))
eventDict['time'].append(LightSetChannel(At(0), TopController, [Light4,], topLightChannel4))

eventDict['time'].append(SettingStatic(At(0), BottomController, leftLightSetting, 0))
eventDict['time'].append(ChannelSetSetting(At(0), BottomController, leftLightChannel, leftLightSetting))
eventDict['time'].append(LightSetChannel(At(0), BottomController, [Light2,], leftLightChannel))

eventDict['time'].append(SettingStatic(At(0), BottomController, rightLightSetting, 0))
eventDict['time'].append(ChannelSetSetting(At(0), BottomController, rightLightChannel, rightLightSetting))
eventDict['time'].append(LightSetChannel(At(0), BottomController, [Light4,], rightLightChannel))


eventDict['time'].append(MusicStart(At(t), 0))

# 0.07
# D & F
# start: 0.17
# end: 10
startTime = 0.07
endTime = 8
# impulseSteptime 
impulseSteptime = 3
decisteps = 50
eventDict['time'].append(SettingImpulseToBezierFadeout(At(t + startTime), TopController, topLightSetting1, 90, 1, 20, impulseSteptime, int(1000*(endTime-startTime-(impulseSteptime/100))/(decisteps*10)), decisteps, 0, 100))
eventDict['time'].append(SettingImpulseToBezierFadeout(At(t + startTime), BottomController, leftLightSetting, 90, 1, 20, impulseSteptime, int(1000*(endTime-startTime-(impulseSteptime/100))/(decisteps*10)), decisteps, 0, 100))

# F & A
# 1.25
startTime = 1.25
endTime = 8
# impulseSteptime 
impulseSteptime = 3
decisteps = 50
eventDict['time'].append(SettingImpulseToBezierFadeout(At(t + startTime), BottomController, rightLightSetting, 90, 1, 20, impulseSteptime, int(1000*(endTime-startTime-(impulseSteptime/100))/(decisteps*10)), decisteps, 0, 100))
eventDict['time'].append(SettingImpulseToBezierFadeout(At(t + startTime), BottomController, leftLightSetting, 90, 1, 20, impulseSteptime, int(1000*(endTime-startTime-(impulseSteptime/100))/(decisteps*10)), decisteps, 0, 100))

# A# & D
# 2.41
startTime = 2.41
endTime = 8
# impulseSteptime 
impulseSteptime = 3
decisteps = 50
eventDict['time'].append(SettingImpulseToBezierFadeout(At(t + startTime), BottomController, rightLightSetting, 90, 1, 20, impulseSteptime, int(1000*(endTime-startTime-(impulseSteptime/100))/(decisteps*10)), decisteps, 0, 100))
eventDict['time'].append(SettingImpulseToBezierFadeout(At(t + startTime), TopController, topLightSetting2, 90, 1, 20, impulseSteptime, int(1000*(endTime-startTime-(impulseSteptime/100))/(decisteps*10)), decisteps, 0, 100))

# C & D
# 3.72
startTime = 3.72
endTime = 8
# impulseSteptime 
impulseSteptime = 3
decisteps = 50
eventDict['time'].append(SettingImpulseToBezierFadeout(At(t + startTime), TopController, topLightSetting1, 90, 1, 20, impulseSteptime, int(1000*(endTime-startTime-(impulseSteptime/100))/(decisteps*10)), decisteps, 0, 100))
eventDict['time'].append(SettingImpulseToBezierFadeout(At(t + startTime), TopController, topLightSetting4, 90, 1, 20, impulseSteptime, int(1000*(endTime-startTime-(impulseSteptime/100))/(decisteps*10)), decisteps, 0, 100))

# A & D
# 5.08
startTime = 5.08
endTime = 8
# impulseSteptime 
impulseSteptime = 3
decisteps = 50
eventDict['time'].append(SettingImpulseToBezierFadeout(At(t + startTime), TopController, topLightSetting1, 90, 1, 20, impulseSteptime, int(1000*(endTime-startTime-(impulseSteptime/100))/(decisteps*10)), decisteps, 0, 100))
eventDict['time'].append(SettingImpulseToBezierFadeout(At(t + startTime), BottomController, rightLightSetting, 90, 1, 20, impulseSteptime, int(1000*(endTime-startTime-(impulseSteptime/100))/(decisteps*10)), decisteps, 0, 100))

# A & G
# 9.87
startTime = 9.97
endTime = 15
# impulseSteptime 
impulseSteptime = 3
decisteps = 50
eventDict['time'].append(SettingImpulseToBezierFadeout(At(t + startTime), TopController, topLightSetting1, 90, 1, 20, impulseSteptime, int(1000*(endTime-startTime-(impulseSteptime/100))/(decisteps*10)), decisteps, 0, 100))
eventDict['time'].append(SettingImpulseToBezierFadeout(At(t + startTime), TopController, topLightSetting3, 90, 1, 20, impulseSteptime, int(1000*(endTime-startTime-(impulseSteptime/100))/(decisteps*10)), decisteps, 0, 100))

# D & A
# 11.11
startTime = 11.11
endTime = 23
# impulseSteptime 
impulseSteptime = 3
decisteps = 50
eventDict['time'].append(SettingImpulseToBezierFadeout(At(t + startTime), TopController, topLightSetting1, 90, 1, 20, impulseSteptime, int(1000*(endTime-startTime-(impulseSteptime/100))/(decisteps*10)), decisteps, 0, 100))
eventDict['time'].append(SettingImpulseToBezierFadeout(At(t + startTime), BottomController, rightLightSetting, 90, 1, 20, impulseSteptime, int(1000*(endTime-startTime-(impulseSteptime/100))/(decisteps*10)), decisteps, 0, 100))


# 12.39
startTime = 13
eventDict['time'].append(SettingImpulseToBezierFadeout(At(t + startTime), TopController, topLightSetting1, 90, 1, 20, impulseSteptime, int(1000*(endTime-startTime-(impulseSteptime/100))/(decisteps*10)), decisteps, 0, 100))

# 13.74

# 17.78


vd = VisualDriver(eventDict, music=music, usesMotor=True, startTime=0, isTake=False)
vd.start()