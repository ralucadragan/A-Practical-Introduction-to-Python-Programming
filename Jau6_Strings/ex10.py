'''
10. Write a program that asks the user to enter a string, then prints out each letter of the string
doubled and on a separate line. For instance, if the user entered HEY, the output would be
HH
EE
YY
'''

ask = input('Enter a string: ')
for i in range(len(ask)):
    print(ask[i]*2)