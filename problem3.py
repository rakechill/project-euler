#Largest Prime Factor
import math

def largest_prime_factor(number):
    def isprime(factor):
        for i in range(2, factor):
            if factor % i == 0:
                return False
        return True

    factor = 0
    for i in range(2, round(math.sqrt(number))):
        if number % i == 0 and isprime(i) and i > factor:
            factor = i
        i += 1
    return factor
