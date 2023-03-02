'''
5. Ask the user to enter a list of strings. Create a new list that consists of those strings with their
first characters removed.
'''

list_strings = ['ana', 'are', 'opt', 'mere']
new_list_strings = []


for i in range(len(list_strings)):
    new_list_strings.append(list_strings[i][1:])
print(new_list_strings)
