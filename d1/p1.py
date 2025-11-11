import sys
file = open(sys.argv[1]).read().strip()
cals = file.split("\n\n")
cals = [elf.split("\n") for elf in cals]
cals = [list(map(int, c)) for c in cals if c]
cals = [sum(c) for c in cals]
max_cals = max(cals)
print(max_cals)
