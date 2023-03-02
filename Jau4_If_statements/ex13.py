'''
13. Write a program that lets the user play Rock-Paper-Scissors against the computer. There
should be five rounds, and after those five rounds, your program should print out who won
and lost or that there is a tie.
'''
import random

total_user = 0
total_computer = 0

for i in range(5):

    choises = ['rock', 'paper', 'scissors' ]
    user = input('Enter a choise: rock, paper, scissors: ')
    computer = random.choice(choises)
    print(f'Your choise is: {user}\n'
        f'Computer choise is: {computer}')

    if user == computer:
        print(f'It is a tie! Bouth players selected: {user}')
    elif user == 'rock' and computer == 'paper':
        print('Paper cover rock! You lose!')
        total_computer += 1
    elif user == 'rock' and computer == 'scissors':
        print('Rock smaches scissors! You win')
        total_user += 1
    elif user == 'paper' and computer == 'rock':
        print('Paper cover rock! You win!')
        total_user +=1
    elif user == 'paper' and computer == 'scissors':
        print('Scissors cut paper! You lose')
        total_computer +=1
    elif user == 'scissors' and computer == 'rock':
        print('Rock smaches scissors! You lose!')
        total_computer += 1
    elif user == 'scissors' and computer == 'paper':
        print('Scissors cut paper! You win')
        total_user += 1

print(f'You have {total_user} points!')
print(f'Computer have {total_computer} points!')
