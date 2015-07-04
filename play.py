#!/use/bin/env python3

seq = ''

with open('seq.txt','rt') as seq_file:
    for line in seq_file:
        line = seq_file.readline()
        while line and line[0] == '>':  
            line = seq_file.readline()
        while line and line[0] != '>':
            seq += line
            line = seq_file.readline()
    print (seq)

 




