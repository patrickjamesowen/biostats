#Either strand of a DNA double helix can serve as the coding strand for RNA transcription. Hence, a given DNA string implies six total reading frames, or ways in which the same region of DNA can be translated into amino acids: three reading frames result from reading the string itself, whereas three more result from reading its reverse complement.
#
#An open reading frame (ORF) is one which starts from the start codon and ends by stop codon, without any other stop codons in between. Thus, a candidate protein string is derived by translating an open reading frame into amino acids until a stop codon is reached.
#
#Given: A DNA string s of length at most 1 kbp in FASTA format.
#
#Return: Every distinct candidate protein string that can be translated from ORFs of s. Strings can be returned in any order.
from string import maketrans

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
'UGG':'W', 'CGG':'R', 'AGG':'R', 'GGG':'G'}

f = open('orf.txt') 

lines = f.read().split('>')

dna = []
string = ''
for i in range(1, len(lines)):
    work = lines[i].split()
    for j in range(1, len(work)):
        string += work[j]
    dna.append(string) 
    string = ''
dna = dna[0]

rna = dna.replace("T", "U")

def transcribe(start, rna):
    transcribe = ''
    flag = 0
    restart = 0
    for i in range(start, len(rna), 3):
        if codon.get(rna[i:i+3]) == None:
            break
        if codon.get(rna[i:i+3]) == "M":
            flag +=1
        if codon.get(rna[i:i+3]) == 'Stop' and flag != 0:
            restart = i+1
            break
        else:
            transcribe += codon.get(rna[i:i+3])
    if restart > len(rna):
        transcribe(restart, rna)
    return transcribe


def split(unsplit):
    proteins = []
    for i, base in enumerate(unsplit):
        if base == "M":
            proteins.append(unsplit[i:])
    return proteins
        
for i in range(3):
    print split(transcribe(i, rna))



