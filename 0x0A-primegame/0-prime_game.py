#!/usr/bin/python3

"""
file to determine the winner
"""


def isprime(n):
    """ Checks if the number is a prime """
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return False
    return True


def isWinner(x, nums):
    if not isinstance(x, int) or not nums or x < 1:
        return None

    n = max(nums)
    sieve = [True] * (n + 1)
    sieve[0] = sieve[1] = False
    for i in range(2, int(n ** 0.5) + 1):
        if sieve[i]:
            for j in range(i * i, n + 1, i):
                sieve[j] = False

    prime_counts = [0] * (n + 1)
    for i in range(1, n + 1):
        prime_counts[i] = prime_counts[i - 1] + int(sieve[i])

    maria = 0
    ben = 0
    for i in range(min(x, len(nums))):
        if prime_counts[nums[i]] % 2 == 1:
            maria += 1
        else:
            ben += 1

    if maria > ben:
        return "Maria"
    elif ben > maria:
        return "Ben"
    return None
