'''
2. Using the dictionary created in the previous problem, allow the user to enter a dollar amount
and print out all the products whose price is less than that amount.
'''

dict = {'a':105, 'b':273, 'c':36, 'd':478, 'e':53}

price = int(input('Enter an amount: '))

for i in dict:
    if dict[i] < price:
        print(f'The product with prices below - {price} - is: {i} - {dict[i]}')

