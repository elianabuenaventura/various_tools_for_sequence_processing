""" This Python script checks if a given dna sequence has in frame stop codons. 
The default reading frame starts in the first codon position (frame=0), but
the user can define other reading frames by invoking the function with the 
arguments (dna, 1) for second codon position or (dna, 2) for third codon 
position"""

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
        
