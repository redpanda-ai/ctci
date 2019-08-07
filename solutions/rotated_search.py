# Imagine we have an image. We'll represent this image as a simple 2D array where every pixel is a 1 or a 0.

# There are N shapes made up of 0s in the image. They are not necessarily rectangles -- they are odd shapes ("islands"). Find them.

image1 = [
    [1, 0, 1, 1, 1, 1, 1],
    [1, 0, 0, 1, 0, 1, 1],
    [1, 1, 1, 0, 0, 0, 1],
    [1, 0, 1, 1, 0, 1, 1],
    [1, 0, 1, 1, 1, 1, 1],
    [1, 0, 0, 0, 0, 1, 1],
    [1, 1, 1, 0, 0, 1, 1],
    [1, 1, 1, 1, 1, 1, 0],
]

# Every single pixel in each shape. For reference, these are (in [row,column] format):

# findShapes(image1) =>
#   [
#     [[0,1],[1,1],[1,2]],
#     [[1,4],[2,3],[2,4],[2,5],[3,4]],
#     [[3,1],[4,1],[5,1],[5,2],[5,3],[5,4],[6,3],[6,4]],
#     [[7,6]],
#   ]


# Other test cases:

image2 = [
    [0],
]

# findShapes(image2) =>
#   [
#     [[0,0]],
#   ]

image3 = [
    [1],
]

# findShapes(image3) => []

from collections import deque


def explore(arr, rows, cols, open_states):
    # this is not finished, it needs to recurse while the open_states are not empty
    results = []
    i, j = open_states.popleft()
    if i > 0:
        if arr[i - 1][j] == 0:
            open_states.append((i - 1, j))
    if i < rows - 1:
        if arr[i + 1][j] == 0:
            open_states.append((i + 1, j))
    if j > 0:
        if arr[i][j - 1] == 0:
            open_states.append((i, j - 1))
    if j < cols - 1:
        if arr[i][j + 1] == 0:
            open_states.append((i, j + 1))


# return the result


def multiple_polys(image):
    rows = len(image)
    cols = len(image[0])

    image_copy = [row[:] for row in image]
    # print(image_copy)

    open_states = deque([])

    results = []
    found = None
    for i in range(rows):
        for j in range(cols):
            if image_copy[i][j] == 0:
                open_states.append((i, j)
                explore(image_copy, rows, cols, open_states)


def helper(i, j, rows, cols, arr):
    i_orig, j_orig = i, j

    while i < rows and arr[i][j] == 0:
        print(i)
        i += 1
    i -= 1
    while j < cols and arr[i][j] == 0:
        j += 1
    j -= 1

    # paint
    for a in range(i_orig, i + 1):
        for b in range(j_orig, j + 1):
            arr[a][b] = 1

    return [i, j], arr


def find_multiple_rectangles(image):
    rows = len(image)
    cols = len(image[0])

    image_copy = [row[:] for row in image]
    # print(image_copy)

    results = []
    found = None
    for i in range(rows):
        for j in range(cols):
            if image_copy[i][j] == 0:
                upper_left = [i, j]
                lower_right, image_copy = helper(i, j, rows, cols, image_copy)
                print(upper_left, lower_right)
                results.append([upper_left, lower_right])


find_multiple_rectangles(image3)

# """
# def find_recatangle(image):
#     rows = len(image)
#     used_cols = len(image[0])

#     first, last = None, None
#     first_found = False

#     for i in range(rows):
#         for j in range(used_cols):
#             if image[i][j] == 0:
#                 if not first_found:
#                     first = last = (i, j)
#                     first_found = True
#                 else:
#                     last = (i, j)

#     return first, last
# """

# tests = [
#     image1,
#     image2,
#     image3,
#     image4,
#     image5
# ]

# for test in tests:
#     print(find_recatangle(test))




