#!/usr/bin/env python

''' To read an mgf file and pull out spectra that match a specific title scan number

To improve make it read a list of spectrum numbers
'''

import sys

# Set main variables
name_of_program = sys.argv[0]
input_file = sys.argv[1]
scan_number = sys.argv[2]
found = 0


#open and read through an mgf file evaluating title lines
with open(input_file, 'r') as in_f:
    for line in in_f:
        line = line.strip()
        if line.startswith("TITLE") and line.find(scan_number) > 0:
            found += 1
            print("BEGIN IONS \n{0}".format(line))
            #print(countMS2)
        elif line.startswith("END") and found ==1:
            found = 0
            print(line)
        elif found ==1:
            print(line)
        else:
            pass









