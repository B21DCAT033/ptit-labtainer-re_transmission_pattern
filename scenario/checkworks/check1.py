#!/usr/bin/env python3
import scapy.all as scapy
from imodule import extract_frr_steg

def main():
    pkts = scapy.rdpcap('retransmission.pcap')
    msg = extract_frr_steg(pkts)
    assert msg == 'FRAME', 'FR/R-based extraction failed'
    print('check1 passed')

if __name__ == '__main__':
    main()
