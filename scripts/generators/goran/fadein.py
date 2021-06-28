import math
import numpy as np
import decimal

def easeInSine(x):
    return 1 - math.cos((x * math.pi) / 2)


def easeInQuint(x):
    return x * x * x * x


length = 10
steptime = 0.02

topLightIntensity = 255
bottomLightIntensity = 32
startSpeed = 28
finalSpeed = 110

rows = [
    ['seconds', 0, '', 'instant', 'ta', 0, 'ba', 0],
    ['seconds', 0, '', 'special', 'ms', 0, 30],
    ['seconds', 0.5, '', 'special', 'tr']
]

seconds = 0
lightrow = ['seconds', 0, '', 'instant', 'ta', 0, 'ba', 0]
motorrow = ['seconds', 0, '', 'special', 'ms', 0, 10]

lastIntensity = -1
lastSpeed = -1

while seconds < length:
    light = lightrow.copy()
    motor = motorrow.copy()
    ease = easeInQuint(seconds/length)
    topIntensity = round(ease * topLightIntensity)
    bottomIntensity = round(ease * bottomLightIntensity)
    if topIntensity == 0:
        topIntensity = 1
    if topIntensity > 255:
        topIntensity = 255
    if bottomIntensity == 0:
        bottomIntensity = 1
    if bottomIntensity > 32:
        bottomIntensity = 32
    speed = startSpeed + round(easeInSine(seconds/length) * (finalSpeed - startSpeed))
    print(topIntensity,bottomIntensity,speed)
    light[1] = seconds
    light[5] = topIntensity
    light[7] = bottomIntensity

    motor[1] = seconds
    motor[5] = speed

    if lastIntensity != topIntensity:
        rows.append(light)
    if lastSpeed != speed:
        rows.append(motor)
    
    lastIntensity = topIntensity
    lastSpeed = speed

    seconds = seconds + steptime

rows.append(['seconds', seconds + 5, '', 'instant', 'ta', 0, 'ba', 0])
rows.append(['seconds', seconds + 5, '', 'special', 'ms', 0, 30])
    

with open("fade_in" + '_110.csv', "w") as f:
    for row in rows:
        f.write(','.join([str(x) for x in row]))
        f.write('\n')

