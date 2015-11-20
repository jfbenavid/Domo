import RPi.GPIO as GPIO 
from time import sleep 
import sys
import os

puerto = int(sys.argv[1])
valor = int(sys.argv[2])

GPIO.setmode(GPIO.BCM)
GPIO.setup(puerto, GPIO.OUT)	#Coloca el puerto enviado por parametro como salida

luz = GPIO.PWM(puerto, valor)

luz.start(0)
#red.start(100)              # red fully on (100%)

try:
    while True:
		luz.ChangeDutyCycle(valor)

except KeyboardInterrupt:
	luz.stop()
	GPIO.cleanup()
