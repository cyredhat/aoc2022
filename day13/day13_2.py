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

def is_decoder(l):
  return type(l) is list and len(l) == 1 and type(l[0]) is list and len(l[0]) == 1 and (l[0][0] == 2 or l[0][0] == 6)

l = []

for pair in data.split('\n\n'):
  first, second = pair.split('\n')
  f, s = eval(first), eval(second)
  l.append(f)
  l.append(s)

l += [[[2]], [[6]]]

for i in range(len(l)-1):
  for j in range(i+1,len(l)):
    if not evaluate(l[i], l[j]):
      l[i], l[j] = l[j], l[i]

key = 1
for i, each in enumerate(l):
  index = i + 1
  if is_decoder(each):
    key *= index

print(key)

