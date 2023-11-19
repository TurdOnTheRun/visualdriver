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

music = '/home/maximilian/music/vertrauung.mp3'

# BOTTOM

bottomRightLightSetting = 0
bottomRightLightChannel = Channel12

bottomLeftLightSetting = 3
bottomLeftLightChannel = Channel16

bottomVibratoControlSetting = 1
bottomVibratoControlChannel = Channel13

bottomVibratoSetting = 2
bottomVibratoChannel = Channel14
bottomVibratoSteptimeChannel = Channel15
bottomVibratoEffect = 0

# Bottom Right Light
eventDict['time'].append(SettingStatic(At(0), BottomController, bottomRightLightSetting, 0))
eventDict['time'].append(ChannelSetSetting(At(0), BottomController, bottomRightLightChannel, bottomRightLightSetting))
eventDict['time'].append(LightSetChannel(At(0), BottomController, [Light3, Light4], bottomRightLightChannel))
# Bottom Right Light
eventDict['time'].append(SettingStatic(At(0), BottomController, bottomLeftLightSetting, 0))
eventDict['time'].append(ChannelSetSetting(At(0), BottomController, bottomLeftLightChannel, bottomLeftLightSetting))
eventDict['time'].append(LightSetChannel(At(0), BottomController, [Light1, Light2], bottomLeftLightChannel))
# Bottom Vibrato Control
eventDict['time'].append(SettingStatic(At(0), BottomController, bottomVibratoControlSetting, 14))
eventDict['time'].append(ChannelSetSetting(At(0), BottomController, bottomVibratoControlChannel, bottomVibratoControlSetting))
# Bottom Vibrato
eventDict['time'].append(ChannelSetStatic(At(0), BottomController, bottomVibratoSteptimeChannel, 7)) # 70 ms per pi
eventDict['time'].append(SettingSinWave(At(0), BottomController, bottomVibratoSetting, StaticChannel0, bottomVibratoControlChannel, bottomVibratoSteptimeChannel, StaticChannel0))
eventDict['time'].append(ChannelSetSetting(At(0), BottomController, bottomVibratoChannel, bottomVibratoSetting))
eventDict['time'].append(EffectSubtractPercentage(At(0), BottomController, bottomVibratoEffect, bottomVibratoChannel))
# Bottom Vibrato Assign
eventDict['time'].append(ChannelAddEffect(At(0), BottomController, bottomRightLightChannel, bottomVibratoEffect, 0))
eventDict['time'].append(ChannelAddEffect(At(0), BottomController, bottomLeftLightChannel, bottomVibratoEffect, 0))


# TOP
topLightSetting = 0
topLightChannel = Channel12

topVibratoControlSetting = 1
topVibratoControlChannel = Channel13

topVibratoSetting = 2
topVibratoChannel = Channel14
topVibratoSteptimeChannel = Channel15
topVibratoEffect = 0

topSquareStrengthSetting = 3
topSquareStrengthChannel = Channel16

topSquareSteptimeSetting = 4
topSquareSteptimeChannel = Channel17

topSquareSetting = 5
topSquareChannel = Channel18
topSquareEffect = 1

# Top Light
eventDict['time'].append(SettingStatic(At(0), TopController, topLightSetting, 0))
eventDict['time'].append(ChannelSetSetting(At(0), TopController, topLightChannel, topLightSetting))
eventDict['time'].append(LightSetChannel(At(0), TopController, [Light1, Light2, Light3, Light4], topLightChannel))
# Top Vibrato Control
eventDict['time'].append(SettingStatic(At(0), TopController, topVibratoControlSetting, 0))
eventDict['time'].append(ChannelSetSetting(At(0), TopController, topVibratoControlChannel, topVibratoControlSetting))
# Top Vibrato
eventDict['time'].append(ChannelSetStatic(At(0), TopController, topVibratoSteptimeChannel, 5)) # 70 ms per pi
eventDict['time'].append(SettingSinWave(At(0), TopController, topVibratoSetting, StaticChannel0, topVibratoControlChannel, topVibratoSteptimeChannel, StaticChannel5))
eventDict['time'].append(ChannelSetSetting(At(0), TopController, topVibratoChannel, topVibratoSetting))
eventDict['time'].append(EffectSubtractPercentage(At(0), TopController, topVibratoEffect, topVibratoChannel))

# Top Square Control
eventDict['time'].append(SettingStatic(At(0), TopController, topSquareStrengthSetting, 0))
eventDict['time'].append(ChannelSetSetting(At(0), TopController, topSquareStrengthChannel, topSquareStrengthSetting))
eventDict['time'].append(SettingStatic(At(0), TopController, topSquareSteptimeSetting, 80))
eventDict['time'].append(ChannelSetSetting(At(0), TopController, topSquareSteptimeChannel, topSquareSteptimeSetting))
# Top Square
eventDict['time'].append(SettingSquareWave(At(0), TopController, topSquareSetting, StaticChannel0, topSquareStrengthChannel, topSquareSteptimeChannel, topSquareSteptimeChannel, StaticChannel0, StaticChannel0))
eventDict['time'].append(ChannelSetSetting(At(0), TopController, topSquareChannel, topSquareSetting))
eventDict['time'].append(EffectSubtractPercentage(At(0), TopController, topSquareEffect, topSquareChannel))


