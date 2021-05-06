
import json

INPUT = './video/strobe/rotating_morphestrobe_test.csv'
OUTPUT = './video/strobe/rotating_morphestrobe_test.json'
FPS = 25


TRIGGERTYPES = ['fps','seconds','pos']
COMMANDTYPES = ['special', 'instant', 'linear', 'strobe', 'instanttolinear', 'lightning', 'lightningdisappear', 'lightningappear', 'machinegun', 'acceleratingstrobe']
SPECIALCOMMANDTYPES = ['ms', 'md', 'tb', 'tr','TRIGGER_DOWN', 'TRIGGER_UP']
TOPLIGHTS = ['t0','t1','t2','t3','t4','t5','t6','t7','t8','t9','ta']
BOTTOMLIGHTS = ['b0','b1','b2','ba']



def fpstime_to_seconds(fpstime):
	fpstime = fpstime.split('.')
	if len(fpstime) == 3:
		fpstime = int(fpstime[0])*60 + int(fpstime[1]) + int(fpstime[2])*(1.0/FPS)
	elif len(fpstime) == 2:
		fpstime = int(fpstime[0]) + int(fpstime[1]) * (1.0/FPS)
	else:
		fpstime = int(fpstime[0]) * (1.0/FPS)
	return fpstime


def parse_trigger_value(triggertype, value):
	if triggertype == 'fps':
		value = fpstime_to_seconds(value)
	elif triggertype == 'pos' or triggertype == 'seconds':
		value = float(value)
	return value


def get_byte_representation(commandtype, lightid):
	if lightid[-1] == 'a':
		if commandtype == 'instant':
			return 200
		if commandtype == 'linear':
			return 201
		if commandtype == 'strobe':
			return 202
		if commandtype == 'instanttolinear':
			return 203
		if commandtype == 'lightning':
			return 204
		if commandtype == 'lightningdisappear':
			return 205
		if commandtype == 'lightningappear':
			return 206
		if commandtype == 'machinegun':
			return 207
		if commandtype == 'acceleratingstrobe':
			return 208
	else:
		light = int(lightid[-1])
		if commandtype == 'instant':
			return light
		if commandtype == 'linear':
			return 10 + light
		if commandtype == 'strobe':
			return 20 + light
		if commandtype == 'instanttolinear':
			return 30 + light
		if commandtype == 'lightning':
			return 40 + light
		if commandtype == 'lightningdisappear':
			return 50 + light
		if commandtype == 'lightningappear':
			return 60 + light
		if commandtype == 'machinegun':
			return 70 + light
		if commandtype == 'acceleratingstrobe':
			return 80 + light


def get_special_comms(comms):

	parsedcomms = []

	i = 0

	# While loop for every commandtype
	while i < len(comms):
		comm = comms[i]
		if comm not in SPECIALCOMMANDTYPES:
			print('Command "' + comm + '" not implemented yet')
			exit(-1)
		# Motor Commands
		if comm.startswith('m'):
			c = ['bottom']
			if comm == 'ms':
				commid = 220
				speed = comms[i+1]
				steptime = comms[i+2]
				c.append(clean_bytes([commid,int(speed),int(steptime)]))
				i += 3
			elif comm == 'md':
				commid = 221
				c.append(clean_bytes([commid,]))
				i += 1
		# Trigger Commands
		elif comm.lower().startswith('t'):
			c = ['raspy']
			if comm == 'tb':
				# trigger button
				commid = 1
				deciseconds = comms[i+1]
				c.append([commid,int(deciseconds)])
				i += 2
			elif comm == 'tr':
				# time reset
				commid = 2
				c.append([commid,])
				i += 1
			elif comm == 'TRIGGER_DOWN':
				commid = 3
				c.append([commid,])
				i += 1
			elif comm == 'TRIGGER_UP':
				commid = 4
				c.append([commid,])
				i += 1

		else:
			print('Special Command "' + comm + '" not implemented yet')
			exit(-1)

		parsedcomms.append(c)
	
	return parsedcomms


def get_instant_comms(comms):

	parsedcomms = []

	i = 0

	# While loop for every commandtype
	while i < len(comms):
		lightid = comms[i]
		state = comms[i+1]
		i += 2

		c = []

		if lightid.startswith('t'):
			c.append('top')
		elif lightid.startswith('b'):
			c.append('bottom')
		else:
			print('Lightid not implemented yet')
			exit(-1)
		
		lightid = get_byte_representation('instant', lightid)
		c.append(clean_bytes([lightid,int(state)]))

		parsedcomms.append(c)
	
	return parsedcomms


