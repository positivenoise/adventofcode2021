lines = open("data.txt").read().splitlines()

crabs = lines[0].split(",")

crabs = [int(x) for x in crabs]

print(crabs)

fuel_list = []


for c in range(min(crabs), max(crabs)):
    fuel = 0
    for b in crabs:
        fuel += abs(c - b)
    fuel_list.append(fuel)

print(min(fuel_list))



