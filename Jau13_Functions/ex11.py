'''
11. Write a function called matches that takes two strings as arguments and returns how many
matches there are between the strings. A match is where the two strings have the same character
at the same index. For instance, 'python' and 'path' match in the first, third, and
fourth characters, so the function should return 3.
'''

def matches(s1, s2):
    count = 0
    for i, j in zip(s1, s2):
        if i == j:
            count = count + 1
    return count

string1 = 'python'
string2 = 'pytoon'
print(matches(string1, string2))