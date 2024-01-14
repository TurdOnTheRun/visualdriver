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

eventDict['time'].append(SettingStatic(At(t), TopController, topLightSetting, 0))
eventDict['time'].append(ChannelSetSetting(At(t), TopController, topLightChannel, topLightSetting))
eventDict['time'].append(LightSetChannel(At(t), TopController, [Light3,], topLightChannel))

eventDict['time'].append(SettingStatic(At(t), TopController, topLightSetting2, 0))
eventDict['time'].append(ChannelSetSetting(At(t), TopController, topLightChannel2, topLightSetting2))
eventDict['time'].append(LightSetChannel(At(t), TopController, [Light2,], topLightChannel2))

eventDict['time'].append(SettingStatic(At(t), TopController, topLightSetting3, 0))
eventDict['time'].append(ChannelSetSetting(At(t), TopController, topLightChannel3, topLightSetting3))
eventDict['time'].append(LightSetChannel(At(t), TopController, [Light1,], topLightChannel3))

eventDict['time'].append(SettingStatic(At(t), TopController, topLightSetting4, 0))
eventDict['time'].append(ChannelSetSetting(At(t), TopController, topLightChannel4, topLightSetting4))
eventDict['time'].append(LightSetChannel(At(t), TopController, [Light4,], topLightChannel4))

eventDict['time'].append(SettingStatic(At(t), BottomController, leftLightSetting, 0))
eventDict['time'].append(ChannelSetSetting(At(t), BottomController, leftLightChannel, leftLightSetting))
eventDict['time'].append(LightSetChannel(At(t), BottomController, [Light2,], leftLightChannel))

eventDict['time'].append(SettingStatic(At(t), BottomController, rightLightSetting, 0))
eventDict['time'].append(ChannelSetSetting(At(t), BottomController, rightLightChannel, rightLightSetting))
eventDict['time'].append(LightSetChannel(At(t), BottomController, [Light4,], rightLightChannel))



flashTime = 0.05
hammerTime = 0.2
hammerDecisteps = 1


# D & F
# start: 0.17
# end: 10
startTime = 0.17
endTime = 8
decisteps = 50
y1 = 100
y2 = 100
eventDict['time'].append(SettingBezierAfterFlash(At(t + startTime), TopController, topLightSetting, 80, 20, int(100* (hammerTime - flashTime) / hammerDecisteps), hammerDecisteps, 0, 100, int(flashTime * 1000)))
eventDict['time'].append(SettingBezierAfterFlash(At(t + startTime), BottomController, leftLightSetting, 80, 20, int(100* (hammerTime - flashTime) / hammerDecisteps), hammerDecisteps, 0, 100, int(flashTime * 1000)))
eventDict['time'].append(SettingBezierAfterFlash(At(t + startTime + hammerTime), TopController, topLightSetting, 20, 0, int(100 * (endTime - startTime - hammerTime) / decisteps ), decisteps, y1, y2, int(flashTime * 1000)))
eventDict['time'].append(SettingBezierAfterFlash(At(t + startTime + hammerTime), BottomController, leftLightSetting, 20, 0, int(100 * (endTime - startTime - hammerTime) / decisteps ), decisteps, y1, y2, int(flashTime * 1000)))


# F & A
# start: 1.37
# end: 10

startTime = 1.37
endTime = 8
decisteps = 50
y1 = 100
y2 = 100
eventDict['time'].append(SettingBezierAfterFlash(At(t + startTime), BottomController, leftLightSetting, 80, 20, int(100* (hammerTime - flashTime) / hammerDecisteps), hammerDecisteps, 0, 100, int(flashTime * 1000)))
eventDict['time'].append(SettingBezierAfterFlash(At(t + startTime), BottomController, rightLightSetting, 80, 20, int(100* (hammerTime - flashTime) / hammerDecisteps), hammerDecisteps, 0, 100, int(flashTime * 1000)))
eventDict['time'].append(SettingBezierAfterFlash(At(t + startTime + hammerTime), BottomController, leftLightSetting, 20, 0, int(100 * (endTime - startTime - hammerTime) / decisteps ), decisteps, y1, y2, int(flashTime * 1000)))
eventDict['time'].append(SettingBezierAfterFlash(At(t + startTime + hammerTime), BottomController, rightLightSetting, 20, 0, int(100 * (endTime - startTime - hammerTime) / decisteps ), decisteps, y1, y2, int(flashTime * 1000)))


