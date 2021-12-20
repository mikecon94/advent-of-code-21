import copy

f = open("input", "r")

caveMap = dict()
for line in f.readlines():
    source,target = line.strip().split("-")
    # Maybe don't include start as a link in the other cells.
    # Don't include end as an element in the dict()
    if(target != "start"):
        caveMap[source] = caveMap.get(source, []) + [target]
    if(source != "start"):
        caveMap[target] = caveMap.get(target, []) + [source]

caveMap.pop('end')
cavePaths = []

# This is inefficient and slows the solution down.
# Could be better by tracking counts when increased.
def visitedSmallCaveTwice(path):
    visited = dict()
    for cave in path:
        if(cave.islower()):
            visited[cave] = visited.get(cave, 0) + 1
            if(visited[cave] > 1):
                return True
    return False

# Current Path - appended to cavePaths once end is reached.
#              - Each node is attached as it is visited.
# Only visit small caves at most once.
# Visit Big Caves as many times as needed.
# Avoid loops e.g. A-B-A-B (remove visited nodes from caveMap as we go)
def getPaths(cave, currentPath, visitSmallCaveTwice=False):
    # print(cave, currentPath)
    # If it's lower case and we have already visited it.
    # End this route and don't append.
    if(cave.islower() and cave != "end" and cave != "start"):
        if(visitSmallCaveTwice):
            # If already visited a small cave twice
            # return currentPath and don't continue
            if(cave in currentPath and visitedSmallCaveTwice(currentPath)):
                return currentPath
        elif(cave in currentPath):
            return currentPath

    currentPath.append(cave)
    
    if(cave == "end"):
        # Only append completed paths that have reached the end.
        cavePaths.append(currentPath)
        # Reset the Current Path
        return currentPath

    for linkedCave in caveMap[cave]:
        getPaths(linkedCave, copy.deepcopy(currentPath), visitSmallCaveTwice)

def part1():
    getPaths("start", [])
    return len(cavePaths)

def part2():
    global cavePaths
    cavePaths = []
    getPaths("start", [], True)
    return len(cavePaths)

print("PART 1:", part1())
print("PART 2:", part2())