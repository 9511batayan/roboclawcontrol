'''
# brief : This file is sample code for roboclaw driver.
# @author : koji kawabata
# @date : 2019/9/27
'''

import time
import signal
import sys
import roboclaw_driver.roboclaw_driver as rc

rc.Open('/dev/ttyACM0',115200)
address = 0x80

print(rc.ReadVersion(address))
print(rc.ReadM1VelocityPID(address))
print(rc.ReadM2VelocityPID(address))

