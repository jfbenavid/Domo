import RPi.GPIO as GPIO 
from time import sleep 
import sys
import os

puerto = int(sys.argv[1])
valor = int(sys.argv[2])

GPIO.setmode(GPIO.BCM)

GPIO.setup(int(sys.argv[1]), GPIO.OUT)

luz = GPIO.PWM(int(sys.argv[1]), 100)    # create object white for PWM on port 25 at 100 Hertz
#red = GPIO.PWM(24, 100)      # create object red for PWM on port 24 at 100 Hertz

white.start(sys.argv[1])              # start white led on 0 percent duty cycle (off)
#red.start(100)              # red fully on (100%)

# now the fun starts, we'll vary the duty cycle to 
# dim/brighten the leds, so one is bright while the other is dim

#pause_time = 0.02           # you can change this to slow down/speed up

try:
    while True:
#        for i in range(0,101):      # 101 because it stops when it finishes 100
            white.ChangeDutyCycle(sys.argv[1])
#            red.ChangeDutyCycle(100 - i)
#            sleep(pause_time)
#        for i in range(100,-1,-1):      # from 100 to zero in steps of -1
#            white.ChangeDutyCycle(i)
#            red.ChangeDutyCycle(100 - i)
#            sleep(pause_time)

except KeyboardInterrupt:
    white.stop()            # stop the white PWM output
#    red.stop()              # stop the red PWM output
    GPIO.cleanup()          # clean up GPIO on CTRL+C exit
