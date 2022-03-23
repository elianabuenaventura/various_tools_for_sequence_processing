#!/usr/bin/python

"""
This Python script computes the GC content of a DNA sequence entered by the user.
"""

dna = raw_input("Enter your DNA sequence: ")

no_g = dna.count('g') #count G's in a DNA sequence
no_c = dna.count('c') #count C's in a DNA sequence
dna_len = len(dna) #compute the length of a DNA sequence
gc_percent = (no_g + no_c) * 100.0 / dna_len #compute the GC% of a DNA sequence 
result = "GC% = " #write the string "GC% = "

print result + str(gc_percent) #print the string "GC% = " and converts the variable gc_percent from integer to string and prints it on the screen

print "The DNA sequence's GC content is %5.3f %%" % gc_percent #print the string "The DNA...", the gc_percent, and the string "%" on the screen


