'''
# brief : This file is program to operate roboclaw to keyboard.
# @author : koji kawabata
# @date : 2019/6/25
'''

import time
import signal
import sys
import roboclaw_driver.roboclaw_driver as rc
from pykbhit import KBHit

def handler(signal,frame):
	rc.ForwardMixed(address,0)
	rc.TurnRightMixed(address,0)
	print('Finish')
	sys.exit(0)

rc.Open('/dev/ttyACM0',115200)
address = 0x80
pwm=32
rc.ForwardMixed(address, 0)
rc.TurnRightMixed(address, 0)
signal.signal(signal.SIGINT,handler)
kb=KBHit()

print('Hit any key(w,a,d,s,e), or Ctr+c to exit')
while True:
	if kb.kbhit():
		c=kb.getch()
		print(c)
		rc.ForwardMixed(address,0)
		rc.TurnRightMixed(address,0)
		if ord(c)==119:
			rc.ForwardMixed(address, pwm)
		elif ord(c)==115:
			rc.BackwardMixed(address, pwm)
		elif ord(c)==100:
			rc.TurnLeftMixed(address, pwm)
		elif ord(c)==97:
			rc.TurnRightMixed(address, pwm)
		elif ord(c)==101:
			rc.ForwardMixed(address,0)
			rc.TurnRightMixed(address,0)

