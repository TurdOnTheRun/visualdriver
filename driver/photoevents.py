from events import *
from settings import TRIGGER_SONY_DOWN, TRIGGER_SONY_UP


def FlashCollection(agentsStatesDurations):

    eventDict = {
        'time': [TriggerAngle(At(0), TRIGGER_SONY_DOWN),]
    }

    currentTime = 0

    for agent, state, duration in agentsStatesDurations:
        eventDict['time'].append(Flash(At(currentTime), agent, state, duration))
        currentTime += 1
    
    eventDict['time'].append(TriggerAngle(At(0), TRIGGER_SONY_UP))