'''
5. Generate a random number between 1 and 10. Ask the user to guess the number and print a
message based on whether they get it right or not.
'''

from random import randint

nr = randint(1,10)
guess = eval(input('Enter your guess: '))
if nr == guess:
    print("You got it!")
else:
    print(f'Sorry, The number is {nr}.')