import sys
from dataclasses import dataclass

input = open(sys.argv[1]).read().rstrip()
instructions = [(line.split()[0], int(line.split()[1])) for line in input.split("\n")]

visited = {}


@dataclass(frozen=True)
class Coord():
    x: int = 0
    y: int = 0


tail = Coord()
head = Coord()
visited = {tail}


for dir, count in instructions:
    for _ in range(count):
        i, j = head.x, head.y
        dir_map = {
            "R": Coord(x=i+1, y=j),
            "U": Coord(x=i, y=j-1),
            "L": Coord(x=i-1, y=j),
            "D": Coord(x=i, y=j+1),
        }
        head = dir_map[dir]
        # is touching
        if abs(head.x - tail.x) <= 1 and abs(head.y - tail.y) <= 1:
            continue
        x, y = tail.x, tail.y
        if tail.x < head.x:
            x += 1
        if tail.x > head.x:
            x -= 1
        if tail.y < head.y:
            y += 1
        if tail.y > head.y:
            y -= 1
        tail = Coord(x=x, y=y)
        visited.add(tail)
print(len(visited))
