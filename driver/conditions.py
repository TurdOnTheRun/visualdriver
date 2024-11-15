

class Condition:

    def __init__(self, value):
        self.value = value
    
    def set_value(self, value):
        self.value = value


class At(Condition):

    def __init__(self, value):
        super().__init__(value)
    
    def met(self, value):
        return self.value <= value
    
    def __str__(self):
        return 'At ({})'.format(self.value)


class GE(Condition):

    def __init__(self, value):
        super().__init__(value)
    
    def met(self, value):
        return self.value <= value
    
    def __str__(self):
        return 'At ({})'.format(self.value)


class LE(Condition):

    def __init__(self, value):
        super().__init__(value)
    
    def met(self, value):
        return self.value >= value
    
    def __str__(self):
        return 'At ({})'.format(self.value)
