import serial
import time

ser1 = serial.Serial("/dev/ttyAMA0", 9600, timeout=10)

try:
    while True:
        ss = ser1.readline()
        ser1.write(ss)
except KeyboardInterrupt:
    pass
