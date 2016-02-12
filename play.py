#!/use/bin/env python3


proteins = ['prot5', 'prot3']




def find_prot(prot):
    with open('seq.txt') as file:
        for line in file:
            line = line.strip()[1:]
            if line.startswith(prot):
                print (prot)
            #call next function here to get sequence
                return read_seq(file)
            else:
                pass
                
def read_seq(in_file):
    seq =''
    for line in in_file:
        if not line or line[0] != '>':
            print (line)
    

for protein in proteins:
    find_prot(protein)

 




