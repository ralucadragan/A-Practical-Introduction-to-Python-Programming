'''
2. (a) Write a function called add_excitement that takes a list of strings and adds an exclamation
point (!) to the end of each string in the list. The program should modify the
original list and not return anything.
(b) Write the same function except that it should not modify the original list and should
instead return a new list.
'''

def add_excitement(list):
    for i in range(len(list)):
        list[i] = list[i] + '!'
    return list

def add_excitement2(list2):
    new_list = []
    for i in range (len(list2)):
        new_list.append(list2[i] + '!')
    return new_list


list = ['apple', 'peach', 'grapes', 'pineapple']
print(add_excitement(list))
list2 = ['apple', 'peach', 'grapes', 'pineapple']
print(add_excitement2(list2))




