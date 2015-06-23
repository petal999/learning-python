#!/use/bin/env python3

ATG = []
GOdict = {}
file_out = open('CLC2_GO.txt', 'wt')

def get_ATG(ATGfile):
    with open(ATGfile) as in_file:
        for line in in_file:
            line = line.strip()
            ATG.append(line)
        return (ATG) 

def make_go_dict(in_file, locus):
    with open(in_file,'rt') as GO:
        for line in GO:
            GOline = line.split('\t')
            GOdict.update({GOline[0]: GOline[5]})


def make_small_go(go_file, locus):
    with open(go_file,'rt') as GO:
        for line in GO:
            #line = line.strip()
            if line.startswith(locus):
                print (line)
                file_out.write(line)
            else:
                pass



#make_go_dict('miniGO.txt')
#print (GOdict['AT2G40WIN'])

get_ATG('CLC2_all_ATG.txt')
for locus in ATG:
    make_small_go('GOSLIM.txt', locus)




file_out.close()