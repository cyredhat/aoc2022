def char_priority(char):
    if ord('a') <= ord(char) <= ord('z'):
        return ord(char) - ord('a') + 1
    if ord('A') <= ord(char) <= ord('Z'):
        return ord(char) - ord('A') + 27
    raise Exception('Invalid char: ' + char)

with open('day3/input.txt', 'r') as f:
    global lines
    lines = f.read().split('\n')

total_priority = 0
group_char_list = [set()] * 3
for l, line in enumerate(lines):
    group_order = l % 3
    group_char_list[group_order] = set()
    for i, char in enumerate(line):
        group_char_list[group_order].add(char)
    if (group_order == 2):
        intersection = group_char_list[0] & group_char_list[1] & group_char_list[2]
        for char_i, char in enumerate(intersection):
            if (char_i > 0):
                raise Exception('More than one char in intersection')
            total_priority += char_priority(char)

print(total_priority)
    
