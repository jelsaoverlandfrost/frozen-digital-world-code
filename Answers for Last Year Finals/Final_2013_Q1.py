# Initialize the grid
def init():
    grid = [['_', '_', '_'], ['_', '_', '_'], ['_', '_', '_']]
    return grid


# Show the grid
def show(grid):
    stringDisplay = ''
    for i in range(0, 3):
        for j in range(0, 3):
            stringDisplay += grid[i][j]
        if i < 2:
            stringDisplay += '\n'
    return stringDisplay


# Letting x to take a move
def movex(grid, x, y):
    x -= 1
    y -= 1
    grid[x][y] = 'x'


# Letting o to take a move
def moveo(grid, x, y):
    x -= 1
    y -= 1
    grid[x][y] = 'o'


# Count the total number of moves
def countMoves(grid):
    count = 0
    for i in range(0, 3):
        for j in range(0, 3):
            if grid[i][j] != '_':
                count += 1
    return count


# Get the move history
def getMoves(grid):
    # History for x and o
    moveListx = []
    moveListo = []
    for i in range(0, 3):
        for j in range(0, 3):
            if grid[i][j] == 'x':
                moveListx.append((i + 1, j + 1))
            elif grid[i][j] == 'o':
                moveListo.append((i + 1, j + 1))
    moveDict = {'x': moveListx, 'o': moveListo}
    return moveDict


# Judge if the x player has win
def winsx(grid):
    judge = False
    for i in range(0, 3):
        if grid[i][0] == grid[i][1] == grid[i][2] == 'x':
            judge = True
    for j in range(0, 3):
        if grid[0][j] == grid[1][j] == grid[2][j] == 'x':
            judge = True
    if (grid[0][0] == grid[1][1] == grid[2][2] == 'x') or (grid[0][2] == grid[1][1] == grid[2][0] == 'x'):
        judge = True
    return judge


# Judge if the o player has win
def winso(grid):
    judge = False
    for i in range(0, 3):
        if grid[i][0] == grid[i][1] == grid[i][2] == 'o':
            judge = True
    for j in range(0, 3):
        if grid[0][j] == grid[1][j] == grid[2][j] == 'o':
            judge = True
    if (grid[0][0] == grid[1][1] == grid[2][2] == 'o') or (grid[0][2] == grid[1][1] == grid[2][0] == 'o'):
        judge = True
    return judge
