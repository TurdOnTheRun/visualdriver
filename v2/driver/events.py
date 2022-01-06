from agents import LIGHT_AGENT_TYPE, Main, Bottom

ARDUINO_COMMUNICATION_START_BYTE = 251
ARDUINO_COMMUNICATION_STOP_BYTE = 252

TIME_RESET_TYPE = 0
TIME_ADD_EVENT_TYPE = 1


class Event:

    def __init__(self, condition, agent=None):
        self.condition = condition
        self.agent = agent
    

    def abort(self, message, error=None):
        print(message)
        if error:
            raise error
        else:
            raise Exception


class ArduinoEvent(Event):

    def __init__(self, condition, agent=None):
        super().__init__(condition, agent)
    

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

    def __init__(self, condition, agent, state):
        self.check_state(state)
        self.state = state
        self.check_is_light_agent(agent)
        super().__init__(condition, agent)
        self.command = self.make_command()
    
    def make_command(self):
        if self.agent.id == -1:
            return self.clean_bytes([200, self.state])
        else:
            return self.clean_bytes([self.agent.id, self.state])
    

class Flash(ArduinoEvent):

    def __init__(self, condition, agent, state, millisecondsOn):
        self.check_state(state)
        self.state = state
        self.millisecondsOn = millisecondsOn
        self.check_is_light_agent(agent)
        super().__init__(condition, agent)
        self.command = self.make_command()
    
    def make_command(self):
        if self.agent.id == -1:
            return self.clean_bytes([204, self.state, self.millisecondsOn])
        else:
            return self.clean_bytes([40 + self.agent.id, self.state, self.millisecondsOn])


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
            return self.clean_bytes([210, self.state1, self.state2, self.ax, self.ay, self.bx, self.by, self.millisecondsStep])
        else:
            return self.clean_bytes([100 + self.agent.id, self.state1, self.state2, self.ax, self.ay, self.bx, self.by, self.millisecondsStep])


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
            return self.clean_bytes([211, self.state1, self.state2, self.ax, self.ay, self.bx, self.by, self.millisecondsStep, self.millisecondsOn])
        else:
            return self.clean_bytes([110 + self.agent.id, self.state1, self.state2, self.ax, self.ay, self.bx, self.by, self.millisecondsStep, self.millisecondsOn])
    

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


class TimeAddEvents(Event):

    def __init__(self, condition, events):
        self.type = TIME_ADD_EVENT_TYPE
        if not events or type(events) != list:
            self.abort('Events in TimeAddEvents is empty or not a list')
        self.events = events
        super().__init__(condition, Main)