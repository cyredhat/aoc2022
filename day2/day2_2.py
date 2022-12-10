symbol_score = {
    'A': 1,
    'B': 2,
    'C': 3,
}

outcome_score = {
    'X': 0,
    'Y': 3,
    'Z': 6,
}

outcome_shift = {
    'X': 2,
    'Y': 0,
    'Z': 1,
}

def get_score(symbol):
    return symbol_score[symbol]

def get_outcome_score(outcome):
    return outcome_score[outcome]

with open('day2/input.txt', 'r') as f:
    matches = [x.split(' ') for x in f.read().split('\n')]

my_score = 0
for match in matches:
    my_score += get_outcome_score(match[1])
    print(match[0], match[1], ': ', end='')
    print(get_outcome_score(match[1]), ' ', end='')
    my_score += ((get_score(match[0]) + outcome_shift[match[1]] - 1) % 3) + 1
    print(((get_score(match[0]) + outcome_shift[match[1]] - 1) % 3) + 1)

print(my_score)
