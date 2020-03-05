filename2 = "dna_mixed.txt"
infile2 = open(filename2, "r")
dna_sequence2 = infile2.read().rstrip("\n")
infile2.close()
print(dna_sequence2)
length = len(dna_sequence2)
# print(length)
perc_A = (dna_sequence2.count('A')/length)*100
print("Percent A: " ,end="")
print(round(perc_A,2))
perc_C = (dna_sequence2.count('C')/length)*100
print("Percent C: " ,end="")
print(round(perc_C,2))
perc_T = (dna_sequence2.count('T')/length)*100
print("Percent T: " ,end="")
print(round(perc_T,2))
perc_G = (dna_sequence2.count('G')/length)*100
print("Percent G: " ,end="")
print(round(perc_G,2))
perc_a = (dna_sequence2.count('a')/length)*100
print("Percent a: " ,end="")
print(round(perc_a,2))
perc_c = (dna_sequence2.count('c')/length)*100
print("Percent c: " ,end="")
print(round(perc_c,2))
perc_t = (dna_sequence2.count('t')/length)*100
print("Percent t: " ,end="")
print(round(perc_t,2))
perc_g = (dna_sequence2.count('g')/length)*100
print("Percent g: " ,end="")
print(round(perc_g,2))
