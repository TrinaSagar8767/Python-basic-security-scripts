import sys
import time
from scapy.all import Ether, IP, TCP, sendp

TARGET = "192.0.2.0" #dummy IP, replace with VM
INTERFACE = "eth0" #dummy interface, replace with VM
NUM_PACKETS = 100
DURATION = 10

def send_pkt(target_ip, interface, num_packets, duration):
    pkt = Ether() / IP(dst=target_ip) / TCP()
    end_time = time.time() + duration
    pkt_count = 0

    while time.time() < end_time and pkt_count < num_packets:
        sendp(pkt, iface = interface, verbose=False)
        pkt_count += 1

if __name__ == "__main__":
    if sys.version_info[0] < 3:
        print("Python 3 required to run script")
        sys.exit(1)

    send_pkt(TARGET, INTERFACE, NUM_PACKETS, DURATION)
