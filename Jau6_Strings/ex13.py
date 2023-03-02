'''
13. Write a program that asks the user to enter two strings of the same length. The program
should then check to see if the strings are of the same length. If they are not, the program
should print an appropriate message and exit. If they are of the same length, the program
should alternate the characters of the two strings. For example, if the user enters abcde and
ABCDE the program should print out AaBbCcDdEe.
'''

print('Enter two strings of the same lenght!!!')
string1 = input('Enter the first string: ')
string2 = input('Enter the second string: ')
string3 = ''


if len(string1) != len(string2):
    print('The strings dont have the same lenght!!!')
else:
    for i,j in zip (string1,string2):
        string3 += i + j
    print(string3)