# A# & D
# start: 2.54
# end: 10
startTime = 2.54
endTime = 8
flashTime = 0.05
decisteps = 50
y1 = 100
y2 = 100
eventDict['time'].append(SettingBezierAfterFlash(At(t + startTime), TopController, topLightSetting2, 80, 20, int(100* (hammerTime - flashTime) / hammerDecisteps), hammerDecisteps, 0, 100, int(flashTime * 1000)))
eventDict['time'].append(SettingBezierAfterFlash(At(t + startTime), BottomController, rightLightSetting, 80, 20, int(100* (hammerTime - flashTime) / hammerDecisteps), hammerDecisteps, 0, 100, int(flashTime * 1000)))
eventDict['time'].append(SettingBezierAfterFlash(At(t + startTime + hammerTime), TopController, topLightSetting2, 20, 0, int(100 * (endTime - startTime - hammerTime) / decisteps ), decisteps, y1, y2, int(flashTime * 1000)))
eventDict['time'].append(SettingBezierAfterFlash(At(t + startTime + hammerTime), BottomController, rightLightSetting, 20, 0, int(100 * (endTime - startTime - hammerTime) / decisteps ), decisteps, y1, y2, int(flashTime * 1000)))


# C & D
# start: 3.81
# end: 10
startTime = 3.81
endTime = 8
flashTime = 0.05
decisteps = 50
y1 = 100
y2 = 100
eventDict['time'].append(SettingBezierAfterFlash(At(t + startTime), TopController, topLightSetting, 80, 20, int(100* (hammerTime - flashTime) / hammerDecisteps), hammerDecisteps, 0, 100, int(flashTime * 1000)))
eventDict['time'].append(SettingBezierAfterFlash(At(t + startTime), TopController, topLightSetting4, 80, 20, int(100* (hammerTime - flashTime) / hammerDecisteps), hammerDecisteps, 0, 100, int(flashTime * 1000)))
eventDict['time'].append(SettingBezierAfterFlash(At(t + startTime + hammerTime), TopController, topLightSetting, 20, 0, int(100 * (endTime - startTime - hammerTime) / decisteps ), decisteps, y1, y2, int(flashTime * 1000)))
eventDict['time'].append(SettingBezierAfterFlash(At(t + startTime + hammerTime), TopController, topLightSetting4, 20, 0, int(100 * (endTime - startTime - hammerTime) / decisteps ), decisteps, y1, y2, int(flashTime * 1000)))


# A & D
# start D: 5.19
# start A: 5.22
# end: 10
startTime1 = 5.19
startTime2 = 5.22
endTime = 8
flashTime = 0.05
decisteps = 50
y1 = 100
y2 = 100
eventDict['time'].append(SettingBezierAfterFlash(At(t + startTime1), TopController, topLightSetting, 80, 20, int(100* (hammerTime - flashTime) / hammerDecisteps), hammerDecisteps, 0, 100, int(flashTime * 1000)))
eventDict['time'].append(SettingBezierAfterFlash(At(t + startTime2), BottomController, rightLightSetting, 80, 20, int(100* (hammerTime - flashTime) / hammerDecisteps), hammerDecisteps, 0, 100, int(flashTime * 1000)))
eventDict['time'].append(SettingBezierAfterFlash(At(t + startTime1 + hammerTime), TopController, topLightSetting, 20, 0, int(100 * (endTime - startTime1 - hammerTime) / decisteps ), decisteps, y1, y2, int(flashTime * 1000)))
eventDict['time'].append(SettingBezierAfterFlash(At(t + startTime2 + hammerTime), BottomController, rightLightSetting, 20, 0, int(100 * (endTime - startTime2 - hammerTime) / decisteps ), decisteps, y1, y2, int(flashTime * 1000)))


# A & G
# start: 10
# end: 23
startTime = 10
endTime = 15
flashTime = 0.05
decisteps = 50
y1 = 100
y2 = 100
eventDict['time'].append(SettingBezierAfterFlash(At(t + startTime), TopController, topLightSetting, 80, 20, int(100* (hammerTime - flashTime) / hammerDecisteps), hammerDecisteps, 0, 100, int(flashTime * 1000)))
eventDict['time'].append(SettingBezierAfterFlash(At(t + startTime), TopController, topLightSetting3, 80, 20, int(100* (hammerTime - flashTime) / hammerDecisteps), hammerDecisteps, 0, 100, int(flashTime * 1000)))
eventDict['time'].append(SettingBezierAfterFlash(At(t + startTime + hammerTime), TopController, topLightSetting, 20, 0, int(100 * (endTime - startTime - hammerTime) / decisteps ), decisteps, y1, y2, int(flashTime * 1000)))
eventDict['time'].append(SettingBezierAfterFlash(At(t + startTime + hammerTime), TopController, topLightSetting3, 20, 0, int(100 * (endTime - startTime - hammerTime) / decisteps ), decisteps, y1, y2, int(flashTime * 1000)))


