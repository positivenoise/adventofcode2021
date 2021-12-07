def stimulate(counts):
    ones = counts[0]
    counts[0] = counts[1]
    counts[1] = counts[2]
    counts[2] = counts[3]
    counts[3] = counts[4]
    counts[4] = counts[5]
    counts[5] = counts[6]
    counts[6] = counts[7] + ones
    counts[7] = counts[8] 
    counts[8] = ones
    print(counts)

lines = open("data.txt").read().splitlines()

fish = lines[0].split(",")

fish = [int(x) for x in fish]

counts = dict({0:0, 6:0, 7:0, 8:0})

for i in fish:
  counts[i] = counts.get(i, 0) + 1

for x in range(0,256):
    fish = stimulate(counts)

results = 0
for i in counts:
    results += counts[i]

print(results)