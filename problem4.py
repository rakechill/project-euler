#general solution to largest palindrome created by 2 n-digited numbers

#1 figure out max and min's of your digits.
def digit_ranges(digits):
    """Takes in amount of digits and gives ranges for specified digits"""
    str_max = ''
    range_min = pow(10, digits - 1)
    for i in range(digits):
        str_max += '1'
    range_max = 9 * int(str_max)
    mult_min, mult_max = pow(range_min, 2), pow(range_max, 2)
    return find_palindromes(range_min, range_max, mult_min, mult_max)

#2 find your palindromes within that range.
def find_palindromes(range_min, range_max, mult_min, mult_max):
    palindromes = []
    for num in range(mult_min, mult_max):
        if str(num) == str(num)[::-1]:
            palindromes.append(num)
    return factors_of_palindromes(palindromes, range_min, range_max)

#3 find the largest palindromes with factors in that range.
def factors_of_palindromes(palindromes, range_min, range_max):
    factors = []
    for palindrome in palindromes:
        for i in range(range_min, range_max + 1):
            if palindrome % i == 0 and palindrome / i >= range_min and palindrome / i <= range_max:
                factors.append([palindrome, i, palindrome // i])
    return factors[len(factors) - 1][0]
