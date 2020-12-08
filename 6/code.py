f = open('input.txt', 'r')
groups = f.read().split('\n\n')

s = 0
s2 = 0

for groupAnswers in groups:
    strippedAnswers = ''.join(groupAnswers.split())
    answerSet = set(strippedAnswers)
    s += len(answerSet)

    lineArrays = groupAnswers.split('\n')

    #the last group answer has an empty char on it
    if '' in lineArrays:
        lineArrays.remove('')    

    listOfSets = [set(l) for l in lineArrays]
    s2 += len(set.intersection(*listOfSets))


print('part 1: ')
print(s)

print('part 2: ')
print(s2)
