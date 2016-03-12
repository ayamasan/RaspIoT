import RPi.GPIO as GPIO
from time import sleep

GPIO.setmode(GPIO.BCM)
GPIO.setup(4,GPIO.OUT)
GPIO.setup(17,GPIO.IN)

try:
    while True:
        if GPIO.input(17) == GPIO.HIGH:
            GPIO.output(4, GPIO.LOW)
        else:
            GPIO.output(4, GPIO.HIGH)
except KeyboardInterrupt:
    pass

GPIO.cleanup()
