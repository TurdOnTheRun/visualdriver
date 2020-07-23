import serial
import time

time_now = lambda: int(round(time.time() * 1000))

ser = serial.Serial( "/dev/cu.HC-06-SPPDev", baudrate=9600 )
time.sleep(3)


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



import pdb; pdb.set_trace()

ser.write(bytes(str(9999) + '\n','utf-8'))
ser.close()