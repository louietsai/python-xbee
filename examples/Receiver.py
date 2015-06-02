#import config
import serial
import time
from xbee import ZigBee

def toHex(s):
    lst = []
    for ch in s:
        hv = hex(ord(ch)).replace('0x', '')
        if len(hv) == 1:
            hv = '0'+hv
        hv = '0x' + hv
        lst.append(hv)

def decodeReceivedFrame(data):
            source_addr_long = toHex(data['source_addr_long'])
            source_addr = toHex(data['source_addr'])
            id = data['id']
            #samples = data['samples']
	    #samples = ''
            options = toHex(data['options'])
            return [source_addr_long, source_addr, id]

PORT = '/dev/ttyUSB1'
BAUD_RATE = 9600

# Open serial port
ser = serial.Serial(PORT, BAUD_RATE)

zb = ZigBee(ser, escaped = True)

while True:
	data = zb.wait_read_frame()
        decodedData = decodeReceivedFrame(data)
	print decodedData
