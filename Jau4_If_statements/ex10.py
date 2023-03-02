'''
10. Write a multiplication game program for kids. The program should give the player ten randomly
generated multiplication questions to do. After each, the program should tell them
whether they got it right or wrong and what the correct answer is.
Question 1: 3 x 4 = 12
Right!
Question 2: 8 x 6 = 44
Wrong. The answer is 48.
...
...
Question 10: 7 x 7 = 49
Right.
'''

from random import randint

print('You have 10 multiplication test! ')
for i in range(10):
    x = randint(0, 10)
    y = randint(0, 10)
    print(f'You have to multiplicate two numbers {x} and {y} !')
    raspuns = int(input('Enter the answer: '))
    if raspuns == x * y:
        print('You got it right!')
    else:
        print(f'You got it wrong! The corect answer is {x * y}.')

