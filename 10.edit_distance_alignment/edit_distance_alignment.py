# import necessary tools from BioPython
from Bio import SeqIO

# create list that will parce text file in fasta format (list of each sequence record)
file = list(SeqIO.parse('input.txt', 'fasta'))

# checks if character in same index of two strings is the same
def align(x, y):
    if x == y:
        return 0 # returns 0 if same
    else:
        return 1 # returns 1 otherwise

def edit_alignment(file):
    seq_1 = str(file[0].seq)  # set first sequence = seq_1

    seq_2 = str(file[1].seq)  # set second sequence = seq_2

    matrix = []  # create list matrix (used to create 2d matrix)
    vertical = len(seq_2) + 1  # create variable horizontal = length of seq 2 + 1
    horizontal = len(seq_1) + 1  # create variable vertical = length of seq 2 + 1

    for i in range(0, vertical):  # create matrix
        matrix.append([0] * horizontal)  # make a seq_2 length row x seq_1 length column matrix filled with zeroes

    for i in range(0, vertical):
        matrix[i][0] = i  # fill first column with range(0, length of seq_2)
    for j in range(0, horizontal):
        matrix[0][j] = j  # fill first row with range(0, length of seq_1)

    # initialize score and gap = 1
    score = 1
    gap = 1

    for i in range(1, vertical):
        for j in range(1, horizontal):  # loop through 2d matrix starting at position 1
            if seq_2[i - 1] == seq_1[j - 1]:  # if same character at same index in both sequences, score = 0
                matrix[i][j] = matrix[i - 1][j - 1]  # edit distance = value at that position

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
    outfile.write(str(matrix[i][j]))
    outfile.write('\n')

    # create list position where tuples of positions will be added
    position = []
    # create list direction where list of strings will be added
    direction = []

    # loop through matrix
    for i in range(1, vertical):
        for j in range(1, horizontal):  # starting at position 1, 1
            # check if seq_2[i-1] = seq_1[j-1] using align method
            count = align(seq_2[i-1],seq_1[j-1])

            # diagonal goes up and left one position
            # count = 0 if match, count = 1 otherwise
            diag = matrix[i - 1][j - 1] + count
            # go up one position
            vert = matrix[i - 1][j] + 1
            # go left one position
            horizon = matrix[i][j - 1] + 1

            # find minimum of 3 variables
            minimum = min(vert, horizon, diag)
            matrix[i][j] = minimum

            # if the minimum is diagonal
            if minimum == diag:
                position.append((i,j)) # append position of location to list 'position'
                direction.append('diagonal') # append direction to list 'direction'
            # same thing as above
            elif minimum == horizon:
                position.append((i,j))
                direction.append('horizontal')
            elif minimum == vert:
                position.append((i,j))
                direction.append('vertical')

    # set i and j = length of both sequences
    i = len(seq_2)
    j = len(seq_1)
    seq1 = ''
    seq2 = ''

    while i > 0 and j > 0:
        # while len(sequences) is greater than 0
        index = position.index((i,j)) # index = index of where tuple of current position is located in list position
        dir = direction[index] # dir = direction at that position in list direction

        if dir == 'diagonal':
        # if direction is diagonal
            seq1 = seq_1[j - 1] + seq1
            seq2 = seq_2[i - 1] + seq2
            i -= 1 # go down one
            j -= 1 # go left one

        elif dir == 'vertical':
        # if direction is vertical
            seq1 = '-' + seq1 # add gap symbol to sequence 1
            seq2 = seq_2[i - 1] + seq2
            i -= 1 # go up one

        elif dir == 'horizontal':
        # if direction is horizontal
            seq1 = seq_1[j - 1] + seq1
            seq2 = '-' + seq2 # add gap symbol to sequence 2
            j -= 1 # go left one

    # write out new sequences to outfile
    outfile.write(str(seq1))
    outfile.write('\n')
    outfile.write(str(seq2))

# create outfile that answer will be written
outfile = open("edit_dist_out_align.txt", 'w')
print(edit_alignment(file))  # write answer to outfile