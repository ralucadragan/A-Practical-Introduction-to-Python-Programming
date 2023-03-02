'''
4. Write a program that uses a dictionary that contains ten user names and passwords. The
program should ask the user to enter their username and password. If the username is not in
the dictionary, the program should indicate that the person is not a valid user of the system. If
the username is in the dictionary, but the user does not enter the right password, the program
should say that the password is invalid. If the password is correct, then the program should
tell the user that they are now logged in to the system.
'''

dict = {
    'Maria' : 123, 'Cristina' : 456, 'Stefania': 789,
    'Raluca' : 147, 'Maia': 258, 'Timea' : 369,
    'Mihaela' : 159, 'Ioana' : 357, 'Dora': 741, 'Jade': 852
}

user_name = input('Enter your user name: ')
password = int(input('Enter your password: '))

for k,v in dict.items():
    if user_name != k and password == v:
        print('That is not a valid user name!')
    elif user_name == k and password != v:
        print('Your user name is corect but your password is not!')
    elif user_name == k and password == v:
        print('You are logged in to the system!')
