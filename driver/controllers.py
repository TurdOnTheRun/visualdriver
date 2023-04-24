TOP_CONTROLLER = 0
BOTTOM_CONTROLLER = 1
MAIN_CONTROLLER = 2


class Controller:

    def __init__(self, type, light=False):
        self.type = type
        #does the controller control light
        self.light = light 

    def __str__(self):
        return 'Controller({})'.format(self.controller)

TopController = Controller(TOP_CONTROLLER, True)
BottomController = Controller(BOTTOM_CONTROLLER, True)
MainController = Controller(MAIN_CONTROLLER)