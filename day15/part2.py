import numpy as np
import pyastar2d

lines = open("data.txt").read().splitlines()



def make_new_line(line):
    new_line = [c + 1 for c in line]
    for l in range(0,len(new_line)):
        if new_line[l] > 9:
            new_line[l] = 1

    return new_line

def make_new_section(lines):
    new_lines = []
    for x in range(0, len(lines)):
        line  = [c + 1 for c in lines[x]]
        for l in range(0,len(line)):
            if line[l] > 9:
                line[l] = 1
        new_lines.append(line)
    return new_lines
   
for x in range(0,len(lines)):
    lines[x] = [int(c) for c in lines[x]]
    new_line = make_new_line(lines[x])
    lines[x] += new_line
    for _ in range(0,3):
        new_line = make_new_line(new_line)
        lines[x] += new_line



new_lines = make_new_section(lines)
lines += new_lines

for _ in range(0, 3):
    new_lines = make_new_section(new_lines)
    lines += new_lines



weights = np.array(lines, dtype=np.float32)

path = pyastar2d.astar_path(weights, (0, 0), (len(lines) - 1, len(lines[x]) - 1), allow_diagonal=False)

results = 0

for x in path[1:]:
    results += weights[x[0]][x[1]]

print(int(results))

