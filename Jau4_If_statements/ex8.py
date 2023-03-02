'''
8. A year is a leap year if it is divisible by 4, except that years divisible by 100 are not leap years
unless they are also divisible by 400. Write a program that asks the user for a year and prints
out whether it is a leap year or not.
'''

year = int(input('Enter a year: '))

if year % 4 ==0:
    if year % 100 == 0 :
        if year % 400 == 0:
            print(f'The year - {year} - is a leap year!')
        else:
            print(f'The year - {year} - is not a leap year!')
    else:
        print(f'The year - {year} - is a leap year!')
else:
    print(f'The year - {year} - is not a leap year!')