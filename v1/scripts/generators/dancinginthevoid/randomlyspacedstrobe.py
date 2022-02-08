import random

# Seconds
length = 29

rows = [
    ['seconds', 0, '', 'ta', 0, 'ba', 0],
    ['seconds', 0, '', 'special', 'ms', 100, 30],
    ['pos', 0.5, '', 'special', 'tr']
]

seconds = 0

baserow = ['seconds', 0, '', 'lightning']

lights = ['t0', 't1', 't4', 't5']
lightintensity = 255
steptime = (40,60)

lastlight = ''

while seconds < length:
    row = baserow.copy()
    row[1] = seconds
    lightoptions = lights.copy()
    try:
        lightoptions.remove(lastlight)
    except ValueError:
        print('lastlight was not found in lightoptions')
    light = random.choice(lightoptions)
    row.append(light)
    row.append(lightintensity)
    lightingtime = random.randint(steptime[0],steptime[1])
    row.append(lightingtime)
    rows.append(row)
    darktime = random.randint(steptime[0],steptime[1])
    seconds = seconds + (lightingtime + darktime)/1000
    lastlight = light

rows.append(['seconds', seconds, '', 'instant', 'ta', 0, 'ba', 0])
rows.append(['seconds', seconds, '', 'special', 'ms', 0, 30])
    

with open("randomlyspacedquickstrobe_" + str(length) + '_' + ''.join(lights) + '.csv', "w") as f:
    for row in rows:
        f.write(','.join([str(x) for x in row]))
        f.write('\n')