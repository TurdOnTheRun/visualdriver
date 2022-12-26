from visualdriver import VisualDriver
from agents import *
from events import *

music = '/home/maximilian/music/lichttanz.mp3'

eventDict = {
    'position': [],
    'time': []
}

#Right Light: 
#0 - 3:75
#4:34 - 8:01
#8:35 - 11:53
#12:00 - 14:76
#15:23 -  18
#18 - low steady until 29
beginning = 0
duration = 4
eventDict['time'].append(InstantBezier(At(beginning), Bottom2, 0, 80, int(duration*10), 100, 100, 100, 100))

starttime = beginning + 4
duration = 0.2
eventDict['time'].append(InstantBezier(At(starttime), Bottom2, 80, 30, int(duration*10), 100, 100, 100, 100))

starttime = beginning + 4.34
duration = 3.67
eventDict['time'].append(InstantBezier(At(starttime), Bottom2, 30, 80, int(duration*10), 100, 100, 100, 100))

starttime = beginning + 8.01
duration = 0.35
eventDict['time'].append(InstantBezier(At(starttime), Bottom2, 80, 30, int(duration*10), 100, 100, 100, 100))

starttime = beginning + 8.36
duration = 3.18
eventDict['time'].append(InstantBezier(At(starttime), Bottom2, 30, 90, int(duration*10), 100, 100, 100, 100))

starttime = beginning + 11.53
duration = 0.47
eventDict['time'].append(InstantBezier(At(starttime), Bottom2, 90, 30, int(duration*10), 100, 100, 100, 100))

#12:00 - 14:76
starttime = beginning + 12
duration = 2.76
eventDict['time'].append(InstantBezier(At(starttime), Bottom2, 30, 80, int(duration*10), 100, 100, 100, 100))

starttime = beginning + 14.76
duration = 0.4
eventDict['time'].append(InstantBezier(At(starttime), Bottom2, 80, 30, int(duration*10), 100, 100, 100, 100))

starttime = beginning + 15.23
duration = 2.77
eventDict['time'].append(InstantBezier(At(starttime), Bottom2, 30, 80, int(duration*10), 100, 100, 100, 100))

# starttime = beginning + 29
# duration = 2.77
# eventDict['time'].append(InstantBezier(At(starttime), Bottom2, 80, 100, int(duration*10), 100, 100, 100, 100))

starttime = beginning + 36
duration = 42.63 - 36
eventDict['time'].append(InstantBezier(At(starttime), Bottom2, 80, 100, int(duration*10), 100, 100, 100, 100))

# 42.5 - 49.24 = 6
# 50 - 54.90 = 5
# 55.3 - 61.5 = 6.2
# 62.18 - 68.3 = 6.1
# 69 - 76 = 7
# 76.30 - 81 = 4.7
# 81.5 - 88 = 6.5
# 88.9 - 94.5 = 5.6

# 42.5 - 49.24 = 6
starttime = beginning + 42.5
totalduration = 6
dimminduration = 1.5
dimmdownduration = 2
on = totalduration - dimminduration - dimmdownduration
strength = 100
eventDict['time'].append(InstantBezier(At(starttime), TopAll, 0, strength, int(dimminduration*10), 100, 100, 100, 100))
eventDict['time'].append(InstantBezier(At(starttime), Bottom2, strength, 0, int(dimminduration*10), 100, 100, 100, 100))
eventDict['time'].append(InstantBezier(At(starttime + dimminduration + on), TopAll, 100, 0, int(dimmdownduration*10), 100, 100, 100, 100))

# 50 - 54.90 = 5
starttime = beginning + 50
totalduration = 5
dimminduration = 1.5
dimmdownduration = 3
on = totalduration - dimminduration - dimmdownduration
strength = 90
eventDict['time'].append(InstantBezier(At(starttime), TopAll, 0, strength, int(dimminduration*10), 100, 100, 100, 100))
eventDict['time'].append(InstantBezier(At(starttime + dimminduration + on), TopAll, strength, 0, int(dimmdownduration*10), 100, 100, 100, 100))

# 55.3 - 61.5 = 6.2
starttime = beginning + 55.3
totalduration = 6.3
dimminduration = 1
dimmdownduration = 3
on = totalduration - dimminduration - dimmdownduration
strength = 100
eventDict['time'].append(InstantBezier(At(starttime), TopAll, 0, strength, int(dimminduration*10), 100, 100, 100, 100))
eventDict['time'].append(InstantBezier(At(starttime + dimminduration + on), TopAll, strength, 0, int(dimmdownduration*10), 100, 100, 100, 100))

