lines = open("data.txt").read().splitlines()


def check_if_low_point(heightmap, x, y):
    low_point = True
    value = heightmap[x][y]
    
    if x + 1 < len(lines):
        if value >= heightmap[x+1][y]:
            low_point = False

    if y + 1 < len(lines[0]):
        if value >= heightmap[x][y+1]:
            low_point = False
    if x + 1 > 1: 
        if value >= heightmap[x-1][y]:
                low_point = False
    if y + 1 > 1:
        if value >= heightmap[x][y-1]:
                low_point = False



    return low_point

heightmap = []

for l in lines:
    heightmap.append([int(i) for i in l])

result = 0



for x in range(0, len(lines)):
    for y in range(0,len(lines[0])):
        if check_if_low_point(heightmap,x,y):
            print(heightmap[x][y])
            result += heightmap[x][y]
            result += 1
            print((x,y))
            
print(heightmap)
print(result)
