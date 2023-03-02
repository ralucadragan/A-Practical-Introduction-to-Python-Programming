'''
12. Write a program that generates 100 random integers that are either 0 or 1. Then find the
longest run of zeros, the largest number of zeros in a row. For instance, the longest run of
zeros in [1,0,1,1,0,0,0,0,1,0,0] is 4.
'''

from random import randint

list = []
zero_count = 0
max_zero_count = 0

for i in range (100):
    list.append(randint(0, 1))
    if i == 0:
        zero_count = zero_count + 1
        max_zero_count = max_zero_count + 1
