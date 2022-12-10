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
max_scenic_score = 0
for i in range(h):
    for j in range(w):
        current_height = grid[(i, j)]
        score = [0] * 4
        for dir_i, dir in enumerate(dirs):
            x, y = i, j
            while True:
                x += dir[0]
                y += dir[1]
                if out_of_bounds(x, y):
                    break
                if grid[(x, y)] >= current_height:
                    score[dir_i] += 1
                    break
                score[dir_i] += 1
        print(i, j, score)
        scenic_score = score[0] * score[1] * score[2] * score[3]
        max_scenic_score = max(max_scenic_score, scenic_score)

print(max_scenic_score)

