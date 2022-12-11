data = open('day11/input.txt', 'r').read().split('\n\n')

class Monkey:
    def __init__(self, items: list[int], operation: str, test: int, iftrue: int, iffalse: int):
        self.items= items
        self.operation = operation
        self.test = test
        self.iftrue = iftrue
        self.iffalse = iffalse
    
    def additem(self, item):
        self.items.append(item)

class MonkeyList:
    def __init__(self):
        self.monkeys = {}
        self.count = {}
    
    def add(self, index, monkey: Monkey):
        self.monkeys[index] = monkey
        self.count[index] = 0
    
    def calc(self, index):
        monkey = self.monkeys[index]
        self.count[index] += len(monkey.items)
        for old in monkey.items:
            new = eval(monkey.operation)
            new //= 3
            if new % monkey.test == 0:
                new_monkey = monkey.iftrue
            else:
                new_monkey = monkey.iffalse
            self.monkeys[new_monkey].additem(new)
        monkey.items = []
    
    def calc_all(self):
        for i in self.monkeys:
            self.calc(i)


monkeylist = MonkeyList()
for d in data:
    lines = d.split('\n')
    index = int(lines[0].split(':')[0][7:])
    items = [int(x) for x in lines[1].split(': ')[1].split(', ')]
    operation = lines[2].split('= ')[1]
    test = int(lines[3].split('by ')[1])
    iftrue = int(lines[4].split('monkey ')[1])
    iffalse = int(lines[5].split('monkey ')[1])
    monkey = Monkey(items, operation, test, iftrue, iffalse)
    monkeylist.add(index, monkey)

for i in range(20):
    monkeylist.calc_all()

sorted_count = sorted(list(monkeylist.count.values()))
print(sorted_count[-1] * sorted_count[-2])

