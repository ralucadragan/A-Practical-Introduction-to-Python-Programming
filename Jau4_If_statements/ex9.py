'''
9. Write a program that asks the user to enter a number and prints out all the divisors of that
number. [Hint: the % operator is used to tell if a number is divisible by something. See Section
3.2.]
'''

nr = int(input('Enter a number: '))
print(f'The divisors of numeber - {nr} - are: ')

for i in range (1, nr+1):
    if nr % i == 0:
        print(i)
