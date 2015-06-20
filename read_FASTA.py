#!/use/bin/env python3

import sys

def read_FASTA_protein(FASTAfile):
    ''' making one def for reading FASTA sequences into a dict with protein name as key'''
    with open (FASTAfile) as in_file:    
        return {part[0]: part[2].replace('\n','') for part in [record.partition('\n') for \
        record in in_file.read().split('>')[1:]]}
    
proteins = read_FASTA_protein('seq.txt')
#print (proteins)
print (proteins[sys.argv[1]])
