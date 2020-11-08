import json

lights = ['bottom-1', 'bottom-2', 'top-1', 'top-2', 'top-5', 'top-6']

fro = 200
to = 20

steps = fro-to

starttime = 1
enddtime = 1.8
timestep = (enddtime-starttime) / steps

time = starttime

total = []

brightness = 20
while brightness <=200:
	tup = ['time', time,]
	for light in lights:
		tup.append((light, str(brightness)))
	brightness += 2
	time += timestep
	total.append(tup)

print(json.dumps(total))