import sys
input = open(sys.argv[1]).read().strip()
scoring = {
    "X": 1,
    "Y": 2,
    "Z": 3,
}
game_map = {
    "A": "X",
    "B": "Y",
    "C": "Z",
}
beats = {
    "X": "C",
    "Y": "A",
    "Z": "B",
}
guide = input.split("\n")
guide = [tuple(s.split()) for s in guide]
points = 0
cache = {}
for a, b in guide:
    if (a, b) in cache:
        points += cache[(a, b)]
        continue
    round_points = 0
    round_points += scoring[b]
    if game_map[a] == b:
        round_points += 3

    if beats[b] == a:
        round_points += 6
    cache[(a, b)] = round_points
    points += round_points
print(points)
