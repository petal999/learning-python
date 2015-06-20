#!/use/bin/env python3

with open('seq.txt','rt') as seq:
    #for line in seq:
     #   print(line)
    full=seq.read()
    r1=full[0:5]
    r2=full[20:25]
    print(r2,r1, sep='\n')