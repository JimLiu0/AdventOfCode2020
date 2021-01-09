f = open('input', 'r')

def getRow(s):
    rows = 128
    low = 0
    high = 127
    mid = 0

    for char in s:
        mid = (high + low) // 2
        if char == 'B':
            low = mid + 1
            mid = mid + 1
        if char == 'F':
            high = mid - 1
            mid = mid - 1

    return mid

def getCol(s):
    cols = 8
    low = 0
    high = 7
    mid = 0

    for char in s:
        mid = (high + low) // 2
        if char == 'R':
            low = mid + 1
            mid = mid + 1
        if char == 'L':
            high = mid - 1
            mid = mid - 1
        
    return mid

def getId(s):
    r = getRow(s[0:7])
    c = getCol(s[7:9])

    return r * 8 + c

ids = []

for line in f:
    currentId = getId(line)

    ids.append(currentId)

i = 904
while i in ids:
    i -= 1

print(i)
