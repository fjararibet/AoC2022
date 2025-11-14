import sys
from collections import defaultdict


def count(d):
    c = 0
    for key in d:
        c += 1 if d[key] else 0
    return c


input = open(sys.argv[1]).read().rstrip()
d = defaultdict(int)
for i in range(4):
    d[input[i]] += 1
result = 0
for i in range(4, len(input)):
    prev = input[i-4]
    c = input[i]
    d[prev] -= 1
    d[c] += 1
    if count(d) == 4:
        result = i + 1
        break
print(result)
