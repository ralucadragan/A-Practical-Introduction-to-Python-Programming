'''
2. (a) Write a program that uses a while loop (not a for loop) to read through a string and print
the characters of the string one-by-one on separate lines.
(b) Modify the program above to print out every second character of the string.
'''

string = 'alabalaportocala'

for i in string:
    print(i)

print('---------------------')

i = 0
while i <= len(string):
    i = i + 1
    print (string[i-2])

print('---------------------')

i = 0
while i <= len(string):
    i = i + 2
    print (string[i-2])