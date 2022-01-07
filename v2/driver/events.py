from agents import LIGHT_AGENT_TYPE, Main, Bottom
from conditions import At
import random


ARDUINO_COMMUNICATION_START_BYTE = 251
ARDUINO_COMMUNICATION_STOP_BYTE = 252

TIME_RESET_TYPE = 0
ADD_EVENTS_TYPE = 1
POSITION_RESET_TYPE = 2
TIME_EVENTS_BLOCK_TYPE = 3
TIME_EVENTS_UNBLOCK_TYPE = 4
TIME_EVENTS_CLEAR_TYPE = 5


class Event:

    def __init__(self, condition, agent=None, hasVariable=False):
        self.condition = condition
        self.agent = agent
        self.hasVariable = hasVariable
    

    def abort(self, message, error=None):
        print(message)
        if error:
            raise error
        else:
            raise Exception


class Variable:

    def get(self, **kwargs):
        pass


class ArduinoEvent(Event):

    def __init__(self, condition, agent=None, hasVariable=False):
        super().__init__(condition, agent, hasVariable)
    

    def check_state(self, state):
        if state < 0 or state > 100:
            self.abort('State not in range 0-100')
    
    # Checks if the agent is a light
    def check_is_light_agent(self, agent):
        if not agent or agent.type != LIGHT_AGENT_TYPE:
            self.abort('Agent is not a light agent')
    
    # Checks that all Arduino inputs are in the range of 0 to 255 
    # Replaces the "Start" & "Stop" bytes used for Arduino communication (251 & 252)
    def clean_bytes(self, command):
        cleanedcommand = []
        errorMessage = 'Invalid Command: '

        for byte in command:
            if type(byte) == int and byte >= 0 and byte <= 255:
                if byte == ARDUINO_COMMUNICATION_START_BYTE:
                    byte = 250
                if byte == ARDUINO_COMMUNICATION_STOP_BYTE:
                    byte = 253
                cleanedcommand.append(byte)
            else:
                self.abort(errorMessage + str(byte))

        return cleanedcommand


class Instant(ArduinoEvent):

    def __init__(self, condition, agent, state, hasVariable=False):
        self.state = state
        super().__init__(condition, agent, hasVariable)
        if not hasVariable:
            self.check_init()
        self.command = self.make_command()
    
    def check_init(self):
        self.check_state(self.state)
        self.check_is_light_agent(self.agent)
    
    def make_command(self):
        if self.agent.id == -1:
            command = [200, self.state]
        else:
            command = [self.agent.id, self.state]
        if not self.hasVariable:
            return self.clean_bytes(command)
        else:
            return command
    

class Flash(ArduinoEvent):

    def __init__(self, condition, agent, state, millisecondsOn, hasVariable=False):
        self.state = state
        self.millisecondsOn = millisecondsOn
        super().__init__(condition, agent, hasVariable)
        if not hasVariable:
            self.check_init()
        self.command = self.make_command()

    def check_init(self):
        self.check_state(self.state)
        self.check_is_light_agent(self.agent)
    
    def make_command(self):
        if self.agent.id == -1:
            command = [204, self.state, self.millisecondsOn]
        else:
            command = [40 + self.agent.id, self.state, self.millisecondsOn]
        if not self.hasVariable:
            return self.clean_bytes(command)
        else:
            return command


class InstantBezier(ArduinoEvent):
    def __init__(self, condition, agent, state1, state2, millisecondsStep, ax, ay, bx, by):
        self.check_state(state1)
        self.check_state(state2)
        # The bezier point coordinates must also be within 0 - 100
        self.check_state(ax)
        self.check_state(ay)
        self.check_state(bx)
        self.check_state(by)
        self.state1 = state1
        self.state2 = state2
        self.ax = ax
        self.ay = ay
        self.bx = bx
        self.by = by
        # millisecondsStep (ms) of 100 bezier steps (Dimmtime = 100 * millisecondsStep)
        self.millisecondsStep = millisecondsStep
        self.check_is_light_agent(agent)
        super().__init__(condition, agent)
        self.command = self.make_command()
    
    def make_command(self):
        if self.agent.id == -1:
            return self.clean_bytes([210, self.state1, self.state2, self.millisecondsStep, self.ax, self.ay, self.bx, self.by])
        else:
            return self.clean_bytes([100 + self.agent.id, self.state1, self.state2, self.millisecondsStep, self.ax, self.ay, self.bx, self.by])


