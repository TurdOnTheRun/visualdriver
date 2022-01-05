from agents import LIGHT_AGENT_TYPE, Main

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
        if self.agent.all:
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
        if self.agent.all:
            return self.clean_bytes([204, self.state, self.millisecondsOn])
        else:
            return self.clean_bytes([40 + self.agent.id, self.state, self.millisecondsOn])
    

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