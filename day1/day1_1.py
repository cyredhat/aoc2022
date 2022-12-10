
with open('./day1/input1.txt', 'r') as f:
    global cals
    cals = [int(x) if x != '' else None for x in f.read().split('\n')]

max = float("-inf")

cum = 0
for each in cals:
    if each is None:
        if cum > max:
            max = cum
        cum = 0
    else:
        cum += each

print(max)

# print(items)