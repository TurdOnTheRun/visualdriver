LIGHT_1 = 1
LIGHT_2 = 2
LIGHT_3 = 4
LIGHT_4 = 8


class Agent:

    def __init__(self, id, bitvalue):
        self.id = id
        self.bitvalue = bitvalue

    def __str__(self):
        return 'Agent({}, {})'.format(self.id, self.bitvalue)


Light1 = Agent(1, LIGHT_1)
Light2 = Agent(2, LIGHT_2)
Light3 = Agent(3, LIGHT_3)
Light4 = Agent(4, LIGHT_4)