#!/usr/bin/env python3

import nmap
import sys

class Network_enumeration():
	def __init__(self):
		def_gateway = input("Enter IPv4 default gateway in decimal notation: ")
		snet = input("Enter the subnet mask in CIDR notation: ")

		self.def_gateway = def_gateway
		self.snet = snet 

	def host_discovery(self):
		""" Returns available hosts given a default gateway and subnet mask in CIDR notation.
		Makes use of nmap's 'sn' option.
		'sn' option: 'tells Nmap not to do a port scan after host discovery, and only print /n
		out the available hosts that responded to the scan.' """
		
		# Ensuring user cannot enter a defualt gateway that is not the length of an IPv4 address in decimal notaion
		# Ensuring user cannot enter a subnet mask that is not in CIDR notation without 
		if self.def_gateway != len () or self.snet == len(3):
			print("# Enter a correct default gateway!")
			print("# Gracefully exiting...")
			sys.exit()
		
		network = self.def_gateway + self.snet
		print("# Scanning network for available hosts...")
		
		# nmap object 
		nm = nmap.PortScanner()
		# scanning network for hosts "sn" argument is the nmap option used to perform a scan 
		nm.scan(hosts=network, arguments="sn") 
		# using list comprehension to output available hosts on the network
		available_hosts = [(host, nm[host]["status"]["state"]) for host in nm.all_hosts()]

		for host, status in available_hosts:
			print(f"Hosts\t{host}")	

if __name__ == "__main__":
	scan = Network_enumeration()
	scan.host_discovery
	


