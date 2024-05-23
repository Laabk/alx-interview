#!/usr/bin/python3
"""the UTF-8 Validation
"""


def validUTF8(data):
    """
    these determines if a given data set
    represents a valid utf-8 encoding
    """
    nubr_byts = 0

    mask_1 = 1 << 7
    mask_2 = 1 << 6

    for i in data:

        mask_byte = 1 << 7

        if nubr_byts == 0:

            while mask_byte & i:
                number_bytes += 1
                mask_byte = mask_byte >> 1

            if number_bytes == 0:
                continue

            if nubr_byts == 1 or nubr_byts > 4:
                return False

        else:
            if not (i & mask_1 and not (i & mask_2)):
                return False

        nubr_byts -= 1

    if nubr_byts == 0:
        return True

    return False

