'''
10. Wordplay – Use the file wordlist.txt for this problem. Find the following:
(a) All words ending in ime
(b) All words whose second, third, and fourth letters are ave
(c) How many words contain at least one of the letters r, s, t, l, n, e
(d) The percentage of words that contain at least one of the letters r, s, t, l, n, e ==========
(e) All words with no vowels
(f) All words that contain every vowel
(g) Whether there are more ten-letter words or seven-letter words
(h) The longest word in the list
(i) All palindromes
(j) All words that are words in reverse, like rat and tar.  ===================
(k) Same as above, but only print one word out of each pair. =========================================================
(l) All words that contain double letters next each other like aardvark or book, excluding words that end in lly  ===================
(m) All words that contain a q that isn’t followed by a u  ===================
(n) All words that contain zu anywhere in the word
(o) All words that contain ab in multiple places, like habitable
(p) All words with four or more vowels in a row =============
(q) All words that contain both a z and a w
(r) All words whose first letter is a, third letter is e and fifth letter is i
(s) All two-letter words
(t) All four-letter words that start and end with the same letter
(u) All words that contain at least nine vowels.
(v) All words that contain each of the letters a, b, c, d, e, and f in any order. There may be other letters in the word. Two examples are backfield and feedback.
(w) All words whose first four and last four letters are the same
(x) All words of the form abcd*dcba, where * is arbitrarily long sequence of letters.
(y) All groups of 5 words, like pat pet pit pot put, where each word is 3 letters, all words share
the same first and last letters, and the middle letter runs through all 5 vowels.
(z) The word that has the most i’s.
'''

#def read():
    #with open ('ex10_wordlist.txt', 'r') as rf:
        #lines = rf.read()
        #print(lines)
        #word = lines.split()
        #print(word)
#read()

with open('ex10_wordlist.txt', 'r') as rf:
    lines = rf.read()
    # print(lines)
    word = lines.split()
'''
print('---------- (a) All words ending in ime ----------')
def ending_ime():
    count = 0
    for i in word:
        if i[-3:] == 'ime':
            count += 1
            print(i)
    print(f'Total words anding with - ime - are: {count}')
ending_ime()
print('')
'''
'''
print('---------- (b) All words whose second, third, and fourth letters are ave ----------')
def ave():
    count = 0
    for i in word:
        if i[2:5] == 'ave':
            count += 1
            print(i)
    print(f'Total words whose second, third, and fourth letters are - ave -  are: {count}')
ave()
print('')
'''
'''
print('---------- (c) How many words contain at least one of the letters r, s, t, l, n, e ----------')
def contain():
    count = 0
    for i in word:
        if ('r' in i) or ('s' in i) or ('t' in i) or ('l' in i) or ('n' in i)  or ('e' in i):
            count += 1
            # print(i)
    print(f'Total words that contain at least one of the letters - r, s, t, l, n, e - are: {count}')
contain()
print('')
'''
'''
print('---------- (e) All words with no vowels ----------')
def no_vowels():
    count = 0
    for i in word:
        if ('a' not in i) and ('e' not in i) and ('i' not in i) and ('o' not in i) and ('u' not in i):
            count += 1
            #print(i)
    print(f'Total words with no vowels are: {count}')
no_vowels()
print('')
'''
'''
print('---------- (f) All words that contain every vowel ----------')
def all_vowels():
    count = 0
    for i in word:
        if ('a' in i) and ('e' in i) and ('i' in i) and ('o' in i) and ('u' in i):
            count += 1
            print(i)
    print(f'Total words with no vowels are: {count}')
all_vowels()
print('')
'''
'''
print('---------- (g) Whether there are more ten-letter words or seven-letter words ----------')
def letters():
    count_ten = 0
    count_seven = 0
    for i in word:
        if len(i) == 7:
            count_seven += 1
        elif len(i) == 10:
            count_ten += 1
    #print(count_seven)
    #print(count_ten)
    if count_seven > count_ten:
        print(f'There are more seven-letters words! Total = {count_seven} ')
    else:
        print(f'There are more ten-letters words! Total = {ten_seven} ')
letters()
print('')
'''
'''
print('---------- (h) The longest word in the list ----------')
def longest_word():
    w = max(word, key=len)
    print(f'The longesr word in the list is: {w} - has {len(w)} letters.')
longest_word()
print('')
'''
'''
print('---------- (i) All palindromes ----------')
def palindromes():
    count = 0
    for i in word:
        if i[:] == i[::-1]:
            count +=1
            print(i)
    print(f'There are - {count} - words who are palindromes!')
palindromes()
print('')
'''
'''
print('---------- (n) All words that contain zu anywhere in the word ----------')
def word_zu():
    count = 0
    for i in word:
        if 'zu' in i:
            count += 1
            print(i)
    print(f'There are - {count} - words that contain - zu - !')
word_zu()
print('')
'''
'''
print('---------- (o) All words that contain ab in multiple places, like habitable ----------')
def multiple_ab():
    count = 0
    for i in word:
        if 'ab' in i and i.count('ab') >= 2:
            count += 1
            print(i)
    print(f'There are - {count} - words that contain - ab - in multiple places!')
multiple_ab()
'''