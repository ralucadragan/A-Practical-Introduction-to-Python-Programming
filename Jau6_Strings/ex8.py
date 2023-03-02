'''
8. At a certain school, student email addresses end with @student.college.edu, while professor
email addresses end with @prof.college.edu. Write a program that first asks the
user how many email addresses they will be entering, and then has the user enter those addresses.
After all the email addresses are entered, the program should print out a message
indicating either that all the addresses are student addresses or that there were some professor
addresses entered.
'''


ask = int(input('How many e-amil adresses you;l be entering? '))
if ask == 1:
    email = input('Enter your e-mail: ')
else:
    for i in range(ask):
        email = input(f'Enter your - {i+1} - e-mail: ')
if email.count('student') == 1:
    print ('Your e-mail adresses is for a student!')
else:
    print('Your e-mail adress is for a professor!')




