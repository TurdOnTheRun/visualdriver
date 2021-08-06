import math
import numpy as np
import decimal

def easeInSine(x):
    return 1 - math.cos((x * math.pi) / 2)


def easeInQuint(x):
    return x * x * x * x

def easeOutQuint(x):
    return (x - 1) * (x - 1) * (x - 1) * (x - 1) * (x - 1) * -1

def easeInCube(x):
    return x * x * x

def easeOutCube(x):
    return (x - 1) * (x - 1) * (x - 1) * -1


finalPosition = 5.5
step = 0.002

startSpeed = 80
finalSpeed = 110

# lastSpeed = -1

dimmUp = False
dimmDown = False
dimmPosition = 0
intensity = 0
maxIntensity = 255
lastIntensity = -1


topUp = False
topDown = False
topDimmPosition = 0
topIntensity = 0
topMaxIntensity = 255
topLastIntensity = -1


rows = [
    ['index'],
    ['seconds', 0.5, '', 'instant', 't1', 255, 'ba', intensity],
    ['seconds', 0.5, '', 'special', 'ms', startSpeed, 30],
]

position = 0.75
lightrow = ['pos', 0, '', 'instant']
frontpart = ['ba', 0]
toppart = ['ta', 0]
# motorrow = ['seconds', 0, '', 'special', 'ms', 0, 10]


while position < finalPosition:

    print(round(position%1, 3))

    if not dimmUp and round(position%1, 3) == 0.75:
        dimmDown = False
        dimmUp = True
        dimmPosition = position

        topDown = False
        topUp = False

    if not dimmDown and (round(position%1, 3) == 0 or round(position%1, 3) == 1):
        dimmDown = True
        dimmUp = False
        position = round(position)
        dimmPosition = position
    
    if round(position%1, 3) == 0.25:
        dimmDown = False
        dimmUp = False

        topDown = False
        topUp = True
        topDimmPosition = position

    if not topDown and (round(position%1, 3) == 0.5):
        topDown = True
        topUp = False
        topDimmPosition = position


    if dimmUp or dimmDown or topUp or topDown:

        light = lightrow.copy()
        light[1] = position

        if dimmUp or dimmDown:
    
            if dimmUp:
                print('up')
                print((position-dimmPosition)/(1/4))
                ease = easeInCube((position-dimmPosition)/(1/4))
                intensity = round(ease * maxIntensity)

            if dimmDown:
                print('down')
                print((position-dimmPosition)/(1/4))
                ease = easeOutCube((position-dimmPosition)/((1/4)))
                intensity = round(ease * maxIntensity)

            if intensity > 255:
                intensity = 255

            if lastIntensity != intensity:
                part = frontpart.copy()
                part[1] = intensity
                light += part

        if topUp or topDown:
        
            if topUp:
                print('topup')
                print((position-topDimmPosition)/(1/4))
                ease = easeInCube((position-topDimmPosition)/(1/4))
                topIntensity = round(ease * topMaxIntensity)

            if topDown:
                print('topdown')
                print((position-topDimmPosition)/(1/4))
                ease = easeOutCube((position-topDimmPosition)/((1/4)))
                topIntensity = round(ease * topMaxIntensity)

            if topIntensity > 255:
                topIntensity = 255

            if topLastIntensity != topIntensity:
                part = toppart.copy()
                part[1] = topIntensity
                light += part
        
        print(intensity)
        print()

        if len(light) > 4:
            rows.append(light)
    
    lastIntensity = intensity
    topLastIntensity = topIntensity
    position = position + step


rows.append(['pos', finalPosition, '', 'instant', 'ta', 0, 'ba', 0])
rows.append(['seconds', finalPosition, '', 'special', 'ms', 0, 30])
    

with open("halbmond" + '_cube_top.csv', "w") as f:
    for row in rows:
        f.write(','.join([str(x) for x in row]))
        f.write('\n')

