'''
Let’s try a guess-a-number program. The computer picks a random number, the player tries to
guess, and the program tells them if they are correct. To see if the player’s guess is correct, we need
something new, called an if statement.
'''

from random import randint

nr = randint(1,10)
guess = eval(input('Enter your guess: '))
if nr == guess:
    print("You got it!")
else:
    print(f'Sorry, The number is {nr}.')

grade = int(input('Enter your scoare: '))

if grade >= 90:
    print('A')
elif grade >= 80:
    print('B')
elif grade >= 70:
    print('C')
elif grade >= 60:
    print('D')
else:
    print('F')