# Top Effect Assign
# Vibrato
eventDict['time'].append(ChannelAddEffect(At(0), TopController, topLightChannel, topVibratoEffect, 0))
# Strobe
eventDict['time'].append(ChannelAddEffect(At(0), TopController, topLightChannel, topSquareEffect, 1))


#Right Light: 
#0 - 3:75
#4:34 - 8:01
#8:35 - 11:53
#12:00 - 14:76
#15:23 -  18
#18 - low steady until 29

beginning = 0


duration = 4
eventDict['time'].append(SettingBezierDimm(At(beginning), BottomController, bottomRightLightSetting, 0, 85, int(duration*10), 10, 50, 100))
# eventDict['time'].append(InstantBezier(At(beginning), Bottom2, 0, 80, int(duration*10), 100, 100, 100, 100))

starttime = beginning + 4
duration = 0.2
eventDict['time'].append(SettingBezierDimm(At(starttime), BottomController, bottomRightLightSetting, 85, 30, int(duration*10), 10, 0, 100))
# eventDict['time'].append(InstantBezier(At(starttime), Bottom2, 80, 30, int(duration*10), 100, 100, 100, 100))

starttime = beginning + 4.34
duration = 3.67
eventDict['time'].append(SettingBezierDimm(At(starttime), BottomController, bottomRightLightSetting, 30, 85, int(duration*10), 10, 0, 100))
# eventDict['time'].append(InstantBezier(At(starttime), Bottom2, 30, 80, int(duration*10), 100, 100, 100, 100))

starttime = beginning + 8.01
duration = 0.35
eventDict['time'].append(SettingBezierDimm(At(starttime), BottomController, bottomRightLightSetting, 85, 30, int(duration*10), 10, 0, 100))
# eventDict['time'].append(InstantBezier(At(starttime), Bottom2, 80, 30, int(duration*10), 100, 100, 100, 100))

starttime = beginning + 8.36
duration = 3.18
eventDict['time'].append(SettingBezierDimm(At(starttime), BottomController, bottomRightLightSetting, 30, 90, int(duration*10), 10, 0, 100))
# eventDict['time'].append(InstantBezier(At(starttime), Bottom2, 30, 90, int(duration*10), 100, 100, 100, 100))

starttime = beginning + 11.53
duration = 0.47
eventDict['time'].append(SettingBezierDimm(At(starttime), BottomController, bottomRightLightSetting, 90, 50, int(duration*10), 10, 0, 100))
# eventDict['time'].append(InstantBezier(At(starttime), Bottom2, 90, 50, int(duration*10), 100, 100, 100, 100))

#12:00 - 14:76
starttime = beginning + 12
duration = 2.76
eventDict['time'].append(SettingBezierDimm(At(starttime), BottomController, bottomRightLightSetting, 50, 85, int(duration*10), 10, 0, 100))
# eventDict['time'].append(InstantBezier(At(starttime), Bottom2, 50, 80, int(duration*10), 100, 100, 100, 100))

starttime = beginning + 14.76
duration = 0.4
eventDict['time'].append(SettingBezierDimm(At(starttime), BottomController, bottomRightLightSetting, 85, 30, int(duration*10), 10, 0, 100))
# eventDict['time'].append(InstantBezier(At(starttime), Bottom2, 80, 30, int(duration*10), 100, 100, 100, 100))

starttime = beginning + 15.23
duration = 2.77
eventDict['time'].append(SettingBezierDimm(At(starttime), BottomController, bottomRightLightSetting, 30, 85, int(duration*10), 10, 0, 100))
eventDict['time'].append(SettingBezierDimm(At(starttime), BottomController, bottomVibratoControlSetting, 14, 8, int(duration*10), 10, 0, 100))

# eventDict['time'].append(InstantBezier(At(starttime), Bottom2, 30, 80, int(duration*10), 100, 100, 100, 100))

# # Motor
# # starttime = beginning + 21
# # eventDict['time'].append(MotorSpeed(At(starttime), 50))

starttime = beginning + 29
duration = 1
# eventDict['time'].append(Vibrato(At(starttime), BottomAll, 3, 5, 3))
eventDict['time'].append(SettingBezierDimm(At(starttime), BottomController, bottomRightLightSetting, 85, 90, int(duration*10), 10, 0, 100))
eventDict['time'].append(SettingBezierDimm(At(starttime), BottomController, bottomVibratoControlSetting, 8, 18, int(duration*10), 10, 0, 40))

# eventDict['time'].append(InstantBezier(At(starttime), Bottom2, 80, 90, int(duration*10), 100, 100, 100, 100))

# starttime = beginning + 30.9
# eventDict['time'].append(Vibrato(At(starttime), BottomAll, 3, 6, 3))

starttime = beginning + 33
duration = 2
eventDict['time'].append(SettingBezierDimm(At(starttime), BottomController, bottomRightLightSetting, 90, 80, int(duration*10), 10, 0, 100))
eventDict['time'].append(SettingBezierDimm(At(starttime), BottomController, bottomVibratoControlSetting, 18, 10, int(duration*10), 10, 0, 100))

# eventDict['time'].append(InstantBezier(At(starttime), Bottom2, 90, 80, int(duration*10), 100, 100, 100, 100))

