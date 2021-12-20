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

# Current Path - appended to cavePaths once end is reached.
#              - Each node is attached as it is visited.
# Only visit small caves at most once.
# Visit Big Caves as many times as needed.
# Avoid loops e.g. A-B-A-B (remove visited nodes from caveMap as we go)
def getPaths(cave, currentPath):
    # print(cave, currentPath)
    # If it's lower case and we have already visited it.
    # End this route and don't append.
    if(cave.islower() and (cave in currentPath)):
        return currentPath

    currentPath.append(cave)
    
    if(cave == "end"):
        # Only append completed paths that have reached the end.
        cavePaths.append(currentPath + ["end"])
        # Reset the Current Path
        return currentPath

    for linkedCave in caveMap[cave]:
        getPaths(linkedCave, copy.deepcopy(currentPath))

def part1():
    getPaths("start", [])
    return len(cavePaths)

print("PART 1:", part1())