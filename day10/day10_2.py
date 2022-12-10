lines = open('day10/input.txt').read().split('\n')

l = [20, 60, 100, 140, 180, 220]

x = 1
curr = 0
ans = 0

lx = []
for line in lines:
    match line.split(' '):
        case ['noop']:
            curr += 1
            lx += [x]
        case ['addx', num]:
            num = int(num)
            curr += 2
            lx += [x] * 2
            x += num

for i, x in enumerate(lx):
    if abs(i % 40 - x) <= 1:
        print('#', end='')
    else:
        print('.', end='')
    if i % 40 == 39:
        print()