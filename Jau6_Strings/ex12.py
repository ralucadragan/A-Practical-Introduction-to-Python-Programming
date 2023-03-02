'''
12. Write a program that asks the user to enter a word and then capitalizes every other letter of
that word. So if the user enters rhinoceros, the program should print rHiNoCeRoS.
'''

word = 'rhinoceros'
new_word = ''

for i in range(0,len(word)):
    if i%2 != 0:
        new_word = new_word + word[i].upper()
    else:
        new_word = new_word + word[i].lower()
print(new_word)





