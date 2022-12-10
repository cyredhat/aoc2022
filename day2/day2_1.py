symbol_score = {
    'X': 1,
    'Y': 2,
    'Z': 3,
    'A': 1,
    'B': 2,
    'C': 3,
}

def get_score(symbol):
    return symbol_score[symbol]

with open('day2/tc1.txt', 'r') as f:
    matches = [x.split(' ') for x in f.read().split('\n')]

my_score = 0
for match in matches:
    score_diff = get_score(match[0]) - get_score(match[1])
    my_score += get_score(match[1])
    if (abs(score_diff) > 1):
        score_diff = int(-score_diff / abs(score_diff))
    # print(match[0], match[1], score_diff)
    if (score_diff == 0):
        my_score += 3
    if (score_diff == -1):
        my_score += 6
    print(my_score)

print(my_score)
