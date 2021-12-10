lines = open("data.txt").read().splitlines()


def retrieve_bastion_pos(heightmap, x, y):
    bastion = []
    bastion.append((x,y))
    cl = []
    cl.append((x,y))
    # get up, down, left, right vals

    while cl:
        for z in cl:
            hp = get_higher_points(heightmap, z[0], z[1])
            for p in hp:
                coords = (p[0],p[1])
                if coords not in cl:
                    cl.append((p[0],p[1]))
                if coords not in bastion:
                    bastion.append(p)

            cl.remove((z[0],z[1]))

    print(f"Bastion for: {(x,y)}")
    print(bastion)
    print("")
    return len(bastion)


def get_higher_points(heightmap, x, y):
    pts = []
    value = heightmap[x][y]
    
    if x + 1 < len(lines):
        if value < heightmap[x+1][y] and heightmap[x+1][y] != 9 :
            pts.append((x+1, y))

    if y + 1 < len(lines[0]):
        if value < heightmap[x][y+1] and heightmap[x][y +1] != 9:
            pts.append((x, y + 1))
    if x + 1 > 1: 
        if value < heightmap[x-1][y] and heightmap[x-1][y] != 9:
                pts.append((x - 1, y))
    if y + 1 > 1:
        if value < heightmap[x][y-1] and heightmap[x][y-1] != 9:
                pts.append((x, y - 1))

    return pts

def check_if_low_point(heightmap, x, y):
    low_point = True
    value = heightmap[x][y]
    
    if x + 1 < len(lines):
        if value > heightmap[x+1][y]:
            low_point = False

    if y + 1 < len(lines[0]):
        if value > heightmap[x][y+1]:
            low_point = False
    if x + 1 > 1: 
        if value > heightmap[x-1][y]:
                low_point = False
    if y + 1 > 1:
        if value > heightmap[x][y-1]:
                low_point = False



    return low_point

heightmap = []

for l in lines:
    heightmap.append([int(i) for i in l])

low_points = []

for x in range(0, len(lines)):
    for y in range(0,len(lines[0])):
        if check_if_low_point(heightmap,x,y):
            low_points.append((x,y))

            
    bastion_list = []
    
for x in low_points:

    bastion_list.append(retrieve_bastion_pos(heightmap, x[0],x[1]))

bastion_list = sorted(bastion_list)

result = 1
for x in bastion_list[-3:]:
    result = result * x

print(result)