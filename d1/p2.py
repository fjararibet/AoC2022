import sys
file = open(sys.argv[1]).read().strip()
cals = file.split("\n\n")
cals = [elf.split("\n") for elf in cals]
cals = [list(map(int, c)) for c in cals if c]
cals = [sum(c) for c in cals]
top1 = cals[0]
top2 = cals[0]
top3 = cals[0]
for c in cals:
    if c > top1:
        top1, top2, top3 = c, top1, top2
        continue
    if c > top2:
        top2, top3 = c, top2
        continue
    if c > top3:
        top3 = c
print(top1+top2+top3)
