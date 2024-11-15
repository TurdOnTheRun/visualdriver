import random


rows = [
    ['seconds', 0, '', 'ta', 0, 'ba', 0],
    ['seconds', 0, '', 'special', 'ms', 100, 30],
    ['pos', 0.5, '', 'special', 'tr']
]

seconds = 0

baserow = ['seconds', 0, '', 'lightning']
disappearrow = ['seconds', 0, '', 'lightningdisappear', 'ta', 80, 0, 1, 80]

lights = ['t0', 't1', 't4', 't5']
lightintensity = 255
lastlight = ''
steptime = (40,60)
maximumsteptime = 150
blinksatstart = 30
blinksatcenter = None
blinksperspeed = 1
blinks = 0

done = False
reverse = False

# import pdb; pdb.set_trace()

while blinksatstart or (not done and blinks <= blinksperspeed) or blinksatcenter:
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
    if blinksatstart: 
        if blinks < blinksatstart:
            blinks += 1
        else:
            blinks = 0
            blinksatstart = None
    elif blinksatcenter:
        if blinks < blinksatcenter:
            blinks += 1
        else:
            blinks = 0
            blinksatcenter = 0
    else:
        if blinks == blinksperspeed:
            if reverse:
                steptime = (steptime[0] - 4, steptime[1] - 4)
            else:
                steptime = (steptime[0] + 4, steptime[1] + 4)
            blinks = 0
        else:
            blinks += 1
    if steptime[1] >= maximumsteptime:
        if blinksatcenter is None:
            blinksatcenter = 3
        elif blinksatcenter == 0:
            reverse = True
    if not done and reverse and steptime[1] <= 60:
        blinksatstart = 30
        done = True

rows.append(['seconds', seconds, '', 'instant', 'ta', 0, 'ba', 0])
rows.append(['seconds', seconds, '', 'special', 'ms', 0, 30])
    

with open('dancingfade_startendlong_transitionshort_longercenter.csv', "w") as f:
    for row in rows:
        f.write(','.join([str(x) for x in row]))
        f.write('\n')