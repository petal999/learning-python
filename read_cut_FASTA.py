#!/use/bin/env python3

import sys

assert sys.argv[1] != None, 'specify a protein name after program' 

prot_name = sys.argv[1]

def read_FASTA_protein(FASTAfile):
    ''' making one def for reading FASTA sequences into a dict with protein 
    name as key'''
    with open (FASTAfile) as in_file:    
        return {name: sequence.replace('\n','') for name, ignore, sequence in \
        [record.partition('\n') for record in in_file.read().split('>')[1:]]}

def cut_seq(base_seq, site, offset=1):
    '''Cuts sequence into two pieces using argv[2] and returns them in a tuple '''
    cut_at = base_seq.find(site)
    if cut_at >-1:
        return base_seq[:cut_at+offset], base_seq[cut_at+offset:]
    else:
        return 'sequence not cut'
 
def keep_cutting():
    '''If site is repeated in rest of sequence string keep cutting at site '''
    pass
 
    
proteins = read_FASTA_protein('seq.txt')
try:
    proteins[prot_name]
except KeyError:
    print ('Protein name not found in FASTA')
else:
    print (proteins[prot_name])
    try:
        site = sys.argv[2] 
    except IndexError:
        pass
    else:
        cutting = cut_seq(proteins[prot_name], site)
        print (cutting)


