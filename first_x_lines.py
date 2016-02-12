#!/usr/bin/env python

''' To read an mgf file and print out the x number of spectra, recognising begin and end ions lines as delineators of mgf files.
'''

import sys

# Set main variables
name_of_program = sys.argv[0]
input_file = sys.argv[1]
target_MS2 = int(sys.argv[2]) + 1
countMS2 = 0


#open and read through an mgf file evaluating precursor lines
with open(input_file, 'r') as in_f:
    for line in in_f:
        line = line.strip()
        if countMS2 < target_MS2:
            if line.startswith("BEGIN"):
                countMS2 += 1
                print(line)
                #print(countMS2)
            else:
                print(line)




#print('target spectra {0} spectra counted {1}'.format(target_MS2, countMS2))



