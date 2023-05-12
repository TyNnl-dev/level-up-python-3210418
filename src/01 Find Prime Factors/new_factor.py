"""
Python Code Challenge #1: Find Prime Factors
Your goal is to implement a function, get_prime_factors(), that takes an integer value as the input argument and returns a list containing all of its prime factors.

Example Test Output
>>> get_prime_factors(630)
[2, 3, 3, 5, 7]

"""


def get_prime_factors(number):
    list_factor = []
    divisor = 2
    while divisor <= number:
        if number % divisor == 0:
            list_factor.append(divisor)
            number /= divisor
        else:
            divisor += 1
    return list_factor

print(get_prime_factors(630))
print(get_prime_factors(1330))    


