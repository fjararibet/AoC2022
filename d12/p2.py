import sys
import math

input = open(sys.argv[1]).read().rstrip()
end = (0, 0)
lines = input.split()
grid = {}
starts = []
for i in range(len(lines[0])):
    for j in range(len(lines)):
        grid[i, j] = lines[j][i]
        if grid[i, j] in ["S", "a"]:
            starts.append((i, j))
            grid[i, j] = "a"
        if grid[i, j] == "E":
            end = i, j
            grid[i, j] = "z"
visited = set()
q = []
for s in starts:
    q.append((s, 0))
min_count = math.inf
while q:
    curr, count = q.pop(0)
    if curr == end:
        min_count = min(math.inf, count)
        continue
    if curr in visited:
        continue

    i, j = curr
    neighbors = [
        (i, j+1),
        (i+1, j),
        (i, j-1),
        (i-1, j),
    ]
    valid_neighbors = []
    for n in neighbors:
        if n in grid and (ord(grid[n]) - ord(grid[curr])) <= 1:
            valid_neighbors.append(n)
    visited.add(curr)
    for vn in valid_neighbors:
        q.append((vn, count+1))
print(min_count)
