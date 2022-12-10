with open('day4/input.txt', 'r') as f:
    global lines
    lines = [line.split(',') for line in f.read().split('\n')]

def extract_coords(s):
    s = s.split('-')
    return (int(s[0]), int(s[1]))

def overlap(x, y):
    if  x[0] <= y[1] <= x[1] or y[0] <= x[1] <= y[1]:
        return True
    return False

count = 0
for line in lines:
    s1, s2 = line
    s1, s2 = extract_coords(s1), extract_coords(s2)
    # print(s1, s2)
    if overlap(s1, s2):
        # print('contains')
        count += 1
    else:
        print(s1, s2)

print(count)
