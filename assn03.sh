#! /bin/bash

# assn03-1
#for i in {808..8008}
#do
	#echo TR-$i
#done


# assn03-2 
# nano .bash_profile
# alias ll='ls -al'
# alias c='clear'
# source ~/.bash_profile


# assn03-3
# ls | grep -c \.fasta
# find . -name "*.fasta" | wc -l
# 15085


# assn03-4
# ls | grep -c \.tre
# find . -name "*.tre" | wc -l
# 14640


# assn03-5
# ls | grep -c \.sched
# find . -name "*.sched" | wc -l
# 15262


# assn03-6
# 445

#counter = 0
#for f in *.fasta
#do
	#fn1 = ${f:0:19}
	#fn2 = "${fn1}_raxml.tre"
	#lines = $(find . -type f -name $fn2 | wc -l)
		#if [ $lines -eq 0 ]
		#then
			#echo "No .tre file for $fn1 .fasta file"
			#counter = $((counter + 1))
		#fi 
#done
#echo "$counter fasta files lack a corresponding tre file"


# assn03-7

#find . -name "*.sched" | grep .sched > sched.txt
#counter = 0
#for i in sched.txt
#do
	#less -S $i
	#if [ -e "Program Return Code: 0" ]
	#then
		#echo "Job finished successfully"
		#counter = $(counter +1)
	#else
		#continue
	#fi
#done
#echo "$counter successful jobs"


