f = open("input", "r")

grid = dict()
for yIndex, line in enumerate(f.readlines()):
    values = line.strip()
    for xIndex, value in enumerate(values):
        grid[(xIndex, yIndex)] = int(value)

# The locations that are lower than any of its adjacent locations.
# Vertical & Horizontal
def part1():
    riskLevels = []
    for (x,y) in grid:
        lowestPoint = True
        height = grid[(x,y)]
        for i in range(-1, 2):
            if (i != 0
                and (height >= grid.get((x + i, y), float('inf'))
                or height >= grid.get((x, y + i), float('inf')))):
                lowestPoint = False        
        if (lowestPoint):
            riskLevels.append(grid[x,y] + 1)
    return sum(riskLevels)

def part2():

    return 0

print("PART 1:", part1())
print("PART 2:", part2())