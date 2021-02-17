# import necessary tools from BioPython
from Bio import SeqIO

# create list that will parce text file in fasta format (list of each sequence record)
file = list(SeqIO.parse('input.txt', 'fasta'))

# create graph where key = id, value = tuple (first 3 characters in seq, last 3 chars in seq)
graph = {}
for i in file:
    graph[i.id] = (str(i.seq)[:3], str(i.seq)[-3:])
print(graph)

# add ids to list id
id = []
# add start of seq to list first
first = []
# add end of seq to list last
last = []
for i, j in graph.items():
    id.append(i)
    first.append(j[0])
    last.append(j[1])

# set i = 0
i = 0

# while i < length of list 'first'
while i < len(first) - 1:
    # if seq of last in list 'first'
    if last[i] in first:
        # iterate through and find where all indices containing last[i] are in list 'first'
        # append all indices to list all_instances
        all_instances = [z for z, d in enumerate(first) if d == last[i]]
        # iterate through all_instances
        for g in all_instances:
            # if id at index i != id at index g (same rosalind_id would indicate first and last seq are w/i one seq)
            if id[i] != id[g]:
                # print id containing last 3 nucleotides and id containing first 3 nucleotides
                print(id[i], id[g])
        # increase i by 1
        i += 1
    else:
        i += 1


