import RPi.GPIO as GPIO
from time import sleep

GPIO.setmode(GPIO.BCM)
GPIO.setup(4,GPIO.OUT)

try:
    while True:
        GPIO.output(4, GPIO.LOW)
        sleep(0.5)
        GPIO.output(4, GPIO.HIGH)
        sleep(0.5)
except KeyboardInterrupt:
    pass

GPIO.cleanup()
