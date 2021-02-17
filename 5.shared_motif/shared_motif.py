# import necessary tools from BioPython
from Bio import SeqIO

# create list that will parce text file in fasta format (list of each sequence record)
file = list(SeqIO.parse('input.txt', 'fasta'))

# create outfile to write answer to
outfile = open("shared_motif_outfile.txt",'w')

def LCS(file):
    # create list of sequences
    sequences = []
    for i in file:
        sequences.append(str(i.seq))

    # create list where all shared substrings will be added
    common = list()

    for i in range(len(sequences[0])): # loop through length of first item
        for j in range(i + 1, len(sequences[0]) + 1): # loop through each index
            combos = sequences[0][i:j] # set all substring combinations = combos

            for k in range(1, len(sequences)): # loop through rest of sequences (not sequences[0])
                if combos in (sequences[k]): # if substring combo found in this sequence
                    common.append(combos)    # append to list common

    # create set containing any substrings in list common that are repeated the amount of times there are
    # sequences - 1 (because excluding sequence[0])
    common_set = set([i for i in common if common.count(i) == len(sequences) - 1])

    # return longest substring using max length
    outfile.write(max(common_set,key=len))

print(LCS(file))
