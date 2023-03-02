'''
10. Write a program that rotates the elements of a list so that the element at the first index moves
to the second index, the element in the second index moves to the third index, etc., and the
element in the last index moves to the first index.
'''

list = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
new_list = []

new_list.append(list[-1])
for i in range(len(list)):
    new_list.append(list[i])
del new_list[-1]
print(new_list)