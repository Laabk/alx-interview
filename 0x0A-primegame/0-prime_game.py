#!/usr/bin/python3
"""
Module: the Game involving choosing Prime numbers
"""


def primeNumbers(n):
    """This will return list of prime numbers between 1 and n inclusive
    """
    primeNs = []
    filted = [True] * (n + 1)
    for prime in range(2, n + 1):
        if (filted[prime]):
            primeNs.append(prime)
            for i in range(prime, n + 1, prime):
                filted[i] = False
    return primeNs


def isWinner(x, nums):
    """
    this Determines winner of Prime Game
    Return:
        Name of winne
    """
    if x is None or nums is None or x == 0 or nums == []:
        return None
    Maria = Ben = 0
    for i in range(x):
        primeNos = primeNumbers(nums[i])
        if len(primeNos) % 2 == 0:
            Ben += 1
        else:
            Maria += 1
    if Maria > Ben:
        return 'Maria'
    elif Ben > Maria:
        return 'Ben'
    return None
