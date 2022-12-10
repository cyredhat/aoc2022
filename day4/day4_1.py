with open('day4/input.txt', 'r') as f:
    global lines
    lines = [line.split(',') for line in f.read().split('\n')]

def extract_coords(s):
    s = s.split('-')
    return (int(s[0]), int(s[1]))

def contains(x, y):
    if x[0] == y[0]:
        return True
    if x[0] > y[0]:
        x, y = y, x
    return x[0] <= y[0] and y[1] <= x[1]

count = 0
for line in lines:
    s1, s2 = line
    s1, s2 = extract_coords(s1), extract_coords(s2)
    print(s1, s2)
    if contains(s1, s2):
        print('contains')
        count += 1

print(count)
