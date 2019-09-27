'''
# brief : This file is sample code for roboclaw driver.
# @author : koji kawabata
# @date : 2019/9/27
'''

import time
import signal
import sys
import roboclaw_driver.roboclaw_driver as rc

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

# loop until ctl + c
while True:
	'''
	# control command
	'''