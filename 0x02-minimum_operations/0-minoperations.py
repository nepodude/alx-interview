#!/usr/bin/python3
"""
Calculates the fewest number of operations (Copy All and Paste)
needed to result in exactly n H characters in a text file that
initially contains a single "H".
"""

def minOperations(n):
    """
    Returns the minimum number of operations to get n 'H' characters.
    If n is less than 2, it's impossible to perform any operations.
    """
    if n < 2:
        return 0

    operations = 0
    divisor = 2

    # Factor n and sum up its prime factors
    while n > 1:
        while n % divisor == 0:
            operations += divisor
            n //= divisor
        divisor += 1

    return operations
