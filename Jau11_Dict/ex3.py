'''
3. For this problem, use the dictionary from the beginning of this chapter whose keys are month
names and whose values are the number of days in the corresponding months.
(a) Ask the user to enter a month name and use the dictionary to tell them how many days
are in the month.
(b) Print out all of the keys in alphabetical order.
(c) Print out all of the months with 31 days.
(d) Print out the (key-value) pairs sorted by the number of days in each month
(e) Modify the program from part (a) and the dictionary so that the user does not have to
know how to spell the month name exactly. That is, all they have to do is spell the first
three letters of the month name correctly.
'''

days = {'January':31, 'February':28, 'March':31, 'April':30,
'May':31, 'June':30, 'July':31, 'August':31,
'September':30, 'October':31, 'November':30, 'December':31}

# (a) Ask the user to enter a month name and use the dictionary to tell them how many days
# are in the month
ask = input('Enter a month: ')
print(f'In mounth - {ask} - are {days[ask]} days.')

#(b) Print out all of the keys in alphabetical order.
print(sorted(days.keys()))

# (c) Print out all of the months with 31 days.
for i in days:
    if days[i] == 31:
        print([i])

# (d) Print out the (key-value) pairs sorted by the number of days in each month
print(sorted(days.items(), key=lambda kv:kv[1]))

# (e) Modify the program from part (a) and the dictionary so that the user does not have to
# know how to spell the month name exactly. That is, all they have to do is spell the first
# three letters of the month name correctly.
jau = input('Enter the first 3 latters of the month: ')
for i in days:
    #print(i[0:3])
    if i[0:3] == jau:
        print(f'In mounth - {i} - are {days[i]} days')


