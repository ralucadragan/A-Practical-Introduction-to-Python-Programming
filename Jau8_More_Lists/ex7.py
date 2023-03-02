'''
7. Write a program that estimates the average number of drawings it takes before the user’s
numbers are picked in a lottery that consists of correctly picking six different numbers that
are between 1 and 10. To do this, run a loop 1000 times that randomly generates a set of
user numbers and simulates drawings until the user’s numbers are drawn. Find the average
number of drawings needed over the 1000 times the loop runs.
'''

from random import shuffle

nr = [1,2,3,4,5,6,7,8,9,10]
user_nr = [2, 7, 10, 1, 4, 8]

shuffle(nr)
nr = []

