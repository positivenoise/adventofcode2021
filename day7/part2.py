lines = open("data.txt").read().splitlines()

crabs = lines[0].split(",")

crabs = [int(x) for x in crabs]

print(crabs)

fuel_list = []

for c in range(min(crabs), max(crabs)):
    fuel = 0
    for b in crabs:
        for x in range(1, abs(c - b) + 1):
            fuel += x
    fuel_list.append(fuel)

print(min(fuel_list))



