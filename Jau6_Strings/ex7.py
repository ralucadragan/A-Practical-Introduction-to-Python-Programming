'''
7. Write a program that asks the user to enter a word and determines whether the word is a
palindrome or not. A palindrome is a word that reads the same backwards as forwards.
'''

ask = input(('Enter a word: '))

if ask[:] == ask[::-1]:
    print('Your word is polidrome!')
else:
    print('Your word is not polidrome! Try another word!')