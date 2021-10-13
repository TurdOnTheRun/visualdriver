# Longer gaps
# less frequent blinking
# new lighting




import random


ms = 0
morphduration = 2000
nomorphduration = 800
iterations = 4
startpos = 0.5

lightninglenghtrange = (32,40)
overlaprange = (10,16)
averagetime = 23

baserow = ['seconds', 0, '', 'lightning']

lights = ['t0', 't1', 't4', 't5']
toplightintensity = 255
bottomlightintensity = 90

lastlight = ''

front = False

rows = [
    ['index'],
    ['seconds', 0, '', 'instant', 'ta', 0, 'ba', 0],
    ['seconds', 0, '', 'special', 'ms', 100, 30],
    ['pos', startpos, '', 'special', 'tr']
]


x = 1/((morphduration/3)/averagetime)

for _ in range(iterations):

    state = 'up'
    iterms = 0
    y = x
    
    while True:

        if state == 'up' and y >= 1:
            state = 'steady'
        if state == 'down' and y >= 1:
            break
        if state == 'steady' and iterms >= morphduration*(2/3):
            state = 'down'
            y = x

        row = baserow.copy()
        row[1] = ms/1000
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

        if state == 'up':
            li = int(lightintensity*y)
        elif state == 'down':
            li = int(lightintensity*(1-y))
        else:
            li = lightintensity
        row.append(li)

        duration = random.randint(lightninglenghtrange[0],lightninglenghtrange[1])
        row.append(duration)
        rows.append(row)
        overlap = random.randint(overlaprange[0],overlaprange[1])
        iterms += (duration-overlap)
        ms += overlap
        if state != 'steady':
            y += x

        front = not front

        print(state)
        print(y)
        print(iterms)
        print()

    ms += nomorphduration


rows.append(['seconds', 0.25 + ms/1000, '', 'instant', 'ta', 0, 'ba', 0])
rows.append(['seconds', 0.25 + ms/1000, '', 'special', 'ms', 0, 30])
    

with open("morpher_" + ''.join(lights) + '_1.csv', "w") as f:
    for row in rows:
        f.write(','.join([str(x) for x in row]))
        f.write('\n')