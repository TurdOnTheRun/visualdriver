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

starttime = 0
firstdimmlength = 3.75
eventDict['time'].append(InstantBezier(At(starttime), Bottom2, 0, 80, int(firstdimmlength*10), 100, 100, 100, 100))
firsthickuptime = starttime + 3.75
firsthickuplength = 0.5
eventDict['time'].append(InstantBezier(At(firsthickuptime), Bottom2, 80, 40, int(firsthickuplength*10), 100, 100, 100, 100))
seconddimmtime = starttime + 4.34
seconddimmlength = 3.67
eventDict['time'].append(InstantBezier(At(seconddimmtime), Bottom2, 40, 80, int(seconddimmlength*10), 100, 100, 100, 100))
secondhickuptime = starttime + 8.01
secondickuplength = 0.35
eventDict['time'].append(InstantBezier(At(secondhickuptime), Bottom2, 80, 40, int(secondickuplength*10), 100, 100, 100, 100))
thirddimmtime = starttime + 8.36
thirddimmlength = 3.18
eventDict['time'].append(InstantBezier(At(thirddimmtime), Bottom2, 40, 100, int(thirddimmlength*10), 100, 100, 100, 100))
thirdhickuptime = starttime + 11.53
thirdickuplength = 0.07
eventDict['time'].append(InstantBezier(At(thirdhickuptime), Bottom2, 100, 50, int(thirdickuplength*10), 100, 100, 100, 100))
#12:00 - 14:76
fourthdimmtime = starttime + 12
fourthdimmlength = 2.76
eventDict['time'].append(InstantBezier(At(fourthdimmtime), Bottom2, 50, 80, int(fourthdimmlength*10), 100, 100, 100, 100))
fourthhickuptime = starttime + 14.76
fourthdimmlength = 0.4
eventDict['time'].append(InstantBezier(At(fourthhickuptime), Bottom2, 80, 40, int(fourthdimmlength*10), 100, 100, 100, 100))
fifthdimmtime = starttime + 15.23
fifthdimmlength = 2.77
eventDict['time'].append(InstantBezier(At(fifthdimmtime), Bottom2, 50, 80, int(fifthdimmlength*10), 100, 100, 100, 100))
sixthdimmtime = starttime + 36
sixthdimmlength = 42.63 - 36
eventDict['time'].append(InstantBezier(At(sixthdimmtime), Bottom2, 80, 100, int(sixthdimmlength*10), 100, 100, 100, 100))
eventDict['time'].append(InstantBezier(At(43), Bottom2, 100, 0, int(1), 100, 100, 100, 100))
vd = VisualDriver(eventDict, music=music)
vd.start()