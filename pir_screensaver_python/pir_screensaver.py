import RPi.GPIO as GPIO
import time
import os
import subprocess
import sys


GPIO.setmode(GPIO.BCM)
PIR_PIN = 4
GPIO.setup(PIR_PIN, GPIO.IN)

time.sleep(2)

inputValue=False
isScreenSaved=False
count=0
#i=0
#willScreenSave=0

#os.system("xscreensaver-command -activate")
#isScreenSaved = True

try:    
    while True:
	inputValue = GPIO.input(4)

	if (inputValue==True and isScreenSaved==True):
		print "got in first true"
		while True:
			time.sleep(0.5)
			inputValue = GPIO.input(4)
			print inputValue
		
			if (inputValue==True and isScreenSaved==True):
				print "Deactivate screensaver"
				os.system("xscreensaver-command -deactivate")
				isScreenSaved = False
				break;

			else:
				break;

	if (inputValue==False and isScreenSaved==False):
		print "got in first false"
		while True:
			
			time.sleep(3)

			inputValue = GPIO.input(4)
			print inputValue

			if (inputValue==False and isScreenSaved==False):
				print "Activate screensaver in 3 seconds"
				time.sleep(3)
				os.system("xscreensaver-command -activate")
				isScreenSaved = True
				break

			else:
				break


#	if (inputValue==True and isScreenSaved==True):
#		willScreenSave = 0
		
#		print "yes_Realllll"
#		os.system("xscreensaver-command -deactivate")
#		isScreenSaved = False

#		time.sleep(1)
		
#		while True:
#			inputValue = GPIO.input(4)
#			if (inputValue==False and isScreenSaved==False):
#				willScreenSave = 0
#				for i in range(0,3):
#					print "nono"
#					print i
#					inputValue = GPIO.input(4)
#					if (inputValue==True and isScreenSaved == True):
#						willScreenSave=1
#						break
#					time.sleep(0.3)
#				if (willScreenSave==0):
#					print "nono_realllll"
#					os.system("xscreensaver-command -activate")
#					time.sleep(1)
#					isScreenSaved = False
#				
#			elif (inputValue==True and isScreenSaved==False):
#				willScreenSave = 0
#				for i in range(0,3):
#					print "yes"
#					print i
#					inputValue = GPIO.input(4)
#					if (inputValue==False and isStop==True):
#						willScreenSave=1
#						break
#					time.sleep(0.3)
#				if (willScreenSave==0):
#					print "yes_realllll"
#					isScreenSaved=False
#					break
#
		
except KeyboardInterrupt:
    print "Quit"
    GPIO.cleanup()