'''
1. Write a program that asks the user to enter a list of integers. Do the following:
(a) Print the total number of items in the list.
(b) Print the last item in the list.
(c) Print the list in reverse order.
(d) Print Yes if the list contains a 5 and No otherwise.
(e) Print the number of fives in the list.
(f) Remove the first and last items from the list, sort the remaining items, and print the result.
(g) Print how many integers in the list are less than 5.
'''

list = [1, 4, 8, 0, 15, 3, 45, 23, 97, 5]
print(f'(a) Print the total number of items in the list: {len(list)}')
print(f'(b) Print the last item in the list: {list[-1]}')
print(f'(c) Print the list in reverse order: {list[::-1]}')
if 5 in list:
    print('Yes if the list contains a 5!')
else:
    print('The list dos not contains a 5!')
print(f'(e) Print the number of fives in the list: {list.count(5)}')
del list[0]
del list[-1]
print(f'(f) Remove the first and last items from the list, sort the remaining items, and print the result: {sorted(list)}')
count = 0
for i in list:
    if i < 5:
        count = count + 1
print(f'(g) Print how many integers in the list are less than 5: {count}')
