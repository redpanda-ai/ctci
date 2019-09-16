from collections import deque
from collections import namedtuple

FORBIDDEN = 1


def rig(grid):
    lim_y = len(grid)
    lim_x = len(grid[0])

    State = namedtuple('State', 'x y path')
    start_state = State(0, 0, [])
    goal_state = State(lim_x - 1, lim_y - 1, None)
    open_states = deque([start_state])
    while open_states:
        s = open_states.popleft()
        _x, _y = s.x + 1, s.y + 1
        if s.x == goal_state.x and s.y == goal_state.y:
            return s.path
        if _x < lim_x and grid[s.y][_x] is not FORBIDDEN:
            open_states.append(State(_x, s.y, s.path + ["R"]))
        if _y < lim_y and grid[_y][s.x] is not FORBIDDEN:
            open_states.append(State(s.x, _y, s.path + ["D"]))

    return None


class State:
    def __init__(self, x, y, path):
        self.x = x
        self.y = y
        self.path = path

    def is_forbidden(self, grid):
        return grid[self.y][self.x] is FORBIDDEN

    def __eq__(self, other):
        return self.x == other.x and self.y == other.y


def new_rig(grid):
    lim_x, lim_y = len(grid[0]), len(grid)
    start_state = State(0, 0, [])
    goal_state = State(lim_x - 1, lim_y - 1, None)
    open_states = deque([start_state])

    while open_states:
        s = open_states.popleft()

        if s == goal_state:
            return s.path

        down = State(s.x, s.y + 1, s.path + ["D"])
        if down.y < lim_y and not down.is_forbidden(grid):
            open_states.append(down)

        right = State(s.x + 1, s.y, s.path + ["R"])
        if right.x < lim_x and not right.is_forbidden(grid):
            open_states.append(right)


def show_grid(grid):
    for line in grid:
        print(line)


if __name__ == "__main__":
    grids = [
        [
            [0, 0, 0, 0],
            [0, 1, 1, 1],
            [0, 0, 0, 0],
            [0, 1, 1, 0]
        ],
        [
            [0, 0, 0, 0],
            [0, 1, 1, 0],
            [0, 0, 1, 0],
            [0, 1, 1, 0]
        ],
        [
            [0, 1, 0, 0],
            [0, 0, 0, 1],
            [0, 1, 0, 1],
            [0, 1, 0, 0]
        ],
        [
            [0, 0, 0, 0],
            [0, 0, 0, 0],
            [0, 0, 1, 1],
            [0, 0, 1, 0]
        ]
    ]
    for grid in grids:
        show_grid(grid)
        path_to_goal = new_rig(grid)
        print(f"Path to goal: {path_to_goal}")



