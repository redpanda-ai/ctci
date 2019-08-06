
def get_clear_board():
    return [[0 for i in range(BOARD_SIZE)] for j in range(BOARD_SIZE)]


def print_board(board):
    for i in range(BOARD_SIZE):
        print(board[i])


def safe_on_diagonals(board, i, j):
    global safe_count
    safe_count += 1

    for a in range(1, BOARD_SIZE):
        if (i + a) < BOARD_SIZE and (j + a) < BOARD_SIZE:
            if board[i + a][j + a] != 0:
                return False
        if (i - a) >= 0 and (j - a) >= 0:
            if board[i - a][j - a] != 0:
                return False
        if (i + a) < BOARD_SIZE and (j - a) >= 0:
            if board[i + a][j - a] != 0:
                return False
        if (i - a) >= 0 and (j + a) < BOARD_SIZE:
            if board[i - a][j + a] != 0:
                return False

    return True


def solve(board=None, queen_num=1, start_cell=0, used_cols=None):

    # Success case
    if queen_num == NUM_QUEENS + 1:
        print_board(board)
        return True

    # create an empty chess board
    if not board:
        board = get_clear_board()

    # create a set to track used columns
    if not used_cols:
        used_cols = set()

    # don't inspect cells where the column has already been used
    cells = [i + start_cell for i in range(BOARD_SIZE) if i not in used_cols]

    for cell in cells:
        i = cell // BOARD_SIZE
        j = cell % BOARD_SIZE
        if safe_on_diagonals(board, i, j):
            board[i][j] = queen_num
            used_cols.add(j)
            start_cell = (i + 1) * BOARD_SIZE  # skip to the next row
            solved = solve(board=board, queen_num=(queen_num + 1), start_cell=start_cell, used_cols=used_cols)
            if not solved:
                board[i][j] = 0
                used_cols.remove(j)
            else:
                return solved

    return False


if __name__ == "__main__":
    for test in list(range(1, 21)):
        print(f"{test} x {test}")
        safe_count = 0
        NUM_QUEENS = test
        BOARD_SIZE = test
        solution = solve()
        if not solution:
            print("No solution")
        print(f"safe_on_diagonal calls: {safe_count}\n")