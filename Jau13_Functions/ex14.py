'''
14. Write a function called is_sorted that is given a list and returns True if the list is sorted
and False otherwise.
'''

def is_sorted(l):
    if l == sorted(l):
        return True
    else:
        return False

list = [1, 2, 3, 4, 5]
print(is_sorted(list))
