'''
2. A simple way to estimate the number of words in a string is to count the number of spaces
in the string. Write a program that asks the user for a string and returns an estimate of how
many words are in the string.
'''

ask = 'Mama merge la piata sa cumpere fructe.'

count = 0
for i in ask:
    if i == ' ':
        count = count + 1
print(f'There are - {count + 1} - estimate words in the string.')