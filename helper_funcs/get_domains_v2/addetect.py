import numpy as np
import dns
from dns import reversename, resolver
# import dns.reversename

# result = dns.reversename.from_address('64.68.90.1')
# print(result)
# print(dns.reversename.to_address(result))

# result = dns.resolver.query('02-com.preview-domain.com', 'A')
# for ipval in result:
#    print('IP', ipval.to_text())


def lookup_domain(ip_addr):
	name = reversename.from_address(ip_addr)
	domain = str(resolver.query(name,"PTR")[0]).strip('.')

def is_advertisment(ip_addr): 
	domains = np.load("domains.npy")
	domain = lookup_domain(ip_addr)
	return_val = True if (domain in domains) else False
	return return_val 

''' SOCKET IMPLEMENTATION

import socket

reversed_dns = socket.gethostbyaddr('203.208.60.1')
# ('crawl-203-208-60-1.googlebot.com', ['1.60.208.203.in-addr.arpa'], ['203.208.60.1'])
print(reversed_dns[0])
# 'crawl-203-208-60-1.googlebot.com'

'''