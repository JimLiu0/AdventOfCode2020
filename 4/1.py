import re

expectedFields = ['byr', 'iyr', 'eyr', 'hgt', 'hcl', 'ecl', 'pid']

# This will end up returning a list of passport strings
def getPassports():
    f = open("input", "r")
    lines = f.read().split('\n\n')
    lines = [line.replace('\n', ' ') for line in lines]
    
    sum = 0
    for passport in lines:
        if isPassportValid(passport):
            sum += 1

    return sum

def isPassportValid(passport):
    keyValuePairs = re.split('\s', passport)
    keys = [pair.split(':')[0] for pair in keyValuePairs]

    for field in expectedFields:
        if not field in keys:
            return False

    return True


print(getPassports())
