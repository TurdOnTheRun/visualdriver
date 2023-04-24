def schattentanzRandomBezier(motorspeed, rounds, swooshsPerRound, agentsAndStates, millisecondsStep, millisecondsOn, currentPosition=0, accelerationArc=0):

    randintrange = (0,100)

    positionEvents = []

    if currentPosition == 0:
        positionEvents.append(PositionReset(At(0)))
    
    positionEvents.append(MotorSpeed(At(0), motorspeed, 30))
    currentPosition += accelerationArc

    for i in range(rounds):
        for j in range(swooshsPerRound):
            ax = random.randint(randintrange[0], randintrange[1])
            ay = random.randint(randintrange[0], randintrange[1])
            bx = random.randint(randintrange[0], randintrange[1])
            by = random.randint(randintrange[0], randintrange[1])
            agentAndState = random.choice(agentsAndStates)
            positionEvents.append(FlashBezier(At(currentPosition), agentAndState[0], agentAndState[1], 0, millisecondsStep, ax, ay, bx, by, millisecondsOn))
            currentPosition += 1/swooshsPerRound
    
    return {
        'position': positionEvents
    }


def breathing(duration, agentsAndStates, millisecondsStep, millisecondsOn, motorspeed=None, currentPosition=0, accelerationArc=0):

    randintrange = (0,100)

    positionEvents = []
    timeEvents = []
    
    timeEvents.append(TimeEventsBlock(At(0)))
    if currentPosition == 0:
        positionEvents.append(PositionReset(At(0)))
    
    if motorspeed:
        positionEvents.append(MotorSpeed(At(0), motorspeed, 50))
    currentPosition += accelerationArc
    positionEvents.append(TimeReset(At(currentPosition)))
    positionEvents.append(TimeEventsUnblock(At(currentPosition)))

    currentTime = 0

    while currentTime < duration:
        ax = random.randint(randintrange[0], randintrange[1])
        ay = random.randint(randintrange[0], randintrange[1])
        bx = random.randint(randintrange[0], randintrange[1])
        by = random.randint(randintrange[0], randintrange[1])
        agentAndState = random.choice(agentsAndStates)
        timeEvents.append(InstantBezier(At(currentTime), agentAndState[0], 0, agentAndState[1],  millisecondsStep, ax, ay, bx, by))
        currentTime += (millisecondsOn + millisecondsStep*100)/1000
        ax = random.randint(randintrange[0], randintrange[1])
        ay = random.randint(randintrange[0], randintrange[1])
        bx = random.randint(randintrange[0], randintrange[1])
        by = random.randint(randintrange[0], randintrange[1])
        timeEvents.append(InstantBezier(At(currentTime), agentAndState[0], agentAndState[1], 0, millisecondsStep, ax, ay, bx, by))
        currentTime += (millisecondsStep*100)/1000
    
    return {
        'position': positionEvents,
        'time': timeEvents
    }

# Resets Time
def dancingInTheVoid(duration, millisecondsOnRange, agentsAndStates, motorspeed=None, currentPosition=0, accelerationArc=0):

    positionEvents = []
    timeEvents = []
    
    timeEvents.append(TimeEventsBlock(At(0)))
    if currentPosition == 0:
        positionEvents.append(PositionReset(At(0)))
    
    if motorspeed:
        positionEvents.append(MotorSpeed(At(0), motorspeed, 30))
    currentPosition += accelerationArc
    positionEvents.append(TimeReset(At(currentPosition)))
    positionEvents.append(TimeEventsUnblock(At(0)))

    currentTime = 0
    lastIndex = random.randint(0, len(agentsAndStates)-1)
    agentIndexes = list(range(len(agentsAndStates)))

    while currentTime < duration:
        indexes = agentIndexes.copy()
        indexes.remove(lastIndex)
        i = random.choice(indexes)
        randomAgent = agentsAndStates[i]
        flashTime = random.randint(millisecondsOnRange[0], millisecondsOnRange[1])
        timeEvents.append(Flash(At(currentTime), randomAgent[0], randomAgent[1], flashTime))
        darkTime = random.randint(millisecondsOnRange[0], millisecondsOnRange[1])
        currentTime += (flashTime + darkTime)/1000
        lastIndex = i

    return {
        'position': positionEvents,
        'time': timeEvents
    }


