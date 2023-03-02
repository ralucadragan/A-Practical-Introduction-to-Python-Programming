'''
2. Write a program that generates a list of 20 random numbers between 1 and 100.
(a) Print the list.
(b) Print the average of the elements in the list.
(c) Print the largest and smallest values in the list.
(d) Print the second largest and second smallest entries in the list
(e) Print how many even numbers are in the list.
'''

from random import randint

list = []
for i in range (20):
    list.append(randint(1, 100))
print(f'(a) Print the list: \n{list}')
print(f'(b) Print the average of the elements in the list: {sum(list)/len(list)}')
print(f'(c) Print the largest - {max(list)} - and smallest values in the list: {min(list)}')
print(f'(d) Print the second largest -{max(list)-1} and second smallest entries in the list: {min(list)-1}')
even_count = 0
for i in list:
    if i % 2 == 0:
        even_count = even_count + 1
print(f'Print how many even numbers are in the list: {even_count}')




