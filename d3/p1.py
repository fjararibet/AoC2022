import sys


def pri(s):
    if ord(s) < ord('a'):
        return ord(s) - ord('A') + 26 + 1
    return ord(s) - ord('a') + 1


input = open(sys.argv[1]).read()
lines = input.split("\n")
result = 0
for line in lines:
    first = line[:len(line)//2]
    second = line[len(line)//2:]
    for c in first:
        if c in second:
            result += pri(c)
            break
print(result)

