'''
6. Create the following lists using a for loop.
(a) A list consisting of the integers 0 through 49
(b) A list containing the squares of the integers 1 through 50.
(c) The list ['a','bb','ccc','dddd', . . . ] that ends with 26 copies of the letter z.
'''

lista = []
listb = []
listc = []

for i in range(0,50):
    lista.append(i)
print(lista)

for i in range(1,51):
    listb.append(i*2)
print(listb)

alphabet = 'abcdefghijklmnopqrstuvwxyz'
for i in range(len(alphabet)):
    listc.append(alphabet[i]*(i+1))
print(listc)