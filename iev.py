#Given: Six positive integers, each of which does not exceed 20,000. The integers correspond to the number of couples in a population possessing each genotype pairing for a given factor. In order, the six given integers represent the number of couples having the following genotypes:
#
#AA-AA
#AA-Aa
#AA-aa
#Aa-Aa
#Aa-aa
#aa-aa
#Return: The expected number of offspring displaying the dominant phenotype in the next generation, under the assumption that every couple has exactly two offspring.
#
import numpy as np

def probofdom(parent1, parent2):
    numb = 0
    for i in range(len(parent1)):
        for j in range(len(parent2)):
            offspring = parent1[i] + parent2[j]
            if "A" in offspring:
                numb += 1 / 4.
    return numb 
    
dom = "AA"
het = "Aa"
rec = "aa"

p = np.zeros(6)
p[0] = probofdom(dom, dom)
p[1] = probofdom(dom, het)
p[2] = probofdom(dom, rec) 
p[3] = probofdom(het, het) 
p[4] = probofdom(het, rec)
p[5] = probofdom(rec,rec) 

f = open('iev.txt').read().split()
k = np.zeros(6)
for i, number in enumerate(f):
    k[i] = number
    
print np.sum(p*k)*2
