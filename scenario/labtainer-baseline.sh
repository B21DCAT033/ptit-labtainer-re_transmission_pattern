#!/bin/bash
# Start TCP dump
tcpdump -w retransmission.pcap &
# Launch interactive prompt
/bin/bash
