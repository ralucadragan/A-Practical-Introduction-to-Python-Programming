'''
11. Write a program that asks the user to enter a word that contains the letter a. The program
should then print the following two lines: On the first line should be the part of the string up
to and including the first a, and on the second line should be the rest of the string. Sample
output is shown below:
Enter a word: buffalo
buffa
lo
'''

ask = input('Enter a string: ')
letter = 'a'
for i in ask:
    if letter in ask:
        print(ask[0:ask.find('a') + 1], '\n' ,ask[ask.find('a') + 1:])
        break
