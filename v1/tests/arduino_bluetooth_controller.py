# baudrate: 115200
# totalCOunter: 1000
# percentage Successfull: <30% --> 100% (Serial1)

# baudrate: 57600
# totalCOunter: 1000
# percentage Successfull: 100%
# ~35 per second

# baudrate: 38400
# totalCOunter: 1000
# percentage Successfull: 100%
# ~30 per second

# baudrate: 9600
# totalCOunter: 1000
# percentage Successfull: 100%
# ~25 per second



import serial
import time

time_now = lambda: int(round(time.time() * 1000))

BAUDRATE = 1382400

ser = serial.Serial( "/dev/cu.HC-06-SPPDev", baudrate=BAUDRATE )
# seru = serial.Serial( "/dev/cu.usbmodem1411", baudrate=9600 , timeout=1)
time.sleep(3)

# 9600 baud: 17139
# 115200 baud: 62747

# 38bytes per message


brightness = 0
up = True

counter = 0
totalCounter = 0

totalSuccess = 0
totalFailure = 0

lights = ['9']

start = time.time()
zwischenzeit = time.time()

throttle = time.time()

while True:

    if time.time() - throttle < 0.004:
        continue

    strbrightness = str(brightness)
    if len(strbrightness) == 2:
        strbrightness = '0' + strbrightness
    elif len(strbrightness) == 1:
        strbrightness = '00' + strbrightness
    for l in lights:
        command = l+strbrightness
        ser.write(bytes('<' + command + ',' + command + '>\n','utf-8'))
        # res = seru.readline()
        # print('Res:', res, type(res))
        # if res == b'0\r\n':
        #     totalSuccess += 1
        # else:
        #     totalFailure += 1
        counter += 1
        totalCounter += 1
        
    if up:
        if brightness < 255:
            brightness += 1
        else:
            brightness -= 1
            up = False
    else:
        if brightness > 1:
            brightness -= 1
        else:
            brightness += 1
            up = True
    
    # if time.time() - start > 30:
    #     for l in lights:
    #         command = l+'001'
    #         while True:
    #             ser.write(bytes('<' + command + ',' + command + '>\n','utf-8'))
    #             res = ser.readline()
    #             if res == '0':
    #                 break
    #     break

    print(brightness)

    throttle = time.time()

    # print('C:', counter)

    zz = time.time() - zwischenzeit
    if zz > 2:
        print('Per second:', (counter/zz))
        zwischenzeit = time.time()
        counter = 0

    if totalCounter == 1000:
        break

print(BAUDRATE)
print(totalCounter)
print(totalSuccess)
print(totalFailure)
print(str((totalSuccess/totalCounter)*100) + '%')


def wave():
    now = time_now()
    for i in range(1,256):
        # print(i)
        ser.write(bytes(str(1000 + i) + '\n','utf-8'))
        # now2 = time_now()
        # passed = print('W:' + str(now2 - now))
        # suc = ser.readline() 
        # passed = print('R:' + str(time_now() - now2))
        # print(suc.decode("utf-8"))
    print('R:' + str(time_now() - now))

