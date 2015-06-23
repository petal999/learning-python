#!/use/bin/env python3

ATG = []
GOdict = {}

def get_ATG(ATGfile):
    with open(ATGfile) as in_file:
        for line in in_file:
            line = line.strip()
            ATG.append(line)
        return (ATG) 

def make_go_dict(go_file, locus):
    with open(go_file,'rt') as GO:
        for line in GO:
            line = line.strip()
            if line.startswith(locus):
                GOline = line.split('\t')
                GOdict.update({GOline[0]: GOline[5]})
            else:
                pass

#make_go_dict('miniGO.txt')
#print (GOdict['AT2G40WIN'])

get_ATG('miniATG.txt')
for locus in ATG:
    make_go_dict('miniGO.txt', locus)
    try:
        print (GOdict[locus])
    except KeyError:
        pass




