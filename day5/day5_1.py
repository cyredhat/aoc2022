with open('day5/input.txt', 'r') as f:
    global lines
    lines = [line for line in f.read().split('\n')]

for i, line in enumerate(lines):
    global crates, operations
    if line == '':
        crates = lines[:i-1]
        operations = lines[i+1:]
        break

stacks = {}
for line in crates:
    for i, c in enumerate(line):
        if i%4 != 1 or c == ' ':
            continue
        stack_id = (i // 4) + 1
        if stack_id not in stacks:
            stacks[stack_id] = []
        stacks[stack_id].append(c)

def move_stack(amount, fromm, to):
    global stacks
    if len(stacks[fromm]) < amount:
        raise Exception('Not enough crates in stack')
    stacks[to] = stacks[fromm][:amount][::-1] + stacks[to]
    stacks[fromm] = stacks[fromm][amount:]
    return
print(stacks)
for operation in operations:
    amount, fromm, to = [int(x) for x in operation.replace('move ', '').replace('from', ',').replace('to', ',').split(',')]
    print(amount, fromm, to)
    move_stack(amount, fromm, to)
    print(stacks)

final_ans = ''
for i in range(1, len(stacks)+1):
    final_ans += stacks[i][0]

print(final_ans)

