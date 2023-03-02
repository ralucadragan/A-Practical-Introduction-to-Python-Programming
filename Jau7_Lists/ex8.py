'''
8. Write a program that asks the user for an integer and creates a list that consists of the factors
of that integer.
'''

nr = 320
list = []

for i in range (1, nr+1):
    if nr % i == 0:
        list.append(i)
print(list)