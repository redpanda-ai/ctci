import sys
board = [[0 for i in range(8)] for j in range(8)]

def print_board():
    for i in range(8):
        print(board[i])


def safe(i, j):
    global board
    #print("safety check")
    v = sum([board[x][j] for x in range(8) if x != i])
    if v != 0:
        return False
    h = sum([board[i][y] for y in range(8) if y != j])
    if h != 0:
        return False

    d1 = []
    for a in range(1, 8):
        if (i + a) < 8 and (j + a) < 8:
            d1.append(board[i+a][j+a])
            # d1.append(((i + a), (j + a)))
        if (i - a) >= 0 and (j - a) >= 0:
            d1.append(board[i-a][j-a])
            # d1.append(((i - a), (j - a)))
        if (i + a) < 8 and (j - a) >= 0:
            d1.append(board[i + a][j - a])
            # d1.append(((i + a), (j - a)))
        if (i - a) >= 0 and (j + a) < 8:
            d1.append(board[i-a][j+a])
            # d1.append(((i - a), (j + a)))

    d1 = sum(d1)

    if d1 != 0:
        return False

    return True


def mark(queen_num, i, j):
    global board
    for x in range(8):
        if board[x][j] == 0:
            board[x][j] = queen_num

    for y in range(8):
        if board[i][y] == 0:
            board[i][y] = queen_num

    d1 = []
    for a in range(1, 8):
        if (i + a) < 8 and (j + a) < 8:
            if safe(i+a, j+a):
                board[i+a][j+a] = queen_num
        if (i - a) >= 0 and (j - a) >= 0:
            if safe(i-a, j-a):
                board[i-a][j-a] = queen_num
        if (i + a) < 8 and (j - a) >= 0:
            if safe(i+a, j-a):
                board[i+a][j-a] = queen_num
        if (i - a) >= 0 and (j + a) < 8:
            if safe(i-a, j+a):
                board[i-a][j+a] = queen_num

def safe_new(i, j):
    if board[i][j] == 0:
        return True
    return False


def solve(queen_num):
    global board
    #print_board()
    #print(f"QN: {queen_num}")
    if queen_num == 9:
        print("Finished")
        print_board()
        sys.exit()
    for i in range(8):
        for j in range(8):
            print(f"q: {queen_num}, i: {i}, j: {j}")
            if board[i][j] == 0:
                if safe(i, j):
                    #print(f"Placing {queen_num} at {i}, {j}")
                    board[i][j] = queen_num
                    #mark(queen_num, i, j)
                    print_board()
                    solved = solve(queen_num + 1)
                    if not solved:
                        board[i][j] = 0
                #else:
                    # print(f"Cannot Place {queen_num} at {i}, {j}")

    return False


solve(1)