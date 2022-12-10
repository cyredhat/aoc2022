datastream = open("day6/input.txt", "r").read()

def is_unique(l):
    return len(l) == len(set(l))

for i in range(14, len(datastream)):
    if is_unique(datastream[i-14:i]):
        print(i)
        break