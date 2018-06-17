#Find the smallest number that is evenly divisible by all of the numbers from 1 to n=20.

def factorial(n):
    running_total = 1
    while n > 1:
        running_total *= n
        n -= 1
    return running_total

def smallest_divisible_number(n):
    numbers = [i for i in range(1, n + 1)]
    for j in range(n, (factorial(n)), n):
        if all(j % number == 0 for number in numbers):
            return j
