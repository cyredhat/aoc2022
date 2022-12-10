visited = set()

tail_pos = (0, 0)
head_pos = (0, 0)
visited.add(tail_pos)

moves = None
with open('day9/input1.txt', 'r') as f:
    moves = [s.split(' ') for s in f.read().split('\n')]

move_dir = {
    'D': (0, -1),
    'U': (0, 1),
    'L': (-1, 0),
    'R': (1, 0),
}

def calc_tail_pos(head, tail):
    diffX = head[0] - tail[0]
    diffY = head[1] - tail[1]
    if (abs(diffX) + abs(diffY) == 3):
        newX = diffX / abs(diffX)
        newY = diffY / abs(diffY)
        return (tail[0] + int(newX), tail[1] + int(newY))
    return (tail[0] + int(diffX / 2), tail[1] + int(diffY / 2))

def move_head(pos, dir):
    d = move_dir[dir]
    return (pos[0] + d[0], pos[1] + d[1])

for move in moves:
    dir, move_len = move[0], int(move[1])
    print(dir, move_len)
    for i in range(move_len):
        head_pos = move_head(head_pos, dir)
        tail_pos = calc_tail_pos(head_pos, tail_pos)
        visited.add(tail_pos)
        print(head_pos, tail_pos)

print(len(visited))