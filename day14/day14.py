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

def calculateScoreFromTemplate(template):
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



def combineDicts(dict1, dict2):
    newDict = copy.deepcopy(dict1)
    for key in dict2:
        newDict[key] = dict1.get(key, 0) + dict2[key]
    return newDict

def calculateScoreFromCounts(charCounts):
    highestCount = 0
    lowestCount = float('inf')
    for value in charCounts.values():
        if (value > highestCount):
            highestCount = value
        elif (value < lowestCount):
            lowestCount = value
    return highestCount - lowestCount

# Part 1 - Simple Solution
# BFS - expanding the string each iteration.
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
    return calculateScoreFromTemplate(polymerTemplate)

# Memoisation
visitedPairs = dict()
# Recursive solution (DFS with Memoisation)
# Returns a dictionary of char counts.
def calculate(pair, remainingIterations):
    # Base Case - Reached 0 iterations remaining so count the chars in the pair.
    if (remainingIterations == 0):
        charCount = dict()
        charCount[pair[0]] = 1
        return charCount
    # Check if we already have a result for this pair & depth
    elif (visitedPairs.get(pair, None) != None
         and visitedPairs.get(pair).get(remainingIterations, None) != None):
            return visitedPairs.get(pair).get(remainingIterations)
    else:
        firstPair = pair[0] + insertionRules[pair]
        secondPair = insertionRules[pair] + pair[1]
        firstPairCounts = calculate(firstPair, remainingIterations - 1)
        secondPairCounts = calculate(secondPair, remainingIterations - 1)
        result = combineDicts(firstPairCounts, secondPairCounts)

        if(visitedPairs.get(pair, None) == None):
            visitedPairs[pair] = {remainingIterations: result}
        else:
            visitedPairs[pair].update({remainingIterations: result})

        return result

def part2():
    iterations = 40
    charCounts = {startingTemplate[-1]: 1}
    for index in range(0, len(startingTemplate) - 1):
        newPair = startingTemplate[index] + startingTemplate[index+1]
        charCounts = combineDicts(charCounts, calculate(newPair, iterations))

    return calculateScoreFromCounts(charCounts)

print("PART 1:", runPairInsertions(10))
print("PART 2:", part2())
