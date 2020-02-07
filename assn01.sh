#! /bin/bash

# assn01-1
cd
find . -name “nad*”

# assn01-2
top
# 2.6% of CPU being used by top command
# PhysMem: 8109M used (1801M wired), 83M unused

# assn01-3
cd ~/Desktop/watermelon_files
less -S watermelon.gff
grep misc_feature watermelon.gff | sort -k7gr | less -S > IR_regions.gff
less -S IR_regions.gff

# assn01-4
cd ~/Desktop/watermelon_files
grep -c misc_feature watermelon.gff
grep -cv misc_feature watermelon.gff
# There are more chloroplast fragments outside the IR (107) compared to inside the IR (37).

# assn01-5
cd ~/Desktop/watermelon_files
grep -v GAATTC genes.fsa | grep -B 1 GGATCC

# assn01-6
cd ~/Desktop/example_files
head -n 1001 shaver_etal.csv | tail -n 501

# assn01-7
cd ~/Desktop/example_files
column -t fruit.txt | sort -k2r,2 -k3,3 < fruit.txt
