data = open('day15/input.txt').read()

def manhattan_distance(a, b):
  return abs(a[0] - b[0]) + abs(a[1] - b[1])

sensors = []
ss = set()
max_dist = 0

x_not_beacon = {}
for line in data.split('\n'):
  sensor, beacon = line.split(':')
  s = int(sensor.split(',')[0].split('=')[1]), int(sensor.split(',')[1].split('=')[1])
  b = int(beacon.split(',')[0].split('=')[1]), int(beacon.split(',')[1].split('=')[1])
  dist = manhattan_distance(s, b)
  for y in range(max(s[1] - dist, 0), min(s[1] + dist + 1, 4000001)):
    if y not in x_not_beacon:
      x_not_beacon[y] = []
    y_dist = abs(y - s[1])
    x_range = dist - y_dist
    if x_range < 0:
      raise Exception('Something went wrong')
    l, r = s[0] - x_range, s[0] + x_range
    x_not_beacon[y].append((l, r))
  print(line)

def normalize(li):
  li = sorted(li, key = lambda x: x[0])
  li2 = []
  while len(li) > 0:
    l, r = li.pop(0)
    temp = []
    for each in li:
      if each[0] <= r:
        r = max(r, each[1])
      else:
        temp.append(each)
    li = temp
    li2.append((l, r))
  return li2

def clamp(li):
  return [(min(max(l, 0), 4000000), min(max(r, 0), 4000000)) for l, r in li]

for y in range(0, 4000001):
  x_not_beacon[y] = clamp(normalize(x_not_beacon[y]))
  count = 0
  for l, r in x_not_beacon[y]:
    count += r - l + 1
  if count < 4000001:
    x = x_not_beacon[y][0][1] + 1
    print(x * 4000000 + y)
    break
