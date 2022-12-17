# data = open('day17/tc.txt').read()
data = open('day17/input.txt').read()

rocks = [
  ([(0,0), (0,1), (0, 2), (0, 3)], 4),
  ([(0,1), (1,0), (1, 1), (1, 2), (2, 1)], 3),
  ([(0,0), (0,1), (0, 2), (1, 2), (2, 2)], 3),
  ([(0,0), (1,0), (2, 0), (3, 0)], 1),
  ([(0,0), (0,1), (1, 0), (1, 1)], 2),
]

jets = [-1 if c == '<' else 1 for c in data]

grid = {}
bottom = -1
curr = 0
def collide(coord, rock):
  y, x = coord
  if x < 0 or x > 6 or y < 0:
    return True
  for ry, rx in rock:
    ny, nx = y + ry, x + rx
    if ny < 0 or nx < 0 or nx > 6 or (ny, nx) in grid:
      return True
  
def visualize():
  for y in range(bottom, -1, -1):
    print('|', end='')
    for x in range(7):
      print('#' if (y, x) in grid else ' ', end='')
    print('|')
  print('-' * 9)

for i in range(2022):
  rock, width = rocks[i % len(rocks)]
  y, x = (bottom + 4, 2)
  while True:
    y, x = y, x + jets[curr]
    if collide((y, x), rock):
      x -= jets[curr]
    curr = (curr + 1) % len(jets)
    y, x = y - 1, x
    if collide((y, x), rock):
      y += 1
      for ry, rx in rock:
        grid[(y + ry, x + rx)] = True
        bottom = max(bottom, y + ry)
      break

print(bottom + 1)

# visualize()