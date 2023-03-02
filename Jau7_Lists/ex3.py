'''
3. Start with the list [8,9,10]. Do the following:
(a) Set the second entry (index 1) to 17
(b) Add 4, 5, and 6 to the end of the list
(c) Remove the first entry from the list
(d) Sort the list
(e) Double the list
(f) Insert 25 at index 3
The final list should equal [4,5,6,25,10,17,4,5,6,10,17]
'''


list = [8, 9, 10]
print(f'Initial list: \n{list}')
list[1] = 17
print(f'(a) Set the second entry (index 1) to 17: {list}')
list.append(4)
list.append(5)
list.append(6)
print(f'(b) Add 4, 5, and 6 to the end of the list: {list}')
list.pop(0)
print(f'(c) Remove the first entry from the list: {list}')
list.sort()
print(f'(d) Sort the list: {list}')
list = list*2
print(f'(e) Double the list: {list}')
list.insert(3, 25)
print(f'(f) Insert 25 at index 3: {list}')


