'''
7. Write a program that asks the user to enter an angle between −180◦ and 180◦. Using an
expression with the modulo operator, convert the angle to its equivalent between 0◦ and
360◦.
'''

print(13%12)
print(25%12)
print(15%4)
print(289%25)


angl = float(input('Enter an agle between -180 and 180: '))
print(angl % 360)