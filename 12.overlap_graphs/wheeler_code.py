#!/usr/bin/python3
import itertools
infile = "input.txt"

seqs = {} #build dictionary, keys=fasta IDs, values=sequence string

with open(infile, 'r') as f:
    for line in f:
        line = line.rstrip()
        if line[0] == '>':
            seqlabel = line[1:]
            seq = ''
        else:
            seq += line
        seqs[seqlabel] = seq

#T/F function for does a length k suffix of s1 match a length k prefix of s2
def is_k_overlap(s1, s2, k):
    return s1[-k:] == s2[:k]

def k_edges(datadict, k): #find edges with overlap of k
    edges = [] #make list to hold edges as tuples
    #combinations function from itertools module pulls all pairwise (2) keys from dict
    for s1,s2 in itertools.combinations(datadict, 2):
        seq1, seq2 = datadict[s1], datadict[s2] #pull out sequences to check for overlap
        if is_k_overlap(seq1, seq2, k):
            edges.append((s1,s2)) #add tuple of accessions to edges list
        if is_k_overlap(seq2, seq1, k): #check the other ends for overlap
            edges.append((s2,s1)) #add tuple of accessions to edges list
    return edges

edgelist = k_edges(seqs,3) #problem asks for O_3 (k=3)

outfile = open("out_grph.txt", "w")
for i in range(0,len(edgelist)):
    outfile.write(" ".join(edgelist[i]) + "\n")
outfile.close()