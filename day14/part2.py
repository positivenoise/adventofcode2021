from collections import Counter

lines = open("data.txt").read().splitlines()

template = lines[0]
rules = lines[2:]

n_rules = []
for r in rules:
    n_rules.append(r.split(" -> "))

pair_map={}
for x in n_rules:
    pair_map[x[0]] = 0

added_chars = {}
for x in n_rules:
    added_chars[x[1]] = 0

for x in range(1, len(template)):
    pair_map[f"{template[x-1]}{template[x]}"] += 1

def process(pair_map):
    new_pair_map = {}
    for x in n_rules:
        new_pair_map[x[0]] = 0
    for x in pair_map:
        for y in n_rules:
            if x == y[0] and pair_map[x] > 0:
                new_pair_map[f"{x[0]}{y[1]}"] += pair_map[x]
                new_pair_map[f"{y[1]}{x[1]}"] += pair_map[x]
                new_pair_map[x] -= pair_map[x]
                added_chars[y[1]] += pair_map[x]
    
    return new_pair_map



for i in range(0,40):
    new_pair_map = process(pair_map)

    for x in new_pair_map:
        pair_map[x] += new_pair_map[x]

    #print(pair_map)

for x in template:
    added_chars[x] += 1


highest  = 0
lowest = 100000000000000
for x in added_chars:
    if added_chars[x] > highest:
        highest = added_chars[x]
    elif added_chars[x] < lowest:
        lowest = added_chars[x]

print(highest - lowest)
