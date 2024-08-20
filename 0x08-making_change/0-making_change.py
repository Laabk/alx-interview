#!/usr/bin/python3
"""This  determines a fewest number of coins needed
   to get the given amount total"""


def makeChange(coins, total):
    """This will take  list of coins to
    calculate how much change the total will require
    """
    if total <= 0:
        return 0

    else:
        coin = sorted(coins)
        coin.reverse()
        counter = 0
        for d in coin:
            while(total >= d):
                counter += 1
                total -= d
        if total == 0:
            return counter
        return -1
