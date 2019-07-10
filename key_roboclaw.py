import time
import signal
import sys
from roboclaw import Roboclaw
from pykbhit import KBHit

#Windows comport name
#rc = Roboclaw("COM9",115200)
#Linux comport name

def handler(signal,frame):
	rc.ForwardMixed(address,0)
	rc.TurnRightMixed(address,0)
	print('Finish')
	sys.exit(0)

rc = Roboclaw("/dev/ttyACM0",115200)

rc.Open()
address = 0x80
pwm=32
rc.ForwardMixed(address, 0)
rc.TurnRightMixed(address, 0)

kb=KBHit()
print('Hit any key(w,a,d,s,e), or Ctr+c to exit')
signal.signal(signal.SIGINT,handler)
while True:
	if kb.kbhit():
		c=kb.getch()
		print(c)
		rc.ForwardMixed(address,0)
		rc.TurnRightMixed(address,0)
		if ord(c)==119:	# w
			rc.ForwardMixed(address, pwm)
		elif ord(c)==115:	# s
			rc.BackwardMixed(address, pwm)
		elif ord(c)==100:	# d
			rc.TurnLeftMixed(address, pwm)
		elif ord(c)==97:	# a
			rc.TurnRightMixed(address, pwm)
		elif ord(c)==101: # e
			rc.ForwardMixed(address,0)
			rc.TurnRightMixed(address,0)

