#! /usr/bin/python

from xbee import XBee, ZigBee
import serial
import time
import sys, getopt

ser = serial.Serial('/dev/ttyUSB1', 9600)
xbee = ZigBee(ser)
#xbee = XBee(ser)
position = 'n'
timeout = 1
def doCommand():
	#destinationAddrLong = b'\x00\x13\xA2\x00\x40\xBA\xF5\xE8'
	destinationAddrLong = b'\x00\x13\xA2\x00\x40\xC5\x5A\x84'
	timeout = 0.05
	print 'position is %c' % position
	xbee.tx_long_addr(dest_addr=destinationAddrLong, data=position)

	print xbee.wait_read_frame()
	time.sleep(timeout)          
	return


def main(argv):
   global position
   try:
      opts, args = getopt.getopt(argv, "hp:", ["position="])
   except getopt.GetoptError:
      print 'sendData.py -p <position - one of n, w, s>'
      sys.exit(2)
   for opt, arg in opts:
      if opt == '-h':
         print 'sendData.py -p <position - one of n, w, s>'
         sys.exit()
      elif opt in ("-p", "--position"):
         position = arg
      print "argument is ", arg
      print "POS is ", position
         
   doCommand()
   ser.close()

if __name__ == "__main__":
   main(sys.argv[1:])

