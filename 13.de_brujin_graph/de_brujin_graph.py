# import necessary tools from BioPython
from Bio.Seq import Seq

# read in sample file and split by new line = how to distinguish between sequence and substring
file = open('input.txt').read().split('\n')

# create outfile to write answer to
outfile = open('output.txt','w')

# create set S and add all sequences from input file to set
S = set()
for i in file:
    S.add(i)

# create set Src and add reverse complement of all sequences from input file
Src = set()
for i in S:
    Src.add(str(Seq(i).reverse_complement()))

# create set both and add all sequences from S and Src
both = set()
for i in S:
    both.add(i)
for i in Src:
    both.add(i)

# create tuple named tup
tup = tuple()
# create list named adj_list
adj_list = list()

# loop through set both
for i in both:
    k = len(i) - 1 # set k = length of 1 sequence -1
    tup = (i[0:k],i[1:k+1]) # create tuple that takes (everything from 0:k, everything from 1:k+1)
    adj_list.append(tup) # append tuple to adj_list

# write to outfile in proper format
for i in adj_list:
    outfile.write('(')
    outfile.write(str(i[0]))
    outfile.write(', ')
    outfile.write(str(i[1]))
    outfile.write(')')
    outfile.write('\n')


