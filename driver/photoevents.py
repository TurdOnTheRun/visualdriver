from events import *
from settings import TRIGGER_SONY_DOWN, TRIGGER_SONY_UP


def flashCollection(agentsStatesDurations, iterations=1):

    eventDict = {
        'time': [TriggerAngle(At(0), TRIGGER_SONY_DOWN),]
    }

    currentTime = 0.5
    iterationDuration = None

    for i in range(iterations):
        for agent, state, duration in agentsStatesDurations:
            eventDict['time'].append(Flash(At(currentTime), agent, state, duration))
            currentTime += 1
        
        eventDict['time'].append(TriggerAngle(At(currentTime), TRIGGER_SONY_UP))

        if not iterationDuration:
            iterationDuration = currentTime
        
        currentTime += iterationDuration


    return eventDict