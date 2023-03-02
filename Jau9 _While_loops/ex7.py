'''
7. Recall that, given a string s, s.index('x') returns the index of the first x in s and an error
if there is no x.
(a) Write a program that asks the user for a string and a letter. Using a while loop, the
program should print the index of the first occurrence of that letter and a message if the
string does not contain the letter.
(b) Write the above program using a for/break loop instead of a while loop.
'''

string = 'barabule'
letter = 'b'

for i in string:
    if letter in string:
        print(f"The first occurrence of the letter is on position {string.find(letter)} in string.")
    else:
        print('The scring does not contain the letter!')
    break

while letter in string:
    print(f"The first occurrence of the letter is on position {string.find(letter)} in string.")
    break
else:
    print('The scring does not contain the letter!')


