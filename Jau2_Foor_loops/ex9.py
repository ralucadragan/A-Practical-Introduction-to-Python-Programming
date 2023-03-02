'''
9. The Fibonacci numbers are the sequence below, where the first two numbers are 1, and each
number thereafter is the sum of the two preceding numbers. Write a program that asks the
user how many Fibonacci numbers to print and then prints that many.
1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89 . . .
'''

ask = int(input('How many Fibonacci numbers you want to print? '))

first_nr = 0
second_nr = 1
sum = 0

if ask <= 0:
    print('Please enter number greather then 0!')
else:
    for i in range(0, ask):
        print(sum, end='')
        first_nr = second_nr
        second_nr = sum
        sum = first_nr + second_nr

