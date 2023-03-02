'''
15. Use a list comprehension to create the list below, which consists of ones separated by increasingly
many zeroes. The last two ones in the list should be separated by ten zeroes.
[1,1,0,1,0,0,1,0,0,0,1,0,0,0,0,1,....]
'''

list = [1]
print(list)

for i in range (11):
    if i == 0:
        list.append(1)
    else:
        for j in range (i):
            list.append(0)
        list.append(1)
print(list)

print([[1, i*0] for i in range(11) for j in range(i)])