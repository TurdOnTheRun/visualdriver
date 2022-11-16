import time
import json
import winsound

INPUT = './dancingfade_startendlong_longercenter_sound.json'
f = open(INPUT,) 
SCRIPT = json.load(f)
f.close()

try:
    last = time.time()
    i = 0
    while i < len(SCRIPT):
        step = SCRIPT[i]
        # print(step[0:2])
        if step[0] == 'time':
            if time.time() - last > step[1]*2:
                winsound.Beep(350, step[2][1][2]*2)
                # winsound.PlaySound('sound.wav', winsound.SND_FILENAME)
                i+=1
except Exception as e:
    print('Error:', e)
    raise e

        