# D & A
# start D: 11.23
# start A: 11.24
# end: 23
startTime1 = 11.23
startTime2 = 11.24
endTime = 23
flashTime = 0.05
decisteps = 50
y1 = 100
y2 = 100
eventDict['time'].append(SettingBezierAfterFlash(At(t + startTime1), TopController, topLightSetting, 80, 20, int(100* (hammerTime - flashTime) / hammerDecisteps), hammerDecisteps, 0, 100, int(flashTime * 1000)))
eventDict['time'].append(SettingBezierAfterFlash(At(t + startTime2), BottomController, rightLightSetting, 80, 20, int(100* (hammerTime - flashTime) / hammerDecisteps), hammerDecisteps, 0, 100, int(flashTime * 1000)))
eventDict['time'].append(SettingBezierAfterFlash(At(t + startTime1 + hammerTime), TopController, topLightSetting, 20, 0, int(100 * (endTime - startTime1 - hammerTime) / decisteps ), decisteps, y1, y2, int(flashTime * 1000)))
eventDict['time'].append(SettingBezierAfterFlash(At(t + startTime2 + hammerTime), BottomController, rightLightSetting, 20, 0, int(100 * (endTime - startTime2 - hammerTime) / decisteps ), decisteps, y1, y2, int(flashTime * 1000)))


# F & E
# start: 12.47
# end: 23

startTime = 12.47
endTime = 23
decisteps = 50
y1 = 100
y2 = 100
eventDict['time'].append(SettingBezierAfterFlash(At(t + startTime), BottomController, leftLightSetting, 80, 20, int(100* (hammerTime - flashTime) / hammerDecisteps), hammerDecisteps, 0, 100, int(flashTime * 1000)))
eventDict['time'].append(SettingBezierAfterFlash(At(t + startTime), TopController, topLightSetting2, 80, 20, int(100* (hammerTime - flashTime) / hammerDecisteps), hammerDecisteps, 0, 100, int(flashTime * 1000)))
eventDict['time'].append(SettingBezierAfterFlash(At(t + startTime + hammerTime), BottomController, leftLightSetting, 20, 0, int(100 * (endTime - startTime - hammerTime) / decisteps ), decisteps, y1, y2, int(flashTime * 1000)))
eventDict['time'].append(SettingBezierAfterFlash(At(t + startTime + hammerTime), TopController, topLightSetting2, 20, 0, int(100 * (endTime - startTime - hammerTime) / decisteps ), decisteps, y1, y2, int(flashTime * 1000)))


# A & F
# start: 13.87
# end: 23
startTime = 13.87
endTime = 23
decisteps = 50
y1 = 100
y2 = 100
eventDict['time'].append(SettingBezierAfterFlash(At(t + startTime), BottomController, leftLightSetting, 80, 20, int(100* (hammerTime - flashTime) / hammerDecisteps), hammerDecisteps, 0, 100, int(flashTime * 1000)))
eventDict['time'].append(SettingBezierAfterFlash(At(t + startTime), BottomController, rightLightSetting, 80, 20, int(100* (hammerTime - flashTime) / hammerDecisteps), hammerDecisteps, 0, 100, int(flashTime * 1000)))
eventDict['time'].append(SettingBezierAfterFlash(At(t + startTime + hammerTime), BottomController, leftLightSetting, 20, 0, int(100 * (endTime - startTime - hammerTime) / decisteps ), decisteps, y1, y2, int(flashTime * 1000)))
eventDict['time'].append(SettingBezierAfterFlash(At(t + startTime + hammerTime), BottomController, rightLightSetting, 20, 0, int(100 * (endTime - startTime - hammerTime) / decisteps ), decisteps, y1, y2, int(flashTime * 1000)))


# F & D
# start: 15.5
# end: 23
startTime = 15.5
endTime = 23
decisteps = 50
y1 = 100
y2 = 100
eventDict['time'].append(SettingBezierAfterFlash(At(t + startTime), TopController, topLightSetting, 80, 20, int(100* (hammerTime - flashTime) / hammerDecisteps), hammerDecisteps, 0, 100, int(flashTime * 1000)))
eventDict['time'].append(SettingBezierAfterFlash(At(t + startTime), BottomController, leftLightSetting, 80, 20, int(100* (hammerTime - flashTime) / hammerDecisteps), hammerDecisteps, 0, 100, int(flashTime * 1000)))
eventDict['time'].append(SettingBezierAfterFlash(At(t + startTime + hammerTime), TopController, topLightSetting, 20, 0, int(100 * (endTime - startTime - hammerTime) / decisteps ), decisteps, y1, y2, int(flashTime * 1000)))
eventDict['time'].append(SettingBezierAfterFlash(At(t + startTime + hammerTime), BottomController, leftLightSetting, 20, 0, int(100 * (endTime - startTime - hammerTime) / decisteps ), decisteps, y1, y2, int(flashTime * 1000)))

eventDict['time'].append(ChannelSetStatic(At(t + endTime + 3), TopController, StaticChannel0, 0))


vd = VisualDriver(eventDict, startTime=0, usesTrigger=True, music=music)
vd.start()