f = open("input.txt", "r")

lines = f.readlines()
lines = [line.strip("\n") for line in lines]

preambleSize = 25

sums = []

def getAllPairs(nums):
    
    pairs = set()
    for num1 in nums:
        for num2 in nums:
            if num1 != num2:
                pairs.add(num1 + num2)

    return pairs

invalidIndex = 0

for i in range(preambleSize, len(lines)):
    preamble = [int(num) for num in lines][i - preambleSize: i]

    if int(lines[i]) not in getAllPairs(preamble):
        print('Part 1: ')
        print(lines[i])
        invalidIndex = i
        break

invalidNum = int(lines[invalidIndex])
l = [int(num) for num in lines]
for i in range(invalidIndex):
    for j in range(invalidIndex):
        if abs(i - j) > 0:
            if j > i:
                accSum = sum(l[i: j+1])
                if accSum == invalidNum:
                    print('Part 2: ')
                    print(min(l[i: j+1]) + max(l[i: j+1]))
            else:
                accSum = sum(l[j: i+1])
                if accSum == invalidNum:
                    print('Part 2: ')
                    print(min(l[j: i+1]) + max(l[j: i+1]))
