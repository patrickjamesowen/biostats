#Given two strings s and t of equal length, the Hamming distance between s and t, denoted dH(s,t), is the number of corresponding symbols that differ in s and t. See Figure 2.
#
#Given: Two DNA strings s and t of equal length (not exceeding 1 kbp).
#
#Return: The Hamming distance dH(s,t).
from string import maketrans

f = open("mutation.txt")

dna = f.read().split()

n = 0
for i in range(len(dna[0])):
    if dna[0][i] != dna[1][i]:
        n += 1
        
print n