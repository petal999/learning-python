#!/use/bin/env python3

import sys
prot_name = sys.argv[1]
site = sys.argv[2]

def read_FASTA_protein(FASTAfile):
    ''' making one def for reading FASTA sequences into a dict with protein name as key'''
    with open (FASTAfile) as in_file:    
        return {part[0]: part[2].replace('\n','') for part in [record.partition('\n') for \
        record in in_file.read().split('>')[1:]]}

def cut_seq(base_seq, site, offset=0):
    '''Cuts sequence into two pieces using argv[2] and returns them in a tuple '''
    cut_at = base_seq.find(site)
    if cut_at >-1:
        return base_seq[:cut_at+offset], base_seq[cut_at+offset:]
    else:
        return base_seq+' not cut'
 
    
proteins = read_FASTA_protein('seq.txt')
cutting = cut_seq(proteins[prot_name], site)

print (proteins[prot_name], cutting)
