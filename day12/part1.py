
lines = open("data.txt").read().splitlines()

lines = [l.split("-") for l in lines]


new_lines = []

for a in lines:
    if a[0] != "start" and a[1] != "end":
        new_lines.append([a[1],a[0]])

lines += new_lines

incomplete = [['start']]
complete = []

while len(incomplete) > 0:
    processing = incomplete[0]
    del incomplete[0]
    
    for current, target in lines:
        if current != processing[-1]: 
            continue
        if target.upper() != target and target in processing:
            continue
        newPath = [processing + [target]]

        if target == 'end': 
            complete += newPath
        else: 
            incomplete+= newPath

print(len(complete))