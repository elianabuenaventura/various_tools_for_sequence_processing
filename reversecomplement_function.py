#!/usr/bin/python

""" 
This Python script returns the reverse the lowercase complement of a given dna sequence
"""

def reversecomplement(seq):
    """This function returns the reverse complement of a given dna sequence"""
    def reverse_string(seq):
        """This function returns the reverse string of a sequence"""
        return seq[::-1]
    seq = reverse_string(seq)
    def complement(dna):
        """This function returns the complimentary sequence string"""
        basecomplement = {'A':'T', 'C':'G', 'G':'C', 'T':'A', 'N':'N', 'a':'t', 
        'c':'g', 'g':'c', 't':'a', 'n':'n'}
        letters = list(dna)
        letters = [basecomplement[base] for base in letters]
        return ''.join(letters)
    seq = complement(seq)
    return seq.lower() #poner 'return seq' pone todo en tamano original        

                
