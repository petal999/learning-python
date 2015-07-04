#!/usr/bin/env python3

data = {}

with open('pride.txt') as f:
    for line in f:
        if line != "\n":
            cell = line.split(":")
            info = cell[1].strip()
            print("{0}\t{1}\n".format(cell[0], cell[1]))
        else:
            pass
            
#this works 