#!/use/bin/env python3

from pprint import pprint

def read_FASTA(FASTAfile):
    ''' creates a tuple for each protein from a FASTA file'''
    with open (FASTAfile) as in_file:
        return (in_file.read().split('>') [1:])
        
#create a list from the FASTAfile
#proteins = (read_FASTA('seq.txt'))
#print (proteins)
#print (proteins[1])


def read_FASTA_split(FASTAfile):
    '''start using comprehension to split fasta entries '''
    return [entry.partition('\n') for entry in read_FASTA(FASTAfile)] 

#protein = read_FASTA_split('seq.txt')
#pprint (protein)

def read_FASTA_protein(FASTAfile):
    return [[seq[0], seq[2].replace('\n','')] for seq in \
    read_FASTA_split(FASTAfile)]
    
pprint(read_FASTA_protein('seq.txt'))