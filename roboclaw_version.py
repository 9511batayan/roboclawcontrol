import time
import roboclaw_driver.roboclaw_driver as rc

rc.Open("/dev/ttyACM0",115200)
address =  0x80

while(1):
	version = rc.ReadVersion(address)
	if version[0] == False:
	        print "GETVERSION Failed"
	else:
        	print repr(version[1])
		break
	time.sleep(1)
