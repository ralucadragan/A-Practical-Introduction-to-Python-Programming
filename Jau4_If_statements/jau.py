
total_user1 = 0
total_user2 = 0

for i in range(5):

    choises = ['rock', 'paper', 'scissors', 'hammer']
    user1 = input('Enter a choise User 1: rock, paper, scissors, hammer: ')
    user2 = input('Enter a choise User 2: rock, paper, scissors, hammer: ')
    print(f'User1 choose is: {user1}\n'
        f'User2 choise is: {user2}')

    if user1 == user2:
        print(f'It is a tie! Bouth players selected: {user1}')

    elif user1 == 'rock' and user2 == 'scissors':
        print('Rock smaches scissors! User1 win!')
        total_user1 += 1
    elif user1 == 'rock' and user2 == 'paper':
        print('Paper cover rock! User2 win!')
        total_user2 += 1
    elif user1 == 'rock' and user2 == 'hammer':
        print('Hammer beats rock! User2 win!')
        total_user2 += 1

    elif user1 == 'scissors' and user2 == 'paper':
        print('Scissors cut paper! User1 win!')
        total_user1 += 1
    elif user1 == 'scissors' and user2 == 'hammer':
        print('Hammer smaches scissors! User2 win!')
        total_user2 += 1
    elif user1 == 'scissors' and user2 == 'rock':
        print('Rock smaches scissors! User2 win!')
        total_user2 += 1

    elif user1 == 'paper' and user2 == 'rock':
        print('Paper cover rock! User1 win!')
        total_user1 +=1
    elif user1 == 'paper' and user2 == 'scissors':
        print('Scissors cut paper! User2 win!')
        total_user2 +=1
    elif user1 == 'paper' and user2 == 'hammer':
        print('Hammer smaches paper! User2 win!')
        total_user2 +=1

print(f'You have {total_user1} points!')
print(f'Computer have {total_user2} points!')