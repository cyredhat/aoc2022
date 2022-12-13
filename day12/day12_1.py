data = open('day12/input.txt').read()

grid = {}
start = None
end = None
for i, line in enumerate(data.split('\n')):
    for j, x in enumerate(line):
        if ord('a') <= ord(x) <= ord('z'):
            grid[i, j] = ord(x) - ord('a')
        elif x == 'S':
            start = (i, j)
            grid[i, j] = 1000000
        elif x == 'E':
            end = (i, j)
            grid[i, j] = ord('z') - ord('a')
        else:
            raise Exception('ajsdkfl')

queue = [(start, 0)]
visited = set()

while queue != []:
    (i, j), step = queue.pop(0)
    if (i, j) in visited:
        continue
    if (i, j) == end:
        print(step)
    visited.add((i, j))
    for di, dj in [(1, 0), (0, 1), (-1, 0), (0, -1)]:
        x, y = i + di, j + dj
        if (x, y) in grid:
            if grid[x, y] <= grid[i, j] + 1:
                queue.append(((x, y), step + 1))
