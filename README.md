# Network-Packet-Sniffer
“A high-performance Python network analysis tool utilizing Scapy to intercept, deep-parse, and audit live packet traffic for security vulnerabilities and unencrypted data leaks.”


# Network Packet Sniffer & Intrusion Detection System

A high-performance Python-based network analysis tool designed to intercept, parse, and analyze live network traffic. This utility proactively flags unencrypted sensitive data and identifies potential security anomalies in real-time.

## 🚀 Key Features
- **Live Traffic Interception:** Captures real-time Wi-Fi and Ethernet data packets.
- **Protocol Deep Parsing:** Extracts structural details from IP, TCP, UDP, and HTTP layers.
- **Security Flagging:** Auto-detects plain-text credentials and flags common vulnerability signatures.
- **Modular Design:** Built for seamless integration with downstream machine learning data pipelines.

## 🛠️ Tech Stack & Libraries
- **Language:** Python 3.10+
- **Core Library:** [Scapy](https://scapy.net) (for packet manipulation and sniffing)
- **Data Structuring:** Logging / Native OS modules

## 📦 Installation & Setup

1. **Clone the Repository:**
```bash
git clone https://github.com
cd network-packet-sniffer
```

2. **Install Dependencies:**
```bash
pip install scapy
```

3. **Run the Application:**
*Note: Root/Administrator privileges are required to interface with network hardware.*
```bash
# On Linux/macOS
sudo python sniffer.py

# On Windows (Run Command Prompt as Administrator)
python sniffer.py
```

## 📊 Usage Demonstration
```text
[+] Packet Captured: TCP | Source: 192.168.1.5 -> Dest: 93.184.216.34
[!] ALERT: Unencrypted HTTP traffic detected on Port 80.
[!] WARNING: Potential plain-text payload signature identified.
```

<img width="1920" height="1087" alt="Network Analysis and Protocols" src="https://github.com/user-attachments/assets/d0e81e48-a8c1-47f3-8c90-575192b2e262"/>
<img width="1920" height="1114" alt="Destinations and Lenghts" src="https://github.com/user-attachments/assets/f3aa6a61-c5ee-4d7b-ab00-e952fb4e9480"/>


## 📝 Future Roadmap
- Integrate an **AI-driven Threat Detection model** to classify advanced network anomalies using the `NSL-KDD` dataset.
- Develop a lightweight web dashboard using `Streamlit` for visual real-time traffic mapping.
