import sys
from dataclasses import dataclass

input = open(sys.argv[1]).read().rstrip()
instructions = [(line.split()[0], int(line.split()[1])) for line in input.split("\n")]

visited = {}


@dataclass(frozen=True)
class Coord():
    x: int = 0
    y: int = 0


rope = [Coord(x=0, y=0) for _ in range(10)]

visited = {rope[-1]}


for dir, count in instructions:
    for _ in range(count):
        head = rope[0]
        i, j = head.x, head.y
        dir_map = {
            "R": Coord(x=i+1, y=j),
            "U": Coord(x=i, y=j-1),
            "L": Coord(x=i-1, y=j),
            "D": Coord(x=i, y=j+1),
        }
        head = dir_map[dir]
        rope[0] = head
        # is touching
        for k in range(len(rope)-1):
            curr = rope[k]
            next = rope[k+1]
            if abs(curr.x - next.x) <= 1 and abs(curr.y - next.y) <= 1:
                continue
            x, y = next.x, next.y
            if next.x < curr.x:
                x += 1
            if next.x > curr.x:
                x -= 1
            if next.y < curr.y:
                y += 1
            if next.y > curr.y:
                y -= 1
            next = Coord(x=x, y=y)
            rope[k+1] = next
        visited.add(rope[-1])
print(len(visited))
