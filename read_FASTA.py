#!/use/bin/env python3

from pprint import pprint

def read_FASTA(FASTAfile):
    ''' creates a tuple for each protein from a FASTA file'''
    with open (FASTAfile) as in_file:
        return (in_file.read().split('>') [1:])
        
def read_FASTA_split(FASTAfile):
    '''start using comprehension to split fasta entries '''
    return [entry.partition('\n') for entry in read_FASTA(FASTAfile)] 

def read_FASTA_protein(FASTAfile):
    '''To end up with a clean two element list of name and sequence '''
    return {name : seq.replace('\n','') for name, ignore, seq in \
    read_FASTA_split(FASTAfile)}
    
proteins = read_FASTA_protein('seq.txt')
print (proteins['prot2'])