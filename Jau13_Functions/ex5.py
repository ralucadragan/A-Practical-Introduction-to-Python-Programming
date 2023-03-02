'''
5. Write a function called first_diff that is given two strings and returns the first location in
which the strings differ. If the strings are identical, it should return -1.
'''

def first_diff(string1, string2):
    if string1 == string2:
        print('The strings are identical')
        return -1
    else:
        index = 0
        for i,j in zip(string1, string2):
            if i !=j:
                break
            index += 1
        return index

s1 = 'maria'
s2 = 'marin'
print(first_diff(s1, s2))