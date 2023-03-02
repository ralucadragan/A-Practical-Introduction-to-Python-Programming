'''
5. Ask the user to enter a number. Print out the square of the number, but use the sep optional
argument to print it out in a full sentence that ends in a period. Sample output is shown
below.
Enter a number: 5
The square of 5 is 25.
'''

ask = int(input('Enter a number: '))
print(f'The square of the number - {ask} -  is: {ask ** 2}.')