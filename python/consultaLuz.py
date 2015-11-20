import RPi.GPIO as GPIO
import sys
import os

#def consultaEstado():
	GPIO.setmode(GPIO.BCM)
	GPIO.setup(int(sys.argv[1]), GPIO.IN)
	if GPIO.input(int(sys.argv[1])):
		return 1
	else
		return 0

