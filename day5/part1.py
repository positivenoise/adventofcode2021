lines = open("data.txt").read().splitlines()

def process_lines(lines):

    results = []

    for x in lines:
        line = x.split(' -> ')
        coord1 = line[0].split(',')
        coord2 = line[1].split(',')

        #is veritcal or horizontal?
        if coord1[0] == coord2[0] or coord1[1] == coord2[1]:
            results.append([coord1, coord2])

    return results

def get_count_of_points(points):
    counts = dict()
    for i in points:
        counts[i] = counts.get(i, 0) + 1
    
    return counts

def get_intersects(lines):

    num = 0

    for k in lines:
        if int(lines[k]) > 1:
            num += 1

    return num

def get_line(x0, x1, y0, y1):
    line = []

        
    if x0 == y0:
        for y in range(y1, x1 + 1):
            line.append((x0, y))
        for y in range(x1, y1 + 1):
            line.append((x0, y))
    elif x1 == y1:
        for x in range(y0, x0 + 1):
            line.append((x, x1))
        for x in range(x0, y0 + 1):
            line.append((x, x1))

    return line


    



results = process_lines(lines)
    
results2 = []

for r in results:
    points = get_line(int(r[0][0]), int(r[0][1]), int(r[1][0]), int(r[1][1]))
    for p in points:
        results2.append(p)

counts = get_count_of_points(results2)

print(get_intersects(counts))

