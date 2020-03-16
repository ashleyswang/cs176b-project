#import numpy as np
#import dns
#from dns import resolver
import subprocess
import time
import socket

### IGNORE THIS ###
# import dns.reversename

# result = dns.reversename.from_address('64.68.90.1')
# print(result)
# print(dns.reversename.to_address(result))

# result = dns.resolver.query('02-com.preview-domain.com', 'A')
# for ipval in result:
#    print('IP', ipval.to_text())

# Reads domains and puts them into set
def get_ip():
	print("Getting list of IPs")
	infile = open("domains.txt", "r")
	domains = set()

	# domain_list is list of domains as string
	domain_list = infile.readlines()

	for d in domain_list: 
		try:
			print(d.strip())
			result = socket.getaddrinfo(d.strip(), 0, 0, 0, 0)
			for ipval in result:
				print("\t"+ipval[-1][0])
				domains.add(ipval[-1][0])
		except:
			print("No results for", d)

	print("IP List generated")
	return domains

# Domains is now a set of IP addresses
# Adding IP tables filter
def add_rules(domains):
	print("Adding rules")
	src_rule = 'iptables -I INPUT -s {} -j DROP'
	dst_rule = 'iptables -I INPUT -d {} -j DROP'

	for ip_addr in domains:
		subprocess.call(src_rule.format(ip_addr), shell=True)
		subprocess.call(dst_rule.format(ip_addr), shell=True)

	print("Finish adding rules")

def flush_rules(): 
	subprocess.call("iptables -F", shell=True)

	print("Flushing rules")

# Allow to save set as numpy set and use for other programs
# np.save("ip_ads.npy", domains)

if __name__ == '__main__':
	try: 
		while(1):
			# flush existing rules of iptable
			flush_rules()
			# stop dnsmasq for nslookup
			print("Stopping DNS server temporarily")
			subprocess.call("service dnsmasq stop", shell=True)
			print("DNS Server stopped")
			# get list of ips
			domain_ips = get_ip()
			# add rules to iptable
			add_rules(domain_ips)
			# start up dnsmask
			print("Starting DNS server")
			subprocess.call("service dnsmasq start", shell=True)
			subprocess.call("service dnsmasq status", shell=True)
			# sleep until next day
			time.sleep(86400)
	except KeyboardInterrupt: 
		flush_rules()
		exit(1)
