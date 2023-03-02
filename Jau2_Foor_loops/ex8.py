'''
8. Write a program that asks the user for their name and how many times to print it. The program
should print out the user’s name the specified number of times.
'''

ask = input('Enter your name: ')
times = int(input('How many times you want to multiply your name: '))

for i in range(times):
    print(ask)