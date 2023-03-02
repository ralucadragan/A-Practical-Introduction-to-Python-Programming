'''
3. People often forget closing parentheses when entering formulas. Write a program that asks
the user to enter a formula and prints out whether the formula has the same number of opening
and closing parentheses.
'''

formula = '{5+[23*7-(5+3+56-7)*2]*5}'

if (formula.count('{') == 1 and formula.count('}') != 1) or (formula.count('{') != 1 and formula.count('}') == 1) :
    print('Your formula si mising one {} !')
elif (formula.count('[') == 1 and formula.count(']') != 1) or (formula.count('[') != 1 and formula.count(']') == 1):
    print('Your formula si mising one [] !')
elif (formula.count('(') == 1 and formula.count(')') != 1) or (formula.count('(') != 1 and formula.count(')') == 1): \
        print('Your formula si mising one () !')
else:
    print('Your formula has all the opening and cloasing patantheses!')