starttime = beginning + 37
duration = 1
# eventDict['time'].append(Vibrato(At(starttime), BottomAll, 3, 3, 3))
eventDict['time'].append(SettingBezierDimm(At(starttime), BottomController, bottomRightLightSetting, 80, 85, int(duration*5), 20, 0, 100))
eventDict['time'].append(SettingBezierDimm(At(starttime), BottomController, bottomVibratoControlSetting, 10, 18, int(duration*10), 10, 0, 100))


starttime = beginning + 39.3
duration = 0.5
eventDict['time'].append(SettingBezierDimm(At(starttime), BottomController, bottomRightLightSetting, 85, 90, int(duration*5), 20, 0, 100))
# eventDict['time'].append(SettingBezierDimm(At(starttime), BottomController, bottomVibratoControlSetting, 18, 20, int(duration*10), 10, 0, 100))


# 42.5 - 49.24 = 6
# 50 - 54.90 = 5
# 55.3 - 61.5 = 6.2
# 62.18 - 68.3 = 6.1
# 69 - 76 = 7
# 76.30 - 81 = 4.7
# 81.5 - 88 = 6.5
# 88.9 - 94.5 = 5.6

# STROBE:

# 51 - 55 leicht
# 55 - 62 saerker
# 62 - 68 auf voll
# 68 - aus
# 81 - 85 medium
# 88 - 94 light


# eventDict['time'].append(MotorSpeed(At(42), 90))

# 1
# 42.5 - 49.24 = 6
starttime = beginning + 42.5
totalduration = 6
dimminduration = 1.5
dimmdownduration = 1.7
on = totalduration - dimminduration - dimmdownduration
strength = 70
# eventDict['time'].append(Vibrato(At(starttime), TopAll, 3, 20, 5))
# eventDict['time'].append(InstantBezier(At(starttime), TopAll, 0, strength, int(dimminduration*10), 100, 100, 100, 100))
eventDict['time'].append(SettingBezierDimm(At(starttime), BottomController, bottomRightLightSetting, 90, 0, int(dimminduration*10), 10, 50, 100))
eventDict['time'].append(SettingBezierDimm(At(starttime), TopController, topLightSetting, 0, strength, int(dimminduration*10), 10, 0, 100))
eventDict['time'].append(SettingBezierDimm(At(starttime), TopController, topVibratoControlSetting, 0, 25, int(dimminduration*10), 10, 0, 100))
# eventDict['time'].append(InstantBezier(At(starttime + dimminduration + on), TopAll, 100, 10, int(dimmdownduration*10), 100, 100, 100, 100))
eventDict['time'].append(SettingBezierDimm(At(starttime + dimminduration + on), TopController, topLightSetting, strength, 6, int(dimmdownduration*10), 10, 0, 100))
eventDict['time'].append(SettingBezierDimm(At(starttime + dimminduration + on), TopController, topVibratoControlSetting, 25, 0, int(dimmdownduration*10), 10, 0, 100))


# 2
# 50 - 54.90 = 5
# vibrato continues. 1 light starts shifting
# light shift at 53
starttime = beginning + 50
totalduration = 5
dimminduration = 1.5
dimmdownduration = 3
on = totalduration - dimminduration - dimmdownduration
strength = 80
# eventDict['time'].append(Vibrato(At(starttime), TopAll, 3, 20, 6))
# eventDict['time'].append(InstantBezier(At(starttime), TopAll, 10, strength, int(dimminduration*10), 100, 100, 100, 100))
eventDict['time'].append(SettingBezierDimm(At(starttime), TopController, topLightSetting, 6, strength, int(dimminduration*10), 10, 0, 100))
eventDict['time'].append(SettingBezierDimm(At(starttime), TopController, topVibratoControlSetting, 0, 10, int(dimminduration*10), 10, 0, 100))
eventDict['time'].append(SettingBezierDimm(At(starttime), TopController, topSquareStrengthSetting, 0, 20, int(dimminduration*10), 10, 0, 100))

# eventDict['time'].append(InstantBezier(At(starttime + dimminduration + on), TopAll, strength, 10, int(dimmdownduration*10), 60, 30, 100, 45))
eventDict['time'].append(SettingBezierDimm(At(starttime + dimminduration + on), TopController, topLightSetting, strength, 6, int(dimmdownduration*10), 10, 0, 100))
eventDict['time'].append(SettingBezierDimm(At(starttime + dimminduration + on), TopController, topVibratoControlSetting, 10, 0, int(dimmdownduration*10), 10, 0, 100))
# eventDict['time'].append(SettingBezierDimm(At(starttime + dimminduration + on), TopController, topSquareStrengthSetting, 20, 0, int(dimmdownduration*10), 10, 0, 100))

# eventDict['time'].append(Vibrato(At(53), Top1, 3, 60, 2))


# 3
# 55.3 - 61.5 = 6.2
# shift intensifies at 58
starttime = beginning + 55.3
totalduration = 6.3
dimminduration = 1
dimmdownduration = 3
on = totalduration - dimminduration - dimmdownduration
strength = 80
# eventDict['time'].append(InstantBezier(At(starttime), TopAll, 10, strength, int(dimminduration*10), 100, 100, 100, 100))
eventDict['time'].append(SettingBezierDimm(At(starttime), TopController, topLightSetting, 6, strength, int(dimminduration*10), 10, 0, 100))
eventDict['time'].append(SettingBezierDimm(At(starttime), TopController, topVibratoControlSetting, 0, 10, int(dimminduration*10), 10, 0, 100))
eventDict['time'].append(SettingBezierDimm(At(starttime), TopController, topSquareStrengthSetting, 20, 50, int(dimminduration*10), 10, 0, 50))

