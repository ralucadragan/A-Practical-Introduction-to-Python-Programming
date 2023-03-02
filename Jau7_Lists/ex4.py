'''
4. Ask the user to enter a list containing numbers between 1 and 12. Then replace all of the
entries in the list that are greater than 10 with 10.
'''

list = [1, 8, 10, 11, 12, 6, 9]

for i in range(len(list)):
    if list[i] > 10:
        list[i] = 10
print(list)