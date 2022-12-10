
with open('./day1/input1.txt', 'r') as f:
    global cals
    cals = [int(x) if x != '' else None for x in f.read().split('\n')]
    cals.append(None)

sum_cals = []

cum = 0
for each in cals:
    if each is None:
        sum_cals.append(cum)
        cum = 0
    else:
        cum += each

print(sum(sorted(sum_cals)[-3:]))
print(sorted(sum_cals))


# print(items)