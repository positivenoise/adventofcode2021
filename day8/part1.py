lines = open("data.txt").read().splitlines()

output = []
for x in lines:
    output.append(x.split("|")[1].split(" ")[1::])

digits = 0

for line in output:
    for word in line:
        if len(word) == 2 or len(word) == 3 or len(word) == 4 or len(word) == 7:
            digits += 1


print(digits)