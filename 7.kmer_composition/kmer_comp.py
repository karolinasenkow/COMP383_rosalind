'''Try initializing a dictionary with keys for every possible 4-mer (itertools.product() may be helpful).
Then, iterate over the DNA sequence and add a count to your dictionary when a 4-mer is encountered.
Remember a string of length n can be seen as composed of n−k+1 overlapping k-mers.'''

# import necessary tools from BioPython
from Bio import SeqIO
from itertools import product

# create list that will parce text file in fasta format (list of each sequence record)
file = list(SeqIO.parse('input.txt', 'fasta'))

# create outfile that answer will be written to
outfile = open("kmer_comp_output.txt",'w')

def k_mer(file):
    # add all 4mer combinations to list kmer_list
    kmer_list = []
    for i in product('ATCG', repeat=4): # use product.itertools() to generate all kmer combinations
        kmer_list.append(''.join(i))
    kmer_list = sorted(kmer_list) #sort list of kmers in lexicographic order

    # create dict where key = 4mer and value = 0
    kmer_count = dict()
    for i in kmer_list:
        kmer_count[i] = 0

    # add file into list string
    string = []
    for i in file:
        string.append(i)

    # set seq = sequence of item in list
    seq = str(string[0].seq)

    # loop through list of all kmers
    for i in kmer_list:
        pos = seq.find(i) # find substring of kmer in sequence
        while pos != -1:  # as long as a kmer is found
            kmer_count[i] += 1 # increase count of that kmer in dictionary
            pos = seq.find(i, pos + 1)  # look for next kmer instance by increasing start position to
                                        # after position where most recent kmer was found

    # append dict values to list in order to print them properly
    list = []
    for i in kmer_count.values():
        list.append(i)

    # return contents of list in proper format (space separated) - write to outfile
    outfile.write(' '.join(map(str, list)))

print(k_mer(file))
