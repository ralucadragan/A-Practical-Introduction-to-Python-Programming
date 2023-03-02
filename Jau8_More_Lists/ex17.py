'''
17. Write a program that finds the average of all of the entries in a 4 × 4 list of integers.
'''

l = [[1,2,3,4],
     [5,6,7,8],
     [1,2,3,4],
     [5,6,7,8]]

count = 0
for i in range (4):
    for c in range (4):
        count = count + 1
print(count)

row = 0
list = ([j for row in l for j in row])
print(list)
sum = sum(list)
print(sum)
average = sum/count
print(average)