# eventDict['time'].append(Vibrato(At(58), Top1, 3, 90, 2))
# eventDict['time'].append(InstantBezier(At(starttime + dimminduration + on), TopAll, strength, 10, int(dimmdownduration*10), 60, 30, 100, 45))
eventDict['time'].append(SettingBezierDimm(At(starttime + dimminduration + on), TopController, topLightSetting, strength, 6, int(dimmdownduration*10), 10, 0, 100))
eventDict['time'].append(SettingBezierDimm(At(starttime + dimminduration + on), TopController, topVibratoControlSetting, 10, 0, int(dimmdownduration*10), 10, 0, 100))
eventDict['time'].append(SettingBezierDimm(At(starttime + dimminduration + on), TopController, topSquareStrengthSetting, 50, 10, int(dimmdownduration*10), 10, 0, 100))

# eventDict['time'].append(Vibrato(At(61), Top1, 3, 20, 6))

#4
# 62.18 - 68.3 = 6.1
# synchronized but intense vibrato
starttime = beginning + 62.18
totalduration = 6.5
dimminduration = 1
dimmdownduration = 2
on = totalduration - dimminduration - dimmdownduration
strength = 70
# eventDict['time'].append(Vibrato(At(starttime), TopAll, 3, 30, 3))
# eventDict['time'].append(InstantBezier(At(starttime), TopAll, 10, strength, int(dimminduration*10), 100, 100, 100, 100))
eventDict['time'].append(SettingBezierDimm(At(starttime), TopController, topLightSetting, 6, strength, int(dimminduration*10), 10, 0, 100))
eventDict['time'].append(SettingBezierDimm(At(starttime), TopController, topVibratoControlSetting, 0, 10, int(dimminduration*10), 10, 0, 100))
eventDict['time'].append(SettingBezierDimm(At(starttime+0.5), TopController, topSquareStrengthSetting, 10, 100, int((dimminduration-0.5)*10), 10, 0, 100))
# eventDict['time'].append(Vibrato(At(63), TopAll, 3, 40, 3))
# eventDict['time'].append(Vibrato(At(64), TopAll, 3, 60, 3))
# eventDict['time'].append(InstantBezier(At(starttime + dimminduration + on), TopAll, strength, 0, int(dimmdownduration*10), 100, 100, 100, 100))
eventDict['time'].append(SettingBezierDimm(At(starttime + dimminduration + on), TopController, topLightSetting, strength, 0, int(dimmdownduration*10), 10, 0, 100))
eventDict['time'].append(SettingBezierDimm(At(starttime + dimminduration + on), TopController, topVibratoControlSetting, 10, 0, int(dimmdownduration*10), 10, 0, 100))
# Square turned off after dark 

#5
# 69 - 76 = 7
#no to very light vibrato
starttime = beginning + 69
totalduration = 7
dimminduration = 1
dimmdownduration = 3
on = totalduration - dimminduration - dimmdownduration
strength = 75
# eventDict['time'].append(Vibrato(At(starttime), TopAll, 3, 20, 5))
# eventDict['time'].append(InstantBezier(At(starttime), TopAll, 0, strength, int(dimminduration*10), 100, 100, 100, 100))
eventDict['time'].append(SettingStatic(At(starttime), TopController, topSquareStrengthSetting, 0))
eventDict['time'].append(SettingBezierDimm(At(starttime), TopController, topLightSetting, 0, strength, int(dimminduration*10), 10, 50, 100))
eventDict['time'].append(SettingBezierDimm(At(starttime), TopController, topVibratoControlSetting, 0, 10, int(dimminduration*10), 10, 0, 100))
# eventDict['time'].append(InstantBezier(At(starttime + dimminduration + on), TopAll, strength, 10, int(dimmdownduration*10), 100, 100, 100, 100))
eventDict['time'].append(SettingBezierDimm(At(starttime + dimminduration + on), TopController, topLightSetting, strength, 6, int(dimmdownduration*10), 10, 0, 100))
eventDict['time'].append(SettingBezierDimm(At(starttime + dimminduration + on), TopController, topVibratoControlSetting, 10, 0, int(dimmdownduration*10), 10, 0, 100))


#6
# 76.30 - 81 = 4.7
#vibrato kicks in again
starttime = beginning + 76.3
totalduration = 4.7
dimminduration = 1
dimmdownduration = 2
on = totalduration - dimminduration - dimmdownduration
strength = 80
# eventDict['time'].append(InstantBezier(At(starttime), TopAll, 10, strength, int(dimminduration*10), 100, 100, 100, 100))
eventDict['time'].append(SettingBezierDimm(At(starttime), TopController, topLightSetting, 6, strength, int(dimminduration*10), 10, 50, 100))
eventDict['time'].append(SettingBezierDimm(At(starttime), TopController, topVibratoControlSetting, 0, 10, int(dimminduration*10), 10, 0, 100))
# eventDict['time'].append(InstantBezier(At(starttime + dimminduration + on), TopAll, strength, 10, int(dimmdownduration*10), 100, 100, 100, 100))
eventDict['time'].append(SettingBezierDimm(At(starttime + dimminduration + on), TopController, topLightSetting, strength, 3, int(dimmdownduration*10), 10, 0, 100))
eventDict['time'].append(SettingBezierDimm(At(starttime + dimminduration + on), TopController, topVibratoControlSetting, 10, 0, int(dimmdownduration*10), 10, 0, 100))

