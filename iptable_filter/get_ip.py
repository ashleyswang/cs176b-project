import socket

print("Getting list of IPs")
infile = open("domains.txt", "r")
domains = set()

# domain_list is list of domains as string
domain_list = infile.readlines()

for d in domain_list:
    print(d.strip())
    result = socket.getaddrinfo(d.strip(), 0, 0, 0, 0)
    '''
    for ipval in result:
        print("\t"+ipval[-1][0])
        domains.add(ipval[-1][0])
    '''
# print(domains)


