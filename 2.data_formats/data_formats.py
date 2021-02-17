# import methods from BioPython
from Bio import Entrez
from Bio import SeqIO

Entrez.email = "ksenkow@luc.edu"

# read file and use ' ' as delimiter
file = open("genbank_entries.txt").read().split(" ")

# create empty list where genbank_id will be appended from file
seq_id = []
for i in file:
    seq_id.append(i)
print(seq_id)
# create outfile that answer will be written to
outfile = open("data_formats_outfile.txt",'w')

# db = database to search, id: GenBank entry IDs from file, rettype: data format to be returned
handle = Entrez.efetch(db="nucleotide", id=seq_id, rettype="fasta")

# get the list of SeqIO objects in FASTA format
records = list(SeqIO.parse(handle, "fasta"))

# create empty dict length where genbank_id : sequence_length
length = dict()
# create empty dict fasta where genbank_id : sequence
fasta = dict()
for i in range(len(seq_id)):
    length[records[i].description] = len(records[i].seq)
    fasta[records[i].description] = records[i].seq
# find shortest sequence using min shortcut
min = min(length, key=length.get)

# write to outfile: key = genbank_id, value = shortest sequence
outfile.write('>')
outfile.write(str(min))
outfile.write('\n')
outfile.write(str(fasta.get(min)))


