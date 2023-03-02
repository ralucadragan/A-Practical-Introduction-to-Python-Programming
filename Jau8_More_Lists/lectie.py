from random import choice
from random import sample
from random import shuffle

name = ['Joe', 'Bob', 'Sue', 'Sally']
curent_player = choice(name) # We can use choice to pick a name from a list of names.
print(curent_player)
team = sample(name, 2) # Whereas choice picks one item from a list, sample can be used to pick several.
print(team)

s='abcdefghijklmnopqrstuvwxyz1234567890!@#$%^&*()'
for i in range(5):
    print(choice(s), end='')
print(i)

# Here is a nice use of shuffle to pick a random ordering of players in a game.
players = ['Joe', 'Bob', 'Sue', 'Sally']
shuffle(players)
for p in players:
    print(p, 'it is your turn.')

'''
Here we use shuffle divide a group of people into teams of two. Assume we are
given a list called names.
'''
shuffle(players)
teams = []
for i in range(0,len(players),2):
    teams.append([players[i], players[i+1]])
print(teams)

s = 'Hi! This is a test.'
print(s.split())

from string import punctuation
for c in punctuation:
    s = s.replace(c, '')
print(s)

'''
Here is a program that counts how many times a certain word occurs in a string.
'''
for c in punctuation:
    s = s.replace(c, '')
s = s.lower()
print(s)
l = s.split()
word = 'is'
print(f'word {word} appears {l.count(word)} times.')

string = 'Hello'
l = [1, 14, 5, 9, 12]
m = ['one', 'two', 'three', 'for', 'five', 'six']

l = [i*10 for i in l]
print(l)
c = [c*2 for c in string]
print(c)
m = [m[0] for m in m]
print(m)
l = [j for j in l if j < 100]
print(l)
