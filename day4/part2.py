def calculate_result(board, i):
    result = 0
    for line in board:
        for num in line:
            result += int(num)
    result = result * int(i)

    return result

def process_into_array(data):
    boards = []
    board = []

    for lines in data:
        c = lines.split(' ')
        if c != ['']:
            t = [i for i in c if i != '']
            board.append(t)
        else:
            boards.append(board)
            board = []
    boards.append(board)
    return boards


def rotate_board(boards):
    rotated_boards = []
    for b in boards:
        new_board = [[],[],[],[],[]]
        for l in b:
            for x in range(0, len(l)):
                new_board[x].append(l[x])
        rotated_boards.append(new_board)
    return rotated_boards

def remove_from_board(boards, num):
    for board in boards:
            for line in boards[board]:
                if number in line:
                    line.remove(num)
    return boards

def check_bingo(boards):
    for board in boards:
        for line in boards[board]:
            if len(line) == 0:
                return board
    return False

def check_bingo_board(board):
    for line in board:
        if len(line) == 0:
            return True
    return False

def add_index(boards):
    result = {}
    i = 1
    for b in boards:
        result[i] = b
        i+= 1
    return result


lines = open("data.txt").read().splitlines()

input = lines[0].split(',')
boards = process_into_array(lines[2:])

rotated_boards = rotate_board(boards)



boards = add_index(boards)
rotated_boards = add_index(rotated_boards)

for number in input:
    remove_from_board(boards, number)
    remove_from_board(rotated_boards, number)
    result1 = check_bingo(boards)
    result2 = check_bingo(rotated_boards)

    if result1 and len(boards) == 1:
        print("bingo")
        print(calculate_result(boards[result1], number))
        break

    elif result2 and len(rotated_boards) == 1:
        print("bingo")
        print(calculate_result(rotated_boards[result2], number))
        break



    new_boards = {}
    new_rotated_boards = {}
    for b in boards:
        if not check_bingo_board(boards[b]):
            new_boards[b] = boards[b]
            new_rotated_boards[b] = rotated_boards[b]
    boards = new_boards
    rotated_boards = new_rotated_boards


    new_boards = {}
    for b in rotated_boards:
        if not check_bingo_board(rotated_boards[b]):
            new_boards[b] = boards[b]
            new_rotated_boards[b] = rotated_boards[b]
    boards = new_boards
    rotated_boards = new_rotated_boards




