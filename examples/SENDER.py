
#! /usr/bin/python

import time
from datetime import datetime
import serial
from xbee import XBee, ZigBee

PORT = '/dev/ttyUSB0'
BAUD_RATE = 9600

# Open serial port and enable flow control
ser = serial.Serial(PORT, BAUD_RATE, bytesize=8, parity='N', stopbits=1, timeout=None, xonxoff=1, rtscts=1, dsrdtr=1)

# Create API object
xbee = ZigBee(ser,escaped=True)

#DEST_ADDR_LONG = "\x00\x13\xA2\x00\x40\x9C\x91\xA5"
#DEST_ADDR_LONG = "\x00\x13\xA2\x00\x40\xC5\x5A\x84"
# Router
DEST_ADDR_LONG = "\x00\x13\xA2\x00\x40\xC5\x5B\x05"

#part to discovery shot 16-bit address
xbee.send("tx",data="000\n",dest_addr_long=DEST_ADDR_LONG,dest_addr="\xff\xfe")
response = xbee.wait_read_frame()
shot_addr = response["dest_addr"]
# Continuously read and print packets
while True:
    try:
        print "send data"
    	tstart = datetime.now()
        xbee.send("tx",data="321\n",dest_addr_long=DEST_ADDR_LONG,dest_addr=shot_addr)
        xbee.send("tx",data="322\n",dest_addr_long=DEST_ADDR_LONG,dest_addr=shot_addr)
        xbee.send("tx",data="323\n",dest_addr_long=DEST_ADDR_LONG,dest_addr=shot_addr)
        xbee.send("tx",data="324\n",dest_addr_long=DEST_ADDR_LONG,dest_addr=shot_addr)
        xbee.send("tx",data="325\n",dest_addr_long=DEST_ADDR_LONG,dest_addr=shot_addr)
    	tend = datetime.now()
    	print tend - tstart
    	time.sleep(1)
    except KeyboardInterrupt:
        break
       
ser.close()
