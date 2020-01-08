from scapy.all import *

flag = ""

packets = rdpcap('capture.pcap')
for packet in packets:
    if UDP in packet and packet[UDP].dport == 22:
        print(f"packet[UDP].sport={packet[UDP].sport}")
        flag += chr(packet[UDP].sport - 5000)
print(flag)