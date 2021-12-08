f = open("input", "r")

outputValues = []
for line in f.readlines():
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
        for signal in outputValue:
            if(len(signal) == 2
                or len(signal) == 3
                or len(signal) == 4
                or len(signal) == 7):
                counter += 1
    return counter

print("PART 1:", part1())
