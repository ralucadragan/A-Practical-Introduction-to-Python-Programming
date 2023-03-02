'''
9. A lot of cell phones have tip calculators. Write one. Ask the user for the price of the meal and
the percent tip they want to leave. Then print both the tip amount and the total bill with the
tip included.
'''

price_meal = int(input('What is the price of the meal? '))
precent_tip = int(input(('What percent of the meal you what to give the tip: ')))

print(f'So, the price of the meal is {price_meal} eur and you whant to live a {precent_tip}% tip ! '
      f'\nThe tip amount is {(price_meal*precent_tip)/100} eur.'
      f'\nThe total bill, with the tip included, is {price_meal + (price_meal*precent_tip)/100 } eur.')