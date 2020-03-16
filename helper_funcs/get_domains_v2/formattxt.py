import numpy as np
import sys

def format_txt(infile_name, outfile_name):

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

def format_npy(infile_name, outfile_name):
	infile = open(infile_name, "r")
	domains = set(infile.readlines())
			
	infile.close()
	np.save(outfile_name, domains)



if (len(sys.argv) != 4):
	print ("USAGE: formattxt.py <EXPORT_FORMAT> <INFILE> <OUTFILE>")
	sys.exit()
else:
	infile_name = sys.argv[2]
	outfile_name = sys.argv[3]
	if (sys.argv[1] == 'txt'):
		format_txt(infile_name, outfile_name)
	elif (sys.argv[1] == 'npy'):
		format_npy(infile_name, outfile_name)
	else: 
		print("USAGE: EXPORT_FORMAT = npy | txt")
