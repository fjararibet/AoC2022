import sys

input = open(sys.argv[1]).read().rstrip()
start = (0, 0)
end = (0, 0)
lines = input.split()
grid = {}
for i in range(len(lines[0])):
    for j in range(len(lines)):
        grid[i, j] = lines[j][i]
        if grid[i, j] == "S":
            start = i, j
            grid[i, j] = "a"
        if grid[i, j] == "E":
            end = i, j
            grid[i, j] = "z"
visited = set()
q = [(start, 0)]
while q:
    curr, count = q.pop(0)
    if curr == end:
        print(count)
        break
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
