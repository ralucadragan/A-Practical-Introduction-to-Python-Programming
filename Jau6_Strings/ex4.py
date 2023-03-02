'''
4. Write a program that asks the user to enter a word and prints out whether that word contains
any vowels.
'''

word = input('Enter a word: ')

if word.count('a') >= 1 or word.count('e') >=1 or word.count('i') >=1 or word.count('o') >=1 or word.count('u') >=1:
    print(f"Your word containd {word.count('a')} letters - a. \n"
          f"Your word containd {word.count('e')} letters - e. \n"
          f"Your word containd {word.count('i')} letters - i. \n"
          f"Your word containd {word.count('o')} letters - o. \n"
          f"Your word containd {word.count('u')} letters - u. \n")
else:
    print('Your word dont contain any vowels!')