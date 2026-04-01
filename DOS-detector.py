import os
import sys
import time
from collections import defaultdict
from scapy.all import sniff, IP

#small scale DOS detection simulator
THRESHOLD = 50 #acceptable packets from single source

def packet_callback(packet):
    src_ip = packet[IP].src
    packet_count[src_ip] += 1 #increment packet count for src_ip
    curr_time = time.time()
    interval = curr_time - start_time[0]

    if interval >= 1: #per second
        for ip, count in packet_count.items():
            packet_rate = count / interval #calculate packets per second

            if packet_rate > THRESHOLD and ip not in blocked_list: #check if ip already blocked, block if not in list already
                print("Blocking IP address: ", ip, "with packet rate: ", packet_rate, "\n")
                os.system(f"iptables -A INPUT -s {ip} -j DROP")
                blocked_list.add(ip) #add to the set for blocked addresses

            packet_count.clear()
            start_time[0] = curr_time

        
    if __name__ == "__main__":
        if os.geteuid() != 0:
            print("Root privileges required to run this script")
            sys.exit(1)

        packet_count = defaultdict(int)
        start_time = [time.time()] #list containing start time as first element
        blocked_list = set()

        print("Starting DOS detection\n", "Threshold:", THRESHOLD,"\n")
        sniff(filter="ip", prn=packet_callback) #start packet sniffing with callback function