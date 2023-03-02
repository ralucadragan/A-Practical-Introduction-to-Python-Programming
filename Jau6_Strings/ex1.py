'''
1. Write a program that asks the user to enter a string. The program should then print the following:
(a) The total number of characters in the string
(b) The string repeated 10 times
(c) The first character of the string (remember that string indices start at 0)
(d) The first three characters of the string
(e) The last three characters of the string
(f) The string backwards
(g) The seventh character of the string if the string is long enough and a message otherwise
(h) The string with its first and last characters removed
(i) The string in all caps
(j) The string with every a replaced with an e
(k) The string with every letter replaced by a space
'''

string = 'Blablablu'

print(f'(a) The total number of characters in the string: {len(string)}')
print(f'(b) The string repeated 10 times: {string * 10}')
print(f'(c) The first character of the string: {string[0]}')
print(f'(d) The first three characters of the string: {string[ :3]}')
print(f'(e) The last three characters of the string: {string[-3:]}')
print(f'(f) The string backwards: {string[ : :-1]}')
if len(string) >= 7:
    print(f'(g) The seventh character of the string: {string[6]}')
else:
    print('Yout string is not long enough.')
print(f'(h) The string with its first and last characters removed: {string[1:-1]}')
print(f'(i) The string in all caps: {string.upper()}')
print(f"(j) The string with every a replaced with an e: {string.replace('a','e')}")