def thatFuzz(duration, millisecondsOnRange, millisecondOverlapRange, agentsAndStates, flipAgentAndState=None, currentTime=0):

    timeEvents = []

    if millisecondsOnRange[0] < millisecondOverlapRange[1]:
        print('Overlap can exceed on time.')

    if currentTime == 0:
        timeEvents.append(TimeReset(At(0)))
    
    duration += currentTime
    lastIndex = random.randint(0, len(agentsAndStates)-1)
    agentIndexes = list(range(len(agentsAndStates)))
    flipping = False
    needsSort = False

    while currentTime < duration:
        if flipAgentAndState and flipping:
            randomAgent = flipAgentAndState
            flipping = False
        else:
            indexes = agentIndexes.copy()
            indexes.remove(lastIndex)
            i = random.choice(indexes)
            randomAgent = agentsAndStates[i]
            lastIndex = i
            if flipAgentAndState:
                flipping = True
        flashTime = random.randint(millisecondsOnRange[0], millisecondsOnRange[1])
        if flashTime > 255:
            timeEvents.append(Instant(At(currentTime), randomAgent[0], randomAgent[1]))
            timeEvents.append(Instant(At(currentTime + flashTime/1000), randomAgent[0], 0))
            needsSort = True
        else:
            timeEvents.append(Flash(At(currentTime), randomAgent[0], randomAgent[1], flashTime))
        overlap = random.randint(millisecondOverlapRange[0], millisecondOverlapRange[1])
        currentTime = currentTime + (flashTime - overlap)/1000
    
    if needsSort:
        timeEvents.sort(key=lambda x:x.condition.value)
    
    return {
        'time': timeEvents
    }


# Resets Time
def thatSpatialEvolvingFuzz(roundsAndMaximumAndBreaks, approximateDurationPerRound, millisecondsOnRange, millisecondOverlapRange, agentsAndStates, flipAgentAndState=None, currentPosition=0, evolveType='pulse'):
    """
    Parameters
    ----------
    rounds : float
        Through what position length the evolvement should take place
    """

    class Var(Variable):

        def __init__(self, state, currentPosition, rounds, maximumRounds):
            self.startPosition = currentPosition
            self.rounds = rounds
            self.maximumRounds = maximumRounds
            self.peakStart = rounds/2 - maximumRounds/2
            self.peakEnd = rounds/2 + maximumRounds/2
            self.state = state
            super().__init__()

        def get_pulse(self, **kwargs):
            if kwargs['position'] - self.startPosition <= self.peakStart:
                return int(self.state * (kwargs['position'] - self.startPosition) / self.peakStart)
            elif kwargs['position'] - self.startPosition >= self.peakEnd:
                return int(self.state * (1 - (kwargs['position'] - self.startPosition - self.peakEnd) / (self.rounds - self.peakEnd)))
            else:
                return self.state

        def get_decrease(self, **kwargs):
            if kwargs['position'] - self.startPosition >= self.maximumRounds:
                return int(self.state * (1 - (kwargs['position'] - self.startPosition - self.maximumRounds) / (self.rounds - self.maximumRounds)))
            else:
                return self.state

        def get_increase(self, **kwargs):
            if kwargs['position'] - self.startPosition <= self.rounds - self.maximumRounds:
                return int(self.state * (kwargs['position'] - self.startPosition) / (self.rounds - self.maximumRounds))
            else:
                return self.state


    
    timeEvents = []
    positionEvents = []

    if millisecondsOnRange[0] < millisecondOverlapRange[1]:
        print('Overlap can exceed on time.')
        return None

    if currentPosition == 0:
        positionEvents.append(PositionReset(At(0)))
    
    for rmb in roundsAndMaximumAndBreaks:

        rounds = rmb[0]
        # how much of the round should it be at the maximum setting?
        maximumRounds = rmb[1]
        breakRounds = rmb[2]

        if rounds < maximumRounds:
            print('MaximumRounds cannot be greater than rounds.')
            return None
    
        targetPosition = currentPosition + rounds

        iterTimeEvents = []
        iterTimeEvents.append(TimeReset(At(0)))
        currentTime = 0

        lastIndex = random.randint(0, len(agentsAndStates)-1)
        agentIndexes = list(range(len(agentsAndStates)))
        flipping = False
        needsSort = False

        while currentTime < approximateDurationPerRound:
            if flipAgentAndState and flipping:
                randomAgent = flipAgentAndState
                flipping = False
            else:
                indexes = agentIndexes.copy()
                indexes.remove(lastIndex)
                i = random.choice(indexes)
                randomAgent = agentsAndStates[i]
                lastIndex = i
                if flipAgentAndState:
                    flipping = True
            flashTime = random.randint(millisecondsOnRange[0], millisecondsOnRange[1])
            var = Var(randomAgent[1], currentPosition, rounds, maximumRounds)
            if evolveType == 'pulse':
                var.get = var.get_pulse
            elif evolveType == 'decrease':
                var.get = var.get_decrease
            else:
                var.get = var.get_increase
            if flashTime > 255:
                iterTimeEvents.append(Instant(At(currentTime), randomAgent[0], var, True))
                iterTimeEvents.append(Instant(At(currentTime + flashTime/1000), randomAgent[0], 0, True))
                needsSort = True
            else:
                iterTimeEvents.append(Flash(At(currentTime), randomAgent[0], var, flashTime, True))
            overlap = random.randint(millisecondOverlapRange[0], millisecondOverlapRange[1])
            currentTime = currentTime + (flashTime - overlap)/1000
        
        if needsSort:
            iterTimeEvents.sort(key=lambda x:x.condition.value)
        
        marker = Marker(At(approximateDurationPerRound))
        iterTimeEvents.append(marker)
        positionEvents.append(TimeEventsClearToMarker(At(targetPosition), marker))

        if breakRounds != 0:
            iterTimeEvents.append(TimeEventsBlock(At(0)))
            positionEvents.append(TimeEventsUnblock(At(targetPosition + breakRounds)))
        timeEvents += iterTimeEvents
        currentPosition = targetPosition + breakRounds
    
    return {
        'time': timeEvents,
        'position': positionEvents
    }


