#Bird cam
from picamera import PiCamera
from gpiozero import MotionSensor
import time

pir = MotionSensor(17)
camera = PiCamera()
print("Waiting for PIR to settle")
pir.wait_for_no_motion()

print("PIR Settled (CTRL-C to exit)")

currentstate = False
previousstate = False
count = 1
try:
	while True:
		currentstate = pir.motion_detected

		if currentstate == True and previousstate == False:
			print("    Motion detected, capture image in 2 seconds")
			camera.start_preview()
			time.sleep(2)
			camera.capture('/home/pi/Desktop/birdtable/image'+str(count)+'.jpg')
			camera.stop_preview()
			count += 1
			previousstate = True
		elif currentstate == False and previousstate == True:
			print("No Motion")
			previousstate = False

		time.sleep(0.01)

except KeyboardInterrupt:
    print("    Quit")
