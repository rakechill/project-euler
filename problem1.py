#Sum of all multiples of m1 or m2 below a certain n.

#return the sum of all multiples of m1 or m2 below a certain n.
#like 3or5.c, but able to account for any multiples and any n.


def all_multiples_below(m1, m2, n):
    """
    >>> all_multiples_below(3, 5, 22)
    104
    """
    return sum([i for i in range(n) if i % (m1 * m2) != 0 and (i % m1 == 0 or i % m2 == 0)])
