f = open("input", "r")

inputSignals = []
outputValues = []
for line in f.readlines():
    inputSignals.append(line.split(" | ")[0].strip().split(" "))
    outputValues.append(line.split(" | ")[1].strip().split(" "))

# The four-digit seven-segment displays are malfunctioning
# 7 Segments named a through g
#   aaaa
#  b    c
#  b    c
#   dddd
#  e    f
#  e    f
#   gggg
# Signals which control segments (a-g) are mixed up on each display
# Signal wires (a-g) are connected to segments randomly.
# The wire/segment connections are mixed up separately for each 4 Digit display.
# All digits within a display use the same connections.

# 10 Unique Signal Patterns | 4 Digit Output Value

def part1():
    counter = 0
    for outputValue in outputValues:
        for digit in outputValue:
            if(len(digit) == 2
                or len(digit) == 3
                or len(digit) == 4
                or len(digit) == 7):
                counter += 1
    return counter


# acedgfb cdfbe gcdfa fbcad dab cefabd cdfgeb eafb cagedb ab | cdfeb fcadb cdfeb cdbaf
#  dddd
# e    a
# e    a
#  ffff
# g    b
# g    b
#  cccc

# Signal:
# acedgfb: 8
# cdfbe: 5
# gcdfa: 2
# fbcad: 3
# dab: 7
# cefabd: 9
# cdfgeb: 6
# eafb: 4
# cagedb: 0
# ab: 1

# Output:
# cdfeb: 5
# fcadb: 3
# cdfeb: 5
# cdbaf: 3

def createInitialDictionary():
    newDictionary = dict()
    for x in range(0, 10):
        newDictionary[x] = ["a", "b", "c", "d", "e", "f", "g"]
    print(newDictionary)
    return newDictionary

def calculateLettersMap(signals):
    # Sorted ['ab', 'dab', 'eafb', 'cdfbe', 'gcdfa', 'fbcad', 'cefabd', 'cdfgeb', 'cagedb', 'acedgfb']
    signals = sorted(signals, key=len)   
    # Index 0 = Digit 1
    # Index 1 = Digit 7
    # Index 2 = Digit 4
    # Index 9 = Digit 8 (Useless)
    lettersDict = dict()
    lettersDict[1] = set(signals[0])
    lettersDict[4] = set(signals[2])
    lettersDict[7] = set(signals[1])
    lettersDict[8] = set(signals[9])

    # Derive 9 by checking the 7 char string using the same chars as 4 & 7
    # Indexes 6-8 contain 7 chars
    lettersInNine = lettersDict[4].union(lettersDict[7])
    remainingSixCharSignals = []
    for index in range(6, 9):
        signal = set(signals[index])
        if(signal.issuperset(lettersInNine)):
            lettersDict[9] = signal
        else:
            remainingSixCharSignals.append(set(signals[index]))
    
    # 9 tells us which letter is at the bottom of the display
    # 6 is the 6 Char string that does not contain BOTH letters in Digit 1
    # 0 is the remaining 6 Char string (it contains both digits in 1)
    if (remainingSixCharSignals[0].issuperset(set(lettersDict[1]))):
        lettersDict[0] = set(remainingSixCharSignals[0])
        lettersDict[6] = set(remainingSixCharSignals[1])
    else:
        lettersDict[0] = set(remainingSixCharSignals[1])
        lettersDict[6] = set(remainingSixCharSignals[0])
        
    # 5 is a subset of 6 but 2 & 3 are not.
    # Signals with length 5 are indexes 3-5
    remainingThreeCharSignals = []
    for index in range(3, 6):
        signal = set(signals[index])
        if(signal.issubset(lettersDict[6])):
            lettersDict[5] = signal
        else:
            remainingThreeCharSignals.append(signal)

    # 3 is a subset of 9 but 2 is not
    if (remainingThreeCharSignals[0].issubset(lettersDict[9])):
        lettersDict[3] = remainingThreeCharSignals[0]
        lettersDict[2] = remainingThreeCharSignals[1]
    else:
        lettersDict[3] = remainingThreeCharSignals[1]
        lettersDict[2] = remainingThreeCharSignals[0]
    return lettersDict

def calculateDigitFromMap(digit, lettersDict):
    digit = set(digit)
    for number in lettersDict:
        if (lettersDict[number] == digit):
            return number

def part2():
    total = 0
    for index, signals in enumerate(inputSignals):
        lettersDict = (calculateLettersMap(signals))
        displayDigits = ""
        for outputDigit in outputValues[index]:
            displayDigits += str(calculateDigitFromMap(outputDigit, lettersDict))
        total += int(displayDigits)

    return total

print("PART 1:", part1())
print("PART 2:", part2())
