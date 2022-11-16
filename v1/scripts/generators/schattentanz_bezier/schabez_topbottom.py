import random

# Seconds
dancinglength = 5
schattensteps = 20
# milliseconds
schattentime = 350

rows = [
    ['seconds', 0, '', 'ta', 0, 'ba', 0],
    ['seconds', 0, '', 'special', 'ms', 100, 30],
    ['pos', 0.5, '', 'special', 'tr']
]

disappearrow = ['seconds', 0, '', 'lightningbezierdimm', 'ta', 80, 0, 1, 0, 0, 0, 0, 70]
randintrange = (0,100)

bottomlight = 90
flip = True

seconds = 0

# this could be a "complex effect" object
for i in range(schattensteps):
    row = disappearrow.copy()
    row[1] = seconds
    row[8] = random.randint(randintrange[0], randintrange[1])
    row[9] = random.randint(randintrange[0], randintrange[1])
    row[10] = random.randint(randintrange[0], randintrange[1])
    row[11] = random.randint(randintrange[0], randintrange[1])
    if not flip:
        row[4] = 'ba'
        row[5] = bottomlight
        flip = not flip
    else:
        flip = not flip

    seconds += (disappearrow[-1] + 250 + 250)/1000
    rows.append(row)


rows.append(['seconds', seconds, '', 'instant', 'ta', 0, 'ba', 0])
rows.append(['seconds', seconds, '', 'special', 'ms', 0, 30])
    

with open('schattenbezier_20_topbottom.csv', "w") as f:
    for row in rows:
        f.write(','.join([str(x) for x in row]))
        f.write('\n')