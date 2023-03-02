'''
10. Write a function called closest that takes a list of numbers L and a number n and returns
the largest element in L that is not larger than n. For instance, if L=[1,6,3,9,11] and n=8,
then the function should return 6, because 6 is the closest thing in L to 8 that is not larger than
8. Don’t worry about if all of the things in L are smaller than n.
'''

def closet(list, nr):
    list2 = []
    for i in list:
        if i < nr:
            list2.append(i)
    # print(list2)
    return max(list2)

l = [1,6,3,9,11]
n = 8
print(closet(l, n))


