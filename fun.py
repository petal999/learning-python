#!/use/bin/env python3

with open('seq.txt','rt') as seq:
    #for line in seq:
     #   print(line)
    r1 = seq.read(20)
    print(r1)
    print(r1.count('g'))
    r2 = seq.read(20)
    print(r2)
    print(r2.count('g'))
    print(seq.read())