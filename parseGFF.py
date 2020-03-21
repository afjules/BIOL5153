# /usr/bin/env python3

# define the input file
infile = "watermelon.gff"

# open and parse watermelon.gff
with open(infile,'r') as watermelon:
	fields = [line.split() for line in watermelon]  # split into fields by spaces in file
	fields = (sorted(fields, key = lambda x: x[10]))

	for line in fields:

		if (line[10] == "similar"):   
			pass   # skip all 'similar to' entries
		else:
			genes = line[10]  # extract the gene name	
		print(genes)

