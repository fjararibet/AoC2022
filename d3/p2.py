import sys


def pri(s):
    if ord(s) < ord('a'):
        return ord(s) - ord('A') + 26 + 1
    return ord(s) - ord('a') + 1


input = open(sys.argv[1]).read().strip()
lines = input.split("\n")
result = 0
for i in range(0, len(lines), 3):
    first, second, third = tuple(lines[i:i+3])
    for c in first:
        if c in second and c in third:
            result += pri(c)
            break
print(result)
