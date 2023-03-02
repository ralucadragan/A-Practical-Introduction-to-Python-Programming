'''
1. Write a program that generates and prints 50 random integers, each between 3 and 6.
'''

from random import randint

for i in range(1,50):
    nr = randint(3, 6)
    print(nr)