#7
# 81.5 - 88 = 6.5
#strong vibrato
starttime = beginning + 81.5
totalduration = 6.5
dimminduration = 1
dimmdownduration = 3
on = totalduration - dimminduration - dimmdownduration
strength = 80
# eventDict['time'].append(InstantBezier(At(starttime), TopAll, 10, strength, int(dimminduration*10), 100, 100, 100, 100))
eventDict['time'].append(SettingBezierDimm(At(starttime), TopController, topLightSetting, 3, strength, int(dimminduration*10), 10, 0, 100))
eventDict['time'].append(SettingBezierDimm(At(starttime), TopController, topVibratoControlSetting, 0, 10, int(dimminduration*10), 10, 0, 100))
eventDict['time'].append(SettingBezierDimm(At(starttime), TopController, topSquareStrengthSetting, 0, 40, int(dimminduration*10), 10, 0, 50))

# eventDict['time'].append(InstantBezier(At(starttime + dimminduration + on), TopAll, strength, 10, int(dimmdownduration*10), 100, 100, 100, 100))
eventDict['time'].append(SettingBezierDimm(At(starttime + dimminduration + on), TopController, topLightSetting, strength, 6, int(dimmdownduration*5), 20, 0, 100))
eventDict['time'].append(SettingBezierDimm(At(starttime + dimminduration + on), TopController, topVibratoControlSetting, 10, 0, int(dimmdownduration*10), 10, 0, 100))
eventDict['time'].append(SettingBezierDimm(At(starttime + dimminduration + on), TopController, topSquareStrengthSetting, 40, 0, int((dimmdownduration-2)*10), 10, 0, 100))

#8
# 88.9 - 94.5 = 5.6
#light vibrato
starttime = beginning + 88.9
totalduration = 5.6
dimminduration = 1
dimmdownduration = 2
on = totalduration - dimminduration - dimmdownduration
strength = 75
# eventDict['time'].append(InstantBezier(At(starttime), TopAll, 10, strength, int(dimminduration*10), 100, 100, 100, 100))
eventDict['time'].append(SettingBezierDimm(At(starttime), TopController, topLightSetting, 6, strength, int(dimminduration*10), 10, 0, 100))
eventDict['time'].append(SettingBezierDimm(At(starttime), TopController, topVibratoControlSetting, 0, 10, int(dimminduration*10), 10, 0, 100))
eventDict['time'].append(SettingBezierDimm(At(starttime), TopController, topSquareStrengthSetting, 0, 10, int(dimminduration*10), 10, 0, 40))

# eventDict['time'].append(InstantBezier(At(starttime + dimminduration + on), TopAll, strength, 5, int(dimmdownduration*10), 100, 100, 100, 100))
eventDict['time'].append(SettingBezierDimm(At(starttime + dimminduration + on), TopController, topLightSetting, strength, 3, int(dimmdownduration*5), 20, 0, 100))
eventDict['time'].append(SettingBezierDimm(At(starttime + dimminduration + on), TopController, topVibratoControlSetting, 10, 0, int(dimmdownduration*10), 10, 0, 100))
eventDict['time'].append(SettingBezierDimm(At(starttime + dimminduration + on), TopController, topSquareStrengthSetting, 10, 0, int(dimmdownduration*10), 10, 0, 100))


# Strings start
# 1
# up 95 -  97 
# down 98-98.6 
# up 98.6-100

# eventDict['time'].append(MotorSpeed(At(93), 50))

starttime = beginning + 95
totalduration = 3.6
dimminduration = 2
dimmdownduration = .6
on = totalduration - dimminduration - dimmdownduration
strength = 80
# eventDict['time'].append(InstantBezier(At(starttime), TopAll, 5, 0, int(dimminduration*10), 100, 100, 100, 100))
eventDict['time'].append(SettingBezierDimm(At(starttime), TopController, topLightSetting, 3, 0, int(dimminduration*10), 10, 0, 100))
# eventDict['time'].append(InstantBezier(At(starttime), Bottom2, 10, strength, int(dimminduration*10), 100, 100, 100, 100))
eventDict['time'].append(SettingBezierDimm(At(starttime), BottomController, bottomRightLightSetting, 0, strength, int(dimminduration*10), 10, 0, 100))
# eventDict['time'].append(InstantBezier(At(starttime + dimminduration + on), Bottom2, strength, 60, int(dimmdownduration*10), 100, 100, 100, 100))
eventDict['time'].append(SettingBezierDimm(At(starttime + dimminduration + on), BottomController, bottomRightLightSetting, strength, 50, int(dimmdownduration*10), 10, 0, 100))


starttime = beginning + 98.6
dimminduration = 1.2
strength = 85
eventDict['time'].append(SettingBezierDimm(At(starttime), BottomController, bottomRightLightSetting, 50, strength, int(dimminduration*10), 10, 0, 100))
# eventDict['time'].append(InstantBezier(At(starttime), Bottom2, 60, strength, int(dimminduration*10), 100, 100, 100, 100))

