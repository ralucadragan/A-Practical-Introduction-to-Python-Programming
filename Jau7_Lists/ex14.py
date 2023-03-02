'''
14. Write a program that asks the user to enter a length in feet. The program should then give
the user the option to convert from feet into inches, yards, miles, millimeters, centimeters,
meters, or kilometers. Say if the user enters a 1, then the program converts to inches, if they
enter a 2, then the program converts to yards, etc. While this can be done with if statements,
it is much shorter with lists and it is also easier to add new conversions if you use lists.
'''
feet = 1
inches = 12 * feet
yard = feet/3
miles = feet * 0.000189394
ml = feet * 304.8
cm = feet * 30.48

list1 = [inches, yard, miles, ml,cm]
list2 = []
print(list1)

ask = int(input('Enter nr of feet you want to transform: '))
for i in range(len(list1)):
    list2.append(list1[i]*ask)
print(list2)

number = int(input('Enter a number between 1 and 5: '))
for i in range(len(list1)):
    if i+1 == number:
        print(list1[i])

