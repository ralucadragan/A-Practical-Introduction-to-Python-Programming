'''
1. Write a class called Investment with fields called principal and interest. The constructor
should set the values of those fields. There should be a method called value_after that
returns the value of the investment after n years. The formula for this is p(1 + i)n, where p is
the principal, and i is the interest rate. It should also use the special method __str__ so that
printing the object will result in something like below:
Principal - $1000.00, Interest rate - 5.12%
'''

class Invesment:
    def __init__(self, principal, interest):
        self.principal = principal
        self.interest = interest
        self.years = 5

    def value_after(self):
        return(self.interest * self.principal * self.years)

    def __str__(self):
        print(f'Principal - ${self.principal}, Interest rate - {self.interest}%' )

i1 = Invesment(1000, 5.12)
print(i1.value_after())
i1.__str__()
