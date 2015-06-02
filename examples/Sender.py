#! /usr/bin/python

import time

from xbee import XBee
import serial

PORT = '/dev/ttyUSB1'
BAUD_RATE = 9600

# Open serial port
ser = serial.Serial(PORT, BAUD_RATE)

# Create API object
xbee = XBee(ser,escaped=True)
import pprint
pprint.pprint(xbee.api_commands)

#DEST_ADDR_LONG = "\x00\x13\xA2\x00\x40\x9A\x1B\xB8"
DEST_ADDR_LONG = "\x00\x13\xA2\x00\x40\xC5\x5A\x84"
#DEST_ADDR_LONG = "\x00\x13\xA2\x00\x40\xC5\x5B\x05"

# Continuously read and print packets
while True:
    try:
        print "send data"
        xbee.tx_long_addr(frame='0x1', dest_addr=DEST_ADDR_LONG, data='AB')
        time.sleep(1)
    except KeyboardInterrupt:
        break

ser.close()
