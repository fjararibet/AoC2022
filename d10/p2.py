import sys
from dataclasses import dataclass

input = open(sys.argv[1]).read().rstrip()
lines = [line for line in input.split("\n")]
cycle = 0
x = 1
result = 0
grid = [["." for _ in range(40)] for _ in range(6)]


@dataclass()
class Pos():
    x: int = 0
    y: int = 0


pos = Pos()
for ins in lines:
    if ins.startswith("noop"):
        cycle_add = 1

    elif ins.startswith("addx"):
        cycle_add = 2
    for _ in range(cycle_add):
        cycle += 1
        if abs(x - pos.x) <= 1:
            grid[pos.y][pos.x] = "#"
        if pos.x == 39:
            pos.y = (pos.y + 1) % 6
        pos.x = (pos.x + 1) % 40

    if ins.startswith("addx"):
        x += int(ins.split()[1])
for line in grid:
    print(''.join(line))
