'''
3. Write a function called sum_digits that is given an integer num and returns the sum of the
digits of num.
'''

def sum_digits(nr):
    sum = 0
    for i in str(nr):
        sum = sum + int(i)
    return sum

print(sum_digits(345))

def sum2(nr):
    sum = 0
    while (nr != 0):
        sum = sum + (nr % 10)
        print(nr%10)
        nr = nr // 10
    return sum
print(sum2(345))



