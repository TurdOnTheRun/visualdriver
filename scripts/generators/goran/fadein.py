import math
import numpy as np
import decimal

def easeInSine(x):
    return 1 - math.cos((x * math.pi) / 2)

length = 10
steptime = 0.01

finalLightIntensity = 255
startSpeed = 28
finalSpeed = 80

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
    ease = easeInSine(seconds/10)
    intensity = round(ease * finalLightIntensity)
    speed = startSpeed + round(ease * (finalSpeed - startSpeed))
    print(intensity,speed)
    light[1] = seconds
    light[5] = intensity
    light[7] = intensity

    motor[1] = seconds
    motor[5] = speed

    if lastIntensity != intensity:
        rows.append(light)
    if lastSpeed != speed:
        rows.append(motor)
    
    lastIntensity = intensity
    lastSpeed = speed

    seconds = seconds + steptime

rows.append(['seconds', seconds + 5, '', 'instant', 'ta', 0, 'ba', 0])
rows.append(['seconds', seconds + 5, '', 'special', 'ms', 0, 30])
    

with open("fade_in" + '_1.csv', "w") as f:
    for row in rows:
        f.write(','.join([str(x) for x in row]))
        f.write('\n')

