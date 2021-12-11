lines = open("data.txt").read().splitlines()

def print_grid(grid):
    for line in grid:
        print(line)
        #print(''.join(str(x) for x in line))
    print("")


def inc_by_one(grid):
    for y in range(len(grid)):
        for x in range(len(grid[0])):
            grid[x][y] += 1
    

def inc_point_by_one(grid, x, y):
    if x > -1 and x < len(grid[0]) and y > -1 and y < len(grid):
        grid[x][y] += 1
    
def check_flash(grid, already_flashed):
    flashed = []
    for y in range(len(grid)):
        for x in range(len(grid[0])):
            if grid[x][y] > 9 and (x,y) not in already_flashed:
                inc_point_by_one(grid,x + 1,y)
                inc_point_by_one(grid,x - 1,y)
                inc_point_by_one(grid,x,y + 1)
                inc_point_by_one(grid,x,y - 1)
                inc_point_by_one(grid,x+1,y+1)
                inc_point_by_one(grid,x-1,y-1)
                inc_point_by_one(grid,x+1,y-1)
                inc_point_by_one(grid,x-1,y+1)
                flashed.append((x,y))
                already_flashed.append((x,y))
    return flashed, already_flashed
    
def set_to_zero(flash, grid):
    for x in flash:
        grid[x[0]][x[1]] = 0


def stimulate(grid):
    inc_by_one(grid)
    flash = ['a']
    flashed = []
    while(flash != []):
        flash, flashed = check_flash(grid, flashed)
        set_to_zero(flashed, grid)
    return grid, len(flashed)

grid = []
for line in lines:
    grid.append([int(i) for i in line])

inc = 0

for x in range(0,10000):
    grid,flashed = stimulate(grid)
    inc += 1
    if flashed == len(grid) * len(grid[0]):
        break


print(inc)