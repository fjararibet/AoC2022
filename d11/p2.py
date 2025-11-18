import sys

input = open(sys.argv[1]).read().rstrip()
monkeys = input.split("\n\n")

monkey_dict = {}


def make_op(operation_line):
    if operation_line.endswith("old"):
        return lambda x: x * x
    if "*" in operation_line:
        return lambda x: x * int(operation_line.split("*")[1])
    if "+" in operation_line:
        return lambda x: x + int(operation_line.split("+")[1])


for i, monkey_info in enumerate(monkeys):
    lines = monkey_info.split("\n")
    items = [int(item) for item in lines[1].split(":")[1].split(",")]
    operation_line = lines[2].split("=")[1].strip()
    operation = make_op(operation_line)
    test = int(lines[3].split()[3])
    is_true = int(lines[4].split()[-1])
    is_false = int(lines[5].split()[-1])
    monkey_dict[i] = {
        "items": items,
        "operation": operation,
        "test": test,
        "true": is_true,
        "false": is_false,
        "inspections": 0,
    }
for j in range(10000):
    for i in range(len(monkey_dict)):
        monkey = monkey_dict[i]
        for item in monkey["items"]:
            worry_level = item
            worry_level = monkey["operation"](worry_level)
            branch = "true" if worry_level % monkey["test"] == 0 else "false"
            monkey_dict[monkey[branch]]["items"].append(worry_level)
            monkey["items"] = monkey["items"][1:]
            monkey["inspections"] += 1
sorted_monkeys = sorted(monkey_dict.items(), key=lambda x: x[1]["inspections"])
print(sorted_monkeys[-1][1]["inspections"] * sorted_monkeys[-2][1]["inspections"])
