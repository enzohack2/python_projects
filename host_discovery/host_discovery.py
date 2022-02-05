#!/usr/bin/env python3

import nmap
import sys

class NETWORK_ENUMERATION():
		def __init__(self):
			dgate = input("Enter IPv4 default gateway in decimal notation: ")
			subnet = int(input("Enter the subnet mask in CIDR notation: /"))
			self.dgate = dgate
			self.subnet = subnet 


		def host_discovery(self):
			""" Prints to stdout hosts on a network given a default gateway IPv4 adddress and subnet mask in CIDR notation.
			Makes use of nmap's 'sn' option.
			'sn' option: 'tells Nmap not to do a port scan after host discovery, and only print /n
			out the available hosts that responded to the scan.' """
			
			# Ensuring user cannot enter a defualt gateway that is longer than the max length of an IPv4 address in decimal notaion, 15 characters.
			# Ensuring user cannot enter a subnet mask that is greater than the value /32.
			if len(self.dgate) > 15 or self.subnet >= 32:
				print("# Enter a correct default gateway!")
				print("# Subnet mask cannot exceed 31 bits!")
				print("# Gracefully exiting...")
				sys.exit(0)
			else: 
				# typecast subnet mask into str as you can't concetante type int
				network = self.dgate + "/" + str(self.subnet)
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
	scan = NETWORK_ENUMERATION()
	scan.host_discovery()
