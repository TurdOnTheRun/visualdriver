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

music = '/home/maximilian/music/ruheI.mp3'


# D is back Top
# F is Left Bottom
# A is Right Bottom

t=0

topLightSetting = 0
topLightChannel = Channel10
otherTopLightSetting = 1
otherTopLightChannel = Channel11

leftLightSetting = 0
leftLightChannel = Channel10
rightLightSetting = 1
rightLightChannel = Channel11

eventDict['time'].append(SettingStaticLight(At(t), TopController, topLightSetting, 0))
eventDict['time'].append(ChannelSetSetting(At(t), TopController, topLightChannel, topLightSetting))
eventDict['time'].append(LightSetChannel(At(t), TopController, [Light3,], topLightChannel))

eventDict['time'].append(SettingStaticLight(At(t), TopController, otherTopLightSetting, 0))
eventDict['time'].append(ChannelSetSetting(At(t), TopController, otherTopLightChannel, otherTopLightSetting))
eventDict['time'].append(LightSetChannel(At(t), TopController, [Light2,], otherTopLightChannel))

eventDict['time'].append(SettingStaticLight(At(t), BottomController, leftLightSetting, 0))
eventDict['time'].append(ChannelSetSetting(At(t), BottomController, leftLightChannel, leftLightSetting))
eventDict['time'].append(LightSetChannel(At(t), BottomController, [Light2,], leftLightChannel))

eventDict['time'].append(SettingStaticLight(At(t), BottomController, rightLightSetting, 0))
eventDict['time'].append(ChannelSetSetting(At(t), BottomController, rightLightChannel, rightLightSetting))
eventDict['time'].append(LightSetChannel(At(t), BottomController, [Light4,], rightLightChannel))


# D & F
# start: 0.17
# end: 10
startTime = 0.17
endTime = 8
flashTime = 0.05
decisteps = 50
y1 = 100
y2 = 100
eventDict['time'].append(SettingBezierAfterFlash(At(t + startTime), TopController, topLightSetting, 80, 0, int(100 * (endTime - startTime - flashTime) / decisteps ), decisteps, y1, y2, int(flashTime * 1000)))
eventDict['time'].append(SettingBezierAfterFlash(At(t + startTime), BottomController, leftLightSetting, 80, 0, int(100 * (endTime - startTime - flashTime) / decisteps ), decisteps, y1, y2, int(flashTime * 1000)))


# F & A
# start: 1.37
# end: 10

startTime = 1.37
endTime = 8
flashTime = 0.05
decisteps = 50
y1 = 100
y2 = 100
eventDict['time'].append(SettingBezierAfterFlash(At(t + startTime), BottomController, leftLightSetting, 80, 0, int(100 * (endTime - startTime - flashTime) / decisteps ), decisteps, y1, y2, int(flashTime * 1000)))
eventDict['time'].append(SettingBezierAfterFlash(At(t + startTime), BottomController, rightLightSetting, 80, 0, int(100 * (endTime - startTime - flashTime) / decisteps ), decisteps, y1, y2, int(flashTime * 1000)))


# A# & D
# start: 2.54
# end: 10


startTime = 2.54
endTime = 8
flashTime = 0.05
decisteps = 50
y1 = 100
y2 = 100
eventDict['time'].append(SettingBezierAfterFlash(At(t + startTime), TopController, otherTopLightSetting, 80, 0, int(100 * (endTime - startTime - flashTime) / decisteps ), decisteps, y1, y2, int(flashTime * 1000)))
eventDict['time'].append(SettingBezierAfterFlash(At(t + startTime), BottomController, rightLightSetting, 80, 0, int(100 * (endTime - startTime - flashTime) / decisteps ), decisteps, y1, y2, int(flashTime * 1000)))


# C & D
# start: 3.81
# end: 10
startTime = 3.81
endTime = 8
flashTime = 0.05
decisteps = 50
y1 = 100
y2 = 100
eventDict['time'].append(LightSetChannel(At(t + startTime), TopController, [Light4,], otherTopLightChannel))
eventDict['time'].append(SettingBezierAfterFlash(At(t + startTime), TopController, topLightSetting, 80, 0, int(100 * (endTime - startTime - flashTime) / decisteps ), decisteps, y1, y2, int(flashTime * 1000)))
eventDict['time'].append(SettingBezierAfterFlash(At(t + startTime), TopController, otherTopLightSetting, 80, 0, int(100 * (endTime - startTime - flashTime) / decisteps ), decisteps, y1, y2, int(flashTime * 1000)))


# A & D
# start D: 5.19
# start A: 5.22
# end: 10
startTime = 5.19
endTime = 8
flashTime = 0.05
decisteps = 50
y1 = 100
y2 = 100
eventDict['time'].append(SettingBezierAfterFlash(At(t + startTime), TopController, topLightSetting, 80, 0, int(100 * (endTime - startTime - flashTime) / decisteps ), decisteps, y1, y2, int(flashTime * 1000)))
eventDict['time'].append(SettingBezierAfterFlash(At(t + startTime), BottomController, rightLightSetting, 80, 0, int(100 * (endTime - startTime - flashTime) / decisteps ), decisteps, y1, y2, int(flashTime * 1000)))


# A & G
# start: 10
# end: 23
startTime = 10
endTime = 15
flashTime = 0.05
decisteps = 50
y1 = 100
y2 = 100
eventDict['time'].append(LightSetChannel(At(t + startTime), TopController, [Light1,], otherTopLightChannel))
eventDict['time'].append(SettingBezierAfterFlash(At(t + startTime), TopController, topLightSetting, 80, 0, int(100 * (endTime - startTime - flashTime) / decisteps ), decisteps, y1, y2, int(flashTime * 1000)))
eventDict['time'].append(SettingBezierAfterFlash(At(t + startTime), TopController, otherTopLightSetting, 80, 0, int(100 * (endTime - startTime - flashTime) / decisteps ), decisteps, y1, y2, int(flashTime * 1000)))



# A & G
# start: 10
# end: 23

# D & A
# start D: 11.23
# start A: 11.24
# end: 23

# F & E
# start: 12.47
# end: 23

# A & F
# start: 13.87
# end: 23

# F & D
# start: 15.5
# end: 23

vd = VisualDriver(eventDict, startTime=0, usesTrigger=True, music=music)
vd.start()