lines = open('day8/input.txt').read().split('\n')

grid = {}

h = len(lines)
w = None
for i, line in enumerate(lines):
    if w is None:
        w = len(line)
    elif w != len(line):
        raise Exception('Invalid line length')
    for j, height in enumerate(line):
        grid[(i, j)] = int(height)

def out_of_bounds(i, j):
    return i < 0 or j < 0 or i >= h or j >= w

visible = set()
dirs = [(1, 0), (0, 1), (-1, 0), (0, -1)]
for i in range(h):
    for j in range(w):
        current_height = grid[(i, j)]
        for dir in dirs:
            x, y = i, j
            while True:
                x += dir[0]
                y += dir[1]
                if out_of_bounds(x, y):
                    visible.add((i, j))
                    break
                if grid[(x, y)] >= current_height:
                    break

print(len(visible))

