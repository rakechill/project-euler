#general solution to largest palindrome created by 2 n-digited numbers

#1 figure out max and min's of your digits.
def digit_ranges(digits):
    range_min, range_max = pow(10, digits - 1), pow(10, digits) - 1
    mult_min, mult_max = pow(range_min, 2), pow(range_max, 2)
    return find_palindromes(range_min, range_max, mult_min, mult_max)

#2 find your palindromes within that range.
def find_palindromes(range_min, range_max, mult_min, mult_max):
    palindromes = [num for num in range(mult_min, mult_max) if str(num) == str(num)[::-1]]
    return factors_of_palindromes(palindromes, range_min, range_max)

#3 find the largest palindromes with factors in that range.
def factors_of_palindromes(palindromes, range_min, range_max):
    for palindrome in palindromes[::-1]:
        for i in range(range_max, range_min, -1):
            if palindrome % i == 0 and palindrome / i >= range_min and palindrome / i <= range_max:
                return palindrome
