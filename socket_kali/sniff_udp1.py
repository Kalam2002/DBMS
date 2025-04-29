from scapy.all import sniff

def packet_callback(packet) :
    if packet.haslayer("UDP") :
        print(f"Captured UDP packet : {packet.summary()}")

sniff(filter="udp", prn=packet_callback, store=0)
