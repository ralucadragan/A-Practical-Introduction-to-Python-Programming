'''
7. Write a function that takes an integer n and returns a random integer with exactly n digits. For
instance, if n is 3, then 125 and 593 would be valid return values, but 093 would not because
that is really 93, which is a two-digit number.
'''

from random import randint

def random_intiger(x):
    if x == 1:
        return randint(0, 9)
    elif x == 2:
        return randint(10, 99)
    elif x == 3:
        return randint(100, 999)

nr = 2
print(random_intiger(nr))

def random_digit(n):
    start = 10 ** (n-1)
    print(f'Nr de start este: {start}')
    end = (10 ** n) - 1
    print(f'Nr de end este: {end}')
    return randint(start, end)

nr2 = 4
print(f'Random number of {nr2} digits is: {random_digit(nr2)}')