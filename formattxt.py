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
	if (line[0] == "!"):
		continue
	else:
		domain=line.strip("|^\n")
		outfile.write(domain)
		outfile.write("\n")
		
infile.close()
outfile.close()
