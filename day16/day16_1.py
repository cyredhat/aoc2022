# data = open('day16/tc.txt').read()
data = open('day16/input.txt').read()

edges = {}
mat = {}
valves = set()

for line in data.split('\n'):
  line = line.replace('Valve ', '').replace(' has flow rate', '').replace(' tunnels lead to valves ', '').replace(' tunnel leads to valve ', '')
  valve, li = line.split(';')
  v, flow = valve.split('=')
  flow = int(flow)
  if flow > 0:
    valves.add(v)
  li = [s.strip() for s in li.split(',')]
  edges[v] = (flow, li)

for i, (_, li) in edges.items():
  for j in edges:
    mat[(i, j)] = float('inf')
  for j in li:
    mat[(i, j)] = 1

for k in edges:
  for i in edges:
    for j in edges:
      mat[(i, j)] = min(mat[(i, j)], mat[(i, k)] + mat[(k, j)])

memo = {}
max_acc = 0
time_limit = 30
def dfs(time, acc, v, valves):
  global memo, max_acc, time_limit
  max_acc = max(max_acc, acc)
  if len(valves) == 0:
    return
  if (v, tuple(valves)) in memo:
    mt, macc = memo[(v, tuple(valves))]
    if time >= mt and acc <= macc:
      return
  memo[(v, tuple(valves))] = time, acc
  for n in valves:
    if (time_limit - mat[(v, n)] - time) * edges[n][0] > 0:
      dfs(time + mat[(v, n)] + 1, acc + (time_limit - mat[(v, n)] - time) * edges[n][0], n, valves - {n})
dfs(1, 0, 'AA', valves)
print(max_acc)
  