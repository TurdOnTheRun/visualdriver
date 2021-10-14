import random

# Seconds
length = 9

rows = [
    ['index'],
    ['seconds', 0, '', 'instant', 'ta', 0, 'ba', 0],
    ['seconds', 0, '', 'special', 'ms', 100, 30],
]

seconds = 0
pos = 0.5

baserow = ['seconds', 0, '', 'lightning']

lights = ['t0', 't1', 't4', 't5']
toplightintensity = 255
bottomlightintensity = 90
lightninglenghtrange = (16,20)
overlaprange = (5,10)

lastlight = ''

front = False

while pos <= 4:

    rows.append(['pos', pos, '', 'special', 'tr'])

    for ratio in [0.1,0.2,0.3,0.4,0.5,0.6,0.7,0.8,0.9,1,1,1,0.9,0.8,0.7,0.6,0.5,0.4,0.3,0.2,0.1]:

        row = baserow.copy()
        row[1] = seconds
        if front:
            light = 'ba'
        else:
            lightoptions = lights.copy()
            try:
                lightoptions.remove(lastlight)
            except ValueError:
                print('lastlight was not found in lightoptions')
            light = random.choice(lightoptions)
        row.append(light)
        if light[0] == 't':
            lightintensity = toplightintensity
            lastlight = light
        else:
            lightintensity = bottomlightintensity
        row.append(int(lightintensity*ratio))
        row.append(random.randint(lightninglenghtrange[0],lightninglenghtrange[1]))
        rows.append(row)
        overlap = random.randint(overlaprange[0],overlaprange[1])
        seconds = seconds + overlap/1000

        front = not front
    
    pos += 0.25

rows.append(['seconds', seconds, '', 'instant', 'ta', 0, 'ba', 0])
rows.append(['seconds', seconds, '', 'special', 'ms', 0, 30])
    

with open("morphrandom_" + str(length) + '_' + ''.join(lights) + '_1.csv', "w") as f:
    for row in rows:
        f.write(','.join([str(x) for x in row]))
        f.write('\n')