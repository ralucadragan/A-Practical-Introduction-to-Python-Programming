'''
8. Write a function called number_of_factors that takes an integer and returns how many
factors the number has.

9. Write a function called factors that takes an integer and returns a list of its factors.
'''

def factors(n):
    result = []
    for i in range(1, n + 1):
        if n % i == 0:
            result.append(i)
    print(result)
    return(len(result))

print(factors(256))