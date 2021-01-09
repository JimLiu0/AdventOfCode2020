f = open('input.txt', 'r')
lines = [line.strip('\n') for line in f.readlines()]

def convert(s):
    l = []
    l[:]=s
    return l

lines = [convert(l) for l in lines]
    

h = len(lines)
w = len(lines[0])

def getNumOccupiedSquares(grid, x, y):
    count = 0

    for i in range(-1, 2):
        for j in range(-1, 2):
            nx = x + i
            ny = y + j
            
            flag = 1
            while flag:
                flag = 0

                if (nx > -1 and nx < h) and (ny > -1 and ny < w) and (i != 0 or j != 0):
                    if (grid[nx][ny] == '#'): 
                        count += 1
                    elif (grid[nx][ny] == '.'):
                        flag = 1

                nx = nx + i
                ny = ny + j

    return count

flag = 1

def copy(l):
    n = []

    for x in l:
        t = []
        for y in x:
            t.append(y)
        n.append(t)

    return n

while flag:
    flag = 0
    cp = copy(lines)

    for i in range(h):
        for j in range(w):
            square = lines[i][j]
            numOcc = getNumOccupiedSquares(lines, i, j)
            if square != '.':
                if numOcc >= 5:
                    cp[i][j] = 'L'
                if numOcc == 0:
                    cp[i][j] = '#'

            if cp[i][j] != lines[i][j]:
                flag = 1
    lines = cp

totalOcc = sum([l.count('#') for l in lines])

print('part 2:')
print(totalOcc)

