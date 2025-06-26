#!/usr/bin/python3

"""
File to determine the winner of the Prime Game.
"""


def is_prime(n):
    """Return True if n is a prime number, else False."""
    if n <= 1:
        return False
    limit = int(n ** 0.5) + 1
    for divisor in range(2, limit):
        if n % divisor == 0:
            return False
    return True


def is_winner(x, nums):
    """
    Play x rounds of the Prime Game with list nums and
    return the overall winner: "Maria", "Ben", or None.
    """
    # Validate inputs
    if x < 1 or not nums or x > len(nums):
        return None

    ben_score = 0
    maria_score = 0

    for i in range(x):
        count = 0
        for j in range(1, nums[i] + 1):
            if is_prime(j):
                count += 1
        # Maria wins if count of primes is odd
        if count % 2 == 1:
            maria_score += 1
        else:
            ben_score += 1

    if maria_score > ben_score:
        return "Maria"
    if ben_score > maria_score:
        return "Ben"
    return None
