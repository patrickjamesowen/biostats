# -*- coding: utf-8 -*-
#A matrix is a rectangular table of values divided into rows and columns. An m×n matrix has m rows and n columns. Given a matrix A, we write Ai,j to indicate the value found at the intersection of row i and column j.
#
#Say that we have a collection of DNA strings, all having the same length n. Their profile matrix is a 4×n matrix P in which P1,j represents the number of times that 'A' occurs in the jth position of one of the strings, P2,j represents the number of times that C occurs in the jth position, and so on (see below).
#
#A consensus string c is a string of length n formed from our collection by taking the most common symbol at each position; the jth symbol of c therefore corresponds to the symbol having the maximum value in the j-th column of the profile matrix. Of course, there may be more than one most common symbol, leading to multiple possible consensus strings.
#
#A T C C A G C T
#G G G C A A C T
#A T G G A T C T
#DNA Strings	A A G C A A C C
#T T G G A A C T
#A T G C C A T T
#A T G G C A C T
#A   5 1 0 0 5 5 0 0
#Profile	C   0 0 1 4 2 0 6 1
#G   1 1 6 3 0 1 0 0
#T   1 5 0 0 0 1 1 6
#Consensus	A T G C A A C T
#Given: A collection of at most 10 DNA strings of equal length (at most 1 kbp) in FASTA format.
#
#Return: A consensus string and profile matrix for the collection. (If several possible consensus strings exist, then you may return any one of them.)
import numpy as np


f = open("cons.txt")

lines = f.read().split('>')
dna = []
string = ''
for i in range(1, len(lines)):
    work = lines[i].split()
    for j in range(1, len(work)):
        string += work[j]
    dna.append(string) 
    string = ''




profile = np.zeros((4, len(dna[0])))

#building up the profile
for dna in dna: 
    for i, base in enumerate(dna):
        if base == 'A':
            profile[0, i] += 1
        if base == 'C':
            profile[1, i] += 1
        if base == 'G':
            profile[2, i] += 1
        if base == 'T':
            profile[3, i] += 1

outputdna = np.argmax(profile, 0)

dnastring = ''

for base in outputdna:
    if base == 0:
        dnastring += 'A'
    if base == 1:
        dnastring += 'C'
    if base == 2:
        dnastring += 'G'
    if base == 3:
        dnastring += 'T'
            
astring = "A:"
cstring = "C:"
gstring = "G:" #fnar!
tstring = "T:" 
#there's got to be a neater way of doing this!
for count in profile[0]:
    astring += ' ' + str(int (count))
for count in profile[1]:
    cstring += ' ' + str(int(count))
for count in profile[2]:
    gstring += ' ' + str(int(count))
for count in profile[3]:
    tstring += ' ' + str(int(count))
    
print dnastring 
print astring
print cstring
print gstring
print tstring

