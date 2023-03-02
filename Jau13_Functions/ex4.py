'''
4. The digital root of a number n is obtained as follows: Add up the digits n to get a new number.
Add up the digits of that to get another new number. Keep doing this until you get a number
that has only one digit. That number is the digital root.
For example, if n = 45893, we add up the digits to get 4 + 5 + 8 + 9 + 3 = 29. We then add up
the digits of 29 to get 2 + 9 = 11. We then add up the digits of 11 to get 1 + 1 = 2. Since 2 has
only one digit, 2 is our digital root.
'''

def digital_root(nr):
    sum = 0
    while (nr != 0):
        sum = sum + (nr % 10)
        nr = nr // 10
    print(f'Suma 1 este: {sum}')

    sum2 = 0
    nr2 = sum
    while (nr2 != 0):
        sum2 = sum2 + (nr2 % 10)
        nr2 = nr2 // 10
    print(f'Suma 2 este: {sum2}')

    if sum2 > 9:
        sum3 = 0
        nr3 = sum2
        while (nr3 != 0):
            sum3 = sum3 + (nr3 % 10)
            nr3 = nr3 // 10
        print(f'Suma 3 este: {sum3}')
        return (sum3)
    else:
        return (sum2)

print(digital_root(45893))


