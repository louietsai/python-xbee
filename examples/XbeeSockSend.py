# 
# This example sends "Hello, World!" using the Digi
# proprietary mesh transport to a fixed node address.
# 
 
 
# include the sockets module into the namespace:
import xbee
from socket import * 
 
 
# The Format of the tuple is:
# (address_string, endpoint, profile_id, cluster_id)
# 
# The values for the endpoint, profile_id, and
# cluster_id given below are the values used to write
# to the serial port on an Ember-based XBee module.
# For 802.15.4 use 0,0,0
DESTINATION=("00:0d:6f:00:00:06:89:29!", \
            0xe8, 0xc105, 0x11) 
 
# Create the socket, datagram mode, proprietary transport:
sd = socket(AF_XBEE, SOCK_DGRAM, XBS_PROT_TRANSPORT) 
 
 
# Bind to endpoint 0xe8 (232) for ZB/DigiMesh, but 0x00 for 802.15.4
sd.bind(("", 0xe8, 0, 0)) 
 
 
# Send "Hello, World!" to the destination node, endpoint,
# using the profile_id and cluster_id specified in
# DESTINATION: 
sd.sendto("Hello, World!", 0, DESTINATION)
