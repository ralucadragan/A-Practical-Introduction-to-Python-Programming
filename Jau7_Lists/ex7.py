'''
7. Write a program that takes any two lists L and M of the same size and adds their elements
together to form a new list N whose elements are sums of the corresponding elements in L
and M. For instance, if L=[3,1,4] and M=[1,5,9], then N should equal [4,6,13].
'''

l = [3, 1, 4]
m = [1, 5, 9]
n = []

for i in range(len(l)):
    n.append(l[i] + m[i])
print(n)