# 2
# up 100-101.5 
# down 102.5 - 103
# up2 103-103.6
starttime = beginning + 100
totalduration = 3
dimminduration = 1.5
dimmdownduration = .5
on = totalduration - dimminduration - dimmdownduration
strength = 90
# # dimmout right
# eventDict['time'].append(InstantBezier(At(starttime), Bottom2, 90, 0, int(dimminduration*10), 100, 100, 100, 100))
eventDict['time'].append(SettingBezierDimm(At(starttime), BottomController, bottomRightLightSetting, 85, 0, int(dimminduration*10), 10, 0, 100))

# # dimmwave left
# eventDict['time'].append(InstantBezier(At(starttime), Bottom1, 0, strength, int(dimminduration*10), 100, 100, 100, 100))
eventDict['time'].append(SettingBezierDimm(At(starttime), BottomController, bottomLeftLightSetting, 0, strength, int(dimminduration*10), 10, 0, 100))
# eventDict['time'].append(InstantBezier(At(starttime + dimminduration + on), Bottom1, strength, 60, int(dimmdownduration*10), 100, 100, 100, 100))
eventDict['time'].append(SettingBezierDimm(At(starttime + dimminduration + on), BottomController, bottomLeftLightSetting, strength, 60, int(dimmdownduration*10), 10, 0, 100))


starttime = beginning + 103
dimminduration = .6
strength = 90
# eventDict['time'].append(InstantBezier(At(starttime), Bottom1, 60, strength, int(dimminduration*10), 100, 100, 100, 100))
eventDict['time'].append(SettingBezierDimm(At(starttime), BottomController, bottomLeftLightSetting, 50, strength, int(dimminduration*10), 10, 0, 100))


# 3:
# up 105 - 106.4
# down 107 - 108.3
# up 108.3 - 109.3
starttime = beginning + 105
totalduration = 3.3
dimminduration = 1.4
dimmdownduration = 1.3
on = totalduration - dimminduration - dimmdownduration
strength = 90
# # dimmout left
# eventDict['time'].append(InstantBezier(At(starttime), Bottom1, strength, 0, int(dimminduration*10), 100, 100, 100, 100))
eventDict['time'].append(SettingBezierDimm(At(starttime), BottomController, bottomLeftLightSetting, 90, 0, int(dimminduration*10), 10, 0, 100))

# # dimmwave right
# eventDict['time'].append(InstantBezier(At(starttime), Bottom2, 0, strength, int(dimminduration*10), 100, 100, 100, 100))
eventDict['time'].append(SettingBezierDimm(At(starttime), BottomController, bottomRightLightSetting, 0, strength, int(dimminduration*10), 10, 0, 100))
# eventDict['time'].append(InstantBezier(At(starttime + dimminduration + on), Bottom2, strength, 60, int(dimmdownduration*10), 100, 100, 100, 100))
eventDict['time'].append(SettingBezierDimm(At(starttime + dimminduration + on), BottomController, bottomRightLightSetting, strength, 50, int(dimmdownduration*10), 10, 0, 100))


starttime = beginning + 108.3
dimminduration = 1
strength = 90
# eventDict['time'].append(InstantBezier(At(starttime), Bottom2, 60, strength, int(dimminduration*10), 100, 100, 100, 100))
eventDict['time'].append(SettingBezierDimm(At(starttime), BottomController, bottomRightLightSetting, 50, strength, int(dimminduration*10), 10, 0, 100))


# 4
# up:  111 - 112 
# down: 112.3 - 113.4
# up 113.4 - 114
# down 115 - 116
starttime = beginning + 111
totalduration = 3
dimminduration = 1
dimmdownduration = 1.2
on = totalduration - dimminduration - dimmdownduration
strength = 90
# # dimmout right
# eventDict['time'].append(InstantBezier(At(starttime), Bottom2, strength, 0, int(dimminduration*10), 100, 100, 100, 100))
eventDict['time'].append(SettingBezierDimm(At(starttime), BottomController, bottomRightLightSetting, 90, 0, int(dimminduration*10), 10, 0, 100))

# # dimmwave left
# eventDict['time'].append(InstantBezier(At(starttime), Bottom1, 0, strength, int(dimminduration*10), 100, 100, 100, 100))
eventDict['time'].append(SettingBezierDimm(At(starttime), BottomController, bottomLeftLightSetting, 0, strength, int(dimminduration*10), 10, 0, 100))
# eventDict['time'].append(InstantBezier(At(starttime + dimminduration + on), Bottom1, strength, 60, int(dimmdownduration*10), 100, 100, 100, 100))
eventDict['time'].append(SettingBezierDimm(At(starttime + dimminduration + on), BottomController, bottomLeftLightSetting, strength, 50, int(dimmdownduration*10), 10, 0, 100))


