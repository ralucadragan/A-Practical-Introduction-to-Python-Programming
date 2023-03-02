'''
12. Use a for loop to print a triangle like the one below. Allow the user to specify how high the
triangle should be.
*
**
***
****
'''

high = int(input('Please specify how high you want to be the triangle: '))

for i in range (1,high+1):
    print ('* ' * i)
print('------------------------------')
for i in range(high):
    for j in range(i + 1):
        print('*', end=' ')
    print() # take us to new row every time

print('------------------------------')

'''
13. Use a for loop to print an upside down triangle like the one below. Allow the user to specify
how high the triangle should be.
****
***
**
*
'''

high = int(input('Please specify how high you want to be the triangle: '))

for i in range (high ,0, -1):
    print ('* ' * i)

print('------------------------------')

for i in range(high):
    for j in range(i, high):
        print('*', end=' ')
    print()

print('------------------------------')

'''
14. Use for loops to print a diamond like the one below. Allow the user to specify how high the
diamond should be.
*
***
*****
*******
*****
***
'''

n = int(input('Please specify how high you want to be the diamond: '))
for i in range(n -1):
    for j in range(i, n):
        print(' ', end=' ')
    for j in range(i):
        print('*', end=' ')
    for j in range(i + 1):
        print('*', end=' ')
    print()

for i in range(n):
    for j in range(i+1):
        print(' ', end=' ')
    for j in range(i, n-1):
         print('*', end=' ')
    for j in range(i, n):
         print('*', end=' ')
    print()

print('------------------------------')

# we have two triangle: 1 decresing triangle of space and one incresing triangle of stars

n = 5
for i in range(n):
    for j in range(i, n):
        print(' ', end=' ')
    for j in range(i + 1):
        print('*', end=' ')
    print()

print('------------------------------')

n = 5
for i in range(n):
    for j in range(i + 1):
        print('*', end=' ')
    for j in range(i, n):
        print(' ', end=' ')
    print()

print('------------------------------')

n = 5
for i in range(n):
    for j in range(i, n):
        print(' ', end=' ')
    for j in range(i):
        print('*', end=' ')
    for j in range(i + 1):
        print('*', end=' ')
    print()

print('------------------------------')

n = 5
for i in range(n):
    for j in range(i+1):
        print(' ', end=' ')
    for j in range(i, n-1):
         print('*', end=' ')
    for j in range(i, n):
         print('*', end=' ')
    print()

print('------------------------------')

n = 5
for i in range(n):
    for j in range(i, n):
        print(' ', end=' ')
    for j in range(i):
        print('*', end=' ')
    for j in range(i + 1):
        print('*', end=' ')
    for j in range(i, n-1):
        print(' ', end=' ')
    for j in range(i, n-1):
        print(' ', end=' ')
    for j in range(i):
        print('*', end=' ')
    for j in range(i + 1):
        print('*', end=' ')

    print()