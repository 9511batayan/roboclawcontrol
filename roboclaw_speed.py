#***Before using this example the motor/controller combination must be
#***tuned and the settings saved to the Roboclaw using IonMotion.
#***The Min and Max Positions must be at least 0 and 50000

import time
import roboclaw_driver.roboclaw_driver as rc

rc.Open("/dev/ttyACM0",115200)

def displayspeed():
	enc1 = rc.ReadEncM1(address)
	enc2 = rc.ReadEncM2(address)
	speed1 = rc.ReadSpeedM1(address)
	speed2 = rc.ReadSpeedM2(address)

	print("Encoder1:"),
	if(enc1[0]==1):
		print enc1[1],
		print format(enc1[2],'02x'),
	else:
		print "failed",
	print "Encoder2:",
	if(enc2[0]==1):
		print enc2[1],
		print format(enc2[2],'02x'),
	else:
		print "failed " ,
	print "Speed1:",
	if(speed1[0]):
		print speed1[1],
	else:
		print "failed",
	print("Speed2:"),
	if(speed2[0]):
		print speed2[1]
	else:
		print "failed "

address = 0x80

version = rc.ReadVersion(address)
if version[0]==False:
	print "GETVERSION Failed"
else:
	print repr(version[1])

try:
	while(1):
		rc.SpeedM1(address,120)
		rc.SpeedM2(address,-120)
		for i in range(0,100):
			displayspeed()
			time.sleep(0.1)

		rc.SpeedM1(address,-120)
		rc.SpeedM2(address,120)
		for i in range(0,100):
			displayspeed()
			time.sleep(0.1)
except Exception as e:
	print(e)
finally:
	rc.SpeedM1M2(address, 0, 0)
	time.sleep(1)

