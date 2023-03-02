# Example 1 This program gets 10 numbers from the user and counts how many of those numbers are greater than 10.

count = 0
for i in range (10):
    nr = int(input('Enter a number: '))
    if nr > 0:
        count = count + 1
    else:
        print('Error Your number have to be greater than 0 !')
print(f'There are {count} numbers greater than 10.')

# 1. count=0— Start the count at 0.
# 2. count=count+1— Increase the count by 1.

'''
Example 2 This modification of the previous example counts how many of the numbers the user
enters are greater than 10 and also how many are equal to 0. To count two things we use two count
variables.
'''

count1 = 0
count2 = 0

for i in range (10):
    nr = int(input('Enter a number: '))
    if nr > 0:
        count1 = count1 + 1
    if nr == 0:
        count2 = count2 +1
print(f'There are {count1} numbers greater than 10.')
print(f'There are {count2} numbers equales to 0.')

'''
Example 1 This program will add up the numbers from 1 to 100. The way this works is that each
time we encounter a new number, we add it to our running total, s.
'''

s = 0
for i in range (1, 101):
    s = s + 1
print(f'The sum is: {s}')

'''
A flag variable can be used to let one part of your program know when something happens in
another part of the program. Here is an example that determines if a number is prime.
'''

num = int(input('Enter number: '))

flag = 0
for i in range (2, num):
    if num % 2 == 0:
        flag = 1
if flag == 1:
    print('Not prime')
else:
    print('Prime')

# A common programming task is to find the largest or smallest value in a series of values.

largest = int(input("Enter a positive number: "))

for i in range (9):
    num = int(input('Enter a positive number: '))
    if num > largest
        largest = num
print(f'Largest number is: {largest}')

