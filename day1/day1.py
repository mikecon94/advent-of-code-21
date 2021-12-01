f = open("input", "r")

inputNums = []
for line in f.readlines():
    inputNums.append(int(line))

def part1():
    previousNum = -1
    increasedCount = -1
    for value in inputNums:
        if (value > previousNum):
            increasedCount += 1
        previousNum = value
    return str(increasedCount)

def part2():
    increasedCount = -1
    previousWindow = -1
    newWindow = -1

    for index, value  in enumerate(inputNums):
        # print("INDEX: ", index, " WINDOW: ", newWindow, "INCREASED: ", increasedCount)

        if((index + 2) >= len(inputNums)):
            return str(increasedCount)

        newWindow = value + inputNums[index + 1] + inputNums[index + 2]
        if (newWindow > previousWindow):
            increasedCount += 1
        previousWindow = newWindow

print("PART 1: " + part1())
print("PART 2: " + part2())
