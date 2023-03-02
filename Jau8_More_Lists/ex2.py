'''
2. Write a program that allows the user to enter five numbers (read as strings). Create a string
that consists of the user’s numbers separated by plus signs. For instance, if the user enters 2,
5, 11, 33, and 55, then the string should be '2+5+11+33+55'.
'''

nr = ['2', '5', '11', '33', '55']
nr1 = ''.join(nr)
print(nr1)
nr2 = ' '.join(nr)
print(nr2)
nr3 = ','.join(nr)
print(nr3)
nr4 = '***'.join(nr)
print(nr4)

nr = '+'.join(nr)
print(nr)