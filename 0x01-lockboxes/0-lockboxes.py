#!/usr/bin/python3
"""
this will defines a function that determines a box containing a list
   of lists can be opened using keys stored in the lists
"""


def canUnlockAll(boxes):
    """
    this determines asto if boxes can be unlocked"""
    position = 0
    unlocked = {}

    for box in boxes:
        if len(box) == 0 or position == 0:
            unlocked[position] = "always_unlocked"
        for key in box:
            if key < len(boxes) and key != position:
                unlocked[key] = key
        if len(unlocked) == len(boxes):
            return True
        position += 1
    return False
