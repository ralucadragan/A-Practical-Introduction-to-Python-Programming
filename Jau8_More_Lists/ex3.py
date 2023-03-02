'''
3. (a) Ask the user to enter a sentence and print out the third word of the sentence.
(b) Ask the user to enter a sentence and print out every third word of the sentence.
'''

sentence = 'Nia has three apples and two grapes and one babana.'

print(sentence[8:13])
sentence = sentence.split()
print(sentence)
print(sentence[2])
print(sentence[2::3])