starttime = beginning + 113.4
totalduration = 2.6
dimminduration = .6
dimmdownduration = 1
on = totalduration - dimminduration - dimmdownduration
strength = 90
# # dimmwave left
# eventDict['time'].append(InstantBezier(At(starttime), Bottom1, 60, strength, int(dimminduration*10), 100, 100, 100, 100))
eventDict['time'].append(SettingBezierDimm(At(starttime), BottomController, bottomLeftLightSetting, 50, strength, int(dimminduration*10), 10, 0, 100))
# eventDict['time'].append(InstantBezier(At(starttime + dimminduration + on), Bottom1, strength, 0, int(dimmdownduration*10), 100, 100, 100, 100))
eventDict['time'].append(SettingBezierDimm(At(starttime + dimminduration + on), BottomController, bottomLeftLightSetting, strength, 0, int(dimmdownduration*5), 20, 0, 100))

# 5
# up: 116 - 117.6
# down 119 - 120
# strong vibrato at 120
# up 120 - 120,4
# down: 120.6 - 121.3
starttime = beginning + 116
totalduration = 4
dimminduration = 1.6
dimmdownduration = 1
on = totalduration - dimminduration - dimmdownduration
strength = 90

# # dimmwave right
# eventDict['time'].append(InstantBezier(At(starttime), Bottom2, 0, strength, int(dimminduration*10), 100, 100, 100, 100))
eventDict['time'].append(SettingBezierDimm(At(starttime), BottomController, bottomRightLightSetting, 0, strength, int(dimminduration*10), 10, 0, 100))
# eventDict['time'].append(InstantBezier(At(starttime + dimminduration + on), Bottom2, strength, 60, int(dimmdownduration*10), 100, 100, 100, 100))
eventDict['time'].append(SettingBezierDimm(At(starttime + dimminduration + on), BottomController, bottomRightLightSetting, strength, 40, int(dimmdownduration*10), 10, 0, 100))


starttime = beginning + 120
totalduration = 1.3
dimminduration = .4
dimmdownduration = .7
on = totalduration - dimminduration - dimmdownduration
strength = 80
# # dimmwave right
# eventDict['time'].append(Vibrato(At(starttime), Bottom2, 3, 40, 3))
# eventDict['time'].append(InstantBezier(At(starttime), Bottom2, 60, strength, int(dimminduration*10), 100, 100, 100, 100))
eventDict['time'].append(SettingBezierDimm(At(starttime), BottomController, bottomRightLightSetting, 40, strength, int(dimminduration*10), 10, 0, 100))
# eventDict['time'].append(InstantBezier(At(starttime + dimminduration + on), Bottom2, strength, 0, int(dimmdownduration*10), 100, 100, 100, 100))
eventDict['time'].append(SettingBezierDimm(At(starttime + dimminduration + on), BottomController, bottomRightLightSetting, strength, 0, int(dimmdownduration*10), 10, 0, 100))
# eventDict['time'].append(Vibrato(At(121.3), Bottom2, 3, 10, 3))

# 6
# top with vibrato 
# up: 121.5 - 123
# down: 124 - 125
# up 125 - 126
# down 126 - 126.8
starttime = beginning + 121.5
totalduration = 3.5
dimminduration = 1.5
dimmdownduration = 1
on = totalduration - dimminduration - dimmdownduration
strength = 70
# topstrength = 40
# #dimmewave top
# eventDict['time'].append(Vibrato(At(starttime), TopAll, 3, 80, 4))
# eventDict['time'].append(InstantBezier(At(starttime), TopAll, 0, topstrength, int(dimminduration*10), 100, 100, 100, 100))
# # dimmwave left
# eventDict['time'].append(Vibrato(At(starttime), Bottom1, 3, 40, 3))
# eventDict['time'].append(InstantBezier(At(starttime), Bottom1, 0, strength, int(dimminduration*10), 100, 100, 100, 100))
eventDict['time'].append(SettingBezierDimm(At(starttime), BottomController, bottomLeftLightSetting, 0, strength, int(dimminduration*10), 10, 0, 100))
# eventDict['time'].append(InstantBezier(At(starttime + dimminduration + on), Bottom1, strength, 40, int(dimmdownduration*10), 100, 100, 100, 100))
eventDict['time'].append(SettingBezierDimm(At(starttime + dimminduration + on), BottomController, bottomLeftLightSetting, strength, 30, int(dimmdownduration*5), 20, 0, 100))


starttime = beginning + 125
totalduration = 1.8
dimminduration = 1
dimmdownduration = .8
on = totalduration - dimminduration - dimmdownduration
strength = 50
# #dimmewave top
# eventDict['time'].append(InstantBezier(At(starttime), TopAll, topstrength, 0, int(totalduration*10), 100, 100, 100, 100))
# # dimmwave left
# eventDict['time'].append(InstantBezier(At(starttime), Bottom1, 40, strength, int(dimminduration*10), 100, 100, 100, 100))
eventDict['time'].append(SettingBezierDimm(At(starttime), BottomController, bottomLeftLightSetting, 30, strength, int(dimminduration*10), 10, 0, 100))
# eventDict['time'].append(InstantBezier(At(starttime + dimminduration + on), Bottom1, strength, 0, int(dimmdownduration*10), 100, 100, 100, 100))
eventDict['time'].append(SettingBezierDimm(At(starttime + dimminduration + on), BottomController, bottomLeftLightSetting, strength, 0, int(dimmdownduration*10), 10, 0, 100))
# eventDict['time'].append(Vibrato(At(126.8), TopAll, 0, 0, 0))
# eventDict['time'].append(Vibrato(At(126.8), Bottom1, 3, 10, 3))


