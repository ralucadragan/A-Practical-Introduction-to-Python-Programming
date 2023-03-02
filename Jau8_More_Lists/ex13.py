'''
13. Let L be a list of strings. Write list comprehensions that create new lists from L for each of the
following.
(a) A list that consists of the strings of s with their first characters removed
(b) A list of the lengths of the strings of s
(c) A list that consists of only those strings of s that are at least three characters long
'''

string = ['Ana', 'are', 'sapte', 'mere']
print([i[1:len(string)+1] for i in string])
print([len(b) for b in string])
print([a for a in string if len(a) > 3])