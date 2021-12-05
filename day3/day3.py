f = open("input", "r")

binaryInput = []
for line in f.readlines():
    binaryInput.append(line.strip())

# Power Consumption = Gamma Rate * Epsilon Rate
# Each bit in the gamma rate can be determined by
# finding the most common bit in the corresponding
# position of all numbers in the diagnostic report
def calculateGammaRate():
    totalValues = [0] * len(binaryInput[0])
    sizeOfInput = len(binaryInput)
    for line in binaryInput:
        # print(line)
        for index, char in enumerate(line):
            value = int(char)
            # print(index, char)
            totalValues[index] += value
    # print(totalValues)
    gammaRate = ""
    for totalValue in totalValues:
        if (totalValue > sizeOfInput / 2):
            gammaRate += "1"
        else:
            gammaRate += "0"
    return gammaRate

def calculateEpsilonRate(gammaRate):
    mask = "1" * len(gammaRate)
    epsilonRate = int(gammaRate, 2) ^ int(mask, 2)
    return epsilonRate

def getModeAtIndex(diagnostics, index):
    totalOnes = 0
    for diagnostic in diagnostics:
        if (diagnostic[index] == "1"):
            totalOnes += 1
    
    if (totalOnes >= len(diagnostics)/2):
        return "1"
    else:
        return "0"

def calculateOxygenRating(diagnostics, index):
    # print(index, diagnostics)
    if (len(diagnostics) == 1):
        return diagnostics[0]
    else:
        # Get the mode at index
        # Equal values = 1
        mode = getModeAtIndex(diagnostics, index)
        # Create new list with only the diagnostics that have the mode at this index
        newDiagnostics = []
        # print(index, mode)
        for diagnostic in diagnostics:
            # print(diagnostic[index], mode)
            if(diagnostic[index] == mode):
                newDiagnostics.append(diagnostic)

        return calculateOxygenRating(newDiagnostics, index+1)

def calculateScrubberRating(diagnostics, index):
    if (len(diagnostics) == 1):
        return diagnostics[0]
    else:
        # Get the mode at index
        # Equal values = 1
        mode = getModeAtIndex(diagnostics, index)
        # Create new list with only the diagnostics that have the mode at this index
        newDiagnostics = []
        # print(index, mode)
        for diagnostic in diagnostics:
            # print(diagnostic[index], mode)
            if(diagnostic[index] != mode):
                newDiagnostics.append(diagnostic)

        return calculateScrubberRating(newDiagnostics, index+1)

def part1():
    gammaRateStr = calculateGammaRate()
    epsilonRate = calculateEpsilonRate(gammaRateStr)
    gammaRate = int(gammaRateStr, 2)
    return gammaRate * epsilonRate

# Generate Life Support Rating
# Oxygen Generator Rating & C02 Scrubber Rating
def part2():
    oxygenRating = calculateOxygenRating(binaryInput, 0)
    scrubberRating = calculateScrubberRating(binaryInput, 0)
    result = int(oxygenRating, 2) * int(scrubberRating, 2)
    return result

print("PART 1:", part1())
print("PART 2:" , part2())