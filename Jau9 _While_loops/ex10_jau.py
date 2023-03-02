'''
10. Write a program that has a list of ten words, some of which have repeated letters and some
which don’t. Write a program that picks a random word from the list that does not have any
repeated letters.
'''


list_words = ['ana', 'maria', 'stefania', 'stefan', 'marius', 'dorel', 'calin', 'dora', 'maia', 'paula']
list_words_new = []
duplicates = []

cuvant = list_words[0]
''' se alege un cuvant'''
#for cuvant in list_words:
for i in range(0, len(cuvant)):
    count = 1
    for j in range(i+1, len(cuvant)):
        if (cuvant[i] == cuvant[j] and cuvant[i] != ''):
            count = count + 1
            #Set string[j] to avoid visited caracter
            cuvant = cuvant[:j] + '0' + cuvant[j+1:]
        #A caracter is coniderd as duplicate if count is greater then 1
    if(count > 1 and cuvant[i] != '0'):
        print(cuvant[i])

print('------------------')
