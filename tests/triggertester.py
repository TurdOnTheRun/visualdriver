from trigger import Trigger
from settings import SONY_TRIGGER

trigger = Trigger(SONY_TRIGGER[0],SONY_TRIGGER[1])

while True:
    value = input("Please enter an exposuretime:\n")
    try:
        angle = float(value)
        if angle >= 0 and angle <= 20:
#             trigger.setPulseWidth(angle)
#         else:
            trigger.trigger(angle)
    except ValueError:
        print('Invalid Command')