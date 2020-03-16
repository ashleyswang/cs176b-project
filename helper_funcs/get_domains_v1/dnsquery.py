import numpy as np
import dns
from dns import resolver
import subprocess

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
	infile = open("domains.txt", "r")
	domains = set()

	# domain_list is list of domains as string
	domain_list = infile.readlines()

	for d in domain_list: 
		try:
			result = resolver.query(d, 'A')
			for ipval in result:
				domains.add(ipval.to_text())
		except:
			print("No results for", d)

	return domains

# Domains is now a set of IP addresses
# Adding IP tables filter
def add_rules(domains):
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
