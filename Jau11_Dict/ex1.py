'''
1. Write a program that repeatedly asks the user to enter product names and prices. Store all
of these in a dictionary whose keys are the product names and whose values are the prices.
When the user is done entering products and prices, allow them to repeatedly enter a product
name and print the corresponding price or a message if the product is not in the dictionary.
'''

dict = {}

for i in range (1, 6):
    product = input(f'Enter your {i} product: ')
    prices = input(f'Enter the price for your {i} product: ')
    dict[product] = prices
print(dict)
intrebare = input(f'Enter the product you whant to see the price: ')
if intrebare in dict:
    print(f'The price of product - {intrebare} - is: {dict[intrebare]}')
else:
    print('The product is not in dictionary!')