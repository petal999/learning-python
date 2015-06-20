#!/use/bin/env python3

def find_site(base_seq, site):
    return (base_seq.find(site))

with open('seq.txt', 'rt') as seq:
    #print(seq.read())
    for line in seq:
        line = line.strip()
        site = find_site (line, '1')
        length = len(line)
        print('line is {0}, length is {1}, site position is {2}'.format\
        (line, length, site), sep = ' ')
        #print (site)