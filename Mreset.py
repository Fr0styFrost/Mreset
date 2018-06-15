#!/usr/bin/python
import RPi.GPIO as GPIO
import time
import os
import subprocess

rig11 = "192.168.1.6" 
rig12 = "192.168.1.7" 
rig13 = "192.168.1.4" 
rig14 = "192.168.1.13" 
rig21 = "192.168.1.8" 
rig22 = "192.168.1.9" 
rig23 = "192.168.1.10" 
rig24 = "192.168.1.11" 
rig25 = "192.168.1.12" 



# init list with pin numbers

pinList = [2,3,4,7,8,9,10,11,14,15,18,23,24,25,]
try:
 while  True:
# loop through pins and set mode and state to 'low'
  GPIO.setmode(GPIO.BCM)
  for i in pinList: 
   GPIO.setup(i, GPIO.OUT) 
   GPIO.output(i, GPIO.HIGH)
  r11 = os.system("ping -c 1 " + rig11)
  if r11 != 0:
   GPIO.output(2, GPIO.LOW)
   print ("reseting rig 1.1")
   time.sleep(10)
   GPIO.output(2, GPIO.HIGH)
  r12 = os.system("ping -c 1 " + rig12)
  if r12 != 0:
   GPIO.output(3, GPIO.LOW)
   print ("reseting rig 1.2")
   time.sleep(10)
   GPIO.output(3, GPIO.HIGH)
  r13 = os.system("ping -c 1 " + rig13)
  if r13 != 0:
   GPIO.output(4, GPIO.LOW)
   print ("reseting rig 1.3")
   time.sleep(10)
   GPIO.output(4, GPIO.HIGH)
  r14 = os.system("ping -c 1 " + rig14)
  if r14 != 0:
   GPIO.output(7, GPIO.LOW)
   print ("reseting rig 1.4")
   time.sleep(10)
   GPIO.output(7, GPIO.HIGH)
  r21 = os.system("ping -c 1 " + rig21)
  if r21 != 0:
   GPIO.output(8, GPIO.LOW)
   print ("reseting rig 2.1")
   time.sleep(10)
   GPIO.output(8, GPIO.HIGH)
  r22 = os.system("ping -c 1 " + rig22)
  if r22 != 0:
   GPIO.output(9, GPIO.LOW)
   print ("reseting rig 2.2")
   time.sleep(10)
   GPIO.output(9, GPIO.HIGH)
  r23 = os.system("ping -c 1 " + rig23)
  if r23 != 0:
   GPIO.output(10, GPIO.LOW)
   print ("reseting rig 2.3")
   time.sleep(10)
   GPIO.output(10, GPIO.HIGH)
  r24 = os.system("ping -c 1 " + rig24)
  if r24 != 0:
   GPIO.output(11, GPIO.LOW)
   print ("reseting rig 2.4")
   time.sleep(10)
   GPIO.output(11, GPIO.HIGH)
  r25 = os.system("ping -c 1 " + rig25)
  if r25 != 0:
   GPIO.output(14, GPIO.LOW)
   print ("reseting rig 2.5")
   time.sleep(10)
   GPIO.output(14, GPIO.HIGH)

 
# Reset GPIO settings
  GPIO.cleanup()
  time.sleep(600)
  print ("sleeping for 10min")
# wait 60 seconds between each loop
except KeyboardInterrupt:
 pass
     
