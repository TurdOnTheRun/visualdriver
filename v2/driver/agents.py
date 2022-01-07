TOP_CONTROLLER = 0
BOTTOM_CONTROLLER = 1
MAIN_CONTROLLER = 2

LIGHT_AGENT_TYPE = 0


class Agent:

    def __init__(self, controller, id, type=None):
        self.controller = controller
        self.id = id
        self.type = type

    def __str__(self):
        return 'Agent({}, {}, {})'.format(self.controller, self.id, self.type)


TopAll = Agent(TOP_CONTROLLER, -1, LIGHT_AGENT_TYPE)
Top1 = Agent(TOP_CONTROLLER, 0, LIGHT_AGENT_TYPE)
Top2 = Agent(TOP_CONTROLLER, 1, LIGHT_AGENT_TYPE)
Top3 = Agent(TOP_CONTROLLER, 2, LIGHT_AGENT_TYPE)
Top4 = Agent(TOP_CONTROLLER, 3, LIGHT_AGENT_TYPE)
# Top5 = Agent(TOP_CONTROLLER, 4, LIGHT_AGENT_TYPE)
# Top6 = Agent(TOP_CONTROLLER, 5, LIGHT_AGENT_TYPE)
# Top7 = Agent(TOP_CONTROLLER, 6, LIGHT_AGENT_TYPE)
# Top8 = Agent(TOP_CONTROLLER, 7, LIGHT_AGENT_TYPE)
# Top9 = Agent(TOP_CONTROLLER, 8, LIGHT_AGENT_TYPE)
# Top10 = Agent(TOP_CONTROLLER, 9, LIGHT_AGENT_TYPE)

Bottom = Agent(BOTTOM_CONTROLLER, None)
BottomAll = Agent(BOTTOM_CONTROLLER, -1, LIGHT_AGENT_TYPE)
Bottom1 = Agent(BOTTOM_CONTROLLER, 0, LIGHT_AGENT_TYPE)
Bottom2 = Agent(BOTTOM_CONTROLLER, 1, LIGHT_AGENT_TYPE)
Bottom3 = Agent(BOTTOM_CONTROLLER, 2, LIGHT_AGENT_TYPE)

Main = Agent(MAIN_CONTROLLER, None, None)