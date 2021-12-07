f = open("input", "r")

lines = []
for line in f.readlines():
    point1 = line.split(" -> ")[0]
    point2 = line.split(" -> ")[1]
    x1 = int(point1.split(",")[0])
    y1 = int(point1.split(",")[1])
    x2 = int(point2.split(",")[0])
    y2 = int(point2.split(",")[1])
    points = {"x1": x1, "y1": y1, "x2": x2, "y2": y2}
    lines.append(points)

# print(lines)

def printGrid(grid):
    points = grid.keys()
    highestX = 0
    highestY = 0
    for point in points:
        if(point[0] > highestX):
            highestX = point[0]
        if(point[1] > highestY):
            highestY = point[1]
    
    for y in range(highestY + 1):
        for x in range(highestX + 1):
            print(grid.get((x,y), 0), end = "")
        print()

def populateCounters(grid, includeDiagonals=False):
    for line in lines:
        # Horizontal Lines
        if(line["y1"] == line["y2"]): 
            y = line["y1"]
            if(line["x1"] < line["x2"]):
                startX = line["x1"]
                endX = line["x2"]
            else:
                startX = line["x2"]
                endX = line["x1"]
            for x in range(startX, endX + 1):
                grid[(x, y)] = grid.get((x,y), 0) + 1
        # Vertical Lines
        elif (line["x1"] == line["x2"]):
            x = line["x1"]
            if(line["y1"] < line["y2"]):
                startY = line["y1"]
                endY = line["y2"]
            else:
                startY = line["y2"]
                endY = line["y1"]
            for y in range(startY, endY + 1):
                grid[(x, y)] = grid.get((x,y), 0) + 1
        # Diagonals
        elif(includeDiagonals):
            if (line["x1"] > line["x2"]):
                xDirection = -1
            else:
                xDirection = 1
            
            if (line["y1"] > line["y2"]):
                yDirection = -1
            else:
                yDirection = 1
            for step in range(abs(line["x1"] - line["x2"]) + 1):
                xStep = step * xDirection
                yStep = step * yDirection
                currentPoint = (line["x1"] + xStep, line["y1"] + yStep)
                grid[currentPoint] = grid.get(currentPoint, 0) + 1

def countOverlaps(grid):
    count = 0
    for value in grid.values():
        if (value >= 2):
            count += 1
    return count

def part1():
    grid = dict()
    populateCounters(grid)
    # printGrid(grid)
    return countOverlaps(grid)

def part2():
    grid = dict()
    populateCounters(grid, True)
    # printGrid(grid)
    return countOverlaps(grid)

print("PART 1:", part1())
print("PART 2:" , part2())