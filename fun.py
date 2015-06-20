#!/use/bin/env python3

import sys

def find_site(base_seq, site):
    '''find the position of a sequence string (site) in a \
    given sequence'''
    return (base_seq.find(site))
    
def cut_seq(base_seq, site, offset=0):
    '''Cuts sequence into two pieces and returns them in a tuple '''
    cut_at = find_site(base_seq, site)
    if cut_at >-1:
        return base_seq[:cut_at+offset], base_seq[cut_at+offset:]
    else:
        return base_seq+' not cut'
    

with open('seq.txt', 'rt') as seq:
    #print(seq.read())
    for line in seq:
        line = line.strip()
        found_site = find_site (line, sys.argv[1])
        print ('position = {0}'.format(found_site))
        print (cut_seq(line, sys.argv[1]))

        
        