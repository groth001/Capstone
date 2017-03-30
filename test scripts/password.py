#!/usr/bin/python
# ======================================================================
#
# password.py
#
# This script tests to see if the Click C0-10DD1E-D PLC will
# accept a password without the legitimate programming software.
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
dstIP = '192.168.0.101'
dstport = 25425 # destination port

# Password packet with password set to "password"
password = binascii.unhexlify("4b4f50001600e73913004d01470010000b0b020070617373776f726400")

# Bind socket
sock.bind((srcIP, srcPort))

# Send password packet and check result
sock.sendto(password, (dstIP, dstPort))
