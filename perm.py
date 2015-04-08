# -*- coding: utf-8 -*-
#A permutation of length n is an ordering of the positive integers {1,2,…,n}. For example, π=(5,3,2,1,4) is a permutation of length 5.
#
#Given: A positive integer n≤7.
#
#Return: The total number of permutations of length n, followed by a list of all such permutations (in any order).

import itertools
n = 6
array = range(1, n+1)

perms = []
count = 0
for length in range(2, len(array)+1):
    for p in itertools.permutations(array, length):
        if len(p) == n:
            count += 1
            string = ''
            for i in range(n):
                string += str(p[i]) + ' '
            perms.append(string)
            
#print count
#for line in perms:
#    print line

f = open('outfile.txt', 'w')

f.write(str(count)+'\n')
for line in perms:
    f.write(line+'\n')
f.close()