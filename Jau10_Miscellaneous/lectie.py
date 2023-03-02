
for i in range(1, 10001):
    s = str(i)
    if s == s[::-1]:
        print(s)
print('----------------------------')

birthday = 'January 1, 1991'
year = int(birthday[-4:])
print(year)
# The year is in the last four characters of birthday. We use int to convert those characters into an
# integer so we can do math with the year.

print('----------------------------')