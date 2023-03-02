'''
6. A store charges $12 per item if you buy less than 10 items. If you buy between 10 and 99
items, the cost is $10 per item. If you buy 100 or more items, the cost is $7 per item. Write a
program that asks the user how many items they are buying and prints the total cost.
'''

items = int(input('How many items are you bought? '))

if items < 10:
    print(f' You bought {items} and your total cost is: ${12 * items}')
elif 10 <= items <= 99:
    print(f' You bought {items} and your total cost is: ${10 * items}')
else:
    print(f' You bought {items} and your total cost is: ${7 * items}')