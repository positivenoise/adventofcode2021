import numpy as np
import pyastar2d

lines = open("data.txt").read().splitlines()

for x in range(0,len(lines)):
    lines[x] = [c for c in lines[x]]

weights = np.array(lines, dtype=np.float32)

path = pyastar2d.astar_path(weights, (0, 0), (len(lines[x]) - 1, len(lines) - 1), allow_diagonal=False)

results = 0

for x in path[1:]:
    results += weights[x[0]][x[1]]

print(int(results))