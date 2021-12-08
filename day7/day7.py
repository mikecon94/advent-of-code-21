import os
print(os.getcwd())
f = open("input", "r")

crabs = list(map(int, f.readline().split(",")))

# Could have simply been n(n+1) // 2 Gauss's Formula
def calculateFuelCost(steps):
    steps = int(steps)
    if(steps == 1):
        fuelCost = 1
    elif (steps % 2  == 0):
        fuelCost = ((steps + 1)//2) * (steps + 1)
    else:
        fuelCost = ((steps // 2) * (steps + 1)) + ((steps+1) // 2)

    return fuelCost

# Essentially the median of the series (integer above or below)
def part1():
    start = min(crabs)
    end = max(crabs)
    positionFuelMap = dict()
    for i in range(start, end+1):
        for crab in crabs:
            positionFuelMap[i] = positionFuelMap.get(i, 0) + abs(crab - i)

    lowestPositionFuel = float("inf")
    for position in positionFuelMap:
        if (positionFuelMap[position] < lowestPositionFuel):
            lowestPositionFuel = positionFuelMap[position]
    return lowestPositionFuel

def part2():
    start = min(crabs)
    end = max(crabs)
    positionFuelMap = dict()
    for i in range(start, end+1):
        for crab in crabs:
            positionFuelMap[i] = positionFuelMap.get(i, 0) + calculateFuelCost(abs(crab - i))

    lowestPositionFuel = float("inf")
    for position in positionFuelMap:
        if (positionFuelMap[position] < lowestPositionFuel):
            lowestPositionFuel = positionFuelMap[position]
    return lowestPositionFuel

print("PART 1:", part1())
print("PART 2:", part2())