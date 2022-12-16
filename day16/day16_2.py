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
time_limit = 26
def dfs(time, acc, v, valves):
  global memo, max_acc, time_limit
  if acc > max_acc:
    max_acc = acc
    print(max_acc)
  if len(valves) == 0:
    return
  if (v, tuple(valves)) in memo:
    mt, macc = memo[(v, tuple(valves))]
    if time[0] >= mt[0] and time[1] >= mt[1] and acc <= macc:
      return
  memo[(v, tuple(valves))] = time, acc
  h, e = v
  time_h, time_e = time
  for n in valves:
    if (time_limit - mat[(h, n)] - time_h) * edges[n][0] > 0:
      dfs((time_h + mat[(h, n)] + 1, time_e), acc + (time_limit - mat[(h, n)] - time_h) * edges[n][0], (n, e), valves - {n})
    if (time_limit - mat[(e, n)] - time_e) * edges[n][0] > 0:
      dfs((time_h, time_e + mat[(e, n)] + 1), acc + (time_limit - mat[(e, n)] - time_e) * edges[n][0], (h, n), valves - {n})

dfs((1, 1), 0, ('AA', 'AA'), valves)
print(max_acc)
  