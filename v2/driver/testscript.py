from events import *
from agents import *
from conditions import *
import pickle

TIMEEVENTS = [
    Instant(At(2), TopAll, 100),
    Instant(At(4), TopAll, 0),
    Instant(At(8), TopAll, 50)
]

POSITIONEVENTS = [
    TimeReset(At(0.15)),
    TimeAddEvents(At(0.3), [
        Flash(At(2), TopAll, 100, 250),
        Flash(At(4), TopAll, 100, 20),
        Flash(At(8), TopAll, 100, 250)
    ])
]

EVENTS = {
    'time': TIMEEVENTS,
    'position': POSITIONEVENTS
}

with open('filename.pickle', 'wb') as handle:
    pickle.dump(EVENTS, handle, protocol=pickle.HIGHEST_PROTOCOL)
