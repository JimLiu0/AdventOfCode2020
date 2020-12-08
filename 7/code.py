# 2 pass system
# first pass is to make sure every bag type has something assigned to it
# second pass is to expand on the parent bags that have children bags

f = open('input.txt', 'r')
lines = f.readlines()


bagDict = {}
for line in lines:
    processedStr = line.replace('bags', '')
    processedStr = processedStr.replace('bag', '')

    split = processedStr.strip('\n').split(' contain ')
    
    parentBag = split[0]
    parentBag = parentBag.strip()

    childBags = split[1]
    childBags = childBags.replace(' .', '')
    childBags = childBags.split(' , ')

    childDict = {}
    for bag in childBags:
        if bag != "no other":
            num = bag.split(' ', 1)[0]
            bagColor = bag.split(' ', 1)[1]
            childDict[bagColor] = num
   
    bagDict[parentBag] = childDict

bagSet = set()
def getParentBagCount(bagList, childDict):
    if len(bagList) == 0:
        return

    newList = []

    for key, value in bagDict.items():
        for key2 in value.keys():
            if key2 in bagList:
                bagSet.add(key)
                newList.append(key)

    getParentBagCount(newList, childDict)

getParentBagCount(['shiny gold'], childDict)

print("part 1: ")
print(len(bagSet))

bagCount = 0

childrenBags = ['shiny gold']

def countBags(bag):
    count = 0

    print('Bag: ' + bag)
    if (len(bagDict[bag].items()) == 0):
        return 1

    for key, value in bagDict[bag].items():
        print('Key: ' + key)
        print('Value: ' + value)
        count += (int(value) * countBags(key))

    return 1 + count

print("part 2: ")
print(countBags('shiny gold') - 1)
