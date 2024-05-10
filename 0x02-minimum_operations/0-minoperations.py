#!/usr/bin/python3
""" ther module for 0-minoperations"""


def minOperations(n):
    """
    thisd minOperations
    Gets fewest # of operations needed to
    result in exactly n H characters"""
    if (n < 2):
        return 0
    op, root = 0, 2
    while root <= n:
        # checking n evenly divides by root
        if n % root == 0:
            # total divisions by root = total operations
            op = op + root
            # setting the n to the remainder
            n = n / root
            root = root - 1
        root = root + 1
    return ops
