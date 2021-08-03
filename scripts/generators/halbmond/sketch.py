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
    return x * x * x * x

def easeOutCube(x):
    return (x - 1) * (x - 1) * (x - 1) * (x - 1) * (x - 1) * -1


finalPosition = 5.5
step = 0.002

intensity = 0
maxIntensity = 255
startSpeed = 80
finalSpeed = 110

rows = [
    ['index'],
    ['seconds', 0.5, '', 'instant', 't1', 255, 'ba', intensity],
    ['seconds', 0.5, '', 'special', 'ms', startSpeed, 30],
]

position = 0.5
lightrow = ['pos', 0, '', 'instant', 'ba', 0]
# motorrow = ['seconds', 0, '', 'special', 'ms', 0, 10]

lastIntensity = -1
# lastSpeed = -1

dimmUp = False
dimmDown = False
dimmStep = 0
dimmPosition = 0


while position < finalPosition:

    print(round(position%1, 4))

    if not dimmUp and round(position%1, 4) == 0.75:
        dimmDown = False
        dimmUp = True
        dimmPosition = position

    if not dimmDown and round(position%1, 4) == 0:
        dimmDown = True
        dimmUp = False
        dimmPosition = position
    
    if round(position%1, 4) == 0.25:
        dimmDown = False
        dimmUp = False

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
        
        light = lightrow.copy()
        if intensity > 255:
            intensity = 255
        light[1] = position
        light[5] = intensity
    
        print(intensity)
        print()

        if lastIntensity != intensity:
            rows.append(light)
    
    lastIntensity = intensity
    position = position + step


rows.append(['pos', finalPosition, '', 'instant', 'ta', 0, 'ba', 0])
rows.append(['seconds', finalPosition, '', 'special', 'ms', 0, 30])
    

with open("halbmond" + '_cube.csv', "w") as f:
    for row in rows:
        f.write(','.join([str(x) for x in row]))
        f.write('\n')

