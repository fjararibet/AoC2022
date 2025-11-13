import sys

input = open(sys.argv[1]).read().strip()
lines = input.split("\n")
result = 0
for line in lines:
    first, second = tuple(line.split(","))
    a, b = tuple(map(int, first.split("-")))
    c, d = tuple(map(int, second.split("-")))
    if a <= c and b >= d:
        result += 1
    elif c <= a and d >= b:
        result += 1
print(result)
