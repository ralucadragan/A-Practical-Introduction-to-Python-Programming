'''
18. The goal of this exercise is to see if you can mimic the behavior of the in operator and the
count and index methods using only variables, for loops, and if statements.
(a) Without using the in operator, write a program that asks the user for a string and a letter
and prints out whether or not the letter appears in the string.
(b) Without using the count method, write a program that asks the user for a string and a
letter and counts how many occurrences there are of the letter in the string.
(c) Without using the index method, write a program that asks the user for a string and
a letter and prints out the index of the first occurrence of the letter in the string. If the
letter is not in the string, the program should say so.
'''

# (a) Without using the in operator, write a program that asks the user for a string and a letter
# and prints out whether or not the letter appears in the string.

string = input('Enter a string: ')
letter = input('Enter a letter: ')

if string.count(letter) == 0:
    print(f'The letter - {letter} - is not in the tring! ')
else:
    print(f'The letter - {letter} - is in the tring! ')

# (b) Without using the count method, write a program that asks the user for a string and a
# letter and counts how many occurrences there are of the letter in the string.

string2 = input('Enter a string: ')
letter2 = input('Enter a letter: ')

count = 0
for i in string2:
    if i == letter2:
        count = count + 1
print(f'The letter - {letter2} - appered {count} in the string.')

# (c) Without using the index method, write a program that asks the user for a string and
# a letter and prints out the index of the first occurrence of the letter in the string. If the
# letter is not in the string, the program should say so.

string3 = input('Enter a string: ')
letter3 = input('Enter a letter: ')

if string3.find(letter3) == 0:
    print(f'The letter - {letter3} - is not in the tring! ')
else:
    print(f'The index of the first occurrence of the letter - {letter3} - is {string3.find(letter3)}.')
