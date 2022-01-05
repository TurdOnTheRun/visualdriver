

class Condition:

    def __init__(self, value):
        self.value = value
    
    def set_value(self, value):
        self.value = value
    
    def met_if_smaller(self, value):
        return self.value <= value


class Time(Condition):

    def __init__(self, value):
        super().__init__(value)
        self.met = self.met_if_smaller


class Position(Condition):

    def __init__(self, value):
        super().__init__(value)
        self.met = self.met_if_smaller


class Distance(Condition):

    def __init__(self, value):
        super().__init__(value)
        self.met = self.met_if_smaller