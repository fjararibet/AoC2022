import sys

input = open(sys.argv[1]).read().strip()
lines = input.split("\n")
result = 0
for line in lines:
    first, second = tuple(line.split(","))
    a, b = tuple(map(int, first.split("-")))
    c, d = tuple(map(int, second.split("-")))
    if a <= c <= b or a <= d <= b:
        result += 1
    elif c <= a <= d or c <= b <= d:
        result += 1
print(result)
