'''
8. Write a program that asks the user to enter three numbers (use three separate input statements).
Create variables called total and average that hold the sum and average of the
three numbers and print out the values of total and average.
'''
x = int(input('Enter the first number: '))
y = int(input('Enter the second number: '))
z = int(input('Enter the third number: '))
total = x + y + z
average = (x + y + z)/3

print(f'The sum af the tree numbers is: {total}.')
print(f'The average af the tree numbers is: {average}.')