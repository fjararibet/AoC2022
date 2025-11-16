import sys

input = open(sys.argv[1]).read().rstrip()

grid = [[int(x) for x in line] for line in input.split("\n")]
result = 0
for i in range(len(grid[0])):
    for j in range(len(grid)):
        n = grid[i][j]
        visibleRDLU = [True, True, True, True]
        if i in [0, len(grid[0])-1] or j in [0, len(grid)-1]:
            result += 1
            continue
        for right in range(i+1, len(grid[0])):
            if n <= grid[right][j]:
                visibleRDLU[0] = False
                break
        for down in range(j+1, len(grid)):
            if n <= grid[i][down]:
                visibleRDLU[1] = False
                break
        for left in range(0, i):
            if n <= grid[left][j]:
                visibleRDLU[2] = False
                break
        for up in range(0, j):
            if n <= grid[i][up]:
                visibleRDLU[3] = False
                break
        if any(visibleRDLU):
            result += 1
print(result)
