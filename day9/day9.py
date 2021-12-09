f = open("input", "r")

grid = dict()
for yIndex, line in enumerate(f.readlines()):
    values = line.strip()
    for xIndex, value in enumerate(values):
        grid[(xIndex, yIndex)] = int(value)

def getLowPoints():
    lowPoints = []
    for (x,y) in grid:
        lowestPoint = True
        height = grid[(x,y)]
        for i in range(-1, 2):
            if (i != 0
                and (height >= grid.get((x + i, y), float('inf'))
                or height >= grid.get((x, y + i), float('inf')))):
                lowestPoint = False
        if (lowestPoint):
            lowPoints.append((x,y))
    return lowPoints

# Recursive function to check all cells in a basin.
# Count isn't required as the visitedIndexes Dictionary is same length as count.
def getBasinSize(point, count, visitedIndexes):
    # If we have already visited this index, do not count it again.
    # If it's not a 9 it is already accounted for.
    if(visitedIndexes.get(point, False)):
        return 0
    # 9 is the edge of basins and can be used for outer bounds as well.
    if(grid.get(point, 9) == 9):
        return 0

    # Ensure no further calls include the current point.
    visitedIndexes[point] = True
    newCount = 0
    # x + 1
    newCount += getBasinSize((point[0] - 1, point[1]), count, visitedIndexes)
    # x - 1
    newCount += getBasinSize((point[0] + 1, point[1]), count, visitedIndexes)
    # y + 1
    newCount += getBasinSize((point[0], point[1] - 1), count, visitedIndexes)
    # y - 1
    newCount += getBasinSize((point[0], point[1] + 1), count, visitedIndexes)
    # Plus 1 to count the current value
    return newCount + 1

# The locations that are lower than any of its adjacent locations.
# Vertical & Horizontal
def part1():
    riskLevels = 0
    for point in getLowPoints():
        riskLevels += grid[point] + 1
    return riskLevels

def part2():
    lowPoints = getLowPoints()
    basinSizes = []
    for point in lowPoints:
        basinSizes.append(getBasinSize(point, 0, dict()))

    # Multiply the 3 largest basin sizes together
    basinSizes.sort()
    result = basinSizes[-1] * basinSizes[-2] * basinSizes[-3]
    return result

print("PART 1:", part1())
print("PART 2:", part2())