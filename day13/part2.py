lines = open("data.txt").read().splitlines()

folds = []
dots = []

for l in lines:
    if l.startswith("fold along"):
        folds.append(l)
    elif l != '':
        dots.append(l)


dots = [d.split(',') for d in dots]

for i in range(0, len(dots)):
    dots[i] = [int(dots[i][0]),int(dots[i][1])]

grid =[]


biggest_x = 0
for i in dots:
    if i[0] > biggest_x:
        biggest_x = i[0]

biggest_y = 0
for i in dots:
    if i[1] > biggest_y:
        biggest_y = i[1]


for y in range(0, biggest_y+1):
    line = []
    for x in range(0, biggest_x+1):
        t = "."
        for d in dots:
            if d == [x,y]:
                t = '#'
                dots.remove(d)
                break
                
        line.append(t)
    grid.append(line)



def fold_hoz(grid, y):
    new_grid = grid[y:]
    new_grid = new_grid[::-1]
    newest_grid = []
    for py in range(0, y):
        line = []
        for x in range(0, len(new_grid[0])):
            if new_grid[py][x] == "#":
                line.append("#")
            else:
                line.append(grid[py][x])
        newest_grid.append(line)
    return newest_grid

def fold_vert(grid, x):
    new_grid = []
    for l in grid:
        r_line = l[x + 1:]
        r_line = r_line[::-1]
        l_line = l[:x]
        new_line = []
        for i in range(0, x):
            
            if r_line[i] == '#' or l_line[i] == '#':
                new_line.append('#')
            else:
                new_line.append('.')
        new_grid.append(new_line)
    return new_grid


for f in folds:
    f = f.split(' ')
    instruction = f[-1].split("=")
    if instruction[0] == 'x':
        grid = fold_vert(grid, int(instruction[1]))

    elif instruction[0] == 'y':
        grid = fold_hoz(grid, int(instruction[1]))

for l in grid:
    print(''.join(l))

