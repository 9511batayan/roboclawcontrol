<<<<<<< HEAD
'''
# brief : This script is code to measurement moter current.
# @author : koji kawabata
# @date : 2019/11/15
'''
import sys,signal,time
import roboclaw_driver.roboclaw_driver as rc

def handler(signal,frame):
	sys.exit(0)

def displayCurrent():
    l_currentA, r_currentA,crc = rc.ReadCurrents(address)
    elapsed_time = time.time() - start
    print("elapsed_time:{0}".format(elapsed_time)+"[sec] "+
    "M1 moter current "+str(l_currentA)+"[A]")
    print("elapsed_time:{0}".format(elapsed_time)+"[sec] "+
    "M2 moter current "+str(r_currentA)+"[A]")

rc.Open('/dev/ttyACM0',115200)
signal.signal(signal.SIGINT,handler)

try:
	# loop until ctl + c
    m1_qpps = m2_qpps = 100
    rc.SpeedM1M2(address, m1_qpps, m2_qpps)
    l_currentA, r_currentA,crc = rc.ReadCurrents(address)
    start = time.time()
	while True:
        displayCurrent()
        time.sleep(0.01)
    
except Exception as e:
=======
'''
# brief : This script is code to measurement moter current.
# @author : koji kawabata
# @date : 2019/11/15
'''
import sys,signal,time
import roboclaw_driver.roboclaw_driver as rc

def handler(signal,frame):
	sys.exit(0)

def displayCurrent():
    l_currentA, r_currentA,crc = rc.ReadCurrents(address)
    elapsed_time = time.time() - start
    print("elapsed_time:{0}".format(elapsed_time)+"[sec] "+
    "M1 moter current "+str(l_currentA)+"[A]")
    print("elapsed_time:{0}".format(elapsed_time)+"[sec] "+
    "M2 moter current "+str(r_currentA)+"[A]")

rc.Open('/dev/ttyACM0',115200)
signal.signal(signal.SIGINT,handler)

try:
	# loop until ctl + c
    m1_qpps = m2_qpps = 100
    rc.SpeedM1M2(address, m1_qpps, m2_qpps)
    l_currentA, r_currentA,crc = rc.ReadCurrents(address)
    start = time.time()
	while True:
        displayCurrent()
        time.sleep(0.01)
    
except Exception as e:
>>>>>>> master
	print(e)