d = {'A':100, 'B':200}
d['A'] = 400
d['C'] = 500
print(d)
del d['A']
print(d)

print('-----------------------------')

d = {'dog' : 'has a tail and goes woof!', 'cat' : 'says meow', 'mouse' : 'chased by cats'}
word = input('Enter a word: ')
print(f'The definition is: {d[word]}')

print('-----------------------------')

points = {'A':1, 'B':3, 'C':3, 'D':2, 'E':1, 'F':4, 'G':2,
'H':4, 'I':1, 'J':8, 'K':5, 'L':1, 'M':3, 'N':1,
'O':1, 'P':3, 'Q':10, 'R':1, 'S':1, 'T':1, 'U':1,
'V':4, 'W':4, 'X':8, 'Y':4, 'Z':10}

total = 0
for c in points:
    total = total + points[c]
print(total)

print('-----------------------------')

d = {'A':100, 'B':200}

letter = input('Enter a letter: ')
if letter in d:
    print('The value is', d[letter])
else:
    print('Not in dictionary')

for key in d: # prints the keys in a dictionary:
    print(key)

for key in d: # prints the values:
    print(d[key])