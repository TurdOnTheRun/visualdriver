
import json

INPUT = 'testscript.csv'
OUTPUT = 'testscript.json'
FPS = 25

TRIGGERTYPES = ['time','pos']
COMMANDTYPES = ['instant', 'linear', 'strobe']
TOPLIGHTS = ['t0','t1','t2','t3','t4','t5','t6','t7','t8','t9','ta']
BOTTOMLIGHTS = ['b0','b1','b2','ba']



def fpstime_to_seconds(fpstime):
	fpstime = fpstime.split('.')
	if len(fpstime) == 3:
		fpstime = int(fpstime[0])*60 + int(fpstime[1]) + int(fpstime[2])*(1.0/FPS)
	else:
		fpstime = int(fpstime[0]) + int(fpstime[1]) * (1.0/FPS)
	return fpstime


def parse_trigger_value(triggertype, value):
	if triggertype == 'time':
		value = fpstime_to_seconds(value)
	elif triggertype == 'pos':
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
	else:
		light = int(lightid[-1])
		if commandtype == 'instant':
			return light
		if commandtype == 'linear':
			return 10 + light
		if commandtype == 'strobe':
			return 20 + light


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
		c.append([lightid,int(state)])

		parsedcomms.append(c)
	
	return parsedcomms


def get_linear_comms(comms, timeframe):


	import pdb;pdb.set_trace()

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
		c.append([lightid,int(tostate),steptime])

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
		c.append([lightid,int(state),int(strobebeat)])

		parsedcomms.append(c)
	
	return parsedcomms


def get_comms(commandtype, comms, timeframe):

	if commandtype == 'instant':
		parsedcomms = get_instant_comms(comms)
	elif commandtype == 'linear':
		parsedcomms = get_linear_comms(comms, timeframe)
	elif commandtype == 'strobe':
		parsedcomms = get_strobe_comms(comms)

	return parsedcomms


def abort(index, message, e=None):
	print('Failure in Line', index)
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

		elements = line.strip().split(',')
		triggertype = elements[0]
		fromvalue = elements[1]
		tovalue = elements[2]
		commandtype = elements[3]
		timeframe = None

		print(triggertype, fromvalue, tovalue, commandtype)

		if triggertype not in TRIGGERTYPES:
			abort(index, 'Invalid Triggertype')
		
		if commandtype not in COMMANDTYPES:
			abort(index, 'Invalid Commandtype')

		try:
			fromvalue = parse_trigger_value(triggertype, fromvalue)
		except Exception as e:
			abort(index, 'Unable to parse fromvalue', e)

		if commandtype == 'linear':
			try:
				tovalue = parse_trigger_value(triggertype, tovalue)
				timeframe = tovalue - fromvalue
			except Exception as e:
				abort(index, 'Unable to parse tovalue', e)

		elif tovalue:
			abort(index, 'Unnecessary definition of tovalue')

		i = 4

		l = [triggertype, fromvalue]

		comms = elements[4:]
		comms = list(filter(lambda a: a != '', comms))

		l += get_comms(commandtype, comms, timeframe)

		script.append(l)


with open(OUTPUT, 'w') as outfile:
    json.dump(script, outfile, indent=4)