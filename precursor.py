#!/usr/bin/env python

''' to check if precursor lines in mgf files have just one number, as they should, and not two as I’ve noticed sometimes. IF so print out the title of the spectrum and the precursor lines
'''

import sys

# Set main variables
name_of_program = sys.argv[0]
input_file = sys.argv[1]


#open and read through an mgf file evaluating precursor lines
with open(input_file, 'r') as in_f:
    countMS2 = 0
    badMS = 0
    title = None
    pepmass = None
    two_pep = None
    for line in in_f:
        line = line.strip()
        if line == "BEGIN IONS":
            title = None
            pepmass = None
            two_pep = None
        elif line.startswith("TITLE="):
            title = line.split('=')[1]
            countMS2 += 1
        elif line.startswith("PEPMASS="):
            pepmass = line.split('=')[1]
            #print("pepmass {0}".format(pepmass))
            two_pep = pepmass.split(' ')
            #print("two_pep {0}".format(two_pep))
            try:
                two_pep[1] !=''
                badMS += 1
                print("title {0} precursor error {1}".format(title, two_pep))
            except IndexError:
                pass

print('total spectra checked {0} precursors with intensity values {1}'.format(countMS2, badMS))



