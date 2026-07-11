from scapy.all import IP, TCP, UDP, ICMP

def packet_callback(packet):
    print("-" * 60)

    if packet.haslayer(IP):
        ip = packet[IP]

        print(f"Source IP      : {ip.src}")
        print(f"Destination IP : {ip.dst}")
        print(f"Length         : {len(packet)} bytes")

        if packet.haslayer(TCP):
            tcp = packet[TCP]
            print("Protocol       : TCP")
            print(f"Source Port    : {tcp.sport}")
            print(f"Destination Port: {tcp.dport}")

        elif packet.haslayer(UDP):
            udp = packet[UDP]
            print("Protocol       : UDP")
            print(f"Source Port    : {udp.sport}")
            print(f"Destination Port: {udp.dport}")

        elif packet.haslayer(ICMP):
            print("Protocol       : ICMP")