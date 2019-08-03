from collections import deque

maze = [
    [0, 0, 0, 0],
    [0, 1, 1, 1],
    [0, 0, 0, 0],
    [0, 1, 1, 0]
]

maze = [
    [0, 0, 0, 0],
    [0, 1, 1, 0],
    [0, 0, 1, 0],
    [0, 1, 1, 0]
]

maze = [
    [0, 1, 0, 0],
    [0, 0, 0, 1],
    [0, 1, 0, 1],
    [0, 1, 0, 0]
]

x_max = len(maze[0]) - 1
y_max = len(maze) - 1

x, y = 0, 0
goal = (x_max, y_max)
start = (0, 0, [])
print(x_max, y_max, goal, start)

open_states = deque([start])

while open_states:
    x, y, my_path = open_states.popleft()
    if x + 1 <= x_max and maze[x + 1][y] == 0:
        right_path = my_path + [(x, y)]
        open_states.append((x + 1, y, right_path))
    if y + 1 <= y_max and maze[x][y + 1] == 0:
        down_path = my_path + [(x, y)]
        open_states.append((x, y + 1, down_path))
    print(x, y, my_path)
    if x == x_max and y == y_max:
        print(my_path + [(x, y)])
        print("Found a path")


