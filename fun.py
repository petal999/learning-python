#!/use/bin/env python3

import sys

def find_site(base_seq, site):
    return (base_seq.find(site))

with open('seq.txt', 'rt') as seq:
    #print(seq.read())
    for line in seq:
        line = line.strip()
        site_position = find_site (line, sys.argv[1])
        length = len(line)
        print('line is {0}, length is {1}, site position is {2}'.format\
        (line, length, site_position), sep = ' ')
        #print (site)