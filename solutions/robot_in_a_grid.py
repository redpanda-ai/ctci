from collections import deque
from collections import namedtuple

FORBIDDEN = 1


def robot_in_a_grid(lim_x: int, lim_y: int, forbidden: set) -> deque:
    start = State(x=0, y=0, parent=None)
    goal = State(x=lim_x - 1, y=lim_y - 1, parent=None)

    open_states = deque([start])

    answer = deque()
    while open_states:
        s = open_states.popleft()
        if s.x is goal.x and s.y is goal.y:
            while s:
                answer.appendleft((s.x, s.y))
                s = s.parent
            return answer

        d = State(x=s.x, y=s.y + 1, parent=s)
        r = State(x=s.x + 1, y=s.y, parent=s)

        for c in [d, r]:
            if c.x < lim_x and c.y < lim_y and (c.x, c.y) not in forbidden and c not in open_states:
                open_states.append(c)

    return answer


class State:
    def __init__(self, x=None, y=None, parent=None):
        self.x = x
        self.y = y
        self.parent = parent

    def __repr__(self):
        return f"({self.x}, {self.y})"

    def __eq__(self, other):
        return self.x is other.x and self.y is other.y


if __name__ == "__main__":
    test_forbidden = {
        (1, 1),
        (1, 2),
        (1, 3),
        (3, 1),
        (3, 2)
    }
    path_to_goal = robot_in_a_grid(5, 5, test_forbidden)
    print(f"Path to goal: {path_to_goal}")

