#!/use/bin/env python3

def find_site(base_seq, site):
    return print(base_seq.find(site))

with open('seq.txt', 'rt') as seq:
    #print(seq.read())
    base_seq = seq.read()
    #print (base_seq)

find_site (base_seq, 'prot')