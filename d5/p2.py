import sys
from collections import defaultdict

input = open(sys.argv[1]).read().rstrip()
boxes, ins = input.split("\n\n")
crates = defaultdict(list)
row_count = 0
for line in boxes.split("\n"):
    curr_row = 1
    if line[1] == '1':
        break
    for i in range(1, len(line), 4):
        if line[i] != ' ':
            crates[curr_row].insert(0, line[i])
        curr_row += 1
    row_count = max(row_count, curr_row)
for line in ins.split("\n"):
    words = line.split()
    count, origin, to = int(words[1]), int(words[3]), int(words[5])
    stack = []
    for _ in range(count):
        stack.insert(0, crates[origin].pop())
    crates[to] += stack
result = ''
for i in range(1, row_count):
    result += crates[i][-1]
print(result)
