'''
10. Write a censoring program. Allow the user to enter some text and your program should print
out the text with all the curse words starred out. The number of stars should match the length
of the curse word. For the purposes of this program, just use the“curse” words darn, dang,
freakin, heck, and shoot. Sample output is below:
Enter some text: Oh shoot, I thought I had the dang problem
figured out. Darn it. Oh well, it was a heck of a freakin try.
Oh *****, I thought I had the **** problem figured out.
**** it. Oh well, it was a **** of a ****** try.
'''

text = 'Oh shoot , I thought I had the dang problem figured out. Darn it . Oh well , it was a heck of a freakin try .'
curse = ['curse', 'darn', 'dang', 'freakin', 'heck','shoot']
curse_stars = []

for i in curse:
    curse_stars.append('*' * len(i))
print(curse)
print(curse_stars)

text = text.split()
print(text)

text_stars = []
for m in text:
    for n in curse:
        if m == n:
            print(f'The curse word is: {m}')


print(text)





