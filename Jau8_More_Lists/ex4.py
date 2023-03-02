'''
4. (a) Write a program that asks the user to enter a sentence and then randomly rearranges the
words of the sentence. Don’t worry about getting punctuation or capitalization correct.
(b) Do the above problem, but now make sure that the sentence starts with a capital, that
the original first word is not capitalized if it comes in the middle of the sentence, and
that the period is in the right place.
'''
from random import shuffle

text = 'Nu conteaza ce scriu pentru ca trebuiesc amestecate !'
text = text.split()
print(text)
shuffle(text)
print(text)
text1 = ' '.join(text)
print(text1)

t = 'Nu conteaza ce scriu pentru ca trebuiesc amestecate !'
t = t.split()
print(t)
shuffle(t)
print(t)
for i in t:
    if i == '!' or i == '.' or i == ',':
        t.remove('!')
print(t)
t.append('!')
print(t)

t1 = ' '.join(t)
print(t1)
t1 = t1.lower()
print(t1)
print(t1.capitalize())





