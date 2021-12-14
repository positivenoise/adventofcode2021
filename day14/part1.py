from collections import Counter

lines = open("data.txt").read().splitlines()

template = lines[0]
rules = lines[2:]

n_rules = []
for r in rules:
    n_rules.append(r.split(" -> "))

def process(template):
    pairs = []
    for x in range(1, len(template)):
        pair = f"{template[x-1]}{template[x]}"
        for y in n_rules:
            if pair == y[0]:
                pair = f"{template[x-1]}{y[1]}{template[x]}"
                break

        pairs.append(pair)
    line = ""
    line += pairs[0]
    for p in pairs[1:]:
        line += p[1:]
    return line

for x in range(0, 10):
    template = process(template)

    
wc = Counter(template)

highest  = 0
lowest = 100000000000000
for x in wc:
    if wc[x] > highest:
        highest = wc[x]
    elif wc[x] < lowest:
        lowest = wc[x]

print(highest - lowest)
