import copy

f = open("input", "r")

# input = []
# for line in f.readlines():
#     input.append(line.strip())

# BINGO
# 5x5 Boards
# Diagonals don't count.
# Result is sum of unmarked numbers on the winning board.
# Multiply by the last number called.

numbersCalled = list(map(lambda x: int(x), f.readline().split(",")))
# print("Numbers Called:", numbersCalled)
# print()
f.readline()

def printBoards(boards):
    for board in boards:
        for row in board:
            for x in row:
                print(x, " ", end='')
            print()
        print()

# Contain an array of each board (3D Array)
boards = []
# 2D Array of Current Board
currentBoard = []
for line in f.readlines():
    if (line == "\n"):
        boards.append(currentBoard)
        currentBoard = []
    else:
        currentLine = filter(lambda x: (x != ''), line.split(" "))
        currentLine = list(map(lambda x: int(x.strip()), currentLine))
        currentBoard.append(currentLine)
boards.append(currentBoard)

def boardHasWon(board):
    for x in range(len(board)):
        currentColumMarkCount = 0
        currentRowMarkCount = 0
        for y in range(len(board[x])):
            if(board[x][y] == -1):
                currentColumMarkCount += 1
            if(board[y][x] == -1):
                currentRowMarkCount += 1
        if (currentColumMarkCount == len(board)):
            return True
        if (currentRowMarkCount == len(board[x])):
            return True
    return False

def playBingo():
    noBoardHasWon = True
    while noBoardHasWon:
        currentNumber = numbersCalled.pop(0)
        winner = -1
        for index, board in enumerate(boards):
            for x in range(len(board)):
                for y in range(len(board[x])):
                    if(board[x][y] == currentNumber):
                        board [x][y] = -1
                        if(boardHasWon(boards[index])):
                            noBoardHasWon = False
                            winner = index
        if(not noBoardHasWon):
            return winner, currentNumber

def getSumOfUnmarkedNumbers(board):
    total = 0
    for row in board:
        for value in row:
            if (value != -1):
                total += value
    return total

def removeWonBoards():
    for index, board in enumerate(boards):
        if(boardHasWon(board)):
            boards.remove(board)

def part1():
    winningIndex, lastNumber = playBingo()
    getSumOfUnmarkedNumbers(boards[winningIndex])
    return getSumOfUnmarkedNumbers(boards[winningIndex]) * lastNumber

def part2():
    lastNumber = -1
    lastSum = -1
    while(len(boards) > 0 and len(numbersCalled) > 0):
        winningIndex, lastNumber = playBingo()
        lastSum = getSumOfUnmarkedNumbers(boards[winningIndex])
        boards.pop(winningIndex)
        # Multiple boards can win on the same number.
        removeWonBoards()
    return lastSum * lastNumber

print("PART 1:", part1())
print("PART 2:" , part2())