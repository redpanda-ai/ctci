
def get_clear_board():
    return [[0 for i in range(BOARD_SIZE)] for j in range(BOARD_SIZE)]


def print_board(board):
    for i in range(BOARD_SIZE):
        print(board[i])


def safe(board, i, j):
    v = sum([board[x][j] for x in range(BOARD_SIZE) if x != i])
    if v != 0:
        return False
    h = sum([board[i][y] for y in range(BOARD_SIZE) if y != j])
    if h != 0:
        return False

    d = []
    for a in range(1, BOARD_SIZE):
        if (i + a) < BOARD_SIZE and (j + a) < BOARD_SIZE:
            d.append(board[i + a][j + a])
        if (i - a) >= 0 and (j - a) >= 0:
            d.append(board[i - a][j - a])
        if (i + a) < BOARD_SIZE and (j - a) >= 0:
            d.append(board[i + a][j - a])
        if (i - a) >= 0 and (j + a) < BOARD_SIZE:
            d.append(board[i - a][j + a])


    d2 = []
    signs = [(1, 1), (-1, -1), (1, -1), (-1, 1)]
    for sign in signs:
        w = [board[i + sign[0] * b][j + sign[1] * b]
             for b in range(1, BOARD_SIZE)
             if 0 <= i + sign[0] * b < BOARD_SIZE and 0 <= j + sign[1] * b < BOARD_SIZE]
        d2.extend(w)

    d = sum(d2)
    if d != 0:
        return False

    return True


def solve(board=None, queen_num=1, start_a=0):
    if not board:
        board = get_clear_board()

    if queen_num == NUM_QUEENS + 1:
        print("Finished")
        print_board(board)
        return True
    for a in range(start_a, BOARD_SIZE ** 2):
        i = a // BOARD_SIZE
        j = a % BOARD_SIZE

        if safe(board, i, j):
            board[i][j] = queen_num
            solved = solve(board=board, queen_num=(queen_num + 1), start_a=(a + 1))
            if not solved:
                board[i][j] = 0
            else:
                return solved

    return False


NUM_QUEENS = 8
BOARD_SIZE = 8
solve()