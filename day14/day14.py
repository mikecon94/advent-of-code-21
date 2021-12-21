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

print("PART 1:", runPairInsertions(10))
