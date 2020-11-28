
FPS = 25


def fpstime_to_seconds(fpstime):
    fpstime = fpstime.split(':')
    if len(fpstime) == 3:
        return int(fpstime[0])*60 + int(fpstime[1]) + int(fpstime[2])*(1/FPS)
    else:
        return int(fpstime[0]) + int(fpstime[1])*(1/FPS)


while True:
    value = input("from,to,steps:\n")
    try:
        commands = value.split(',')
        fro = fpstime_to_seconds(commands[0])
        to = fpstime_to_seconds(commands[1])
        print(fro, to, end='')
        diff = to-fro
        for step in commands[2:]:
            step = int(step)
            steptime = diff/step * 1000
            print(' ', steptime, ' ', end='')
        print()
    except ValueError as e:
        print('Invalid Command')
        raise e