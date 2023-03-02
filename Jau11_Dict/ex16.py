'''
16. (a) Write a program that converts Roman numerals into ordinary numbers. Here are the
conversions: M=1000, D=500, C=100, L=50, X=10, V=5 I=1. Don’t forget about things
like IV being 4 and XL being 40.
(b) Write a program that converts ordinary numbers into Roman numerals
'''

roman_numbers = {
    'M' : 1000, 'D' : 500, 'C' : 100, 'L' : 50,
    'X' : 10, 'V' : 5, 'I' : 1
}
list_roman = list(roman_numbers)
print(list_roman)
list_cifre = list(roman_numbers.values())
print(list_cifre)

nr = int(input('Enter a number: '))

for i in list_roman:
    for j in list_cifre:
        if nr > 0 and nr <= 3:
            nr_tranformat = i * nr
        elif nr == 4:
            nr_tranformat = list_roman[-1] + list_roman[-2]
        elif nr == 5:
            nr_tranformat = list_roman[-2]
        elif nr > 4 and nr <= 8:
            nr_tranformat = list_roman[-2] + list_roman[-1] * (nr-5)
        elif nr == 9:
            nr_tranformat = list_roman[-1] + list_roman[-3]
        elif nr == 10:
            nr_tranformat = list_roman[-3]
print(nr_tranformat)