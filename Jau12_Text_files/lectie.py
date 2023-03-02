with open ('lectie_example.txt', 'r') as f:
    print(f.readlines()) # convert the content of the text file in to a list

print('------------------------')

s = open('lectie_example.txt').read() # convert the content of the text file in to a string
print(s)

print('------------------------')

lines = [line.strip() for line in open ('lectie_example.txt')] # convert the content of the text file in to a list

print('------------------------')
'''
The file is assumed to be in the same directory as your program itself. If it is in a different directory,
then you need to specify that, like below:
s = open('c:/users/heinold/desktop/file.txt').read()
'''

with open ('lectie_writefile.txt', 'w') as f:
    f.writelines('mama')
    f.writelines('\nbanana')
    f.writelines('\n')

f = open('lectie_writefile.txt', 'w')
print('This is line 1.', file=f)
print('This is line 2.', file=f)
f.close()

print('------------------------')

# Example 1 Write a program that reads a list of temperatures from a file called temps.txt, converts
# those temperatures to Fahrenheit, and writes the results to a file called ftemps.txt.

file1 = open('lectie_ex1_ftemps.txt', 'w') # se initializaeza  automat. Intai fac fisierul in care vreau sa scriu
t1 = [line.strip() for line in open('lectie_ex1_temps.txt')]
for t in t1:
    print(int(t)*9, file=file1)
file1.close()



