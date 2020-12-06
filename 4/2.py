import re

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

def isFourDigitNum(s):
    pattern = re.compile('\d{4}')
    if pattern.fullmatch(s):
        return True
    return False

def isNineDigitNum(s):
    pattern = re.compile('\d{9}')
    if pattern.fullmatch(s):
        return True
    return False

def isValidHeight(s):
    pattern = re.compile("(\d+)(cm|in)$")
    match = re.search(pattern, s)
    
    if match:
        num = int(match.group(1))
        unit = match.group(2)

        if unit == 'cm':
            if num >= 150 and num <= 193:
                return True

        if unit == 'in':
            if num >= 59 and num <= 76:
                return True
    return False

def isHex(s):
    pattern = re.compile("^#([0-9|a-f]{6})")
    match = re.search(pattern, s)

    if match:
        return True

def isPassportValid(passport):
    expectedFields = ['byr', 'iyr', 'eyr', 'hgt', 'hcl', 'ecl', 'pid']
    keyValuePairs = re.split('\s', passport)

    for keyValuePair in keyValuePairs:
        lst = keyValuePair.split(':')
        
        key = lst[0]
        value = lst[1]

        if key == 'byr':
            if not(isFourDigitNum(value) and (int(value) >= 1920 and int(value) <= 2002)):
                return False
        if key == 'iyr':
            if not(isFourDigitNum(value) and (int(value) >= 2010 and int(value) <= 2020)):
                return False
        if key == 'eyr':
            if not(isFourDigitNum(value) and (int(value) >= 2020 and int(value) <= 2030)):
                return False
        if key == 'hgt':
            if not isValidHeight(value):
                return False
        if key == 'hcl':
            if not isHex(value):
                return False
        if key == 'ecl':
            if not (value in ['amb', 'blu', 'brn', 'gry', 'grn', 'hzl', 'oth']):
                return False
        if key == 'pid':
            if not isNineDigitNum(value):
                return False

        #Always remove a field from fields
        if key in expectedFields:
            expectedFields.remove(key)

    if len(expectedFields) == 0:
        return True
    return False

print(getPassports())
