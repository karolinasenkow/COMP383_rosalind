# cycles = list
# append to substring, then append substring to list cycle
# append each cycle to list
# if cycles = 2, print string
import itertools
import graphviz
from Bio.Seq import Seq
from collections import defaultdict

# create set of all sequences and reverse complements
kmers = set()
file = open('input.txt').read().split('\n')
for i in file:
    kmers.add(str(i))
    kmers.add(str(Seq(i).reverse_complement()))

# create outfile
outfile = open('output.txt', 'w')

# set kmer = len - 1 (this will need to be changed to have all kmer sizes)
kmer_list = list()
for i in kmers:
    k = len(i) - 1  # set k = length of 1 sequence -1

# create tuple of kmer size len(seq)-1 (will need to find tuples of all kmer lengths and separate them into seperate
# lists or files
kmer_dict = defaultdict(set)
for i in kmers:
    for x in range(3, k + 1):
        kmer_dict[len(i[0:x])].add(i[0:x])
        kmer_dict[len(i[1:x + 1])].add(i[1:x + 1])

# make graph another defaultdict
graph = {}
big_graph = defaultdict(list)
for key, value in kmer_dict.items():
    for i in value:
        prefix = i[:-1]
        suffix = i[1:]
        big_graph[key].append((prefix, suffix))
# print(big_graph)

cycles = defaultdict(list)
for key, value in big_graph.items():
    for i, j in itertools.combinations(value, 2):
        # print(i,j)
        if i[1] == j[0]:
            x = (i[0], j[1])
            # cycles[key].append(x)
            cycles[key].append(''.join(map(str, x)))
print(cycles)

substring = ''
concatenated_str = defaultdict(list)
for x, y in cycles.items():
    first = y[0]
    substring += first
    s = 1
    y.remove(y[0])
    for j in y:
        if first.endswith(j[:-1], s):
            substring += j[-1]
            first += j[-1]
            y.remove(j)
            s += 1
    concatenated_str[x].append(substring)
# print(concatenated_str)

# append first key to substring and last char of that value
# find key that matches that last value, append last char of its value
# check to make sure doesn't match what's already in list
# once no more matches, append to list 'cycles', substring = ''
# if cycles == 2: return one of the substrings in that list
# cycles = defaultdict: key = kmer length, value = cycles list


# # write out all tuples to outfile (each kmer size = diff outfile for now)
# for i in kmer_list:
#     outfile.write('(')
#     outfile.write(str(i[0]))
#     outfile.write(', ')
#     outfile.write(str(i[1]))
#     outfile.write(')')
#     outfile.write('\n')
# outfile.close()
#
# # create graph from outfile
# dbg = graphviz.Digraph('dBgraph', format='png')
# with open("new.txt", 'r') as f:
#     for line in f:
#         e1, e2 = line.rstrip().split(', ')
#         e1 = e1[1:]
#         e2 = e2[:-1]
#         dbg.edge(e1, e2)
# dbg.render()

'''create dict
key = len(i[0]), value = tuple
if key = i, create list %i'''
