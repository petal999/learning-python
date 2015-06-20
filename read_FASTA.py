#!/use/bin/env python3

from pprint import pprint

def read_FASTA(FASTAfile):
    ''' creates a tuple for each protein from a FASTA file'''
    with open (FASTAfile) as in_file:
        return (in_file.read().split('>') [1:])

def read_FASTA_split(FASTAfile):
    return [entry.partition('\n') for entry in read_FASTA(FASTAfile)] 

         
#create a list from the FASTAfile
#proteins = (read_FASTA('seq.txt'))
#print (proteins)
#print (proteins[1])

protein = read_FASTA_split('seq.txt')
pprint (protein)