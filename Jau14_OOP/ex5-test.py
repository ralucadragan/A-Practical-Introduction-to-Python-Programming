

words = ['ala', 'bala', 'sarmale', 'banane', 'salopeta', 'baterie', 'ama']
letters = ['a', 'm']
new = []

for i in words:
    for j in i:
        if j == letters[0] and j == letters[1]:
            new.append(i)

print(new)
