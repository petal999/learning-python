#!/use/bin/env python3

import sys
    
def cut_seq(base_seq, site, offset=0):
    '''Cuts sequence into two pieces using argv[1] and returns them in a tuple '''
    cut_at = base_seq.find(site)
    if cut_at >-1:
        return base_seq[:cut_at+offset], base_seq[cut_at+offset:]
    else:
        return base_seq+' not cut'
  

with open('seq.txt', 'rt') as seq:
    #print(seq.read())
    for line in seq:
        line = line.strip()
        parts = (cut_seq(line, sys.argv[1]))
        #print (parts)
        print ('{0}, {1}'.format(line, parts))
        
        