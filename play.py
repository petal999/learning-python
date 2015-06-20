#!/use/bin/env python3

with open('seq.txt','rt') as seq:
    for line in seq:
        print(line.count('k'))




    
    
    
#def read_FASTA('seq.txt'):
 #   with open('seq.txt') as seq:
  #      return seq.read().split('>')[1:]