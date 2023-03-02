
for i in range(10):
    print('Hello')

for i in range(3): # the value we put in range determines how many times we will loop
    num = int(input('Enter a number: '))
    print(f'The square of your number  is {num * num}')
print('The loop is now done') # only get executed once, after the loop is complet.

print('A')
print('B')
for i in range (5):
    print('C')
    print('D')
print('E')

print('A')
print('B')
for i in range (5):
    print('C')
for i in range(5):
    print('D')
print('E')

for i in range(3):
    print(i+1, '--Hello')

for i in range (5, 0, -1):
    print(i, end= ' ') # end= just keeps everithing inthe same line
print('Blast off!!!')

for i in range(4):
    print('*' * 6)

for i in range(4):
    print('*' * (i+1))
