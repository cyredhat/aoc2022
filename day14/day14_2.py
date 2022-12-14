data = open('day14/input.txt').read()


grid = {}

def fill_grid(prev, curr):
  x1, y1 = prev
  x2, y2 = curr
  if x1 == x2:
    for y in range(min(y1, y2), max(y1, y2) + 1):
      grid[(x1, y)] = '#'
  else:
    for x in range(min(x1, x2), max(x1, x2) + 1):
      grid[(x, y1)] = '#'

rockbottom = 0
for line in data.split('\n'):
  prev = None
  for coords in line.split('->'):
    if coords == '':
      continue
    x, y = [int(x) for x in coords.split(',')]
    if prev is None:
      prev = (x, y)
      continue
    if y > rockbottom:
      rockbottom = y
    fill_grid(prev, (x, y))
    prev = (x, y)

def sand_falling(x, y):
  for dir in [0, -1, 1]:
    x2 = x + dir
    y2 = y + 1
    if (x2, y2) not in grid and y2 != rockbottom + 2:
      return sand_falling(x2, y2)
  grid[(x, y)] = 'o'
  if (x, y) == (500, 0):
    return False
  return True

count = 0
while True:
  if sand_falling(500, 0):
    count += 1
  else:
    print(count + 1)
    break
    
