'''
6. Write a simple lottery drawing program. The lottery drawing should consist of six different
numbers between 1 and 48.
'''

from random import choice

lottery_nr = [1, 2, 3, 4, 5, 6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24,25,26,27,28,29,30,31,32,33,34,35,36,37,38,39,40,41,42,43,44,45,46,47,48]
for i in range(6):
    print(choice(lottery_nr), end=' ')
