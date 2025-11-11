import sys
input = open(sys.argv[1]).read().strip()
scoring = {
    "A": 1,
    "B": 2,
    "C": 3,
}
beats = {
    "A": "C",
    "B": "A",
    "C": "B",
}
loses = {
    "A": "B",
    "B": "C",
    "C": "A",
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
    if b == "X":
        round_points += scoring[beats[a]]
    if b == "Y":
        round_points += scoring[a] + 3
    if b == "Z":
        round_points += scoring[loses[a]] + 6
    cache[(a, b)] = round_points
    points += round_points
print(points)
