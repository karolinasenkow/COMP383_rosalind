# import necessary tools from BioPython
from Bio import SeqIO
from Bio.SeqUtils import GC

#create list that will parce text file in fasta format (list of each sequence record)
list = list(SeqIO.parse('GC.txt', 'fasta')) # list of SeqRecords

# create outfile to write answer to
outfile = open("GC_outfile.txt",'w')

# create empty dictionary which will contain rosalind_id : sequence
id_to_seq = dict()

# loop through length of list and append id and GC content to dictionary
for i in range(0, len(list)):
    id_to_seq[list[i].id] = GC(list[i].seq)

# find maximum of values in dictionary (highest GC content)
id_max = max(id_to_seq, key=id_to_seq.get)

# write answer to outfile in format: rosalind_id \n gc_content
outfile.write(str(id_max))
outfile.write('\n')
outfile.write(str(id_to_seq[id_max]))


