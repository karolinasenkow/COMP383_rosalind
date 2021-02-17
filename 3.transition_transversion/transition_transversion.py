# import necessary tools from BioPython
from Bio import SeqIO

#create list that will parce text file in fasta format (list of each sequence record)
sequences = list(SeqIO.parse('dna_strings.txt', 'fasta')) # list of SeqRecords

# create outfile to write answer to
outfile = open("trans_outfile.txt",'w')

# create each sequence as seperate string
string_1 = str(sequences[0].seq)
string_2 = str(sequences[1].seq)

# set initial number of transitions and transversions to 0
transition = 0
transversion = 0

# loop through length of string_1 (both strings have same lengths)
# if there is difference in nucleotides at that position between strings, and if it is a transition, +=1
# if the difference between nucleotides is a transversion, add 1 to transversion variable
for i in range(len(string_1)):
    if (string_1[i] == 'C' and string_2[i] == 'T') or (string_1[i] == 'T' and string_2[i] == 'C'):
        transition += 1
    if (string_1[i] == 'A' and string_2[i] == 'G') or (string_1[i] == 'G' and string_2[i] == 'A'):
        transition += 1
    if (string_1[i] == 'G' and string_2[i] == 'T') or (string_1[i] == 'T' and string_2[i] == 'G'):
        transversion += 1
    if (string_1[i] == 'A' and string_2[i] == 'C') or (string_1[i] == 'C' and string_2[i] == 'A'):
        transversion += 1
    if (string_1[i] == 'A' and string_2[i] == 'T') or (string_1[i] == 'T' and string_2[i] == 'A'):
        transversion += 1
    if (string_1[i] == 'C' and string_2[i] == 'G') or (string_1[i] == 'G' and string_2[i] == 'C'):
        transversion += 1

# calculate the ratio by dividing transition by transversion
ratio = transition/transversion

# write answer to outfile
outfile.write(str(ratio))
