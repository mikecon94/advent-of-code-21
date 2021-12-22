import heapq
from os import X_OK
f = open("input", "r")

riskLevels = dict()
y = 0
for line in f.readlines():
    line = line.strip()
    for index in range(0, len(line)):
        riskLevels[(index, y)] = int(line[index])
    y += 1
gridSize = y

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
    end = (gridSize - 1, gridSize - 1)
    lowestRiskValues = dict()
    lowestRiskPaths = dict()
    lowestRiskPaths[start] = set()
    lowestRiskPaths[start].add(start)
    calculateShortestPaths(start,  end, start, lowestRiskValues, lowestRiskPaths)
    return lowestRiskValues[end] - riskLevels[start]

def printGrid(grid, gridSize):
    for y in range(0, gridSize):
        for x in range(0, gridSize):
            print(grid[(x,y)], end='')
        print()

def getAllRiskLevels(noOfTiles):
    allRiskLevels = dict()
    for y in range(0, gridSize * noOfTiles):
        for x in range(0, gridSize * noOfTiles):
            tileIncrement = (x // gridSize) + (y // gridSize)
            riskLevel = riskLevels[x % gridSize, y % gridSize] + tileIncrement
            if (riskLevel > 9):
                riskLevel = riskLevel - 9
            allRiskLevels[(x, y)] = riskLevel
    return allRiskLevels

neighbouringNodes = [[0, 1], [0, -1], [1, 0], [-1, 0]]
# Dijkstra implementation using heapq / Priority Queue
def dijkstra(grid, start, end):
    priorityQueue = []
    distances = dict()
    for coordinate in grid:
        distances[coordinate] = float('inf')
        heapq.heappush(priorityQueue, (float('inf'), coordinate))
    distances[start] = 0
    unvisited = set(grid.keys())
    
    currentNode = heapq.heappop(priorityQueue)[1]
    # Loop until the end node has been visited
    while (end in unvisited):
        # Consider unvisited neighbors and calculate their tentative distances from current node.
        for offset in neighbouringNodes:
            neighbour = (currentNode[0] + offset[0], currentNode[1] + offset[1])
            if (neighbour in unvisited):
                tentativeDistance = distances[currentNode] + grid[neighbour]
                # Compare distannce to current assigned value
                # If lower then assign that distance.
                if(tentativeDistance < distances[neighbour]):
                    distances[neighbour] = tentativeDistance
                    heapq.heappush(priorityQueue, (tentativeDistance, neighbour))

        # Remove Current Node from Unvisited
        unvisited.remove(currentNode)
        # Get the next unvisited node with shorted distance.
        currentNode = heapq.heappop(priorityQueue)[1]

    return distances

def part2():
    # Input is 1 tile
    # Make the inpuut 5 times bigger for Part 2
    noOfTiles = 5
    allRiskLevels = getAllRiskLevels(noOfTiles)
    start = (0,0)
    end = ((gridSize*noOfTiles) - 1, (gridSize*noOfTiles) - 1)
    return dijkstra(allRiskLevels, start, end)[end]

print("PART 1:", dijkstra(riskLevels, (0,0), (gridSize - 1, gridSize - 1))[(gridSize - 1, gridSize - 1)])
print("PART 2:", part2())