
'''
11. Section 8.3 described how to use the shuffle method to create a random anagram of a string.
Use the choice method to create a random anagram of a string.
'''

from random import shuffle

word = input('Enter a word: ')
letter_list = list(word)
print(letter_list)
shuffle(letter_list)

anagram = ''.join(letter_list)
print(anagram)