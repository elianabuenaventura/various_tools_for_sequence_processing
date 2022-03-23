"""
This is my first funciton in Python program.
It computes the GC content of a DNA sequence.
"""

def gc(dna):
    """This function computes the GC content of a DNA sequence entered by the user."""
    nbases = dna.count('n') + dna.count('N') #count undefined bases
    no_g = dna.count('g') + dna.count('G') #count G's in a DNA sequence
    no_c = dna.count('c') + dna.count('C') #count C's in a DNA sequence
    dna_len = len(dna) #compute the length of a DNA sequence
    gc_percent = (no_g + no_c) * 100.0 / (dna_len - nbases) #compute the GC% of a DNA sequence 
    return gc_percent
