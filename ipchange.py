import socket
import binascii
import struct
import time
import sys
import random

sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

ip = "255.255.255.255"
port = 25425

sock.bind(('192.168.0.20', random.randint(40000, 50000)))
sock.setsockopt(socket.SOL_SOCKET, socket.SO_BROADCAST, 1)


setup = binascii.unhexlify("4b4f50000a00d9f20e0045016683c0a8006d00d07c120e4d")
                           # Command?                           old IP
                           # 4b4f50000a00 fc53 0e0045016683   c0a8006b   00d07c120e4d

change_ip = binascii.unhexlify("4b4f5000100038ff1d0045016682000100c0a8006dc0a80065ffffff00c0a800f400d07c120e4d")
                              # Command?                              old IP    new IP  subnetmask gateway
                              # 4b4f50001000 8192 1d0045016682000100 c0a8006b c0a8006c  ffffff00  c0a800f4 00d07c120e4d
sock.sendto(setup, ('<broadcast>', port))
time.sleep(5)

sock.sendto(change_ip, ('<broadcast>', port))

# PLC response after setup packet success
# 4b4f50000a001d280700450166c2100000

# PLC response after setup packet failure
# 4b4f50000a001f6105004501668315

# PLC response after change ip packet success
#4b4f50001000 763c 0500450166 c310
#4b4f50001000 763c 0500450166 c310
#4b4f50001000 763c 0500450166 c310

# PLC response after change ip packet failure
#4b4f50001000 2e52 0500450166 8215



