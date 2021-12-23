f = open("input", "r")

input = f.readline()
input = input.strip().removeprefix("target area: ")
xValues, yValues = input.split(", ")
minX = int(xValues.split("..")[0][2:])
maxX = int(xValues.split("..")[1])
minY = int(yValues.split("..")[0][2:])
maxY = int(yValues.split("..")[1])
targets = set()
for y in range(minY, maxY + 1):
    for x in range(minX, maxX + 1):
        targets.add((x, y))

# Take Step
# Probe's x position increases by x velocity
# y position increases by y velocity
# x velocity moves towards 0
# y velocity decreases by 1
def takeStep(position, velocity):
    newPosition = (position[0] + velocity[0], position[1] + velocity[1])
    if (velocity[0] > 0):
        newXVelocity = velocity[0] - 1
    elif (velocity[0] == 0):
        newXVelocity = 0
    else:
        newXVelocity = velocity[0] + 1
    newYVelocity = velocity[1] - 1
    newVelocity = (newXVelocity, newYVelocity)
    return newPosition, newVelocity

def fireProbe(velocity):
    position = (0,0)
    maxY = velocity[1]
    hitTarget = False
    loop = True
    while (loop):
        # Take Another step - updating position and velocity
        position, velocity = takeStep(position, velocity)
        # If the New Position is the highest then store this value.
        if (position[1] > maxY):
            maxY = position[1]

        # If position is in the Target then end the loop and set hitTarget to true
        # Return Max Y & Hit Target
        if(position in targets):
            loop = False
            hitTarget = True

        # Check if position has gone beyond the target (X & Y > Max Target X & Y)
        elif((position[0] > maxX
                or (position[0] < minX and velocity[0] == 0))
                or ((position[1] < minY and velocity[0] == 0 )
            )):
            loop = False

    return hitTarget, maxY

def findOptimalShot():
    maxY = -10
    bestVelocity = (0,0)
    hitVelocities = set()
    for yVelocity in range(-200, 200):
        for xVelocity in range(-200, 200):
            hit, heightReached = fireProbe((xVelocity, yVelocity))
            if(hit):
                hitVelocities.add((xVelocity, yVelocity))
                if (heightReached > maxY):
                    maxY = heightReached
                    bestVelocity = (xVelocity, yVelocity)
    return bestVelocity, maxY, hitVelocities

results = findOptimalShot()
print("Part 1:", results[1])
print("Part 2:", len(results[2]))