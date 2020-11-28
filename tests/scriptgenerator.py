
INPUT = 'uma.script'
OUTPUT = 'uma.py'
FPS = 25


def fpstime_to_seconds(fpstime):
	fpstime = fpstime.split(';')
	return int(fpstime[0])*60 + int(fpstime[1]) + int(fpstime[2])*(1/FPS)


if __name__ == "__main__":

	lines = open(INPUT, 'r') 
	lines = lines.readlines()

	for line in lines:
		elements = line.split(';')
		froms = elements[0]
		tos = elements[1]

		if froms != tos:
			fro = fpstime_to_seconds(froms)
			to = fpstime_to_seconds(tos)
			diff = to-fro
			


# out = open(OUTPUT,'w')