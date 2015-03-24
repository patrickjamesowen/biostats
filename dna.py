#this is a python thing for doing ROSALIND project 1
#Problem
#
#A string is simply an ordered collection of symbols selected from some alphabet and formed into a word; the length of a string is the number of symbols that it contains.
#
#An example of a length 21 DNA string (whose alphabet contains the symbols 'A', 'C', 'G', and 'T') is "ATGCTTCAGAAAGGTCTTACG."
#
#Given: A DNA string s of length at most 1000 nt.
#
#Return: Four integers (separated by spaces) counting the respective number of times that the symbols 'A', 'C', 'G', and 'T' occur in s.


#openning the file
f = open("dna.txt")
string = f.read()
#setting counters
a = 0
c = 0
g = 0
t = 0

for base in string:
    if base == "A":
        a += 1
    if base == "C":
        c += 1
    if base == "G":
        g += 1
    if base == "T":
        t += 1
        
print a, c, g, t

#Or a much quicker/more pythonic way of doing it... learning FORTRAN first starting to show...
#def qt(s):
#      return s.count("A"), s.count("G"), s.count("C"), s.count("T")