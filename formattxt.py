import sys

if (len(sys.argv) != 3):
	print ("USAGE", len(sys.argv))
	sys.exit()

infile_name = sys.argv[1]
outfile_name = sys.argv[2]
infile = open(infile_name, "r")
outfile = open(outfile_name, "w")

domain_names = infile.readlines()

for line in domain_names:
	if (line[0] == "#"):
		continue
	elif (line[:2] == "::"):
		continue
	else:
		domain=line.split(" ")[1]
		outfile.write(domain)
		
infile.close()
outfile.close()
