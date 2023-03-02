'''
17. Write a program that generates the 26-line block of letters partially shown below. Use a loop
containing one or two print statements.
abcdefghijklmnopqrstuvwxyz
bcdefghijklmnopqrstuvwxyza
cdefghijklmnopqrstuvwxyzab
...
yzabcdefghijklmnopqrstuvwx
zabcdefghijklmnopqrstuvwxy
'''

abc= 'abcdefghijklmnopqrstuvwxyz'
print(abc)

for i in range(25):
    abc = abc[1:len(abc)] + abc[0]
    print(abc)
