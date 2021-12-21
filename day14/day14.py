import copy
from os import SCHED_OTHER, PathLike
f = open("input", "r")

startingTemplate = list(f.readline().strip())
f.readline()

insertionRules = dict()
for line in f.readlines():
    line = line.strip()
    pair = line.split(" -> ")[0]
    insertionRules[pair] = line.split(" -> ")[1]

def calculateScore(template):
    highestValue = 0
    lowestValue = float('inf')
    charScores = dict()
    for char in template:
        charScores[char] = charScores.get(char, 0) + 1
        if(charScores[char] > highestValue):
            highestValue = charScores[char]
    for value in charScores.values():
        if(value < lowestValue):
            lowestValue = value

    score = highestValue - lowestValue
    return score

def runPairInsertions(noOfIterations):
    polymerTemplate = copy.deepcopy(startingTemplate)
    iterationCount = 0
    while (iterationCount < noOfIterations):
        newTemplate = []
        lastChar = ""
        for char in polymerTemplate:
            currentPair = lastChar + char
            newTemplate += insertionRules.get(currentPair, "")
            newTemplate += char
            lastChar = char
        polymerTemplate = newTemplate
        iterationCount += 1
    return calculateScore(polymerTemplate)

# This recursive method gets the correct result but is just as slow as part 1.
# This is DFS whilst the method used for Part 1 is BFS.
# It requires some preparation - e.g. to call with NNCB.
#   charValues["N"] = 2
#   charValues["C"] = 1
#   charValues["B"] = 1
#   calculate("NN", "C", 0, 40, charValues)
#   calculate("NC", "B", 0, 40, charValues)
#   calculate("CB", "H", 0, 40, charValues)

# Visited Pairs:
# Dictionary of pairs to track values for previously visited pairs.
# NN -> {
#           1 -> {
#                   Values: {B: 2, N: 1}
#                   String: {"NBB"}
#                }
#       }
visitedPairs = dict()
def calculate(pair, insertedChar, currentIteration, iterationLimit, charValues):
    if(currentIteration == iterationLimit):
        print(charValues)
        return pair
    else:
        charValues[insertedChar] = charValues.get(insertedChar, 0) + 1
        newPair1 = pair[0] + insertedChar
        newPair2 = insertedChar + pair[1]
        # Memoization
        # If we have already calculated a pair for a certain number of iterations then update those values instead.


        return calculate(newPair1, insertionRules[newPair1], currentIteration+1, iterationLimit, charValues) \
                + calculate(newPair2, insertionRules[newPair2],currentIteration+1, iterationLimit, charValues)

def part2():
    charValues = dict()
    charValues["N"] = 2
    charValues["C"] = 1
    charValues["B"] = 1
    calculate("NN", "C", 0, 40, charValues)
    calculate("NC", "B", 0, 40, charValues)
    calculate("CB", "H", 0, 40, charValues)
    print(charValues)
    return 0

print("PART 1:", runPairInsertions(10))
print("PART 2:", part2())
