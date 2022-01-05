

TOP_CONTROLLER = 0
BOTTOM_CONTROLLER = 1
MAIN_CONTROLLER = 2

LIGHT_AGENT_TYPE = 0


class Agent:

    def __init__(self, controller, id, all, type=None):
        self.controller = controller
        self.id = id
        self.all = all
        self.type = type


TopAll = Agent(TOP_CONTROLLER, None, True, LIGHT_AGENT_TYPE)
Top1 = Agent(TOP_CONTROLLER, 0, False, LIGHT_AGENT_TYPE)
Top2 = Agent(TOP_CONTROLLER, 1, False, LIGHT_AGENT_TYPE)
Top3 = Agent(TOP_CONTROLLER, 2, False, LIGHT_AGENT_TYPE)
Top4 = Agent(TOP_CONTROLLER, 3, False, LIGHT_AGENT_TYPE)
Top5 = Agent(TOP_CONTROLLER, 4, False, LIGHT_AGENT_TYPE)
Top6 = Agent(TOP_CONTROLLER, 5, False, LIGHT_AGENT_TYPE)
Top7 = Agent(TOP_CONTROLLER, 6, False, LIGHT_AGENT_TYPE)
Top8 = Agent(TOP_CONTROLLER, 7, False, LIGHT_AGENT_TYPE)
Top9 = Agent(TOP_CONTROLLER, 8, False, LIGHT_AGENT_TYPE)
Top10 = Agent(TOP_CONTROLLER, 9, False, LIGHT_AGENT_TYPE)

BottomAll = Agent(BOTTOM_CONTROLLER, None, True, LIGHT_AGENT_TYPE)
Bottom1 = Agent(BOTTOM_CONTROLLER, 0, False, LIGHT_AGENT_TYPE)
Bottom2 = Agent(BOTTOM_CONTROLLER, 1, False, LIGHT_AGENT_TYPE)
Bottom3 = Agent(BOTTOM_CONTROLLER, 2, False, LIGHT_AGENT_TYPE)

Main = Agent(MAIN_CONTROLLER, None, None)