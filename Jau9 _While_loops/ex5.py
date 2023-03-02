'''
5. Write a program that allows the user to enter any number of test scores. The user indicates
they are done by entering in a negative number. Print how many of the scores are A’s (90 or
above). Also print out the average.

Peste 9 => A
Peste 8 => B
Peste 7 => C
Peste 6 => D
Peste 4 => E
4 sau sub 4 = F

'''

ask  = 1
total = 0
count_note = 0
count_a = 0
total_a = 0


while ask > 0:
    ask = int(input('Enter your scores: '))
    if ask < 0:
        break
    else:
        total = total + ask
        print(f'Your total score is: {total}')
        count_note = count_note + 1

    if ask >= 9:
        total_a = total_a + ask
        count_a = count_a + 1

print()
print('Eror!!! You enter a negative number!!!')
print(f'Your total score until now is: {total}')
print(f"You have - {count_a} -  scoares of A's! ")
print(f'The average of your scoares is: {total/count_note}')