# 62.18 - 68.3 = 6.1
starttime = beginning + 62.18
totalduration = 6.1
dimminduration = 1
dimmdownduration = 2
on = totalduration - dimminduration - dimmdownduration
strength = 80
eventDict['time'].append(InstantBezier(At(starttime), TopAll, 0, strength, int(dimminduration*10), 100, 100, 100, 100))
eventDict['time'].append(InstantBezier(At(starttime + dimminduration + on), TopAll, strength, 0, int(dimmdownduration*10), 100, 100, 100, 100))

# 69 - 76 = 7
starttime = beginning + 69
totalduration = 7
dimminduration = 1
dimmdownduration = 3
on = totalduration - dimminduration - dimmdownduration
strength = 90
eventDict['time'].append(InstantBezier(At(starttime), TopAll, 0, strength, int(dimminduration*10), 100, 100, 100, 100))
eventDict['time'].append(InstantBezier(At(starttime + dimminduration + on), TopAll, strength, 0, int(dimmdownduration*10), 100, 100, 100, 100))

# 76.30 - 81 = 4.7
starttime = beginning + 76.3
totalduration = 4.7
dimminduration = 1
dimmdownduration = 2
on = totalduration - dimminduration - dimmdownduration
strength = 100
eventDict['time'].append(InstantBezier(At(starttime), TopAll, 0, strength, int(dimminduration*10), 100, 100, 100, 100))
eventDict['time'].append(InstantBezier(At(starttime + dimminduration + on), TopAll, strength, 0, int(dimmdownduration*10), 100, 100, 100, 100))

# 81.5 - 88 = 6.5
starttime = beginning + 81.5
totalduration = 6.5
dimminduration = 1
dimmdownduration = 3
on = totalduration - dimminduration - dimmdownduration
strength = 100
eventDict['time'].append(InstantBezier(At(starttime), TopAll, 0, strength, int(dimminduration*10), 100, 100, 100, 100))
eventDict['time'].append(InstantBezier(At(starttime + dimminduration + on), TopAll, strength, 0, int(dimmdownduration*10), 100, 100, 100, 100))

# 88.9 - 94.5 = 5.6
starttime = beginning + 88.9
totalduration = 5.6
dimminduration = 1
dimmdownduration = 2
on = totalduration - dimminduration - dimmdownduration
strength = 86
eventDict['time'].append(InstantBezier(At(starttime), TopAll, 0, strength, int(dimminduration*10), 100, 100, 100, 100))
eventDict['time'].append(InstantBezier(At(starttime + dimminduration + on), TopAll, strength, 0, int(dimmdownduration*10), 100, 100, 100, 100))

# Strings start
# up 95 -  97 
# down 98-98.6 
# up 98.6-100

# up2 100-101.5

starttime = beginning + 95
totalduration = 3.6
dimminduration = 2
dimmdownduration = .6
on = totalduration - dimminduration - dimmdownduration
strength = 100
eventDict['time'].append(InstantBezier(At(starttime), Bottom2, 0, strength, int(dimminduration*10), 100, 100, 100, 100))
eventDict['time'].append(InstantBezier(At(starttime + dimminduration + on), Bottom2, strength, 60, int(dimmdownduration*10), 100, 100, 100, 100))

starttime = beginning + 98.6
dimminduration = 1.2
strength = 100
eventDict['time'].append(InstantBezier(At(starttime), Bottom2, 60, strength, int(dimminduration*10), 100, 100, 100, 100))

# up2 100-101.5
# down2 103 - 105
starttime = beginning + 100
totalduration = 5
dimminduration = 1
dimmdownduration = 2
on = totalduration - dimminduration - dimmdownduration
strength = 100
# dimmout right
eventDict['time'].append(InstantBezier(At(starttime), Bottom2, strength, 0, int(dimminduration*10), 100, 100, 100, 100))
# dimmwave left
eventDict['time'].append(InstantBezier(At(starttime), Bottom1, 0, strength, int(dimminduration*10), 100, 100, 100, 100))
eventDict['time'].append(InstantBezier(At(starttime + dimminduration + on), Bottom1, strength, 0, int(dimmdownduration*10), 100, 100, 100, 100))


eventDict['time'].append(InstantBezier(At(108), TopAll, 100, 0, int(duration*10), 100, 100, 100, 100))
vd = VisualDriver(eventDict, music=music, startTime=98)
vd.start()