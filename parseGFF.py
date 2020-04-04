# /usr/bin/env python3

# import modules
import csv
import argparse

# create an argument parser object
parser = argparse.ArgumentParser(description = "This script parses a GFF file and opens a FASTA file")

# add positional arguments
parser.add_argument('filename', help='Enter the name of the GFF file')
parser.add_argument('filename2', help='Enter the name of the corresponding genome file')
args = parser.parse_args()

# initialize list for gene names
gene_list = []

# open input files
with open(args.filename) as gff:
	with open(args.filename2) as fasta:

		# read GFF file, line by line
		for line in gff:

			# create a csv reader object
			reader = csv.reader(gff, delimiter="\t")
	
			for line in reader:
				
				# split fields
				fields = line[8].split(";")

				# extract the first item from split fields
				gene_fields = fields[0].split("Gene ")
				genes_split = gene_fields[1].split()
				
				if (genes_split[0] == "similar"):   
					pass   # skip all 'similar to' entries
		
				else:
					gene_list.append(genes_split[0])  # store gene name
	
		# print genes in alphabetical order			
		for gene in sorted(gene_list):
			print(gene)

# close files
gff.close()
fasta.close()
