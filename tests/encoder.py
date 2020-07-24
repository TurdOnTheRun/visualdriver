import time
import RPi.GPIO as GPIO

ENC_COUNT_REV = 400
ENC_IN = 23

# Declare the GPIO settings
GPIO.setmode(GPIO.BCM)
GPIO.setup(ENC_IN, GPIO.IN, pull_up_down=GPIO.PUD_UP)

encoderValue = 0
interval = 0.5
previousSecs = 0
currentSecs = 0
rps = 0

def rpm_counter(channel):
	global encoderValue
	encoderValue += 1

GPIO.add_event_detect(ENC_IN, GPIO.RISING, callback=rpm_counter)

while True:
	currentSecs = time.time()
	
	if (currentSecs - previousSecs) > interval:
		print('CurrentSecs vs prevsecs:',currentSecs - previousSecs)
		previousSecs = currentSecs
	
		rps = encoderValue * 2 / ENC_COUNT_REV
		
		print('PWM:',rps)
		
		encoderValue = 0