# 7
# up: 126.8 - 129
# down: 129.4 - 130
# up 130.2 - 131.2
# down 132-132.6
starttime = beginning + 126.8
totalduration = 3.2
dimminduration = 2.2
dimmdownduration = .6
on = totalduration - dimminduration - dimmdownduration
strength = 85
topstrength = 20

# eventDict['time'].append(Vibrato(At(starttime), TopAll, 3, 10, 4))
# eventDict['time'].append(InstantBezier(At(starttime), TopAll, 0, topstrength, int(dimminduration*10), 100, 100, 100, 100))
# # dimmwave right
# eventDict['time'].append(InstantBezier(At(starttime), Bottom2, 0, strength, int(dimminduration*10), 100, 100, 100, 100))
eventDict['time'].append(SettingBezierDimm(At(starttime), BottomController, bottomRightLightSetting, 0, strength, int(dimminduration*10), 10, 0, 100))
# eventDict['time'].append(InstantBezier(At(starttime + dimminduration + on), Bottom2, strength, 60, int(dimmdownduration*10), 100, 100, 100, 100))
eventDict['time'].append(SettingBezierDimm(At(starttime + dimminduration + on), BottomController, bottomRightLightSetting, strength, 50, int(dimmdownduration*10), 10, 0, 100))


starttime = beginning + 130.2
totalduration = 2.4
dimminduration = 1
dimmdownduration = .6
on = totalduration - dimminduration - dimmdownduration
strength = 80
# # dimmwave right
# eventDict['time'].append(InstantBezier(At(starttime), TopAll, topstrength, 0, int(totalduration*10), 100, 100, 100, 100))
# eventDict['time'].append(InstantBezier(At(starttime), Bottom2, 60, strength, int(dimminduration*10), 100, 100, 100, 100))
eventDict['time'].append(SettingBezierDimm(At(starttime), BottomController, bottomRightLightSetting, 50, strength, int(dimminduration*10), 10, 0, 100))
# eventDict['time'].append(InstantBezier(At(starttime + dimminduration + on), Bottom2, strength, 0, int(dimmdownduration*10), 100, 100, 100, 100))
eventDict['time'].append(SettingBezierDimm(At(starttime + dimminduration + on), BottomController, bottomRightLightSetting, strength, 0, int(dimmdownduration*10), 10, 0, 100))


# 8
# strong vibrato 133 - 137
# up: 132 - 134.8
# down: 136 - 138
starttime = beginning + 132
totalduration = 6
dimminduration = 2.8
dimmdownduration = 2
on = totalduration - dimminduration - dimmdownduration
strength = 90
topstrength = 30

# eventDict['time'].append(Vibrato(At(starttime), TopAll, 3, 5, 4))
# eventDict['time'].append(InstantBezier(At(starttime), TopAll, 0, topstrength, int(dimminduration*10), 100, 100, 100, 100))

# # dimmwave left
# eventDict['time'].append(InstantBezier(At(starttime), Bottom1, 0, strength, int(dimminduration*10), 100, 100, 100, 100))
eventDict['time'].append(SettingBezierDimm(At(starttime), BottomController, bottomLeftLightSetting, 0, strength, int(dimminduration*10), 10, 0, 100))

# eventDict['time'].append(Vibrato(At(starttime), TopAll, 3, 80, 4))
# eventDict['time'].append(Vibrato(At(133.5), Bottom1, 3, 40, 4))
# eventDict['time'].append(InstantBezier(At(starttime + dimminduration + on), TopAll, topstrength, 0, int(dimmdownduration*10), 100, 100, 100, 100))
# eventDict['time'].append(InstantBezier(At(starttime + dimminduration + on), Bottom1, strength, 0, int(dimmdownduration*10), 100, 100, 100, 100))
eventDict['time'].append(SettingBezierDimm(At(starttime + dimminduration + on), BottomController, bottomLeftLightSetting, strength, 0, int(dimmdownduration*10), 10, 0, 100))
# eventDict['time'].append(Vibrato(At(137), Bottom2, 3, 10, 3))
# eventDict['time'].append(Vibrato(At(137), TopAll, 0, 0, 0))


# 9
# up: 138 - 139.5
# down: 143 - 146
starttime = beginning + 138
totalduration = 8
dimminduration = 1.5
dimmdownduration = 2
on = totalduration - dimminduration - dimmdownduration
strength = 80
# dimmwave right
# eventDict['time'].append(InstantBezier(At(starttime), Bottom2, 0, strength, int(dimminduration*10), 100, 100, 100, 100))
eventDict['time'].append(SettingBezierDimm(At(starttime), BottomController, bottomRightLightSetting, 0, strength, int(dimminduration*10), 10, 0, 100))
# eventDict['time'].append(InstantBezier(At(starttime + dimminduration + on), Bottom2, strength, 0, int(dimmdownduration*10), 100, 100, 100, 100))
eventDict['time'].append(SettingBezierDimm(At(starttime + dimminduration + on), BottomController, bottomRightLightSetting, strength, 0, int(dimmdownduration*10), 10, 0, 100))

eventDict['time'].append(ChannelRemoveEffects(At(150), BottomController, Channel20))

# eventDict['time'].append(InstantBezier(At(150), TopAll, 100, 0, int(duration*10), 100, 100, 100, 100))


vd = VisualDriver(eventDict, music=music, startTime=90)
vd.start()