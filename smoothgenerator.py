import json

lights = ['bottom-1', 'bottom-2', 'top-1', 'top-2', 'top-5', 'top-6']

fro = 215
to = 45

steps = fro-to

starttime = 1
enddtime = 1.8
timestep = (enddtime-starttime) / steps

time = starttime

total = []

brightness = 213
while brightness >=45:
	tup = ['time', time,]
	for light in lights:
		tup.append((light, str(brightness)))
	brightness -= 2
	time += timestep
	total.append(tup)

print(json.dumps(total))