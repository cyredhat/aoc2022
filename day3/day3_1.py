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
for line in lines:
    found = set()
    for i, char in enumerate(line):
        if i < len(line) // 2:
            found.add(char)
        else:
            if char in found:
                total_priority += char_priority(char)
                break

print(total_priority)
    
