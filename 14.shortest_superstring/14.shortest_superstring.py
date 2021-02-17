import itertools
from Bio import SeqIO

# create list that will parce text file in fasta format (list of each sequence record)
file = list(SeqIO.parse('input.txt', 'fasta'))

orig_sequences = []
for i in file:     #add to the dictionary the key as the id and the seq as the valeu
    orig_sequences.append((str(i.seq)))

def concatenate(a,b):
    # reverse loop of range(0, min(len(first_seq, len(second_seq)
    for i in range(min(len(a),len(b)),-1,-1):
        # compare smaller sequence
        # loop from biggest to smallest because more efficient (look for big overlaps first, then small overlaps)
        suffix = a[len(a)- i:] # values of last i characters
        prefix = b[:i] # values of first i characters
        # if suffix of first seq = prefix of second seq
        if prefix == suffix:
            return a + b[i:] # append suffix of second seq to first seq
    # else concatenate two sequences
    return a + b

def common_substr(orig_seqs):
    combinations = itertools.combinations(orig_seqs,2) # generate all possible sequence combinations
    overlap_track = list() # keep track of all sequences concatenated and their overlaps
    # loop through all combinations
    for first_seq,second_seq in combinations:
        # as long as they're not equal
        if first_seq != second_seq:
            combined_sequence = concatenate(first_seq, second_seq) # call function concatenate
            # find the number of nucleotides that are not overlapping
            overlap_count = abs(len(first_seq) + len(second_seq) - len(combined_sequence))
            overlap_track.append([first_seq, second_seq, combined_sequence, overlap_count])
    # sort list from max to min based on overlap_count
    most_overlap = max(overlap_track, key = lambda x:x[3])  
    # remove sequence 1 from original list
    orig_seqs.remove(most_overlap[0]) 
    # remove sequence 2 from original list
    orig_seqs.remove(most_overlap[1])
    # append combined sequence that has the most overlap
    orig_seqs.append(most_overlap[2])
    # if there is more than one sequence in overlap_track list, not all overlaps were addressed
    if len(overlap_track) > 1:
        # run through algorithm again
        return common_substr(orig_seqs)
    # else
    outfile.write(''.join(map(str,orig_seqs))) # write answer to file in proper format


outfile = open('outfile.txt','w')
print(common_substr(orig_sequences))