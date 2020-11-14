import json

lights = ['top-9', 'bottom-9']

MINIMUM_TIMESTEP_PER_COMMAND = 0.004

command = [20.75,21.45,254,0,['bottom-9','top-9']]

fro = None
to = None

if command[2] < command[3]:
	steps = command[3] - command[2]
	increasing = True
else:
	steps = command[2] - command[3]
	increasing = False

timestep = (command[1]-command[0]) / steps
print(timestep)

if timestep < MINIMUM_TIMESTEP_PER_COMMAND:
	print('Stepsize 2')
	stepsize = 2
	timestep = (command[1]-command[0]) / (steps/2)
else:
	print('Stepsize 1')
	stepsize = 1

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
		brightness += stepsize
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
		brightness -= stepsize
		time += timestep
		line.append(tup)

print(json.dumps(line))