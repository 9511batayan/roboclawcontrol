'''
# @brief : This file is a program for PWM control while reading the encoder.
# @author : koji kawabata
# @date : 2019/9/27
'''

import time
import signal
import sys
import roboclaw_driver.roboclaw_driver as rc
from pykbhit import KBHit

def handler(signal,frame):
	rc.ForwardMixed(address,0)
	rc.TurnRightMixed(address,0)
	file.close()
	print('Finish')
	sys.exit(0)

def displayspeed():
	enc1 = rc.ReadEncM1(address)
	enc2 = rc.ReadEncM2(address)
	speed1 = rc.ReadSpeedM1(address)
	speed2 = rc.ReadSpeedM2(address)
	list=[str(enc1[1])+",",str(enc2[1])+",",str(speed1[1])+",",str(speed2[1])]

	print("Encoder1:"),
	if(enc1[0]==1):
		print enc1[1],
		print format(enc1[2],'02x'),
	else:
		print "failed",
		list[0]="failed"

	print "Encoder2:",
	if(enc2[0]==1):
		print enc2[1],
		print format(enc2[2],'02x'),
		
	else:
		print "failed " ,
		list[1]="failed"
		
	print "Speed1:",
	if(speed1[0]):
		print speed1[1],
		
	else:
		print "failed",
		list[2]="failed"
	
	print("Speed2:"),
	if(speed2[0]):
		print speed2[1]
		
	else:
		print "failed"
		list[3]="failed"
	file.writelines(list)
	file.write('\n')

path='test.csv'
file=open(path,'w')
rc.Open('/dev/ttyACM0',115200)
address = 0x80
pwm=32
rc.ForwardMixed(address, 0)
rc.TurnRightMixed(address, 0)
rc.ResetEncoders(address)
signal.signal(signal.SIGINT,handler)
kb=KBHit()

print('Hit any key(w,a,d,s,e), or Ctr+c to exit')
version = rc.ReadVersion(address)
if version[0]==False:
	print "GETVERSION Failed"
else:
	print repr(version[1])

while True:
	time.sleep(0.010)
	displayspeed()
	if kb.kbhit():
		c=kb.getch()
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

