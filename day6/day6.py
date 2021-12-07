import copy
from collections import defaultdict

f = open("input", "r")

initialState = []
for fish in f.readline().split(","):
    initialState.append(int(fish))

def incrementDay(currentFish):
    newFish = []
    for index, fish in enumerate(currentFish):
        if (fish == 0):
            newFish.append(8)
            currentFish[index] = 6
        else:
            currentFish[index] = fish - 1
    currentFish.extend(newFish)
    return currentFish

def runSimulation(noOfDays):
    currentDay = 0
    currentFish = copy.deepcopy(initialState)
    while (currentDay < noOfDays):
        currentFish = incrementDay(currentFish)
        currentDay += 1
    return len(currentFish)

def part1():
    return runSimulation(80)

# Need a more optimized way
def part2():
    # Dictionary with Key = Day
    # Value = Number of Fish on that day.
    # Then Each Day we only have to loop around 8 days instead of all of the fish.
    dayMap = defaultdict(lambda : 0)
    
    # Set Initial Day Counters
    for fish in initialState:
        dayMap[fish] += 1

    currentDay = 0
    while (currentDay < 256):
        # Temporary Day Map to avoid operating on new results
        newDayMap = defaultdict(lambda : 0)
        for day in dayMap:
            if(day == 0):
                newDayMap[8] += dayMap[0]
                newDayMap[6] += dayMap[0]
            else:
                newDayMap[day-1] += dayMap[day]
        dayMap = copy.deepcopy(newDayMap)
        currentDay += 1
    
    totalFish = sum(dayMap.values())
    return totalFish

print("PART 1:", part1())
print("PART 2:", part2())