import RPi.GPIO as GPIO

GPIO.setmode(GPIO.BCM)
GPIO.setup(4,GPIO.IN)
GPIO.setup(17,GPIO.OUT)

try:
    while True:
        if GPIO.input(4) == GPIO.LOW:
            GPIO.output(17, GPIO.LOW)
        else:
            GPIO.output(17, GPIO.HIGH)
except KeyboardInterrupt:
    pass

GPIO.cleanup()
