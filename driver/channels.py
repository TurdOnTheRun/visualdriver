

class Channel:

    def __init__(self, id, static=False):
        self.id = id
        if static or id <= 10:
            self.isStatic = True
        else:
            self.isStatic = False

    def __str__(self):
        return 'Channel({}, {})'.format(self.id, self.isStatic)

StaticChannel0 = Channel(0,True)
StaticChannel1 = Channel(1,True)
StaticChannel2 = Channel(2,True)
StaticChannel3 = Channel(3,True)
StaticChannel4 = Channel(4,True)
StaticChannel5 = Channel(5,True)
StaticChannel6 = Channel(6,True)
StaticChannel7 = Channel(7,True)
StaticChannel8 = Channel(8,True)
StaticChannel9 = Channel(9,True)
StaticChannel10 = Channel(10,True)

Channel1 = Channel(11)
Channel2 = Channel(12)
Channel3 = Channel(13)
Channel4 = Channel(14)
Channel5 = Channel(15)
Channel6 = Channel(16)
Channel7 = Channel(17)
Channel8 = Channel(18)
Channel9 = Channel(19)
Channel10 = Channel(20)
