#!/usr/bin/python

"""
dnautil contains a few useful functions for dna sequence
"""

def gc(dna):
    """This function computes the GC content of a DNA sequence entered by the user."""
    nbases = dna.count('n') + dna.count('N') #count undefined bases
    no_g = dna.count('g') + dna.count('G') #count G's in a DNA sequence
    no_c = dna.count('c') + dna.count('C') #count C's in a DNA sequence
    dna_len = len(dna) #compute the length of a DNA sequence
    gc_percent = (no_g + no_c) * 100.0 / (dna_len - nbases) #compute the GC% of a DNA sequence 
    return gc_percent

def has_stop_codon (dna, frame=0):
    """This function checks if a given dna sequence has in frame stop codons """
    stop_codon_found = False
    stop_codons = ['tga', 'tag', 'taa']
    for i in range (frame, len(dna), 3):
        codon = dna[i:i+3].lower()
        if codon in stop_codons:
            stop_codon_found = True
            break
        return stop_codon_found
        
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
        
