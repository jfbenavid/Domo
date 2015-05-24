import RPi.GPIO as GPIO
import sys
import os

GPIO.setmode(GPIO.BCM)
GPIO.setup(int(sys.argv[1]), GPIO.OUT)

viene=sys.argv[2]
valor=False

if viene=="1":
	valor=True

GPIO.output(int(sys.argv[1]), valor)