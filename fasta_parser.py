
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

