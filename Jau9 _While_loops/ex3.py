'''
3. A good program will make sure that the data its users enter is valid. Write a program that
asks the user for a weight and converts it from kilograms to pounds. Whenever the user
enters a weight below 0, the program should tell them that their entry is invalid and then ask
them again to enter a weight. [Hint: Use a while loop, not an if statement].
'''

ask = int(input('Enter a weight converts it from kilograms to pounds:  '))
po = 2.2046226218
transform = 0
while ask >= 0:
    transform = ask * po
    print(transform)
    break
if ask < 0:
    print('Your entry is invalid!')
    print('Enter another weight: ')
