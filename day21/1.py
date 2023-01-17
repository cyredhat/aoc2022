# inp = open('day21/tc.txt').read().split('\n')
inp = open('day21/input.txt').read().split('\n')

in_degrees = {}
values = {}
rdeps = {}
for line in inp:
  name, job = line.split(': ')
  in_degrees[name] = 0
  try :
    job = int(job)
    values[name] = job
  except:
    dep1, dep2 = job.replace('+', '').replace('-', '').replace('*', '').replace('/', '').replace('  ', ' ').split(' ')
    rdeps[name] = (dep1, dep2)
    values[name] = job

def evaluate(name):
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

evaluate('root')
print(globals()['root'])
