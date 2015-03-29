#To allow for the presence of its varying forms, a protein motif is represented by a shorthand as follows: [XY] means "either X or Y" and {X} means "any amino acid except X." For example, the N-glycosylation motif is written as N{P}[ST]{P}.
#
#You can see the complete description and features of a particular protein by its access ID "uniprot_id" in the UniProt database, by inserting the ID number into
#
#http://www.uniprot.org/uniprot/uniprot_id
#Alternatively, you can obtain a protein sequence in FASTA format by following
#
#http://www.uniprot.org/uniprot/uniprot_id.fasta
#For example, the data for protein B5ZC00 can be found at http://www.uniprot.org/uniprot/B5ZC00.
#
#Given: At most 15 UniProt Protein Database access IDs.
#
#Return: For each protein possessing the N-glycosylation motif, output its given access ID followed by a list of locations in the protein string where the motif can be found.

import urllib

f = open("mprt.txt").read().split()

def data(inputfile):
    protein = []
    for i, line in enumerate(inputfile):
        url = "http://www.uniprot.org/uniprot/" + str(line) + ".fasta"       
        fasta = urllib.urlopen(url).readlines()
        strand = ''
        for i in range(1, len(fasta)):
            fasta[i] = fasta[i].rstrip('\n')
            strand += fasta[i]
        protein.append(strand)
    
    return protein
        
       
def location(protein):
    loc = ''
    count = 0
    for i, acid in enumerate(protein):
        if protein[i] == "N" and protein[i+1] != "P" and (protein[i+2] == "S" or protein[i+2] == "T") and protein[i+3] != "P":
            loc += str(i+1)+' '
            count += 1
    return loc, count

protein = data(f)

for i, acid in enumerate(protein):
    glyc = location(protein[i])
    if glyc[1] != 0:
        print f[i]
        print glyc[0]

