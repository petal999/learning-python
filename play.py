#!/use/bin/env python3

seq = ''

with open('seq.txt','rt') as seq_file:
    for line in seq_file:
        if line.startswith ('>'):
            pass
        elif line and line[0] != '>':
            print (line)



 




