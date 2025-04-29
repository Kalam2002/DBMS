from scapy.all import sniff, TCP, IP

def packet_callback(pkt) :
    if pkt.haslayer(TCP) and pkt[TCP].dport == 9999 :
        print(f"captured : {pkt[IP].src} : {pkt[TCP].sport} > {pkt[IP].dst} : {pkt[TCP].dport}")
        print(f"SEQ : {pkt[TCP].seq} | ACK : {pkt[TCP].ack}")

sniff(filter="tcp port 9999", prn=packet_callback, store=0)
