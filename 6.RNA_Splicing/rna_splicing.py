# import necessary tools from BioPython
from Bio import SeqIO
from Bio.Seq import Seq

# create list that will parce text file in fasta format (list of each sequence record)
file = list(SeqIO.parse('input.txt', 'fasta'))

def RNA_Splice(file):
    # create empty list sequence and append all sequences from file
    sequences = []
    for i in file:
        sequences.append(str(i.seq)) # convert from Seq to str type

    # set first sequence = original
    original = str(sequences[0])
    # create empty list of introns and append all sequences besides first to list
    introns = []
    for i in range(1,len(sequences)):
        introns.append(sequences[i])

    # loop through list of introns
    for i in introns:
        if i in original: # if intron in original sequence, replace that intron with '' (to delete it)
            original = original.replace(i,'')

    DNA = Seq(original) #convert original to Seq type
    return str(DNA.translate()) # use BioPython tool .translate() to translate sequence

# create outfile that answer will be written
outfile = open("RNA_splice_output.txt",'w')
outfile.write(RNA_Splice(file)) #write answer to outfile
