import math

class Ship():
    insts = []
    x = 0
    y = 0
    degrees = 0
    wx = 10
    wy = 1

    def __init__(self):
        lines = open('input.txt', 'r').readlines()
        self.insts = [line.strip('\n') for line in lines]

    def processInst1(self, inst):
        arg1 = inst[0]
        arg2 = int(inst[1:])

        if arg1 == 'N':
            self.y += arg2
        if arg1 == 'S':
            self.y -= arg2
        if arg1 == 'E':
            self.x += arg2
        if arg1 == 'W':
            self.x -= arg2
        if arg1 == 'L':
            self.degrees += arg2
        if arg1 == 'R':
            self.degrees -= arg2
        if arg1 == 'F':
            self.x += math.cos(math.radians(self.degrees)) * arg2
            self.y += math.sin(math.radians(self.degrees)) * arg2

    def processInst2(self, inst):
        arg1 = inst[0]
        arg2 = int(inst[1:])

        if arg1 == 'N':
            self.wy += arg2
        if arg1 == 'S':
            self.wy -= arg2
        if arg1 == 'E':
            self.wx += arg2
        if arg1 == 'W':
            self.wx -= arg2
        if arg1 == 'L':
            self.wx = self.wx * math.cos(math.radians(arg2)) - self.wy * math.sin(math.radians(arg2))
            self.wy = self.wx * math.sin(math.radians(arg2)) + self.wy * math.cos(math.radians(arg2))
        if arg1 == 'R':
            self.wx = self.wx * math.cos(math.radians(arg2)) + self.wy * math.sin(math.radians(arg2))
            self.wy = (-1 * self.wx * math.sin(math.radians(arg2))) + self.wy * math.cos(math.radians(arg2))
        if arg1 == 'F':
            self.x += (arg2 * self.wx)
            self.y += (arg2 * self.wy)

    def start1(self):
        for inst in self.insts:
            self.processInst1(inst)

    def start2(self):
        for inst in self.insts:
            self.processInst2(inst)

    def getManhattanDistance(self):
        return abs(self.x) + abs(self.y)

s = Ship()
s.start1()
print('part 1:')
print(s.getManhattanDistance())
s2 = Ship()
s2.start2()
print('part 2:')
print(s2.getManhattanDistance())

