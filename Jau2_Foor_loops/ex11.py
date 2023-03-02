'''
11. Use a for loop to print a box like the one below. Allow the user to specify how wide and how
high the box should be.
*******************
* *
* *
*******************
'''

high = int(input('Haw many rows you want to print: '))
wide = int(input('Haw wide you want to print: '))

print('*' * wide)
for i in range (high-2):
    print('*' + ' ' * (wide - 2) + '*')
print('*' * wide)