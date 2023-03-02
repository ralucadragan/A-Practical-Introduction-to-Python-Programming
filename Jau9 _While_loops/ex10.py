
'''
10. Write a program that has a list of ten words, some of which have repeated letters and some
which don’t. Write a program that picks a random word from the list that does not have any
repeated letters.
'''

import random

list_words = ['ana', 'maria', 'stefania', 'stefan', 'marius', 'dorel', 'calin', 'dora', 'maia', 'paula']
list_words_new = []
list_duplicates = []


for i in list_words:
    print(i)
    for j in i:
        print(j)
        if i.count(j) > 1:
            list_duplicates.append(i)
            break
print(list_duplicates)

for k in list_words:
    if k not in list_duplicates:
        list_words_new.append(k)
print(list_words_new)

print(random.choice(list_words_new))
