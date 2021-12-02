lines = open("data.txt").read().splitlines()

h  = 0
v = 0
aim = 0

for line in lines:
    a = line.split(" ")
    if a[0] == "forward":
        v+= int(a[1])
        h += aim * int(a[1])
    elif a[0] == "down":
        aim += int(a[1])
    elif a[0] == "up":
        aim -= int(a[1])

print(h * v)
