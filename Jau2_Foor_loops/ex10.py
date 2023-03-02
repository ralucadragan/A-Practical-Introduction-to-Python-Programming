'''
10. Use a for loop to print a box like the one below. Allow the user to specify how wide and how
high the box should be. [Hint: print('*'*10) prints ten asterisks.]
*******************
*******************
*******************
*******************
'''

high = int(input('Haw many rows you want to print: '))
wide = int(input('Haw wide you want to print: '))

for i in range (high):
    print('*' * wide)