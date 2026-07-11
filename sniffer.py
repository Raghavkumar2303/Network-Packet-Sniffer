
from scapy.all import sniff
from parser import packet_callback
from save_pcap import save_packets

captured_packets = []

def capture(packet):
    captured_packets.append(packet)
    packet_callback(packet)

def start_sniffer():
    print("Starting Packet Sniffer...")
    print("Press Ctrl+C to stop.\n")

    try:
        sniff(prn=capture, store=False)
    except KeyboardInterrupt:
        print("\nStopping capture...")
        save_packets(captured_packets)