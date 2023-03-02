'''
8. Write a program that asks the user for a number of seconds and prints out how many minutes
and seconds that is. For instance, 200 seconds is 3 minutes and 20 seconds. [Hint: Use the //
operator to get minutes and the % operator to get seconds.]
'''

ask = int(input('Enter a number of seconds: '))

print(f'You have {ask // 60} minutes and {ask % 60} sec.')