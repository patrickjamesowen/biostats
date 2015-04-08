def longest_substring(data):
    substring = ''
    if len(data) > 1 and len(data[0]) > 0:
        for i in range(len(data[0])):
            for j in range(len(data[0])-i+1):
                if j > len(substring) and is_substring(data[0][i:i+j], data):
                    substring = data[0][i:i+j]
    return substring

def is_substring(find, data):
    if len(data) < 1 and len(find) < 1:
        return False
    for i in range(len(data)):
        if find not in data[i]:
            return False
    return True
    
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
    
f = open("lcsm.txt")

dna = fastaparser(f)

print longest_substring(dna)