def get_linear_comms(comms, timeframe):

	parsedcomms = []

	i = 0

	# While loop for every commandtype
	while i < len(comms):
		lightid = comms[i]
		fromstate = int(comms[i+1])
		tostate = int(comms[i+2])
		i += 3

		c = []

		if lightid.startswith('t'):
			c.append('top')
		elif lightid.startswith('b'):
			c.append('bottom')
		else:
			print('Lightid not implemented yet')
			exit(-1)
		
		lightid = get_byte_representation('linear', lightid)
		steptime = int(round(1000 * timeframe/(abs(fromstate-tostate))))
		c.append(clean_bytes([lightid,int(tostate),steptime]))

		parsedcomms.append(c)
	
	return parsedcomms


def get_strobe_comms(comms):

	parsedcomms = []

	i = 0

	# While loop for every commandtype
	while i < len(comms):
		lightid = comms[i]
		state = comms[i+1]
		strobebeat = comms[i+2]
		i += 3

		c = []

		if lightid.startswith('t'):
			c.append('top')
		elif lightid.startswith('b'):
			c.append('bottom')
		else:
			print('Lightid not implemented yet')
			exit(-1)
		
		lightid = get_byte_representation('strobe', lightid)
		c.append(clean_bytes([lightid,int(state),int(strobebeat)]))

		parsedcomms.append(c)
	
	return parsedcomms


def get_instanttolinear_comms(comms, timeframe):

	parsedcomms = []

	i = 0

	# While loop for every commandtype
	while i < len(comms):
		lightid = comms[i]
		state1 = int(comms[i+1])
		state2 = int(comms[i+2])
		i += 3

		c = []

		if lightid.startswith('t'):
			c.append('top')
		elif lightid.startswith('b'):
			c.append('bottom')
		else:
			print('Lightid not implemented yet')
			exit(-1)
		
		lightid = get_byte_representation('instanttolinear', lightid)
		steptime = int(round(1000 * timeframe/(abs(state1-state2))))
		c.append(clean_bytes([lightid,int(state1),int(state2),steptime]))

		parsedcomms.append(c)
	
	return parsedcomms


def get_lightning_comms(comms):

	parsedcomms = []

	i = 0

	# While loop for every commandtype
	while i < len(comms):
		lightid = comms[i]
		state = comms[i+1]
		exposure = comms[i+2]
		i += 3

		c = []

		if lightid.startswith('t'):
			c.append('top')
		elif lightid.startswith('b'):
			c.append('bottom')
		else:
			print('Lightid not implemented yet')
			exit(-1)
		
		lightid = get_byte_representation('lightning', lightid)
		c.append(clean_bytes([lightid,int(state),int(exposure)]))

		parsedcomms.append(c)
	
	return parsedcomms


def get_lightningdisappear_comms(comms):

	parsedcomms = []

	i = 0

	# While loop for every commandtype
	while i < len(comms):
		lightid = comms[i]
		state1 = comms[i+1]
		state2 = comms[i+2]
		steptime = comms[i+3]
		exposure = comms[i+4]
		i += 5

		c = []

		if lightid.startswith('t'):
			c.append('top')
		elif lightid.startswith('b'):
			c.append('bottom')
		else:
			print('Lightid not implemented yet')
			exit(-1)
		
		lightid = get_byte_representation('lightningdisappear', lightid)
		c.append(clean_bytes([lightid,int(state1),int(state2),int(steptime),int(exposure)]))

		parsedcomms.append(c)
	
	return parsedcomms


def get_lightningappear_comms(comms):

	parsedcomms = []

	i = 0

	# While loop for every commandtype
	while i < len(comms):
		lightid = comms[i]
		state1 = comms[i+1]
		state2 = comms[i+2]
		steptime = comms[i+3]
		exposure = comms[i+4]
		i += 5

		c = []

		if lightid.startswith('t'):
			c.append('top')
		elif lightid.startswith('b'):
			c.append('bottom')
		else:
			print('Lightid not implemented yet')
			exit(-1)
		
		lightid = get_byte_representation('lightningappear', lightid)
		c.append(clean_bytes([lightid,int(state1),int(state2),int(steptime),int(exposure)]))

		parsedcomms.append(c)
	
	return parsedcomms


