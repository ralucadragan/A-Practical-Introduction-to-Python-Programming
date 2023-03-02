# A class is a template for objects. It contains the code for all the object’s methods.

class Example: # Class names usually start with a capital.
    def __init__(self, a, b): # Most classes will have a method called __init__.
        self.a = a
        self.b = b
        # The constructor is usually used to set up the class’s variables. In
        # the above program, the constructor takes two values, a and b, and assigns the class variables
        # a and b to those values.

    def add(self):
        return self.a + self.b

e = Example(8, 6)   # To create a new object from the class, you call the class name along with any values that you
                    # want to send to the constructor
print(e.add())

print('----------------------------')

from string import punctuation

class Analyzer:
    def __init__(self,s):
        for i in punctuation:
            s = s.replace(i, '')
            s = s.lower()
            self.words = s.split()
    def nr_of_words(self):
        return len(self.words)
    def start_with(self,s):
        for w in self.words:
            if w[:len(s)] == s:
                return len(w)
    def number_with_lenght(self, n):
        for w in self.words:
            if len(w) == n:
                return len(w)

s = 'This is a test of the class'
a = Analyzer(s)
print(a.words)
print(a.nr_of_words())
print(a.start_with('t'))
print(a.number_with_lenght(2))