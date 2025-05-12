#!/usr/bin/env python3
import scapy.all as scapy
from imodule import detect_rsteg

def main():
    pkts = scapy.rdpcap('retransmission.pcap')
    score = detect_rsteg(pkts)
    assert score < 0.07, 'Retransmission rate too high, potential RSTEG detected'
    print('check3 passed')

if __name__ == '__main__':
    main()
