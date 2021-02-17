'''Given: A positive integer n (n≤20,000) and two subsets A and B of {1,2,…,n}.
Return: Six sets: A∪B, A∩B, A−B, B−A, Ac, and Bc (where set complements are taken with respect to {1,2,…,n}).'''

# read in sample file and split by new line = how to distinguish between sequence and substring
file = open('input.txt').read().split('\n')

# create outfile that answer will be written to
outfile = open("set_operations_out.txt",'w')

# create set named complement which contains range 1 - n
complement = set(range(1,int(file[0])+1))

# since file[1] is a string, must clean up and replace extra characters
# split list by commas
a_str = str(file[1]).replace(' ','').replace('{','').replace('}','').split(',')

# create set named A
A = set()
# loop through a_str and append to set A
for i in a_str:
    A.add(int(i))

# same as above but for set B, file[2]
b_str = str(file[2]).replace(' ','').replace('{','').replace('}','').split(',')
B = set()
for i in b_str:
    B.add(int(i))

# in A or B
union = set() # create set named union
for i in A:
    for j in B: # loop through sets A and B
        union.add(i)
        union.add(j) # add contents of A and B to set union
outfile.write(str(union)) # write to outfile
outfile.write('\n')

# in both A and B
intersection = set() # create set named intersection
for i in A: # loop through set A
    if i in B: # if contents of B also in A
        intersection.add(i) # add to set
outfile.write(str(intersection)) # write to outfile
outfile.write('\n')

# A - B
a_minus_b = set() # create new set named a_minus_b
for i in A:
    a_minus_b.add(i) # add entire contents of A to a_minus_b
for i in B: # loop through set B
    if i in a_minus_b:
        a_minus_b.remove(i) # if i in a_minus_b, remove i
outfile.write(str(a_minus_b)) # write to outfile
outfile.write('\n')

# B - A
b_minus_a = set() # create set b_minus_a
for i in B: # loop through contents of B
    b_minus_a.add(i) # add everything to b_minus_a
for i in A: # loop through contents of A
    if i in b_minus_a: # if i in b_minus_a
        b_minus_a.remove(i) # remove i
outfile.write(str(b_minus_a)) # write to outfile
outfile.write('\n')

# A^c
a_to_c = set() # create set named a_to_c
for i in complement: # loop through set named complement
    if i not in A: # as long as i isn't in A
        a_to_c.add(i) # add i to a_to_c
outfile.write(str(a_to_c)) # write to outfile
outfile.write('\n')

# B^c
b_to_c = set() # create set named b_to_c
for i in complement: # loop through contents of set named complement
    if i not in B: # as long as i isn't in B
        b_to_c.add(i) # add i to b_to_c
outfile.write(str(b_to_c)) # write to outfile