def thatTimeEvolvingFuzz(duration, millisecondsOnRange, millisecondOverlapRange, agentsAndStates, flipAgentAndState=None, iterations=1, currentTime=0, currentPosition=0):
    pass


def schattenFuzzNotTested(motorspeed, rounds, swooshsPerRound, swooshSplit, lightningAgentsAndStates, fuzzAgentsAndStates, approximateDurationPerDecreasePart, fuzzMillisecondsOnRangeFuzz, fuzzMillisecondOverlapRange, currentPosition=0, accelerationArc=0):

    """
    Keyword arguments:
    swooshSplit -- (float, float, float): split between lightPart, decreasePart, and offPart. The three must add up to 1.
    """

    eventDict = {
        'position': [],
        'time': [TimeEventsBlock(At(0)),]
    }
    positionEvents = []

    if currentPosition == 0:
        positionEvents.append(PositionReset(At(0)))
    
    positionEvents.append(MotorSpeed(At(0), motorspeed, 30))
    currentPosition += accelerationArc

    lightPart = swooshSplit[0]
    decreasePart = swooshSplit[1]
    offPart = swooshSplit[2]

    if (lightPart + decreasePart + offPart) != 1:
        print('The three swooshSplit Elements must add up to 1.')
        return None

    swooshLength = 1/swooshsPerRound
    lightOn = swooshLength*lightPart
    decreaseOn = swooshLength*decreasePart
    offOn = swooshLength*offPart

    for i in range(rounds):
        for j in range(swooshsPerRound):
            for agentAndState in lightningAgentsAndStates:
                eventDict['position'].append(Instant(At(currentPosition), agentAndState[0], agentAndState[1]))
            currentPosition += lightOn
            for agentAndState in lightningAgentsAndStates:
                eventDict['position'].append(Instant(At(currentPosition), agentAndState[0], 0))
            eventDict['position'].append(TimeEventsUnblock(At(currentPosition)),)
            evolveFuzz = thatSpatialEvolvingFuzz([(decreaseOn, 0, 0),], approximateDurationPerDecreasePart, fuzzMillisecondsOnRangeFuzz, fuzzMillisecondOverlapRange, fuzzAgentsAndStates, evolveType='decrease', currentPosition=currentPosition)
            currentPosition += decreaseOn
            eventDict['position'] += evolveFuzz['position'] + [TimeEventsBlock(At(currentPosition)),]
            eventDict['time'] += evolveFuzz['time']
            currentPosition += offOn

    return eventDict            


