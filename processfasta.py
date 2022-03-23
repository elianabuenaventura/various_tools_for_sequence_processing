#!/usr/bin/python

""" 
This Python script builds a dictionary with all sequences of FASTA file
"""

import sys
filename = sys.argv[1]

try:
    f = open(filename)           #This will try to open myfile.fa
except IOError:                     #If I haven't open myfile.fa
    print("File %s does not exist!!" % filename)    #It will print this
    
seqs = {}                           #This creates a dictionary called seqs
for line in f:                      #This starts reading line by line
    line = line.rstrip()            #This defines variable line as omitting the endline character
    if line [0] == '>':             #This checks if the line is a header, which should start with >
        words = line.split()        #This creates a list under the variable name words that contain all words in the header
        name = words [0][1:]        #This creates a variable called name which contains all words in variable words
        seqs[name] = ''             #This creates a key called whatever words are in variable 'name' in the dictionary seqs
    else:                           #This executes an alternative block og code if the line is not a header
        seqs[name] = seqs[name] + line  #This adds the values of the key, which are the actual nucleotides of the sequence
close(f)                            #This closes the file when the loop is completed
        
