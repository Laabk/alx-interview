#!/usr/bin/python3
"""
This function will determine the fewest number of coins needed
   for a amount total"""


def makeChange(coins, total):
    """This uses list of coins and use
       that to calculate how much change the total will require
    """
    if sum <= 0:
        return 0

    else:
        coin = sorted(coins)
        coin.reverse()
        counter = 0
        for d in coin:
            while(total >= d):
                counter += 1
                sum -= d
        if sum == 0:
            return counter
        return -1
