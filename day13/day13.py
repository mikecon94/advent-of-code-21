import copy

f = open("input", "r")

coordinates = dict()
foldInstructions = []
for line in f.readlines():
    if ("fold along x" in line):
        foldInstruction = ("x", int(line.strip().split("=")[1]))
        foldInstructions.append(foldInstruction)
    elif ("fold along y" in line):
        foldInstruction = ("y", int(line.strip().split("=")[1]))
        foldInstructions.append(foldInstruction)
    elif (line.strip() != ""):
        x,y = line.strip().split(",")
        coordinates[(int(x), int(y))] = True

# These are the largest values a coordinate can have based on the last x & y folds.
xLength = 197
yLength = 7
def printGrid():
    for y in range(0, yLength + 1):
        for x in range(0, xLength + 1):
            if (coordinates.get((x, y), False)):
                print("#", end='')
            else:
                print(" ", end='')
        print("")

def foldUp(foldLine):
    for point in copy.deepcopy(coordinates):
        # Only operate on the point if it is above(below) the fold line.
        x = point[0]
        y = point[1]
        if(y > foldLine):
            # New Y = difference between Fold line & Y
            newY = foldLine - (y - foldLine)
            coordinates[(x, newY)] = True
            # Remove all points below the fold line.
            coordinates.pop(point)

def foldLeft(foldLine):
    for point in copy.deepcopy(coordinates):
        # Only operate on the point if it is above(below) the fold line.
        x = point[0]
        y = point[1]
        if(x > foldLine):
            # New X = difference between Fold line & X
            newX = foldLine - (x - foldLine)
            coordinates[(newX, y)] = True
            coordinates.pop(point)

def part1():
    foldInstruction = foldInstructions.pop(0)
    if(foldInstruction[0] == "x"):
        foldLeft(foldInstruction[1])
    else:
        foldUp(foldInstruction[1])
    return len(coordinates)

def part2():
    for instruction in foldInstructions:
        if (instruction[0] == "x"):
            foldLeft(instruction[1])
        else:
            foldUp(instruction[1])
    return "BLHFJPJF"

print("PART 1:", part1())
print("PART 2:", part2())
printGrid()