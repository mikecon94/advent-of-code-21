import statistics

f = open("input", "r")

lines = []
for line in f.readlines():
    lines.append(line.strip())

# () is a legal chunk that contains no other chunks, as is [].
# Valid chunks include
# ([])
# {()()()}
# <([{}])>
# [<>({}){}[([])<>]]
# (((((((((())))))))))

# Some lines are incomplete, but others are corrupted.
# Find and discard the corrupted lines first.

# Examples of corrupted chunks include
# (], {()()()>
# (((()))}
# <([]){()}[{}])
# Whole line is considered corrupted.

# ): 3 points.
# ]: 57 points.
# }: 1197 points.
# >: 25137 points.
illegalCharPoints = {
                        ')': 3,
                        ']': 57,
                        '}': 1197,
                        '>': 25137
                    }
closingBrackets = {
                    '(': ')',
                    '[': ']',
                    '{' : '}',
                    '<' : '>'
                    }

autoCompletePoints = {
                        ')': 1,
                        ']': 2,
                        '}': 3,
                        '>': 4
                     }

# Stop at the first incorrect closing character on each corrupted line.
def part1():
    illegalChars = []
    for line in lines:
        stack = []
        for char in line:
            if (char == '('
                or char == '{'
                or char == '['
                or char == '<'):
                stack.append(char)
            else:
                lastChar = stack.pop()
                if (char != closingBrackets[lastChar]):
                    illegalChars.append(char)
                    break
    totalPoints = 0
    for illegalChar in illegalChars:
        totalPoints += illegalCharPoints[illegalChar]
    return totalPoints

def part2():
    completionStrings = []
    totalScores = []
    for line in lines:
        completionString = ''
        illegalLine = False
        stack = []
        score = 0
        for char in line:
            if (char == '('
                or char == '{'
                or char == '['
                or char == '<'):
                stack.append(char)
            else:
                lastChar = stack.pop()
                if (char != closingBrackets[lastChar]):
                    illegalLine = True
        if (not illegalLine):
            # Loop until the stack is empty
            while stack:
                score *= 5
                score += autoCompletePoints[closingBrackets[stack.pop()]]
            totalScores.append(score)
    return statistics.median(totalScores)

print("PART 1:", part1())
print("PART 2:", part2())