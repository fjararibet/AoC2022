import sys

input = open(sys.argv[1]).read().rstrip()
lines = [line for line in input.split("\n")]
cycle = 0
x = 1
result = 0
for ins in lines:
    if ins.startswith("noop"):
        cycle += 1
        if (cycle - 20) % 40 == 0:
            result += x * cycle
    elif ins.startswith("addx"):
        for _ in range(2):
            cycle += 1
            if (cycle - 20) % 40 == 0:
                result += x * cycle
        x += int(ins.split()[1])
print(result)

