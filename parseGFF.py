# /usr/bin/env python3

# import modules
import argparse
import csv
from Bio import SeqIO

# create an argument parser object
parser = argparse.ArgumentParser(description = "This script parses a GFF file, extracts CDS features from a corresponding FASTA file, and calculates the GC content of the substrings")

# add positional arguments
parser.add_argument("gff", help = "Name of the GFF file")
parser.add_argument("fasta", help = "Name of the FASTA file")

# parse the arguments
args = parser.parse_args()

# read and parse the FASTA file
genome = SeqIO.read(args.fasta,'fasta')

gene_list = []

# open input file
with open(args.gff,'r') as gff_file:
	with open(args.fasta,'r') as fasta_file:
 
		# create a csv reader object
		reader = csv.reader(gff_file, delimiter="\t")

		for line in reader:
			# skip empty lines
			if not line:
				continue
				
			else:
				# test whether this is a CDS feature
				if (line[2]=="CDS"):
					start = int(line[3])
					end = int(line[4])
					gene_list.append(genome.seq[start:end])

# calculate and print the GC content of the substring to 2 decimal places
def get_gc_content(gene_list):   
    length = len(gene_list)
    g_count = gene_list.upper().count('G')
    c_count = gene_list.upper().count('C') 
    gc_content = (g_count + c_count) / length
    return round(gc_content, 2)


for i in gene_list:

	print("GC content of substring = " + str(get_gc_content(i)))
					
# close the files
gff_file.close()
fasta_file.close()