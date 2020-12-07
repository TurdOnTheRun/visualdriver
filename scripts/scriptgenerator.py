
INPUT = 'uma.script'
OUTPUT = 'uma.py'
FPS = 25

TRIGGERTYPES = ['time','pos']
COMMANDTYPES = ['instant', 'linear', 'strobe']
TOPLIGHTS = ['t0','t1','t2','t3','t4','t5','t6','t7','t8','t9','ta']
BOTTOMLIGHTS = ['b0','b1','b2','ba']



def fpstime_to_seconds(fpstime):
	fpstime = fpstime.split(':')
	if len(fpstime) == 3:
		fpstime = int(fpstime[0])*60 + int(fpstime[1]) + int(fpstime[2])*(1/FPS)
	else:
		fpstime = int(fpstime[0] + int(fpstime[1] * (1/FPS)))
	return fpstime

def parse_trigger_value(commandtype, value):
	if commandtype == 'time':
		value = fpstime_to_seconds(value)
	elif commandtype == 'pos':
		value = float(value)
	return value

def get_byte_representation(commandtype, lightid):
	if lightid[0] == 'a':
		if commandtype == 'instant':
			return 200
		if commandtype == 'linear':
			return 201
		if commandtype == 'strobe':
			return 202
	else:
		light = int(lightid[0])
		if commandtype == 'instant':
			return 100 + light
		if commandtype == 'linear':
			return 110 + light
		if commandtype == 'strobe':
			return 120 + light



script = []


if __name__ == "__main__":

	lines = open(INPUT, 'r') 
	lines = lines.readlines()
	first = True

	for line in lines:
		if first:
			first = False
			continue

		elements = line.split(',')
		triggertype = elements[0]
		fromvalue = elements[1]
		tovalue = elements[2]
		commandtype = elements[3]

		print(triggertype, fromvalue, tovalue, commandtype)

		if triggertype not in TRIGGERTYPES:
			print('Invalid Triggertype')
			exit(-1)
		
		if commandtype not in COMMANDTYPES:
			print('Invalid Commandtype')
			exit(-1)

		try:
			fromvalue = parse_trigger_value(commandtype, fromvalue)
		except Exception as e:
			print('Unable to parse fromvalue')
			raise e

		if commandtype == 'linear':
			try:
				tovalue = parse_trigger_value(commandtype, tovalue)
			except Exception as e:
				print('Unable to parse tovalue')
				raise e
		elif tovalue:
			print('Unnecessary definition of tovalue')

		i = 4

		l = [triggertype, fromvalue]

		# While loop for every commandtype
		while i < len(elements):
			lightid = elements[i]
			state = elements[i+1]

			l = []

			if lightid.startswith('t'):
				l.append('top')
			elif lightid.startswith('b'):
				l.append('bottom')
			else:
				print('Lightid not implemented yet')
				exit(-1)
			
			lightid = get_byte_representation(commandtype, lightid)
			l.append([lightid,state])


			
			


# out = open(OUTPUT,'w')