# 🔍 TCP Port Scanner (v1.0)

A lightweight Python-based TCP port scanner that allows users to scan a target host using either a random set of ports or a list of commonly used service ports. Built as part of a hands-on cybersecurity learning journey, this tool is designed for clarity, extendability, and real-world relevance.

---

## 🚀 Features

- Hostname or IP input with DNS resolution
- Random 100-port scan or common port scan (user selectable)
- Open port detection using TCP (AF_INET + SOCK_STREAM)
- Inferred service mapping (e.g., SSH, HTTP, RDP)
- Built-in timer for benchmarking scan duration
- Clean, informative output
- Graceful handling of:
  - Invalid input
  - Ctrl + C (KeyboardInterrupt)
  - Ctrl + Z / EOF (EOFError)
  - Network errors (socket.error, OSError)

---

## 🛠️ Installation

1. Clone the repo:
   ```bash
   git clone https://github.com/your-username/tcp-scanner.git
   cd tcp-scanner
Run the script:

bash
Copy code
python tcp_scanner.py
✅ Python 3.7+ recommended (no external packages required)

💻 Example Usage
java
Copy code
Enter IP address or hostname to scan: scanme.nmap.org

Choose scan mode:
1 - Random 100 ports
2 - Common ports (well-known services)
Enter scan mode (1 or 2): 2

Port 22 is OPEN (SSH)
Port 80 is OPEN (HTTP)

Scan completed in: 0:00:02.304201
🔄 Planned Features (Future Versions)
Version	Feature
v1.1	User-defined port ranges
v1.2	IPv6 support (AF_INET6)
v1.3	Multi-threaded scanning
v1.4	UDP scanner support
v1.5	Banner grabbing / service detection
v1.6	CLI arguments with argparse
v1.7	Save results to file (log or CSV)

📁 Project Structure
bash
Copy code
/tcp-scanner
│
├── tcp_scanner.py       # Main scanner script
├── README.md            # You are here
└── /logs/               # Session notes, dev logs (optional)
⚠️ Legal Note
This tool is intended for educational and authorized testing purposes only.
Always obtain permission before scanning any network you do not own.

📚 Author & Background
This project is part of a structured cybersecurity journey led by a former U.S. Naval Academy computer science graduate. It blends tool building, system hardening, and creative exploration — including an evolving character-based design framework inspired by Layla Lunara (Star Wars universe).