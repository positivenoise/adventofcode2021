lines = open("data.txt").read().splitlines()


for x in range(0, len(lines[0])):
    first_bit = [y[x] for y in lines]
    n_in_fb = first_bit.count('1')
    o_in_fb = first_bit.count('0')

    if n_in_fb > o_in_fb:

        lines = [b for b in lines if b[x] == '1']
    elif n_in_fb == o_in_fb:
        lines = [b for b in lines if b[x] == '1']
    else:
        lines = [b for b in lines if b[x] == '0']

    if len(lines) == 1:
        break


r1 = lines[0]
print(r1)
lines = open("data.txt").read().splitlines()

for x in range(0, len(lines[0])):
    first_bit = [y[x] for y in lines]
    n_in_fb = first_bit.count('1')
    o_in_fb = first_bit.count('0')

    if n_in_fb < o_in_fb:

        lines = [b for b in lines if b[x] == '1']
    elif n_in_fb == o_in_fb:
        lines = [b for b in lines if b[x] == '0']
    else:
        lines = [b for b in lines if b[x] == '0']

    if len(lines) == 1:
        break


r2 = lines[0]
print(r2)
print(int(r1,2) * int(r2,2))
