'''
5. Write a simple quote-of-the-day program. The program should contain a list of quotes, and
when the user runs the program, a randomly selected quote should be printed.
'''
from random import choice

quote1 = ['Nia', 'are', '5', 'mere']
quote2 = ['Nia', 'merge', 'in', 'parc']
quote3 = ['Nia', 'sare', 'coarda']

quote = []
quote.append(quote1)
quote.append(quote2)
quote.append(quote3)
print(quote)

quote_of_the_day = choice(quote)
print(quote_of_the_day)
quote_of_the_day = ' '.join(quote_of_the_day)
print(quote_of_the_day)




