import numpy as np



def stimulate(fish):
    new_fish = np.array([])
    fish = fish - 1
    n_zeros = np.count_nonzero(fish==0)
    es = np.linspace(8,8,n_zeros)
    ss = np.linspace(6,6,n_zeros)
    new_fish = np.append(new_fish,es)
    new_fish = np.append(new_fish,ss)
    new_fish = np.append(new_fish,fish[fish != 0])

    return new_fish


lines = open("data.txt").read().splitlines()

fish = lines[0].split(",")

fish = [int(x) for x in fish]
fish_np = np.array(fish)



for x in range(0,256):
    print(f"day {x}")
    print(len(fish_np))
    fish_np = stimulate(fish_np)

print(len(fish_np))
