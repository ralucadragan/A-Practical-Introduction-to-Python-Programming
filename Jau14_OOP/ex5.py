'''
5. Write a class called Wordplay. It should have a field that holds a list of words. The user
of the class should pass the list of words they want to use to the class. There should be the
following methods:
• words_with_length(length)— returns a list of all the words of length length
• starts_with(s)— returns a list of all the words that start with s
• ends_with(s)— returns a list of all the words that end with s
• palindromes()— returns a list of all the palindromes in the list
• only(L)— returns a list of the words that contain only those letters in L
• avoids(L)— returns a list of the words that contain none of the letters in L
'''

class Wordplay:

    def __init__(self):
        self.words = []

    def words_with_length(self, length):
        # returns a list of all the words of length length
        rezult = []
        for i in range(len(self.words)):
            if len(self.words[i]) == length:
                rezult.append(self.words[i])
        return rezult

    def starts_with(self,s):
        # returns a list of all the words that start with s
        rezult = []
        for i in range(len(self.words)):
            if self.words[i].startswith(s):
                rezult.append(self.words[i])
        return rezult

    def ends_with(self,s):
        # returns a list of all the words that end with s
        rezult = []
        for i in range(len(self.words)):
            if self.words[i].endswith(s):
                rezult.append(self.words[i])
        return rezult

    def palindromes(self):
        # returns a list of all the palindromes in the list
        rezult = []
        for i in range(len(self.words)):
            if self.words[i][:] == self.words[i][::-1]:
                rezult.append(self.words[i])
        return rezult


    def only(self, L):
        # returns a list of the words that contain only those letters in L
        rezult = []
        for i in range(len(self.words)):
            if L in self.words[i]:
                rezult.append(self.words[i])
        return rezult

    def avoids(self, L):
        # returns a list of the words that contain none of the letters in L
            pass



x = Wordplay()
x.words = ['ala', 'bala', 'sarmale', 'banane', 'salopeta', 'baterie', 'ama']

print('')
print('==== words_with_length: 3,6 ====')
print(x.words_with_length(3))
print(x.words_with_length(6))
print('')

print('======= starts_with: s,b =======')
print(x.starts_with('s'))
print(x.starts_with('b'))
print('')

print('======== ends_with: a,e ========')
print(x.ends_with('a'))
print(x.ends_with('e'))
print('')

print('========= palindromes =========')
print(x.palindromes())
print('')

print('======== only: l,x ========')
print(x.only('l'))
print(x.only('x'))
print('')

print('======== avoids: l,x ========')
print(x.avoids('l'))
print(x.avoids('x'))
print('')