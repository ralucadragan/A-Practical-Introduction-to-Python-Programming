'''
6. Ask the user to enter a number x. Use the sep optional argument to print out x, 2x, 3x, 4x,
and 5x, each separated by three dashes, like below.
Enter a number: 7
7---14---21---28---35
'''

ask = int(input('Enter a number: '))
print(f'{ask}---{ask*2}---{ask*3}---{ask*4}---{ask*5}')