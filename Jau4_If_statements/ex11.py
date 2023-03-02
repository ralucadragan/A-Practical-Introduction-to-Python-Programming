'''
11. Write a program that asks the user for an hour between 1 and 12, asks them to enter am or pm,
and asks them how many hours into the future they want to go. Print out what the hour will
be that many hours into the future, printing am or pm as appropriate. An example is shown
below.
Enter hour: 8
am (1) or pm (2)? 1
How many hours ahead?
'''

ask1 = int(input('Enter a hour: '))
ask2 = input('Enter am(1) or pm(2): ')
ask3 = int(input('How many hours ahead?: '))

am = 'am'
pm = 'pm'

if ask2 == 1:
    if ask1 + ask3 < 12:
        new_hour = ask1 + ask3
        print(f'New hour: {new_hour} {am}')
    elif ask1 + ask3 > 12:
        new_hour = (ask1 + ask3) - 12
        print(f'New hour: {new_hour} {pm}')
    elif ask1 + ask3 == 12:
        new_hour = 12
        print(f'New hour: {new_hour} {pm}')


else:
    if ask1 + ask3 < 12:
        new_hour = ask1 + ask3
        print(f'New hour: {new_hour} {pm}')
    elif ask1 + ask3 > 12:
        new_hour = (ask1 + ask3) - 12
        print(f'New hour: {new_hour} {am}')
    elif ask1 + ask3 == 12:
        new_hour = 12
        print(f'New hour: {new_hour} {am}')


