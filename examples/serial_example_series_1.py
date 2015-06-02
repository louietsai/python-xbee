#! /usr/bin/python

from xbee import XBee, ZigBee
import serial

"""
serial_example.py
By Paul Malmsten, 2010

Demonstrates reading the low-order address bits from an XBee Series 1
device over a serial port (USB) in API-mode.
"""

def main():
    """
    Sends an API AT command to read the lower-order address bits from 
    an XBee Series 1 and looks for a response
    """
    try:
        
        # Open serial port
        ser0 = serial.Serial('/dev/ttyUSB0', 9600)
        ser1 = serial.Serial('/dev/ttyUSB1', 9600)
        
        # Create XBee Series 1 object
        #xbee = XBee(ser)
	xbee = ZigBee(ser1, escaped=True)
        
        
        # Send AT packet
        xbee.send('at', frame_id='A', command='DH')
        
        # Wait for response
        response = xbee.wait_read_frame()
        print response
        
        # Send AT packet
        xbee.send('at', frame_id='B', command='DL')
        
        # Wait for response
        response = xbee.wait_read_frame()
        print response
        
        # Send AT packet
        xbee.send('at', frame_id='C', command='MY')
        
        # Wait for response
        response = xbee.wait_read_frame()
        print response
        
        # Send AT packet
        xbee.send('at', frame_id='D', command='CE')
        
        # Wait for response
        response = xbee.wait_read_frame()
        print response
    except KeyboardInterrupt:
        pass
    finally:
        ser0.close()
        ser1.close()
    
if __name__ == '__main__':
    main()
