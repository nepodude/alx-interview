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
    """ Checks howmany prime integers less than numbers in nums """
    if x < 0 or x != len(nums) or not nums:
        return None
    if x = 0 and nums == []:
        return "Ben"
    benMaria = []
    Marias = 0
    Bens = 0
    for i in range(x):
        howmanyprimes = 0
        for j in range(1, nums[i] + 1):
            if isprime(j):
                howmanyprimes += 1
        if howmanyprimes % 2 == 1:
            benMaria.append("Ben")
        else:
            benMaria.append("Maria")
    for i in benMaria:
        if i == "Ben":
            Bens += 1
        elif i == "Maria":
            Marias += 1
    if Bens > Marias:
        return "Ben"
    elif Marias > Bens:
        return "Maria"
    else:
        print("none")
        return None
