lines = open("data.txt").read().splitlines()

def calculate_result(board, i):
    result = 0
    for line in board:
        for num in line:
            result += int(num)
    result = result * int(i)
    return result



boards = []
board = []
for b in lines[2:]:
    c = b.split(' ')
    if c != ['']:
        t = [i for i in c if i != '']
        board.append(t)
    else:
        boards.append(board)
        board = []
boards.append(board)



rotated_boards = []


for b in boards:
    new_board = [[],[],[],[],[]]
    for l in b:
        for x in range(0, len(l)):
            new_board[x].append(l[x])
    rotated_boards.append(new_board)





for i in lines[0].split(','):
    for b in boards:
        for l in b:
            if i in l:
                l.remove(i)
                if len(l) == 0:
                    index_n = boards.index(b)
                    del boards[index_n]
                    del rotated_boards[index_n]
                    if len(boards) == 1 or len(rotated_boards) == 1:
                        print(calculate_result(boards[0], i))
                        exit()

    for b in rotated_boards:
        for l in b:
            if i in l:
                l.remove(i)
                if len(l) == 0:
                    index_n = rotated_boards.index(b)
                    del boards[index_n]
                    del rotated_boards[index_n]
                    if len(boards) == 1 or len(rotated_boards) == 1:
                        print(calculate_result(rotated_boards[0], i))
                        exit()       





