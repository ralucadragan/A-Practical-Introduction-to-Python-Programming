'''
7. Write a program that asks the user for two numbers and prints Close if the numbers are
within .001 of each other and Not close otherwise.
'''

a = float(input('Enter your first number: '))
b = float(input('Enter your second number: '))

if a - b <=0.001:
    print('Close')
else:
    print('Not Clouse')