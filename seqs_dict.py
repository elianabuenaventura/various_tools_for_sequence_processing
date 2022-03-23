#!/usr/bin/python

"""
This Python script will read a fasta file and create a dictionary containing 
the keys, which are the headers or sequence IDs starting with '>'
and the values, which are the sequences
"""

try:
    f = open("myfile.fa")           #This will try to open myfile.fa
except IOError:                     #If I haven't open myfile.fa
    print("File myfile.fa does not exist!!")    #It will print this
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
        
