'''
2. Ask the user for a temperature. Then ask them what units, Celsius or Fahrenheit, the temperature
is in. Your program should convert the temperature to the other unit. The conversions
are F = 95
C + 32 and C = 59
(F − 32).
'''

user = int(input('Enter the temperature: '))
ask = input('What units is: Celsius or Fahrenheit? - ')

if ask == 'Celsius':
    print('We need to transform it in Fahrenheit!')
    F = (9/5) * user + 32
    print(f'Your transform temperature is: {F} Fahrenheit')
else:
    print('We need to transform it in Celsius!')
    F = int((5/9) * (user -32))
    print(f'Your transform temperature is: {F} Celsius.')