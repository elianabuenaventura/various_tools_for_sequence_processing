#python3 number_of_records.py dna.example.fasta

import sys

#import getopt

filename = sys.argv[1]

try:
    f = open(filename)           #This will try to open dna.example.fasta
except IOError:                     #If I haven't open dna.example.fasta
    print("File %s does not exist!!" % filename)    #It will print this

#PUNTO 1

componentes = {}                    #Create a dictionary for the two components of the file
for line in f:                      #This starts reading line by line
    if line[0] == ">":              #Check if this line is a header or a sequence
        cosa = line.split()[0]      #create 'key' variable cosa to store the first word (become keys in the next step) of each header with method split
        componentes[cosa] = ""      #add a values to each key of dictionary componentes. values are empty ""
    else:                           #This executes an alternative block of code if the line is not a header
        componentes[cosa] = componentes[cosa] + line.rstrip()   #assign values (=sequences ignoring endline symbol) to each 'key' (=first word of header)
    
#QUESTION How many records are in the file?            
print ("There are %d records in the fasta file" % (len(componentes))) #This prints the number of keys of dictionary componentes
#print (list(componentes.keys())) #print all keys which correspond to the first word of each header
#print (list(componentes.values())) #print all values which correspond to the sequences without endline symbols


#PUNTO 2

sequences = []
for i in componentes.values():
    sequences.append(i)

#sequences = (list(componentes.values())) 
Lengths = {}
for i in sequences:
    length_seqs = len(i)
    Lengths[length_seqs] = "" 

Longitudes = (Lengths.keys()) #esta se imprime como dict_keys([990, 724,...
Longs = list(Longitudes)      #esta vuelve las longitudes una lista
#print (Lengths.keys())        #imprimir dict_keys([990, 724,...
#print (Longs)                 #imprime la lista de longitudes en su orden original
#QUESTION What are the lengths of the sequences in the file?
print ("These are the lengths of the sequences in the fasta file: %s" % (Longs))  #imprimo las longitudes en su orden original
Longs_sorted = sorted(Longs)    #creo la valiable que ordena las longitudes
#QUESTION What is the longest sequence and what is the shortest sequence?
print ("The longest sequence in the fasta file is %d and the shortest is %d" % (Longs_sorted[-1],Longs_sorted[0]))   #max and min long de secuencia

#QUESTION Is there more than one longest or shortest sequence? 
#QUESTION What are their identifiers?

#PUNTO 3

#Findging ORFs

def is_an_orf (sequences, frame):
    """This function checks if a given dna sequence has an 
    in frame start or stop codon """

    lostarts = []
    lostops = []
    
    start_codon = ["ATG"]
    stop_codons = ["TAA", "TAG", "TGA"]
    
    for i in range (0, len(sequences), 3):
        if sequences[i:i+3] in start_codon:
            lostarts.append(i)
    
        if sequences[i:i+3] in stop_codons:
            lostops.append(i)

    ORFs = []

    for a in lostarts:
        for z in lostops:
            if (a > z) or (z - a < 6):
                continue
            ORFs.append(sequences[a:z+1])
            break
    return ORFs



# What is the length of the longest ORF appearing in reading frame 2 of any of the sequences?
# What is the starting position of the longest ORF in reading frame 3 in any of the sequences?
#ORFs_f1 = is_an_orf(sequences, 0)
ORFs_f2 = is_an_orf (sequences, 1)
#ORFs_f3 = is_an_orf (sequences, 2)


#ALL_ORFs = ORFs_f1 + ORFs_f2 + ORFs_f3
#ALL_ORFs_sorted = sorted(ALL_ORFs)    
ORFs_f2_sorted = sorted(ORFs_f2)
#print ("The longest ORF in the file is %d" % (ALL_ORFs_sorted[-1]))   
print ("The longest ORF in the file is %d" % (ORFs_f2_sorted[-1]))   


#QUESTION what is the length of the longest ORF in the file?

#QUESTION What is the identifier of the sequence containing the longest ORF?


#QUESTION For a given sequence identifier, what is the longest ORF contained in the sequence represented by that identifier?

#QUESTION What is the starting position of the longest ORF in the sequence that contains it?