def backAndForward(duration, backAgentsAndStates, forwardAgentsAndStates, millisecondsOn, millisecondsStep, currentTime=0):

    eventDict = {
        'position': [],
        'time': []
    }
   
    if currentTime == 0:
        eventDict['time'].append(TimeReset(At(0)))
    
    duration += currentTime
    forward = True
    randintrange = (0, 100)
    lastBack = random.choice(backAgentsAndStates)
    lastForward = None

    eventDict['time'].append(InstantBezier(At(currentTime), lastBack[0], 0, lastBack[1], millisecondsStep, 100, 100, 100, 100))
    currentTime += (millisecondsOn + millisecondsStep)/1000

    while currentTime < duration:

        ax = random.randint(randintrange[0], randintrange[1])
        ay = random.randint(randintrange[0], randintrange[1])
        bx = random.randint(randintrange[0], randintrange[1])
        by = random.randint(randintrange[0], randintrange[1])

        if forward:
            lastForward = random.choice(forwardAgentsAndStates)
            eventDict['time'].append(InstantBezier(At(currentTime), lastForward[0], 0, lastForward[1], millisecondsStep, ax, ay, bx, by))
            eventDict['time'].append(InstantBezier(At(currentTime), lastBack[0], lastBack[1], 0, millisecondsStep, ax, ay, bx, by))
        else:
            lastBack = random.choice(backAgentsAndStates)
            eventDict['time'].append(InstantBezier(At(currentTime), lastBack[0], 0, lastBack[1], millisecondsStep, ax, ay, bx, by))
            eventDict['time'].append(InstantBezier(At(currentTime), lastForward[0], lastForward[1], 0, millisecondsStep, ax, ay, bx, by))
        
        forward = not forward
        currentTime += (millisecondsOn + millisecondsStep)/1000

    return eventDict


def leftCenterRight(duration, leftAgentAndStateAndOn, centerAgentAndStateAndOn, rightAgentAndStateAndOn, millisecondsStep, currentTime=0):

    eventDict = {
        'position': [],
        'time': []
    }
   
    if currentTime == 0:
        eventDict['time'].append(TimeReset(At(0)))
    
    duration += currentTime
    randintrange = (0, 100)
    nextAgentAndState = 'center'
    lastAgentAndState = 'left'

    eventDict['time'].append(InstantBezier(At(currentTime), leftAgentAndStateAndOn[0], 0, leftAgentAndStateAndOn[1], millisecondsStep, 100, 100, 100, 100))
    currentTime += (leftAgentAndStateAndOn[2] + millisecondsStep*100)/1000

    while currentTime < duration:

        ax = random.randint(randintrange[0], randintrange[1])
        ay = random.randint(randintrange[0], randintrange[1])
        bx = random.randint(randintrange[0], randintrange[1])
        by = random.randint(randintrange[0], randintrange[1])

        if nextAgentAndState == 'center':
            eventDict['time'].append(InstantBezier(At(currentTime), centerAgentAndStateAndOn[0], 0, centerAgentAndStateAndOn[1], millisecondsStep, ax, ay, bx, by))
            if lastAgentAndState == 'left':
                eventDict['time'].append(InstantBezier(At(currentTime), leftAgentAndStateAndOn[0], leftAgentAndStateAndOn[1], 0, millisecondsStep, ax, ay, bx, by))
                nextAgentAndState = 'right'
            else:
                eventDict['time'].append(InstantBezier(At(currentTime), rightAgentAndStateAndOn[0], rightAgentAndStateAndOn[1], 0, millisecondsStep, ax, ay, bx, by))
                nextAgentAndState = 'left'
            currentTime += (centerAgentAndStateAndOn[2] + millisecondsStep*100)/1000
        elif nextAgentAndState == 'right':
            eventDict['time'].append(InstantBezier(At(currentTime), rightAgentAndStateAndOn[0], 0, rightAgentAndStateAndOn[1], millisecondsStep, ax, ay, bx, by))
            eventDict['time'].append(InstantBezier(At(currentTime), centerAgentAndStateAndOn[0], centerAgentAndStateAndOn[1], 0, millisecondsStep, ax, ay, bx, by))
            nextAgentAndState = 'center'
            lastAgentAndState = 'right'
            currentTime += (rightAgentAndStateAndOn[2] + millisecondsStep*100)/1000
        elif nextAgentAndState == 'left':
            eventDict['time'].append(InstantBezier(At(currentTime), leftAgentAndStateAndOn[0], 0, leftAgentAndStateAndOn[1], millisecondsStep, ax, ay, bx, by))
            eventDict['time'].append(InstantBezier(At(currentTime), centerAgentAndStateAndOn[0], centerAgentAndStateAndOn[1], 0, millisecondsStep, ax, ay, bx, by))
            nextAgentAndState = 'center'
            lastAgentAndState = 'left'
            currentTime += (leftAgentAndStateAndOn[2] + millisecondsStep*100)/1000


    eventDict['time'].append(Instant(At(currentTime), TopAll, 0))
    eventDict['time'].append(Instant(At(currentTime), BottomAll, 0))
    return eventDict


