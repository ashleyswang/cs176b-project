'''
import numpy as np
import dns
from dns import resolver
'''
# import dns.reversename

# result = dns.reversename.from_address('64.68.90.1')
# print(result)
# print(dns.reversename.to_address(result))

# result = dns.resolver.query('02-com.preview-domain.com', 'A')
# for ipval in result:
#    print('IP', ipval.to_text())

infile = open("domains.txt", "r")
domains = set()
domain_list = infile.readlines()


''' SAVE TO NUMPY ARRAY
for d in domain_list: 
	try:
		result = resolver.query(d, 'A')
		for ipval in result:
			domains.add(ipval.to_text())
	except:
		print("No results for", d)

np.save("ip_ads.npy", domains)
'''

outfile = open("/etc/dnsmasq.d/blacklist.conf", "w")
for d in domain_list:
    d_str = str(d).strip()
    str_add = "address=/"+d_str+"/127.0.0.1\n"
    outfile.write(str_add)

infile.close()
outfile.close()

