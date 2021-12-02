f = open("input", "r")

inputInstructions = []
for line in f.readlines():
    inputInstructions.append(line.strip())

# print(inputInstructions)

def part1():
    horizontalPos = 0
    depth = 0
    for instruction in inputInstructions:
        direction = instruction.split(" ")[0]
        value = int(instruction.split(" ")[1])
        if (direction == "forward"):
            horizontalPos += value
        elif (direction == "down"):
            depth += value
        elif (direction == "up"):
            depth -= value
    result = horizontalPos * depth
    return str(result)

def part2():
    horizontalPos = 0
    depth = 0
    aim = 0

    for instruction in inputInstructions:
        direction = instruction.split(" ")[0]
        value = int(instruction.split(" ")[1])
        if (direction == "forward"):
            horizontalPos += value
            depth += aim * value
        elif (direction == "down"):
            aim += value
        elif (direction == "up"):
            aim -= value

    result = horizontalPos * depth
    return str(result)

print("PART 1: " + part1())
print("PART 2: " + part2())
