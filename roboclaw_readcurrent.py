'''
# brief : This script is code to measurement moter current.
# @author : koji kawabata
# @date : 2019/11/15
'''
import sys,signal,time
import roboclaw_driver.roboclaw_driver as rc

def handler(signal,frame):
	rc.SpeedM1M2(address, 0, 0)
	sys.exit(0)

def displayCurrent():
    crc, l_currentA, r_currentA = rc.ReadCurrents(address)
    elapsed_time = time.time() - start
    l_currentA /= 100.0
    r_currentA /= 100.0
    if crc == 1:
#	print("M1 moter current "+'{:.3}'.format(l_current)+"[A]")
#	print("M2 moter current "+'{:.3}'.format(r_current)+"[A]") 
    	print("elapsed_time:{0}".format(elapsed_time)+"[sec] "+
    	"M1 moter current "+'{:.3}'.format(l_currentA)+"[A]")
    	print("elapsed_time:{0}".format(elapsed_time)+"[sec] "+
    	"M2 moter current "+'{:.3}'.format(r_currentA)+"[A]")
    else:
	print("Failed")

rc.Open('/dev/ttyACM0',115200)
signal.signal(signal.SIGINT,handler)
address = 0x80

try:
	# loop until ctl + c
    m1_qpps = m2_qpps = 200
    rc.SpeedM1M2(address, m1_qpps, m2_qpps)
    time.sleep(0.5)
    start = time.time()
    
    while True:
        displayCurrent()
        time.sleep(0.01)
    
except Exception as e:
	print(e)
finally:
	rc.SpeedM1M2(address, 0, 0)

