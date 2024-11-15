import random

# Seconds
length = 12

rows = [
    ['seconds', 0, '', 'ta', 0, 'ba', 0],
    ['seconds', 0, '', 'special', 'ms', 100, 30],
    ['pos', 0.5, '', 'special', 'tr']
]

seconds = 0

baserow = ['seconds', 0, '', 'lightning']

lights = ['t0', 't1', 't4', 't5']
lightintensity = 255
lightninglenghtrange = (41,50)
overlaprange = (20,30)

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
    row.append(random.randint(lightninglenghtrange[0],lightninglenghtrange[1]))
    rows.append(row)
    overlap = random.randint(overlaprange[0],overlaprange[1])
    seconds = seconds + overlap/1000
    lastlight = light

rows.append(['seconds', seconds, '', 'instant', 'ta', 0, 'ba', 0])
rows.append(['seconds', seconds, '', 'special', 'ms', 0, 30])
    

with open("morphrandom_" + str(length) + '_' + ''.join(lights) + '_1.csv', "w") as f:
    for row in rows:
        f.write(','.join([str(x) for x in row]))
        f.write('\n')