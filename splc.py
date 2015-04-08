#After identifying the exons and introns of an RNA string, we only need to delete the introns and concatenate the exons to form a new string ready for translation.
#
#Given: A DNA string s (of length at most 1 kbp) and a collection of substrings of s acting as introns. All strings are given in FASTA format.
#
#Return: A protein string resulting from transcribing and translating the exons of s. (Note: Only one solution will exist for the dataset provided.)

#RNA codon table
codon = {'UUU':'F', 'CUU':'L', 'AUU':'I', 'GUU':'V',
'UUC':'F', 'CUC':'L', 'AUC':'I', 'GUC':'V',
'UUA':'L', 'CUA':'L', 'AUA':'I', 'GUA':'V',
'UUG':'L', 'CUG':'L', 'AUG':'M', 'GUG':'V',
'UCU':'S', 'CCU':'P', 'ACU':'T', 'GCU':'A',
'UCC':'S', 'CCC':'P', 'ACC':'T', 'GCC':'A',
'UCA':'S', 'CCA':'P', 'ACA':'T', 'GCA':'A',
'UCG':'S', 'CCG':'P', 'ACG':'T', 'GCG':'A',
'UAU':'Y', 'CAU':'H', 'AAU':'N', 'GAU':'D',
'UAC':'Y', 'CAC':'H', 'AAC':'N', 'GAC':'D',
'UAA':'Stop', 'CAA':'Q', 'AAA':'K', 'GAA':'E',
'UAG':'Stop', 'CAG':'Q', 'AAG':'K', 'GAG':'E',
'UGU':'C', 'CGU':'R', 'AGU':'S', 'GGU':'G',
'UGC':'C', 'CGC':'R', 'AGC':'S', 'GGC':'G',
'UGA':'Stop', 'CGA':'R', 'AGA':'R', 'GGA':'G',
'UGG':'W', 'CGG':'R', 'AGG':'R', 'GGG':'G', 'AUG': 'M'}


#remove the introns
def splice(dna, intron):
    dna = dna.replace(intron, "")
    return dna
    
#convert the dna in to rna
def dna2rna(dna):
    rna = dna.replace("T", "U")
    return rna
      
#transcripte the rna in to protein 
def transcribe(start, rna):
    transcribe = ''
    flag = 0
    for i in range(start, len(rna), 3):
        if codon.get(rna[i:i+3]) == None:
            break
        if codon.get(rna[i:i+3]) == 'Stop':
            break
        else:
            transcribe += codon.get(rna[i:i+3])
    return transcribe 

def fastaparser(f):
    lines = f.read().split('>')
    dna = []
    string = ''
    for i in range(1, len(lines)):
        work = lines[i].split()
        for j in range(1, len(work)):
            string += work[j]
        dna.append(string) 
        string = ''
    return dna
    
f = open("splc.txt")

dna = fastaparser(f)

for i in range(1, len(dna)):
    dna[0] = splice(dna[0], str(dna[i]))
    
rna = dna2rna(dna[0])

protein = transcribe(0, rna)

print protein
