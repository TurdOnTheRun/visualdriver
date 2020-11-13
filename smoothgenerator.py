import json

lights = ['bottom-9', 'top-9']

MINIMUM_TIMESTEP_PER_COMMAND = 0.004

command = [1,0.8,200,20,['bottom-9','top-9']]

fro = None
to = None

if command[2] < command[3]:
	steps = command[3] - command[2]
	increasing = True
else:
	steps = command[2] - command[3]
	increasing = False

timestep = command[1] / steps

if timestep < MINIMUM_TIMESTEP_PER_COMMAND:
	print('The Timesteps are too short.')
	exit(1)

time = command[0]
brightness = command[2]
line = []

if increasing:
	while brightness <= command[3]:
		tup = ['time', time,]

		strbrightness = str(brightness)
		if len(strbrightness) == 2:
			strbrightness = '0' + strbrightness
		elif len(strbrightness) == 1:
			strbrightness = '00' + strbrightness

		for light in command[4]:
			tup.append((light, str(strbrightness)))
		brightness += 1
		time += timestep
		line.append(tup)
else:
	while brightness >= command[3]:
		tup = ['time', time,]

		strbrightness = str(brightness)
		if len(strbrightness) == 2:
			strbrightness = '0' + strbrightness
		elif len(strbrightness) == 1:
			strbrightness = '00' + strbrightness

		for light in command[4]:
			tup.append((light, str(strbrightness)))
		brightness -= 1
		time += timestep
		line.append(tup)

print(json.dumps(line))