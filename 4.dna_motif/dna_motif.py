# import necessary tools from BioPython
from Bio.Seq import Seq

# read in sample file and split by new line = how to distinguish between sequence and substring
file = open('sample_dataset.txt').read().split('\n')

# create outfile that answer will be written to
outfile = open("dna_motif_outfile.txt",'w')

# create method 4.dna_motif
def dna_motif(file):
    strings = []                 # create empty list strings
    for i in file:               # append sequence and substring to list
        strings.append(i)
    full = Seq(strings[0])       # sequence = first item in list, set to variable full
    substring = Seq(strings[1])  # substring = 2nd item in list, set to variable substring

    positions = []               # create empty list positions
    pos = full.find(substring)   # find function finds first position of substring
    while pos != -1:             # as long as substring is within string (otherwise find() returns -1)
        positions.append(pos + 1)             # append that position + 1 (since this is 1-based numbering)
        pos = full.find(substring, pos + 1)   # find next substring position by increasing start position by 1
                                              # from last position found

    outfile.write(' '.join(map(str, positions))) # write answer to outfile in expected format

dna_motif(file)
