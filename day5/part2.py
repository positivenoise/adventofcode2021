lines = open("data.txt").read().splitlines()

def line_alg(x0, y0, x1, y1):
        "Bresenham's line algorithm"
        points_in_line = []
        dx = abs(x1 - x0)
        dy = abs(y1 - y0)
        x, y = x0, y0
        sx = -1 if x0 > x1 else 1
        sy = -1 if y0 > y1 else 1
        if dx > dy:
            err = dx / 2.0
            while x != x1:
                points_in_line.append((x, y))
                err -= dy
                if err < 0:
                    y += sy
                    err += dx
                x += sx
        else:
            err = dy / 2.0
            while y != y1:
                points_in_line.append((x, y))
                err -= dx
                if err < 0:
                    x += sx
                    err += dy
                y += sy
        points_in_line.append((x, y))
        return points_in_line


results = []

for x in lines:
    line = x.split(' -> ')
    coord1 = line[0].split(',')
    coord2 = line[1].split(',')

    #is veritcal or horizontal?
    if coord1[0] in coord2 or coord1[1] in coord2:
        results.append([coord1, coord2])

    elif int(coord1[0]) - int(coord2[0]) == int(coord1[1]) - int(coord2[1]):
        results.append([coord1, coord2])

results2 = []

for r in results:
    points = line_alg(int(r[0][0]), int(r[1][0]), int(r[0][1]), int(r[1][1]))
    for p in points:
        results2.append(p)

counts = dict()
for i in results2:
  counts[i] = counts.get(i, 0) + 1

num = 0

for k in counts:
    if int(counts[k]) > 1:
        num += 1

print(num)


