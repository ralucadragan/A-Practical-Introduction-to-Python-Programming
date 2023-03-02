'''
4. You are given a file called students.txt. A typical line in the file looks like:
walter melon    melon@email.msmary.edu      555-3141
There is a name, an email address, and a phone number, each separated by tabs. Write a
program that reads through the file line-by-line, and for each line, capitalizes the first letter
of the first and last name and adds the area code 301 to the phone number. Your program
should write this to a new file called students2.txt. Here is what the first line of the new
file should look like:
Walter Melon    melon@email.msmary.edu      301-555-3141
'''

with open ('ex4_input.txt', 'r') as rf:
    content = rf.readlines()
    print(content)
    words = content[0].split()
    print(words)


with open ('ex4_output.txt', 'w') as wf:
    wf.write(words[0].title())
    wf.write(' ')
    wf.write(words[1].title())
    wf.write('\t')
    wf.write(words[2])
    wf.write('\t')
    wf.write('301-' + words[3])
