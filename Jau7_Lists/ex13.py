'''
13. Write a program that removes any repeated items from a list so that each item appears at most
once. For instance, the list [1,1,2,3,4,3,0,0] would become [1,2,3,4,0].
'''

list1 = [1,1,2,3,4,3,0,0]
list2 = []

for i in range(len(list1)):
    if i not in list2:
        list2.append(i)
print(list2)

