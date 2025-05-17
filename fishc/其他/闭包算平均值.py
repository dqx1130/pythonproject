def make_avg():
    total = 0
    count = 0
    def averager(value):
        nonlocal total, count
        total += value
        count += 1
        return total / count
    return averager

import sys
for line in sys.stdin:
    avg = make_avg()
    print(avg(int(line)))
