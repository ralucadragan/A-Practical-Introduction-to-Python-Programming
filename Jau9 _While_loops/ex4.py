'''
4. Write a program that asks the user to enter a password. If the user enters the right password,
the program should tell them they are logged in to the system. Otherwise, the program
should ask them to reenter the password. The user should only get five tries to enter the
password, after which point the program should tell them that they are kicked off of the
system.
'''

ask = input('Enter your password: ')
incercari = 0
password = 'mama'

while ask != password and incercari < 5:
    ask = input('Incorect password! Try another password: ')
    incercari = incercari + 1
if password == ask and incercari <=5:
    print('You are login in to the system!')
