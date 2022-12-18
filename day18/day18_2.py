import sys
# data = open('day18/tc.txt').read()
data = open('day18/input.txt').read()

sys.setrecursionlimit(100000000)

grid = {}

minx, maxx = float('inf'), float('-inf')
miny, maxy = float('inf'), float('-inf')
minz, maxz = float('inf'), float('-inf')


for line in data.split('\n'):
  x, y, z = [int(x) for x in line.split(',')]
  grid[(x, y, z)] = True
  minx, maxx = min(minx, x), max(maxx, x)
  miny, maxy = min(miny, y), max(maxy, y)
  minz, maxz = min(minz, z), max(maxz, z)
minx -= 1
maxx += 1
miny -= 1
maxy += 1
minz -= 1
maxz += 1

outside = set()
def dfs(x, y, z):
  global grid, outside, minx, maxx, miny, maxy, minz, maxz
  if (x, y, z) in grid or (x, y, z) in outside:
    return
  if x < minx or x > maxx or y < miny or y > maxy or z < minz or z > maxz:
    return
  outside.add((x, y, z))
  for dir in [(1, 0, 0), (0, 1, 0), (0, 0, 1), (-1, 0, 0), (0, -1, 0), (0, 0, -1)]:
    dfs(x + dir[0], y + dir[1], z + dir[2])

count = 0
dfs(minx, miny, minz)
for (x, y, z) in grid:
  for dir in [(1, 0, 0), (0, 1, 0), (0, 0, 1), (-1, 0, 0), (0, -1, 0), (0, 0, -1)]:
    if (x + dir[0], y + dir[1], z + dir[2]) in outside:
      count += 1

print(count)
