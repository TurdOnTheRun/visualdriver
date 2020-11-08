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

	strbrightness = str(brightness)
	if len(strbrightness) == 2:
		strbrightness = '0' + strbrightness
	elif len(strbrightness) == 1:
		strbrightness = '00' + strbrightness

	for light in lights:
		tup.append((light, str(strbrightness)))
	brightness += 4
	time += timestep
	total.append(tup)

print(json.dumps(total))