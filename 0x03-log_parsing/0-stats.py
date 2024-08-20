#!/usr/bin/python3
"""Takes and reads standard input line by line and computes metrics
"""


def parseLogs():
    """
    Takes and reads logs from standard input and generates reports
    Reports:
    """
    stdin = __import__('sys').stdin
    lin_number = 0
    fil_size = 0
    statusCodes = {}
    _codes = ('200', '301', '400', '401', '403', '404', '405', '500')
    try:
        for line in stdin:
            lin_number += 1
            line = line.split()
            try:
                fil_size += int(line[-1])
                if line[-2] in _codes:
                    try:
                        statusCodes[line[-2]] += 1
                    except KeyError:
                        statusCodes[line[-2]] = 1
            except (IndexError, ValueError):
                pass
            if lin_number == 10:
                report(fil_size, statusCodes)
                lin_number = 0
        report(fil_size, statusCodes)
    except KeyboardInterrupt as e:
        report(fil_size, statusCodes)
        raise


def report(fil_size, statusCodes):
    """
    this generated printed reports to standard output
    """
    print("File size: {}".format(fil_size))
    for key, value in sorted(statusCodes.items()):
        print("{}: {}".format(key, value))


if __name__ == '__main__':
    parseLogs()
