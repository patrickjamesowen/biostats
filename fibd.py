# -*- coding: utf-8 -*-
#Recall the definition of the Fibonacci numbers from “Rabbits and Recurrence Relations”, which followed the recurrence relation Fn=Fn−1+Fn−2 and assumed that each pair of rabbits reaches maturity in one month and produces a single pair of offspring (one male, one female) each subsequent month.
#
#Our aim is to somehow modify this recurrence relation to achieve a dynamic programming solution in the case that all rabbits die out after a fixed number of months. See Figure 4 for a depiction of a rabbit tree in which rabbits live for three months (meaning that they reproduce only twice before dying).
#
#Given: Positive integers n≤100 and m≤20.
#
#Return: The total number of pairs of rabbits that will remain after the n-th month if all rabbits live for m months.

def fib(n, m):
    bunnies = [1, 1]
    for i in range(2, n):
        if i < m:
            bunnies.append(bunnies[i-2] + bunnies[i-1])
        elif i == m or i == m+1:
            bunnies.append(bunnies[i-2] + bunnies[i-1]-1)
        else: 
            bunnies.append((bunnies[i-2] + bunnies[i-1])- bunnies[i - m - 1])
    return bunnies[-1]
n = 98
m = 16
print fib(n, m)