# Resets Time
def topBottomLightTest(duration, millisecondsOnOff, agentsAndStates, motorspeed=None, currentPosition=0, accelerationArc=0):

    positionEvents = []
    timeEvents = []
    
    timeEvents.append(TimeEventsBlock(At(0)))
    if currentPosition == 0:
        positionEvents.append(PositionReset(At(0)))
    
    if motorspeed:
        positionEvents.append(MotorSpeed(At(0), motorspeed, 30))
    currentPosition += accelerationArc
    positionEvents.append(TimeReset(At(currentPosition)))
    positionEvents.append(TimeEventsUnblock(At(currentPosition)))

    currentTime = 0
    index = 0

    while currentTime < duration:
        if index == len(agentsAndStates)-1:
            index = 0
        else:
            index += 1
        agent = agentsAndStates[index]
        timeEvents.append(Flash(At(currentTime), agent[0], agent[1], millisecondsOnOff))
        if index == 1:
            currentTime += (millisecondsOnOff)/1000
        else:
            currentTime += (millisecondsOnOff + millisecondsOnOff)/1000

    return {
        'position': positionEvents,
        'time': timeEvents
    }


def flower(motorspeed, rounds, swooshsPerRound, agentsAndStates, millisecondsStep, currentPosition=0, accelerationArc=0):

    eventDict = {
        'position': [],
        'time': []
    }

    randintrange = (80,100)

    if currentPosition == 0:
        eventDict['position'].append(PositionReset(At(0)))
    
    eventDict['position'].append(MotorSpeed(At(0), motorspeed, 30))
    currentPosition += accelerationArc
    
    lastAgentAndState = agentsAndStates[1]
    agentsIndex = 0

    for i in range(rounds):
        for j in range(swooshsPerRound):
            ax = random.randint(randintrange[0], randintrange[1])
            ay = random.randint(randintrange[0], randintrange[1])
            bx = random.randint(randintrange[0], randintrange[1])
            by = random.randint(randintrange[0], randintrange[1])
            agentAndState = agentsAndStates[agentsIndex]
            if not (i == 0 and j == 0):
                eventDict['position'].append(InstantBezier(At(currentPosition), lastAgentAndState[0], lastAgentAndState[1], 0, millisecondsStep, ax, ay, bx, by))
            if i == rounds-1 and j == swooshsPerRound-1:
                currentPosition += 1/swooshsPerRound
                continue
            eventDict['position'].append(InstantBezier(At(currentPosition), agentAndState[0], 0, agentAndState[1], millisecondsStep, ax, ay, bx, by))
            lastAgentAndState = agentAndState
            if agentsIndex == len(agentsAndStates)-1:
                agentsIndex = 0
            else:
                agentsIndex += 1
            currentPosition += 1/swooshsPerRound

    eventDict['position'].append(MotorSpeed(At(currentPosition), 0, 30))
    return eventDict


def kinectTest(seconds, agent, millisecondsStep):


    class Var(Variable):

        def __init__(self):
            self.lowHeight = 0.5
            self.highHeight = 0.1
            super().__init__()

        def get(self, **kwargs):
            height = (kwargs['pose'][LEFT_WRIST][1] + kwargs['pose'][RIGHT_WRIST][1])/2
            if height >= self.lowHeight:
                return 0
            elif height <= self.highHeight:
                return 100
            else:
                return int(125-250*height)

    eventDict = {
        'position': [],
        'time': []
    }

    currentTime = 0
    increments = 0.05

    var = Var()

    while currentTime < seconds:
        eventDict['time'].append(Linear(At(currentTime), agent, var, millisecondsStep, hasVariable=True))
        currentTime += increments
    
    return eventDict