class FlashBezier(ArduinoEvent):
    def __init__(self, condition, agent, state1, state2, millisecondsStep, ax, ay, bx, by, millisecondsOn):
        self.check_state(state1)
        self.check_state(state2)
        # The bezier point coordinates must also be within 0 - 100
        self.check_state(ax)
        self.check_state(ay)
        self.check_state(bx)
        self.check_state(by)
        self.state1 = state1
        self.state2 = state2
        self.ax = ax
        self.ay = ay
        self.bx = bx
        self.by = by
        # millisecondsStep (ms) of 100 bezier steps (Dimmtime = 100 * millisecondsStep)
        self.millisecondsStep = millisecondsStep
        self.millisecondsOn = millisecondsOn
        self.check_is_light_agent(agent)
        super().__init__(condition, agent)
        self.command = self.make_command()

    def make_command(self):
        if self.agent.id == -1:
            return self.clean_bytes([211, self.state1, self.state2, self.millisecondsStep, self.ax, self.ay, self.bx, self.by, self.millisecondsOn])
        else:
            return self.clean_bytes([110 + self.agent.id, self.state1, self.state2, self.millisecondsStep, self.ax, self.ay, self.bx, self.by, self.millisecondsOn])
    

class MotorSpeed(ArduinoEvent):

    def __init__(self, condition, state, millisecondsStep):
        self.check_state(state)
        self.state = state
        self.millisecondsStep = millisecondsStep
        super().__init__(condition, Bottom)
        self.command = self.make_command()

    def make_command(self):
        return self.clean_bytes([220, self.state, self.millisecondsStep])


class MotorChangeDirection(ArduinoEvent):

    def __init__(self, condition):
        super().__init__(condition, Bottom)
        self.command = self.make_command()
    
    def make_command(self):
        return self.clean_bytes([221,])


class TimeReset(Event):

    def __init__(self, condition):
        self.type = TIME_RESET_TYPE
        super().__init__(condition, Main)


class TimeEventsBlock(Event):

    def __init__(self, condition):
        self.type = TIME_EVENTS_BLOCK_TYPE
        super().__init__(condition, Main)


class TimeEventsUnblock(Event):

    def __init__(self, condition):
        self.type = TIME_EVENTS_UNBLOCK_TYPE
        super().__init__(condition, Main)


class TimeEventsClear(Event):

    def __init__(self, condition):
        self.type = TIME_EVENTS_CLEAR_TYPE
        super().__init__(condition, Main)


class EventsAdd(Event):

    def __init__(self, condition, events):
        self.type = ADD_EVENTS_TYPE
        if not events or type(events) != dict:
            self.abort('Events in TimeAddEvents is empty or not a dict')
        self.events = events
        super().__init__(condition, Main)


class PositionReset(Event):

    def __init__(self, condition):
        self.type = POSITION_RESET_TYPE
        super().__init__(condition, Main)


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
            for a in agentsAndStates:
                positionEvents.append(FlashBezier(At(currentPosition), a[0], a[1], 0, millisecondsStep, ax, ay, bx, by, millisecondsOn))
            currentPosition += 1/swooshsPerRound
    
    return {
        'position': positionEvents
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


def thatEvolvingFuzz(rounds, approximateDuration, millisecondsOnRange, millisecondOverlapRange, agentsAndStates, flipAgentAndState=None, currentTime=0, currentPosition=0):
    """
    Parameters
    ----------
    rounds : float
        Through what position length the evolvement should take place
    """

    class Var(Variable):

        def __init__(self, state, currentPosition, rounds):
            self.startPosition = currentPosition
            self.rounds = rounds
            self.peak = rounds/2
            self.state = state
            super().__init__()

        def get_pulse(self, **kwargs):
            if kwargs['position'] - self.startPosition <= self.peak:
                return int(self.state * (kwargs['position'] - self.startPosition) / self.peak)
            else:
                return int(self.state * (1 - (kwargs['position'] - self.startPosition - self.peak) / self.peak))


        def get_increase(self, **kwargs):
            return int(self.state * (1 - (kwargs['position'] - self.startPosition) / self.rounds))


    
    timeEvents = []
    positionEvents = []

    if millisecondsOnRange[0] < millisecondOverlapRange[1]:
        print('Overlap can exceed on time.')

    if currentTime == 0:
        timeEvents.append(TimeReset(At(0)))

    if currentPosition == 0:
        positionEvents.append(PositionReset(At(0)))
    
    targetPosition = currentPosition + rounds
    positionEvents.append(TimeEventsClear(At(targetPosition)))

    approximateDuration += currentTime
    lastIndex = random.randint(0, len(agentsAndStates)-1)
    agentIndexes = list(range(len(agentsAndStates)))
    flipping = False
    needsSort = False

    while currentTime < approximateDuration:
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
        var = Var(randomAgent[1], currentPosition, rounds)
        var.get = var.get_pulse
        if flashTime > 255:
            timeEvents.append(Instant(At(currentTime), randomAgent[0], var, True))
            timeEvents.append(Instant(At(currentTime + flashTime/1000), randomAgent[0], 0, True))
            needsSort = True
        else:
            timeEvents.append(Flash(At(currentTime), randomAgent[0], var, flashTime, True))
        overlap = random.randint(millisecondOverlapRange[0], millisecondOverlapRange[1])
        currentTime = currentTime + (flashTime - overlap)/1000
    
    if needsSort:
        timeEvents.sort(key=lambda x:x.condition.value)
    
    return {
        'time': timeEvents,
        'position': positionEvents
    }
