'''
19. Write a program that asks the user for a large integer and inserts commas into it according
to the standard American convention for commas in large numbers. For instance, if the user
enters 1000000, the output should be 1,000,000.
'''

nr = '1234567891'
list_nr = list(nr)
print(list_nr)
list_nr.insert(-3,',')
list_nr.insert(-7,',')
list_nr.insert(-11,',')
print(list_nr)

new_nr = (''.join(list_nr))
print(new_nr)