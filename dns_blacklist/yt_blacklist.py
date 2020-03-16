infile = open("black.list", "r")
outfile = open("blacklist2.conf", "w")

for line in infile.readlines():
	if (line[0:7] == "r1---sn"):
		domain = line[8:].strip("-\n")
		addr_str = "address=/"+domain+"/127.0.0.1\n"
		outfile.write(addr_str)