import re

lines = open("data.txt").read().splitlines()

output = []
for x in lines:
    output.append(x.split("|"))

final = 0

for z in output:
    x = z[0].split(" ")

    x = [''.join(sorted(i)) for i in x if i != '']

    results = {}

    for r in x:
        if len(r) == 2:
            results[1] = r
        if len(r) == 4:
            results[4] = r
        if len(r) == 3:
            results[7] = r
        if len(r) == 7:
            results[8] = r

    # find top char
    for b in results[7]:
        if b not in results[1]:
            top = b

    # join the 4 with top char to find 9
    t = ''.join(sorted(f"{results[4]}{top}"))

    # find which char is missing for 9
    for b in x:
        r_chars = re.sub(f'[{t}]', '', b)
        if len(r_chars) == 1:
            bottom = r_chars

    # 4 + top + bottom = 9
    results[9] = ''.join(sorted(f"{results[4]}{top}{bottom}"))

    #bottom left = 9 - 8
    for b in results[8]:
        if b not in results[9]:
            bottom_left = b

    # 1 + bottom + top, only missing is middle in 3
    temp = ''.join(sorted(f"{results[1]}{top}{bottom}"))
    for b in x:
        r_chars = re.sub(f'[{temp}]', '', b)
        if len(r_chars) == 1:
            middle = r_chars

    # 1 + bottom + top + middle = 3
    results[3] = ''.join(sorted(f"{results[1]}{top}{bottom}{middle}"))

    # 8 - middle = 0
    results[0] = re.sub(f'[{middle}]', '', results[8])

    #6 is only 6 digit not found
    for b in x:
        if len(b) == 6:

            if b == results[0]:
                pass
            elif b == results[9]:
                pass
            else:
                results[6] = b

    # 6 - bottom left = 5
    results[5] = re.sub(f'[{bottom_left}]', '', results[6])

    # only remaining is 2
    for b in x:
        if len(b) == 5:
            if b == results[5]:
                pass
            elif b == results[3]:
                pass
            else:
                results[2] = b

    print(results)

    x = z[1].split(" ")

    x = [''.join(sorted(i)) for i in x if i != '']

    print(x)

    s = []
    for p in x:
        for r in results:
            if results[r] == p:
                s.append(r)
    s = [str(x) for x in s]
    s = ''.join(s)
    final += int(s)

print(final)
