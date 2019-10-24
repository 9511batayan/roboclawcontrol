'''
# brief : This file is speed script for roboclaw driver.
# @author : koji kawabata
# @date : 2019/10/23
'''

import time
import signal
import sys
import roboclaw_driver.roboclaw_driver as rc

rc.Open('/dev/ttyACM0',115200)
address = 0x80
rc.ForwardMixed(address, 0)
rc.TurnRightMixed(address, 0)
print("run speed command")
try:
	rc.SpeedM1(address, 300)
	time.sleep(2)
	rc.SpeedM2(address, 300)
	time.sleep(2)
	rc.SpeedM1M2(address, 150, 150)
	time.sleep(2)

	rc.SpeedM1(address, -300)
	time.sleep(2)
	rc.SpeedM2(address, -300)
	time.sleep(2)
	rc.SpeedM1M2(address, -150, -150)
	time.sleep(2)
	rc.SpeedM1M2(address, 0, 0)
except Exception as e:
	print(e)
finally:
	print("Finish")
	rc.ForwardM1(address, 0)
	rc.ForwardM2(address, 0)

