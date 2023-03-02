'''
12. Write a program that gets a string from the user containing a potential telephone number.
The program should print Valid if it decides the phone number is a real phone number, and
Invalid otherwise. A phone number is considered valid as long as it is written in the form
abc-def-hijk or 1-abc-def-hijk. The dashes must be included, the phone number should contain
only numbers and dashes, and the number of digits in each group must be correct. Test your
program with the output shown below.
Enter a phone number: 1-301-447-5820
Valid
Enter a phone number: 301-447-5820
Valid
Enter a phone number: 301-4477-5820
Invalid
Enter a phone number: 3X1-447-5820
Invalid
Enter a phone number: 3014475820
Invalid
'''

phone_nr = '1-301-447-5820'
if phone_nr[0] == '1' and phone_nr[1] == '-' and phone_nr[5] == '-' and phone_nr[9] == '-' and phone_nr.count('-') == 3 and len(phone_nr) == 14:
    print('Valid')
else:
    print('Invalid')

phone_nr2 = '301-4477-5820'
if phone_nr2[3] == '-' and phone_nr2[7] == '-' and phone_nr2.count('-') == 2 and len(phone_nr2) == 12:
    print('Valid')
else:
    print('Invalid')


