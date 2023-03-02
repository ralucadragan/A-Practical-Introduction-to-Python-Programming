'''
1. You are given a file called class_scores.txt, where each line of the file contains a oneword
username and a test score separated by spaces, like below:.
GWashington 83
JAdams 86
Write code that scans through the file, adds 5 points to each test score, and outputs the usernames
and new test scores to a new file, scores2.txt.
'''

'''
with open ('ex1_input.txt', 'r') as rf: #read file  - we have our original file open and we are reading from that file
    with open('ex1_output.txt', 'w') as wf: #write file - and we have another file that we are writing to this file
        for line in rf:  # for each line in ower original file(read file)
            wf.write(line) # write that line to wf

'''

'''
with open ('ex1_input.txt', 'r') as f:
    for line in f.readlines(): # read line by line
        words = int(line.split(' ')[1]) # imparte continutul liniei in elemente diferite
        print(words)    
'''

'''
asta e ok
with open ('ex1_input.txt', 'r') as rf:
    content1 = rf.readline()
    print(content1)
    new1 = content1.replace('83', '88')
    content2 = rf.readline()
    print(content2)
    new2 = content2.replace('86', '91')
    content2 = rf.readline()


    with open ('ex1_output.txt', 'w') as wf:
        wf.writelines(new1)
        wf.writelines(new2)
'''
'''
list_words = []
with open ('ex1_input.txt', 'r') as rf:
    with open('ex1_output.txt', 'w') as wf:
        for i in rf:
            list_words.append(i.rsplit())
        print(list_words)

        list_words[0][1] = int(list_words[0][1]) + 5
        list_words[1][1] = int(list_words[1][1]) + 5
        print(list_words)
        string = str(list_words)
        wf.write(string)
'''
'''
with open ('ex1_input.txt', 'r') as rf:
    for line in rf: # citest linie cu linie
        if line.endswith('3') is True:
            with open('ex1_output.txt', 'a') as af:
                af.write(line)
'''

with open ('ex1_input.txt', 'r') as rf:
    line = rf.read().split()
    print(line)

    for i in range(1,len(line), 2):
       x = int(line[i]) + 5
       # line[i] = str(int(line[i]) + 5)
       if i < len(line) - 2:
          line[i] = " " + str(x) + "\n"
       else:
           line[i] = " " + str(x)
    print(line)

with open ('ex1_output.txt', 'w') as wf:
    wf.write(''.join(line))









