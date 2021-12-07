def stimulate(fish):
    new_fish = []
    for x in fish:
        if x == 0:
            new_fish.append(6)
            new_fish.append(8)
        else:
            new_fish.append(x - 1)
    return new_fish

lines = open("data.txt").read().splitlines()

fish = lines[0].split(",")

fish = [int(x) for x in fish]

print(fish)

for x in range(0,80):

    fish = stimulate(fish)
    print(fish)

print(len(fish))
