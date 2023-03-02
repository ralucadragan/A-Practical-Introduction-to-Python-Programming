'''
1. Write a program that counts how many of the squares of the numbers from 1 to 100 end in a 1.
'''

count = 0

for i in range(1, 101):
    if  (i * i ) % 10 == 1:
        count = count +1
print(count)

'''
2. Write a program that counts how many of the squares of the numbers from 1 to 100 end in a
4 and how many end in a 9.
'''
count1 = 0
count2 = 0

for i in range(1, 101):
    if  (i * i ) % 10 == 4:
        count1 = count1 +1
    if  (i * i ) % 10 == 9:
        count2 = count2 +1
print(count1)
print(count2)