import random
import numpy as np
import decimal


finalPosition = 2.5

startSpeed = 80
finalSpeed = 110
stepSize = 50

rows = [
    ['index'],
    ['seconds', 0.5, '', 'instant', 't0', 0, 'ba', 0],
    ['seconds', 0.5, '', 'special', 'ms', finalSpeed, stepSize],
]

position = 0
lightrow = ['pos', 0, '', 'lightning']

lights = ['t0', 't1', 't4', 't5', 'ba']
lastlight = ''

toplightintensity = 255
bottomlightinsity = 100
steptime = (40,60)
# motorrow = ['seconds', 0, '', 'special', 'ms', 0, 10]

partitions = 48
position = round((1/partitions),4)

while position < finalPosition:

    row = lightrow.copy()
    row[1] = position
    lightoptions = lights.copy()
    try:
        lightoptions.remove(lastlight)
    except ValueError:
        print('lastlight was not found in lightoptions: ', lastlight)
    light = random.choice(lightoptions)
    row.append(light)
    if light[0] == 't':
        lightintensity = toplightintensity
    else:
        lightintensity = bottomlightinsity
    row.append(lightintensity)
    lightingtime = random.randint(steptime[0],steptime[1])
    row.append(lightingtime)
    rows.append(row)
    lastlight = light
    position = position + round((1/partitions),4)


rows.append(['pos', finalPosition, '', 'instant', 'ta', 0, 'ba', 0])
rows.append(['pos', finalPosition, '', 'special', 'ms', 0, 30])
    

with open("positionlightning" + '_top_bottom.csv', "w") as f:
    for row in rows:
        f.write(','.join([str(x) for x in row]))
        f.write('\n')

