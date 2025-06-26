#!/usr/bin/python3

"""
file to determine the winner
"""


def isprime(n):
    """ Checks if the number is a prime """
    for i in range(n):
        if n % i == 1 and i != 1:
            return False
    return True

def isWinner(x, nums):
    """ Checks howmany prime integers less than numbers in nums """
    benMaria = []
    Marias = 0
    Bens = 0
    for i in range(x):
        howmanyprimes = 0
        for j in range(nums[i] + 1):
            if isprime(j):
                howmanyprimes = howmanyprimes + 1
        if howmanyprimes % 2 == 0:
            benMaria.append("Ben")
        else:
            benMaria.append("Maria")
    for i in benMaria:
        if i == "Ben":
            Bens = Bens + 1
        elif i == "Maria":
            Marias = Marias + 1
    if Bens > Marias:
        return "Ben"
    elif Marias > Bens:
        return "Maria"
    else:
        return None
