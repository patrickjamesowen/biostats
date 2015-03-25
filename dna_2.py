#Problem
#
#In DNA strings, symbols 'A' and 'T' are complements of each other, as are 'C' and 'G'.
#
#The reverse complement of a DNA string s is the string sc formed by reversing the symbols of s, then taking the complement of each symbol (e.g., the reverse complement of "GTCA" is "TGAC").
#
#Given: A DNA string s of length at most 1000 bp.
#
#Return: The reverse complement sc of s.

f = open("dna_2.txt")
dna = f.read()

dna = dna.replace('A', 't')
dna = dna.replace('T', 'a')
dna = dna.replace('C', 'g')
dna = dna.replace('G', 'c')

dna = dna.swapcase()

dna = dna[::-1]
print dna

#or the simpler version... I didn't know 'maketrans' existed

#from string import maketrans
#s = 'AAAACCCGGT'
#print(s[::-1].translate(maketrans('ACGT', 'TGCA')))