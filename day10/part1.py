lines = open("data.txt").read().splitlines()

results = 0

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
                if i == ")": results += 3
                if i == "]": results += 57
                if i == "}": results += 1197
                if i == ">": results += 25137
                break

print(results)

