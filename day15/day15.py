import copy
f = open("input", "r")

riskLevels = dict()
y = 0
for line in f.readlines():
    line = line.strip()
    for index in range(0, len(line)):
        riskLevels[(index, y)] = int(line[index])
    y += 1

# SUBOPTIMAL SOLUTION FOR PART 1
# ASSUMES PATHS ONLY MOVE RIGHT & DOWN
# NEEDS TO BE UPDATED TO DIJKSTRAS or SIMILAR
# Store the coordinates involved in each path to avoid maximum recursion depth
# Current Paths:
# lowestRiskValues = Coordinate -> Integer Value
# lowestRiskPaths = Coordinate -> Set of Coordinates in the path
# Do not revisit coordinates already in the path.
def calculateShortestPaths(coordinate, endCoordinate, previousCoordinate, lowestRiskValues, lowestRiskPaths):
    # If the new value is lower than the previously stored value then use the new value.
    newRiskValue = lowestRiskValues.get(previousCoordinate, 0) + riskLevels[coordinate]
    if(newRiskValue < lowestRiskValues.get(coordinate, float('inf'))):
        lowestRiskValues[coordinate] = newRiskValue
        # lowestRiskPaths[coordinate] = copy.deepcopy(lowestRiskPaths[previousCoordinate])
        # lowestRiskPaths[coordinate].add(coordinate)
        # If it's not the end coordinate compute new values for surrounding cells.
        if (coordinate != endCoordinate
            and newRiskValue < lowestRiskValues.get(endCoordinate, float('inf'))):
            # Down
            if (coordinate[1] < endCoordinate[1]):
                up = (coordinate[0], coordinate[1] + 1)
                # if(up not in lowestRiskPaths[coordinate]):
                calculateShortestPaths(up, endCoordinate, coordinate, lowestRiskValues, lowestRiskPaths)
            # Up
            # if (coordinate[1] > 0):
            #     down = (coordinate[0], coordinate[1] - 1)
            #     if(down not in lowestRiskPaths[coordinate]):
            #         calculateShortestPaths(down, endCoordinate, coordinate, lowestRiskValues, lowestRiskPaths)
            # Left
            # if (coordinate[0] > 0):
            #     left = (coordinate[0] - 1, coordinate[1])
                # if(left not in lowestRiskPaths[coordinate]):
                    # calculateShortestPaths(left, endCoordinate, coordinate, lowestRiskValues, lowestRiskPaths)
            # Right
            if (coordinate[0] < endCoordinate[0]):
                right = (coordinate[0] + 1, coordinate[1])
                # if(right not in lowestRiskPaths[coordinate]):
                calculateShortestPaths(right, endCoordinate, coordinate, lowestRiskValues, lowestRiskPaths)

def part1():
    # Start in the top left
    start = (0,0)
    # Assumes a square
    end = (y-1, y-1)
    lowestRiskValues = dict()
    lowestRiskPaths = dict()
    lowestRiskPaths[start] = set()
    lowestRiskPaths[start].add(start)
    calculateShortestPaths(start,  end, start, lowestRiskValues, lowestRiskPaths)
    print(lowestRiskValues[end])
    return lowestRiskValues[end] - riskLevels[start]

print("PART 1:", part1())