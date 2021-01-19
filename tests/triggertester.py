from trigger import Trigger

trigger = Trigger(84, 90)

while True:
    value = input("Please enter an angle:\n")
    try:
        angle = int(value)
        if angle == -1:
            trigger.trigger(0.5)
        else:
            trigger.setAngle(angle)
    except ValueError:
        print('Invalid Command')