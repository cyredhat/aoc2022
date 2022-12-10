visited = set()

positions = [(0, 0)] * 10
visited.add(positions[-1])

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
        positions[0] = move_head(positions[0], dir)
        for j in range(len(positions) - 1):
            positions[j+1] = calc_tail_pos(positions[j], positions[j+1])
        visited.add(positions[-1])

print(len(visited))