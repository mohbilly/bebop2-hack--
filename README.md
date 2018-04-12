# Bebop2-hack
Research project conducted on the open source drone model name: Bebop 2

# Requirements and packages
- Python 2.7-3.xx
- Wireshark
- Linux OS 
- [Bebop Drone 2](https://www.amazon.com/Parrot-Quadcopter-Flight-Inclusive-Battery/dp/B01BW0Q4F6/ref=sr_1_1_sspa?ie=UTF8&qid=1523479368&sr=8-1-spons&keywords=Bebop+drone+2&psc=1)

**Linux Controller**
- [ARSDK3](https://github.com/Parrot-Developers/ARSDK3)
- netifaces
- zeroconf
- tkinter
- [libARNetwork](https://github.com/Parrot-Developers/libARNetwork)
- [libARCommands](https://github.com/Parrot-Developers/libARCommands)

**Attacks**
- Kali linux
- Aircrack-ng suite
- [Wirless adapter (2.4/5 GHZ)](https://www.amazon.com/Alfa-AWUS036NH-802-11g-Wireless-Long-Range/dp/B003YIFHJY/ref=sr_1_1_sspa?ie=UTF8&qid=1523479203&sr=8-1-spons&keywords=alfa+wireless+network+adapter&psc=1&smid=A2LM6ZPY06LT1N)
- Python scapy

**Mitigations**
- Macspoof

# Vulnerabilites
- FTP port open
- Telnet port open
- ARSDK protocol based on UDP (no sequence check)
- Use of ARP
- No password required by default

# Attacks
- ARP MITM attack
- Deauth frames flood attack
  Utilizing aircrak-ng tool, send de-authenticaion to kick victim off network
- Packet injection
  - Captured takeoff, landing, emergency packets between drone and controller
  - Inspected and disected packet payload
  - From [Developer pdf](https://developer.parrot.com/docs/bebop/ARSDK_Protocols.pdf)
    Page 12 --> show casing payload payload frame Datatype/Target Buffer ID/Sequence number/Total fram size/Actual data
    Actual data --> contains the actuall command weather it's takeoff,land,emergency land
    Page 13 --> specified that "The ARNetwork library will ignore out of order and duplicate data, but will still send Acks       for them if requested. If the back-gap in sequence number is too high"he frame is not considered out of order, and
    instead is accepted as the new reference sequence number.**I utilized this to forge a packet starting with a large seq num**
    
- EvilTwin

# Mitigations
- Channel hopping
- MAC address spoofing
- Use strong passwords
- close FTP port
- close telnet port --> If needed, use SSh


