# inp = open('day21/tc.txt').read().split('\n')
inp = open('day21/input.txt').read().split('\n')

values = {}
rdeps = {}
for line in inp:
  name, job = line.split(': ')
  try :
    job = int(job)
    values[name] = job
  except:
    dep1, dep2 = job.replace('+', '').replace('-', '').replace('*', '').replace('/', '').replace('  ', ' ').split(' ')
    if name == 'root':
      l = dep1
      r = dep2
      continue
    rdeps[name] = (dep1, dep2)
    values[name] = job

def evaluate(name):
  if name == 'humn':
    raise Exception('humn')
  if name in globals():
    return globals()[name]
  if name not in rdeps:
    globals()[name] = values[name]
    return
  dep1, dep2 = rdeps[name]
  if dep1 not in globals():
    evaluate(dep1)
  if dep2 not in globals():
    evaluate(dep2)
  globals()[name] = int(eval(values[name]))

def solve(name, val):
  if name == 'humn':
    return val
  if name in globals():
    return globals()[name]
  if name not in rdeps:
    globals()[name] = values[name]
    return globals()[name]
  dep1, dep2 = rdeps[name]
  match values[name][5]:
    case '+':
      op1, op2 = f'val - {dep1}', f'val - {dep2}'
    case '-':
      op1, op2 = f'{dep1} - val', f'val + {dep2}'
    case '*':
      op1, op2 = f'val // {dep1}', f'val // {dep2}'
    case '/':
      op1, op2 = f'{dep1} // val', f'val * {dep2}'
  try:
    evaluate(dep1)
  except:
    dep1, dep2 = dep2, dep1
    op1, op2 = op2, op1
    evaluate(dep1)
  n_val = eval(op1)
  globals()[name] = val
  return solve(dep2, n_val)

try:
  evaluate(l)
except:
  l, r = r, l
  evaluate(l)
print(solve(r, globals()[l]))