def get_machinegun_comms(comms):

	parsedcomms = []

	i = 0

	# While loop for every commandtype
	while i < len(comms):
		lightid = comms[i]
		state = comms[i+1]
		steps = comms[i+2]
		exposure = comms[i+3]
		i += 4

		c = []

		if lightid.startswith('t'):
			c.append('top')
		elif lightid.startswith('b'):
			c.append('bottom')
		else:
			print('Lightid not implemented yet')
			exit(-1)
		
		lightid = get_byte_representation('machinegun', lightid)
		c.append(clean_bytes([lightid,int(state),int(steps),int(exposure)]))

		parsedcomms.append(c)
	
	return parsedcomms


def get_acceleratingstrobe_comms(comms):

	parsedcomms = []

	i = 0

	# While loop for every commandtype
	while i < len(comms):
		lightid = comms[i]
		state = comms[i+1]
		steptime = comms[i+2]
		darktime = comms[i+3]
		darktimestep = comms[i+4]
		i += 5

		c = []

		if lightid.startswith('t'):
			c.append('top')
		elif lightid.startswith('b'):
			c.append('bottom')
		else:
			print('Lightid not implemented yet')
			exit(-1)
		
		lightid = get_byte_representation('acceleratingstrobe', lightid)
		c.append(clean_bytes([lightid,int(state),int(steptime),int(darktime),int(darktimestep)]))

		parsedcomms.append(c)
	
	return parsedcomms


def get_comms(commandtype, comms, timeframe):

	if commandtype == 'special':
		parsedcomms = get_special_comms(comms)
	elif commandtype == 'instant':
		parsedcomms = get_instant_comms(comms)
	elif commandtype == 'linear':
		parsedcomms = get_linear_comms(comms, timeframe)
	elif commandtype == 'strobe':
		parsedcomms = get_strobe_comms(comms)
	elif commandtype == 'instanttolinear':
		parsedcomms = get_instanttolinear_comms(comms, timeframe)
	elif commandtype == 'lightning':
		parsedcomms = get_lightning_comms(comms)
	elif commandtype == 'lightningdisappear':
		parsedcomms = get_lightningdisappear_comms(comms)
	elif commandtype == 'lightningappear':
		parsedcomms = get_lightningappear_comms(comms)
	elif commandtype == 'machinegun':
		parsedcomms = get_machinegun_comms(comms)
	elif commandtype == 'acceleratingstrobe':
		parsedcomms = get_acceleratingstrobe_comms(comms)
	return parsedcomms


def clean_bytes(comms):
	cleanedComms = []
	errorMessage = 'Invalid Command: '

	for comm in comms:
		if type(comm) == int and comm >= 0 and comm <= 255:
			if comm == 251:
				comm = 250
			if comm == 252:
				comm = 253
			cleanedComms.append(comm)
		else:
			abort(errorMessage + str(comm))

	return cleanedComms


def abort(message, e=None):
	print(message)
	if e:
		raise e
	else:
		exit(-1)


script = []


if __name__ == "__main__":

	lines = open(INPUT, 'r') 
	lines = lines.readlines()

	for index, line in enumerate(lines):

		if index == 0:
			continue
		
		print(str(index) + ': ', end='')

		elements = line.strip().split(',')
		triggertype = elements[0]
		fromtime = elements[1]
		totime = elements[2]
		commandtype = elements[3]
		timeframe = None

		print(triggertype, fromtime, totime, commandtype, '- ', end='')

		if triggertype not in TRIGGERTYPES:
			abort('Invalid Triggertype')
		
		if commandtype not in COMMANDTYPES:
			abort('Invalid Commandtype')

		try:
			fromtime = parse_trigger_value(triggertype, fromtime)
		except Exception as e:
			abort('Unable to parse fromtime', e)

		if commandtype in ['linear', 'instanttolinear']:
			try:
				totime = parse_trigger_value(triggertype, totime)
				timeframe = totime - fromtime
			except Exception as e:
				abort('Unable to parse totime', e)

		elif totime:
			abort('Unnecessary definition of totime')
		
		if triggertype in ['fps','seconds']:
			triggertype = 'time'

		l = [triggertype, fromtime]

		comms = elements[4:]
		comms = list(filter(lambda a: a != '', comms))
		comms = get_comms(commandtype, comms, timeframe)
		l += comms
		script.append(l)
		print('Done')


with open(OUTPUT, 'w') as outfile:
    json.dump(script, outfile, indent=4)