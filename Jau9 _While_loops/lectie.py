
# while True:
# # statements to be repeated go here

'''
from random import randint

secret_nr = randint(1,10)
guess = 0
while guess != secret_nr:
    guess = input('Guess the secret nr: ')
print('You finaly got it!')
'''

i = 0
while i<10:
    print(i)
    i = i+1

i = 0
while i<50:
    print(i)
    i = i+2
print('Bye!')

# The break statement can be used to break out of a for or while loop before the loop is finished.
for i in range(10):
    num = eval(input('Enter number: '))
    if num<0:
        break

i = 0
num  = 1
while i<10 and num>0:
    num = eval(input('Enter a number: '))

# There is an optional else that you can use with break statements. The code indented under the
# else gets executed only if the loop completes without a break happening.

for i in range(10):
    num = eval(input('Enter number: '))
    if num < 0:
        print('Stopped early')
        break
else:
    print('User entered all ten values')


from random import randint

secret_nr = randint(1,10)
num_guess = 0 # este nr de incercari.
while num_guess != secret_nr and num_guess <= 4:
    guess = int(input('Enter your gues (1-10): '))
    num_guess = num_guess + 1
    if guess > secret_nr:
        print('Higher')
    elif guess < secret_nr:
        print('Lower')
    else:
        print('You got it!')
if num_guess == 5 and guess != secret_nr:
    print(f'You lose. The corect number is: {secret_nr}')

