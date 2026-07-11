from scapy.all import wrpcap

def save_packets(packets):
    if packets:
        wrpcap("capture.pcap", packets)
        print(f"\nSaved {len(packets)} packets to capture.pcap")
    else:
        print("No packets captured.")