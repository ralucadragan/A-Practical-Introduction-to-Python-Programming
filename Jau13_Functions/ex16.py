'''
16. Write a function called one_away that takes two strings and returns True if the strings are of
the same length and differ in exactly one letter, like bike/hike or water/wafer.
'''

def one_away(s1, s2):
    count = 0
    for i, j in zip(s1, s2):
        if i == j:
            count = count + 1
    print(f'The two strings have {count} letters in common.')
    if len(s1) == len(s2) and (len(s1) - count == 1):
        return True
    else:
        return False

string1 = 'water'
string2 = 'wafer'
print(one_away(string1, string2))