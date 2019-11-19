#***Before using this example the motor/controller combination must be
#***tuned and the settings saved to the Roboclaw using IonMotion.
#***The Min and Max Positions must be at least 0 and 50000

import time,sys,signal
import roboclaw_driver.roboclaw_driver as rc

def handler(signal,frame):
        rc.ForwardMixed(address,0)
        sys.exit(0)

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

rc.Open("/dev/ttyACM0", 115200)
address = 0x80
signal.signal(signal.SIGINT,handler)

version = rc.ReadVersion(address)
if version[0]==False:
	print "GETVERSION Failed"
else:
	print repr(version[1])

qpps_m1 = 50; qpps_m2 = 50; accel = 100
try:
	while(1):
		rc.SpeedAccelM1(address,accel,qpps_m1)
		rc.SpeedAccelM2(address,accel,-qpps_m2)
		for i in range(0,200):
			displayspeed()
			time.sleep(0.01)

		rc.SpeedAccelM1(address,accel,-qpps_m1)
		rc.SpeedAccelM2(address,accel,qpps_m2)
		for i in range(0,200):
			displayspeed()
			time.sleep(0.01)
except Exception as e:
	print(e)
