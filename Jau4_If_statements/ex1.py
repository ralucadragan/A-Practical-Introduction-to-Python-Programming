'''
1. Write a program that asks the user to enter a length in centimeters. If the user enters a negative
length, the program should tell the user that the entry is invalid. Otherwise, the program
should convert the length to inches and print out the result. There are 2.54 centimeters in an
inch.
'''

user = int(input('Enter the lenght witch you want to convert from cm in inch: '))

if user < 0:
    print('Your entry is invalid! Try anather lenght !')
else:
    inch = 2.54 * user
    print(f'Your lenght convert in inch is: {inch}')