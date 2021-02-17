from Bio import Entrez
# read in sample file and split by new line = how to distinguish between sequence and substring
file = open('input.txt').read().split('\n')

# create outfile that answer will be written to
outfile = open("output.txt",'w')

# first line of input file = genus
genus = file[0]
# second line of input file = start date
start_date = file[1]
# third line of input file = end date
end_date = file[2]
# term = string that will be used in the query
term = genus + ' [Organism] AND (' + start_date + '[PDAT] : ' + end_date + '[PDAT])'
Entrez.email = "ksenkow@luc.edu"

# used to search NCBI db
# db = nucleotide indicates you're searching genbank
# term = The search term for the "Query" field. You can use search tags here.
handle = Entrez.esearch(db="nucleotide", term=term)
record = Entrez.read(handle)
# The number of Nucleotide GenBank entries for the given genus that were published between the dates specified.
outfile.write(str(record['Count']))
