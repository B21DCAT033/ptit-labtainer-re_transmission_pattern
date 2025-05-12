#!/usr/bin/env python3
import scapy.all as scapy
from imodule import extract_rto_steg

def main():
    pkts = scapy.rdpcap('retransmission.pcap')
    msg = extract_rto_steg(pkts)
    assert msg == 'STEGO', 'RTO-based extraction failed'
    print('check0 passed')

if __name__ == '__main__':
    main()
