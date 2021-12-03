lines = open("data.txt").read().splitlines()

gamma_rate = ""
epsilon_rate = ""

for x in range(0, len(lines[0])):
    first_bit = [y[x] for y in lines]
    n_in_fb = first_bit.count('1')
    o_in_fb = first_bit.count('0')

    if n_in_fb > o_in_fb:
        gamma_rate = gamma_rate + "1"
        epsilon_rate = epsilon_rate + "0"
    else:
        gamma_rate = gamma_rate + "0"
        epsilon_rate = epsilon_rate + "1"



print(gamma_rate)
print(epsilon_rate)

print(int(epsilon_rate, 2) * int(gamma_rate, 2))