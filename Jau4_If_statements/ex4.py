'''
4. Write a program that asks the user how many credits they have taken. If they have taken 23
or less, print that the student is a freshman. If they have taken between 24 and 53, print that
they are a sophomore. The range for juniors is 54 to 83, and for seniors it is 84 and over.
'''

ask = int(input('How many credits have you taken? '))

if ask <= 23:
    print('You are a freshman!')
elif 24 <= ask <= 53:
    print('You are a sophomore!')
elif 54 <= ask <= 83:
    print('You are a junior!')
else:
    print('You are a senior!')