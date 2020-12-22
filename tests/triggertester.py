from servocontroller import Trigger

trigger = Trigger(0, 30)

while True:
    value = input("Please enter an angle:\n")
    try:
        angle = int(value)
        if angle == -1:
            trigger.trigger()
        else:
            trigger.setAngle(angle)
    except ValueError:
        print('Invalid Command')