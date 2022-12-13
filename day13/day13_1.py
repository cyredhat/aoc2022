data = open('day13/input.txt').read()

def evaluate(f, s):
  if f == [] and s == []:
    return 2
  if f == []:
    return True
  if s == []:
    return False
  ff, sf = f[0], s[0]
  if type(ff) == int and type(sf) == int:
    if ff == sf:
      return evaluate(f[1:], s[1:])
    else:
      return ff < sf
  if type(ff) == int:
    ff = [ff]
  if type(sf) == int:
    sf = [sf]
  ev = evaluate(ff, sf)
  if ev == 2:
    return evaluate(f[1:], s[1:])
  else:
    return ev


count = 0
for i, pair in enumerate(data.split('\n\n')):
  index = i  + 1
  first, second = pair.split('\n')
  f, s = eval(first), eval(second)
  if evaluate(f, s):
    count += index
  
print(count)