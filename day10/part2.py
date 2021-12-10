lines = open("data.txt").read().splitlines()

results = []

for l in lines:
    open_tup = tuple('({[<')
    close_tup = tuple(')}]>')
    map = dict(zip(open_tup, close_tup))
    queue = []
  
    for i in l:
        if i in open_tup:
            queue.append(map[i])
        elif i in close_tup:
            if not queue or i != queue.pop():
                queue = []
                break

    if queue:
        r = 0
        queue.reverse()
        for z in queue:
            r = 5 * r
            if z == ")": r += 1
            if z == "]": r += 2
            if z == "}": r += 3
            if z == ">": r += 4
        results.append(r)


results = sorted(results)
middle = int((len(results) - 1 )/ 2)

print(results[middle])