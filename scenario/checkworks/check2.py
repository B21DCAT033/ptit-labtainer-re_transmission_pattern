#!/usr/bin/env python3
import scapy.all as scapy
from imodule import extract_sack_steg

def main():
    pkts = scapy.rdpcap('retransmission.pcap')
    msg = extract_sack_steg(pkts)
    assert msg == 'SELECT', 'SACK-based extraction failed'
    print('check2 passed')

if __name__ == '__main__':
    main()
