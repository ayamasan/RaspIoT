import smbus
from time import sleep

bus = smbus.SMBus(1)

# LCD display function
def lcdout(msg):
    for c in msg:
        bus.write_byte_data(0x3e, 0x40, ord(c))

# init LCD
bus.write_byte_data(0x3e, 0x00, 0x38)
bus.write_byte_data(0x3e, 0x00, 0x39)
bus.write_byte_data(0x3e, 0x00, 0x14)
bus.write_byte_data(0x3e, 0x00, 0x70)
bus.write_byte_data(0x3e, 0x00, 0x56)
bus.write_byte_data(0x3e, 0x00, 0x6c)
sleep(0.5)
# clear LCD
bus.write_byte_data(0x3e, 0x00, 0x38)
bus.write_byte_data(0x3e, 0x00, 0x0d)
bus.write_byte_data(0x3e, 0x00, 0x01)
sleep(0.5)
# disp RASPI
lcdout("RASPI")
sleep(0.5)
# next Line
bus.write_byte_data(0x3e, 0x00, 0xc0)
sleep(0.5)
# disp LCDtest
lcdout("LCDtest")
sleep(0.5)
