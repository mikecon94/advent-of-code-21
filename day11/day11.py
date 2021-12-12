import copy

# 10 x 10 grid of octopuses
# Gain energy over time
# flash brightly for a moment when energy is full
# During a step:
# - Energy level of each octopus increases by 1
# - Energy Level > 9 flashes
#       which increases adjacent octopuses by 1.
#       including diagonals
#       This octopus then also flashes.
#       This continues - an octopus can only flash once per step.
# - Any octopus that flashed during the step has it's energy level set to 0.

f = open("input", "r")

startingGrid = dict()
for yIndex, line in enumerate(f.readlines()):
    for xIndex, value in enumerate(line.strip()):
        startingGrid[xIndex,yIndex] = int(value)

def printGrid(grid):
    for y in range(0, 10):
        for x in range(0, 10):
            print(grid[x, y], end="")
        print()

# Any octopus with energy above 9 has flashed this step.
# Reset it to 0 energy at the end of each step.
def resetOctopuses(grid):
    flashCount = 0
    for y in range(0, 10):
        for x in range(0, 10):
            if(grid[x, y] > 9):
                flashCount += 1
                grid[x, y] = 0
    return flashCount

def increaseEnergy(x, y, grid):
    grid[x, y] += 1
    if (grid[x, y] == 10):
        # FLASH
        # Increment surrounding cells
        for adjacentY in range(-1, 2):
            for adjacentX in range(-1, 2):
                if (adjacentY == 0 and adjacentX == 0):
                    pass
                else:
                    newX = x + adjacentX
                    newY = y + adjacentY
                    if (newX >= 0 and newX < 10
                        and newY >= 0 and newY < 10):
                        increaseEnergy(newX, newY, grid)
    
def takeStep(grid):
    newGrid = copy.deepcopy(grid)
    for y in range(0, 10):
        for x in range(0, 10):
            increaseEnergy(x, y, newGrid)
    return newGrid
    
def part1():
    newGrid = takeStep(startingGrid)
    flashCount = 0
    for i in range(1, 100):
        newGrid = takeStep(newGrid)
        flashCount += resetOctopuses(newGrid)
    return flashCount

def part2():
    stepNumber = 1
    newGrid = takeStep(startingGrid)
    allFlashStep = -1
    while (allFlashStep == -1):
        stepNumber += 1
        newGrid = takeStep(newGrid)
        if(resetOctopuses(newGrid) == 100):
            return stepNumber

print("PART 1:", part1())
print("PART 2:", part2())
