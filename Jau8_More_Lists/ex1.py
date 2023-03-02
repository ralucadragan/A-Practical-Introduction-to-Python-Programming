'''
1. Write a program that asks the user to enter some text and then counts how many articles are
in the text. Articles are the words 'a', 'an', and 'the'.
'''

from string import punctuation

a1 = 'a'
a2 = 'an'
a3 = 'the'
text = 'In the woods are tree animals: a bear, a giraffe and an pinguin.'

for i in punctuation:
    text = text.replace(i, '')
print(text)
text = text.lower()
print(text)
text1 = text.split()
print(text1)
print(f'Word {a1} appears {text1.count(a1)} times.')
print(f'Word {a2} appears {text1.count(a2)} times.')
print(f'Word {a3} appears {text1.count(a3)} times.')