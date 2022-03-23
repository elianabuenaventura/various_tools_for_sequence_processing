#!/usr/bin/python

"""
This Python script computes the GC content of a DNA sequence.
"""

#get the DNA sequence
dna = 'atgtacgatcgtagctagtttttttaaaag'
no_g = dna.count('g') #count G's in a DNA sequence
no_c = dna.count('c') #count C's in a DNA sequence
dna_len = len(dna) #compute the length of a DNA sequence
gc_percent = (no_g + no_c) * 100.0 / dna_len #compute the GC% of a DNA sequence 
print gc_percent #print the GC% on the screen

