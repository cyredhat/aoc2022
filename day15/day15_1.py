data = open('day15/input.txt').read()

def manhattan_distance(a, b):
  return abs(a[0] - b[0]) + abs(a[1] - b[1])

sensors = []
ss = set()
max_dist = 0

y = 2000000
sb = set()
x_not_beacon = []
for line in data.split('\n'):
  sensor, beacon = line.split(':')
  s = int(sensor.split(',')[0].split('=')[1]), int(sensor.split(',')[1].split('=')[1])
  b = int(beacon.split(',')[0].split('=')[1]), int(beacon.split(',')[1].split('=')[1])
  if s[1] == y:
    sb.add(s[0])
  if b[1] == y:
    sb.add(b[0])
  dist = manhattan_distance(s, b)
  y_dist = abs(y - s[1])
  x_range = dist - y_dist
  if x_range < 0:
    continue
  l, r = s[0] - x_range, s[0] + x_range
  x_not_beacon.append((l, r))

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

x_not_beacon = normalize(x_not_beacon)
count = 0
for l, r in x_not_beacon:
  count += r - l + 1
count -= len(sb)
print(count)
