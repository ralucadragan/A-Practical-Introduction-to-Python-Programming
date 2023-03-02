'''
2. You are given a file called grades.txt, where each line of the file contains a one-word student
username and three test scores separated by spaces, like below:.
GWashington 83 77 54
JAdams 86 69 90
Write code that scans through the file and determines how many students passed all three
tests.
'''

# min score for passing the test in 60

with open ('ex2_input.txt', 'r') as rf:
    content = rf.readlines()
    print(content)

    for i in content:
        #print(i)
        line = i.split()
        #print(line)

        count = 0
        for j in range(1,4):
            if int(line[j]) >= 60:
                count = count + 1
        if count == 3:
            #print(line[j])
            print(f'The stundent {line[0]}  has pass all the three tests!')
