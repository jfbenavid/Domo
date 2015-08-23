import RPi.GPIO as GPIO
import sys
import os

puerto	= int(sys.argv[1])
viene	= sys.argv[2]
valor	= False

GPIO.setmode(GPIO.BCM)
GPIO.setup(puerto, GPIO.OUT)

if viene=='1':
	valor=True

GPIO.output(puerto, valor)