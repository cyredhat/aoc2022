lines = open('day10/input.txt').read().split('\n')

l = [20, 60, 100, 140, 180, 220]

x = 1
curr = 0
ans = 0
for line in lines:
    if len(l) == 0:
        break
    match line.split(' '):
        case ['noop']:
            curr += 1
            while len(l) > 0 and curr >= l[0]:
                ans += l.pop(0) * x
        case ['addx', num]:
            num = int(num)
            curr += 2
            while len(l) > 0 and curr >= l[0]:
                ans += l.pop(0) * x
            x += num
    
print(ans)
