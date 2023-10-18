#!/usr/bin/python3

import sys
possible_status_codes = [200, 301, 400, 401, 403, 404, 405, 500]
totalFilesize = 0
numberOfLines = 0
statusCodeMap = {}

def print_status():
    print(f"File Size: {totalFilesize}")

    for status, count in sorted(statusCodeMap.items()):
        print(f"{status}: {count}")

try:
    for line in sys.stdin:
        try:
            line = line.split()
            fileSize = int(line[-1])
            totalFilesize += fileSize
            statusCode = int(line[-2])

            if statusCode in possible_status_codes:
                if statusCode in statusCodeMap:
                    statusCodeMap[statusCode] += 1
                else:
                    statusCodeMap[statusCode] = 1
            numberOfLines += 1
            if numberOfLines % 10 == 0:
                (print_status())
        except ValueError:
            pass
    if (numberOfLines == 0) or (numberOfLines % 10 != 0):
        (print_status())

except KeyboardInterrupt:
        (print_status())
