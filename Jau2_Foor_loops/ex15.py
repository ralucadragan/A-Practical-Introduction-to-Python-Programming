'''
15. Write a program that prints a giant letter A like the one below. Allow the user to specify how
large the letter should be.
            *
          *   *
        * * * * *
       *         *
      *            *
'''
n = 5
for i in range(n):
    for j in range (n):
        if (j == 0 or j == n-1):
            print('*', end=' ')
        else:
            print(' ', end=' ')
    print()

print('----------------------------')

n = 5
for i in range(n):
    for j in range (n):
        if (i == n // 2 or j == n // 2):
            print('*', end=' ')
        else:
            print(' ', end=' ')
    print()

print('----------------------------')

n = 5
for i in range(n):
    for j in range (n):
        if (i == j or i + j == n - 1):
            print('*', end=' ')
        else:
            print(' ', end=' ')
    print()

print('----------------------------')

n = 5
for i in range(n):
    for j in range (n):
        if (i == 0 or i == n-1 or j == 0 or j == n-1):
            print('*', end=' ')
        else:
            print(' ', end=' ')
    print()

print('----------------------------')

n = 5
for i in range(n):
    for j in range(i + 1):
        if (i == n-1 or j == 0 or i == j):
            print('*', end=' ')
        else:
            print(' ', end=' ')
    print()

print('------------------------------')

n = 5
for i in range(n):
    for j in range(i, n):
        if (i == 0 or j == i or j == n-1):
            print('*', end=' ')
        else:
            print(' ', end=' ')
    print()

print('------------------------------')

n = 5
for i in range(n):
    for j in range(i, n):
        print(' ', end=' ')
    for j in range(i):
        if (i == n - 1 or j == 0):
            print('*', end=' ')
        else:
            print(' ', end=' ')
    for j in range(i + 1):
        if (i == n - 1 or j == i):
            print('*', end=' ')
        else:
            print(' ', end=' ')
    print()

print('------------------------------')

n = 5
for i in range(n):
    for j in range(i, n):
        print(' ', end=' ')
    for j in range(i):
        if (j == 0 or i == n // 2):
            print('*', end=' ')
        else:
            print(' ', end=' ')
    for j in range(i + 1):
        if (j == i or i == n // 2):
            print('*', end=' ')
        else:
            print(' ', end=' ')
    print()