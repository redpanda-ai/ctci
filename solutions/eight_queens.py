from collections import defaultdict

def get_clear_board():
    return [[0 for i in range(BOARD_SIZE)] for j in range(BOARD_SIZE)]


def print_board(board):
    for i in range(BOARD_SIZE):
        print(board[i])


def safe_helper(board, queen_num, i, j, a, used_cells):
    row_cols = [
        (i + a, j + a),
        (i - a, j - a),
        (i + a, j - a),
        (i - a, j + a)
    ]

    for row, col in row_cols:
        # print(row, col)
        if 0 <= row < BOARD_SIZE and 0 <= col < BOARD_SIZE:
            if board[row][col] != 0:
                return False
            else:
                used_cells[queen_num].append(row * BOARD_SIZE + col)


def safe_on_diagonals(board, queen_num, i, j, used_cells):
    global safe_count
    safe_count += 1

    for a in range(1, BOARD_SIZE):
        if safe_helper(board, queen_num, i, j, a, used_cells) is False:
            return False
    return True


def solve(board=None, queen_num=1, start_cell=0, used_cols=None, used_cells=None):

    # Success case
    if queen_num == NUM_QUEENS + 1:
        print_board(board)
        # print(used_cells)
        return True

    # create an empty chess board
    if not board:
        board = get_clear_board()

    # create a set to track used columns
    if not used_cols:
        used_cols = set()

    # create a set of used cells
    if not used_cells:
        used_cells = defaultdict(list)

    # don't inspect cells where the column has already been used
    cells = [i + start_cell for i in range(BOARD_SIZE) if i not in used_cols]

    # don't inspect cells that have already been used
    bad_cells = []
    for key in used_cells:
        bad_cells.extend([cell for cell in used_cells[key] if cell in cells])
    # print(f"Bad cells: {bad_cells}")
    cells = [cell for cell in cells if cell not in bad_cells]

    for cell in cells:
        i = cell // BOARD_SIZE
        j = cell % BOARD_SIZE
        if safe_on_diagonals(board, queen_num, i, j, used_cells):
            board[i][j] = queen_num
            used_cells[queen_num].append(cell)
            used_cols.add(j)
            start_cell = (i + 1) * BOARD_SIZE  # skip to the next row
            solved = solve(
                board=board, queen_num=(queen_num + 1), start_cell=start_cell,
                used_cols=used_cols, used_cells=used_cells)
            if not solved:
                board[i][j] = 0
                used_cols.remove(j)
                del used_cells[queen_num]
                if queen_num + 1 in used_cells:
                    del used_cells[queen_num + 1]

            else:
                return solved

    return False


if __name__ == "__main__":
    for test in list(range(1, 25)):
        safe_count = 0
        NUM_QUEENS = test
        BOARD_SIZE = test
        solution = solve()
        if not solution:
            print("No solution")
        print(f"{test} x {test} safe_on_diagonal calls: {safe_count}\n")