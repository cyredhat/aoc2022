# data = open('day18/tc.txt').read()
data = open('day18/input.txt').read()

grid = {}

count = 6 * len(data.split('\n'))
for line in data.split('\n'):
  x, y, z = [int(x) for x in line.split(',')]
  grid[(x, y, z)] = True
  for dir in [(1, 0, 0), (0, 1, 0), (0, 0, 1), (-1, 0, 0), (0, -1, 0), (0, 0, -1)]:
    if (x + dir[0], y + dir[1], z + dir[2]) in grid:
      count -= 2

print(count)
