#!/usr/bin/python3
"""
an alorigthm to solves the lock boxes puzzle
"""

def look_next_opened_box(opened_boxes):
    """
    checks if the next opened box
    Args:
        the opened_boxes (dict): Dictionary which contains
        boxes already opened
    Returns:
        list: Listing the keys contained in the opened box
    """
    for index, box in opened_boxes.items():
        if box.get('status') == 'opened':
            box['status'] = 'opened/checked'
            return box.get('keys')
    return None


def canUnlockAll(boxes):
    """Checking if all boxes can be opened
    Args:
        boxes (list): List which contain all the boxes with the keys
    Returns:
        bool: True if all boxes can be opened, otherwise, False
    """
    if len(boxes) <= 1 or boxes == [[]]:
        return True

    au = {}
    while True:
        if len(au) == 0:
            au[0] = {
                'status': 'opened',
                'keys': boxes[0],
            }
        keys = look_next_opened_box(au)
        if keys:
            for key in keys:
                try:
                    if au.get(key) and au.get(key).get('status') \
                       == 'opened/checked':
                        continue
                    au[key] = {
                        'status': 'opened',
                        'keys': boxes[key]
                    }
                except (KeyError, IndexError):
                    continue
        elif 'opened' in [box.get('status') for box in au.values()]:
            continue
        elif len(au) == len(boxes):
            break
        else:
            return False

    return len(au) == len(boxes)


def main():
    """
    the main entry point
    """
    canUnlockAll([[]])


if __name__ == '__main__':
    main()
