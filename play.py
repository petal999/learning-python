#!/use/bin/env python3

seq = ''
count = 0
length = 0

with open('seq.txt','rt') as seq_file:
    for line in seq_file:
        line = line.strip()
        count += 1
        if line.startswith ('>'):
            pass
        elif line and line[0] != '>':
            length = line.count('')
        print ("line {0} is seq is {1} of length {2}".format(count, line, length))



 




