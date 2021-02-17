#import necessary tools from BioPython
from Bio import SeqIO

# create list that will parce text file in fasta format (list of each sequence record)
file = list(SeqIO.parse('input.txt', 'fasta'))

def edit_distance(file):
    seq_1 = str(file[0].seq) # set first sequence = seq_1

    seq_2 = str(file[1].seq) # set second sequence = seq_2

    matrix = [] # create list matrix (used to create 2d matrix)
    horizontal = len(seq_2) + 1 # create variable horizontal = length of seq 2 + 1
    vertical = len(seq_1) + 1 # create variable vertical = length of seq 2 + 1

    for i in range(0,horizontal): # create matrix
        matrix.append([0] * vertical) #make a seq_2 length row x seq_1 length column matrix filled with zeroes

    for i in range(0, horizontal):
        matrix[i][0] = i # fill first row with range(0, length of seq_2)
    for j in range(0,vertical):
        matrix[0][j] = j # fill first column with range(0, length of seq_1)

    # initialize score and gap = 1
    score = 1
    gap = 1

    for i in range(1,horizontal):
        for j in range(1,vertical): # loop through 2d matrix starting at position 1
            if seq_2[i-1] == seq_1[j-1]: # if same character at same index in both sequences, score = 0
                matrix[i][j] = matrix[i - 1][j - 1] # edit distance = value at that position

            else:
                # if diagonal <= horizontal and diagonal <= vertical
                if matrix[i - 1][j - 1] <= matrix[i][j - 1] and matrix[i - 1][j - 1] <= matrix[i - 1][j]:
                    # matrix[i][j] = diagonal + score
                    matrix[i][j] = matrix[i - 1][j - 1] + score

                # if horizontal <= vertical and horizontal <= diagonal
                if matrix[i][j - 1] <= matrix[i - 1][j] and matrix[i][j - 1] <= matrix[i - 1][j - 1]:
                    # matrix[i][j] = horizontal + gap
                    matrix[i][j] = matrix[i][j - 1] + gap

                # if vertical <= horizontal and vertical <= diagonal
                if matrix[i - 1][j] <= matrix[i][j - 1] and matrix[i - 1][j] <= matrix[i - 1][j - 1]:
                    # matrix[i][j] = vertical + gap
                    matrix[i][j] = matrix[i - 1][j] + gap

    return str(matrix[i][j]) # this will return edit distance (final value in matrix)

# create outfile that answer will be written
outfile = open("edit_dist_out.txt", 'w')
outfile.write(edit_distance(file))  # write answer to outfile