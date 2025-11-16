import sys
from dataclasses import dataclass

input = open(sys.argv[1]).read().rstrip()

grid = [[int(x) for x in line] for line in input.split("\n")]
result = 0


@dataclass
class Score():
    right: int = 0
    down: int = 0
    left: int = 0
    up: int = 0


for i in range(len(grid[0])):
    for j in range(len(grid)):
        n = grid[i][j]
        score = Score()
        for right in range(i+1, len(grid[0])):
            score.right += 1
            if n <= grid[right][j]:
                break
        for down in range(j+1, len(grid)):
            score.down += 1
            if n <= grid[i][down]:
                break
        for left in reversed(range(0, i)):
            score.left += 1
            if n <= grid[left][j]:
                break
        for up in reversed(range(0, j)):
            score.up += 1
            if n <= grid[i][up]:
                break

        scenic_score = score.right * score.down * score.left * score.up
        result = max(scenic_score, result)
print(result)
